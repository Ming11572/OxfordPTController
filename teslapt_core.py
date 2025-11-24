import pyvisa
import threading
from datetime import datetime


def connect_to_tesla_pt(loger_saver, ips_addr: str, itc_addr_ls: list, itc_alias_ls: list):
    rm = pyvisa.ResourceManager()
    try:
        # connect to the ips controller
        ips = rm.open_resource(ips_addr)
        ips = MutexVisa(ips, 'ips')
        # connect to the itc controller
        itc_ls = []
        itc_alias_ls = itc_alias_ls
        for i, addr in enumerate(itc_addr_ls):
            temp_itc = rm.open_resource(addr)
            itc_ls.append(MutexVisa(temp_itc, itc_alias_ls[i]))

        ids = ips.query('*IDN?')
        for itc in itc_ls:
            ids = f"{ids}, {itc.query('*IDN?')}"

        pt_core = TeslaPTCore(log_saver=loger_saver, ips=ips, itc_ls=itc_ls, itc_alias_ls=itc_alias_ls)
        return True, pt_core
    except Exception as e:
        return False, repr(e)


class MutexVisa:

    def __init__(self, ins, alias):
        self.ins = ins
        self.alias = alias

        self.ins.read_termination = '\n'
        self.instr_lock = threading.Lock()

    def query(self, qcode):
        with self.instr_lock:
            res = self.ins.query(qcode)
        return res

    def multi_query(self, qcode_ls):
        qcode = ';'.join(qcode_ls)
        res = []
        with self.instr_lock:
            self.ins.write(qcode)
            for i in range(len(qcode_ls)):
                res.append(self.ins.read())
        return res

    def write(self, qcode):
        self.ins.write(qcode)

    def read(self):
        res = self.ins.read()
        return res


class TeslaPTCore:

    def __init__(self, log_saver, ips, itc_ls, itc_alias_ls):
        self.debug_value = 9999.99032
        self.flag_magnet_ready = True
        self.log_saver = log_saver
        self.alias = 'pt_core'

        self.magnet_ls = [7.5, -7.5, 0.2, 1e-4]     # max, min, max_rate, min_step
        self.temperature_ls = [300, 0.01, 2, 0.005]

        # the daughter board and itc controller
        self.db_magnet_temperature = None
        self.db_pt2 = None
        self.db_pt1 = None
        self.tuple_1k_pool = None
        self.tuple_vti = None
        self.tuple_sorb = None
        self.tuple_probe_temperature = None
        self.__probe_temperature_high = None
        self.__probe_temperature_low = None

        self.ips = ips
        self.ips_alias = 'ips'
        self.itc_ls = itc_ls
        self.itc_alias_ls = itc_alias_ls

    def get_pt_setting(self):
        return self.magnet_ls + self.temperature_ls

    def init_pt_core(self, settings):
        """
        1. init the magnet, temperature setpoint boundary
        2. init the itc controller, DB numbers.
        :return:
        """
        magnet_ls = settings['magnet_set']
        temp_ls = settings['temp_set']
        db_sets = settings['db_set']
        itc_sets = settings['itc_set']

        try:
            self.magnet_ls = magnet_ls
            self.temperature_ls = temp_ls

            index = self.itc_alias_ls.index(itc_sets[0])
            self.__probe_temperature_low = (self.itc_ls[index], db_sets[0])

            index = self.itc_alias_ls.index(itc_sets[1])
            self.__probe_temperature_high = (self.itc_ls[index], db_sets[1])

            self.tuple_probe_temperature = self.__probe_temperature_high

            index = self.itc_alias_ls.index(itc_sets[2])
            self.tuple_vti = (self.itc_ls[index], db_sets[2])

            index = self.itc_alias_ls.index(itc_sets[3])
            self.tuple_1k_pool = (self.itc_ls[index], db_sets[3])

            if itc_sets[4] == "None":
                self.tuple_sorb = None
            else:
                index = self.itc_alias_ls.index(itc_sets[4])
                self.tuple_sorb = (self.itc_ls[index], db_sets[4])

            self.db_magnet_temperature = settings['db_magnet_temp']
            self.db_pt1 = settings['db_pt1']
            self.db_pt2 = settings['db_pt2']
            return True, "OK"
        except Exception as e:
            return False, repr(e)

    def use_low_temperature_sensor(self, flag: bool):  # flag is True or False
        if flag:
            self.tuple_probe_temperature = self.__probe_temperature_low
        else:
            self.tuple_probe_temperature = self.__probe_temperature_high

    def scan_magnet_to_goal(self, goal, rate=None):
        try:
            self.set_magnet(goal)
            if rate is not None:
                self.set_magnet_rate(rate)
            self.set_magnet_status('to set')
        except Exception as e:
            # print(f'scan field failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'scan field failed because: {repr(e)}')

    def set_probe_and_vti_temperature(self, goal):
        self.set_probe_temperature(goal)
        if goal <= 3:
            self.set_vti_temperature(goal*0.9)
        elif 3 < goal <= 20:
            self.set_vti_temperature(goal-1)
        elif 20 < goal <= 22:
            self.set_vti_temperature(20)
        elif 22 < goal <= 150:
            self.set_vti_temperature(goal-2)
        elif 150 < goal <= 155:
            self.set_vti_temperature(150)
        elif goal > 150:
            self.set_vti_temperature(goal-5)

    def get_magnet(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:SIG:PFLD')
            return res[27:-1]
        except Exception as e:
            # print(f'get magnet failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet failed because: {repr(e)}')
            return self.debug_value

    def get_magnet_setpoint(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:SIG:FSET')
            return res[27:-1]
        except Exception as e:
            # print(f'get magnet set point failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet set point failed because: {repr(e)}')
            return self.debug_value

    def set_magnet_ready(self, flag: bool):
        self.flag_magnet_ready = flag

    def set_magnet(self, goal):
        if self.flag_magnet_ready:
            if self.magnet_ls[1] <= goal <= self.magnet_ls[0]:
                try:
                    res = self.ips.query(f'SET:DEV:GRPZ:PSU:SIG:FSET:{goal:.5f}T')
                    self.log_saver.log_debug(self.alias, res)
                except Exception as e:
                    self.log_saver.error(self.alias, f'set magnet to {goal} failed because: {repr(e)}')
            else:
                self.log_saver.error(self.alias, 'magnet setpoint out of range')
        else:
            self.log_saver.error(self.alias, 'magnet is not ready')

    def get_magnet_rate(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:SIG:RFST')
            return res[27:-3]
        except Exception as e:
            # print(f'get magnet rate failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet rate failed because: {repr(e)}')
            return self.debug_value

    def set_magnet_rate(self, rate):
        if 0 < rate <= self.magnet_ls[2]:
            try:
                res = self.ips.query(f'SET:DEV:GRPZ:PSU:SIG:RFST:{rate:.5f}T/m')
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set magnet rate failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set magnet rate failed because: {repr(e)}')
                # return self.debug_value
        else:
            self.log_saver.error(self.alias, 'magnet ramp rate out of range')

    def get_magnet_status(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:ACTN')
            if 'RTOS' in res:
                return 'to set'
            elif 'HOLD' in res:
                return 'hold'
            elif 'RTOZ' in res:
                return 'to zero'
            else:
                return 'error'
        except Exception as e:
            # print(f'get magnet scan status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet scan status failed because: {repr(e)}')
            return self.debug_value

    def set_magnet_status(self, status):
        try:
            if status == 'to set':
                # print(self.ips.query('SET:DEV:GRPZ:PSU:ACTN:RTOS'))
                tres = self.ips.query('SET:DEV:GRPZ:PSU:ACTN:RTOS')
                self.log_saver.log_debug(self.alias, tres)
            elif status == 'hold':
                # print(self.ips.query('SET:DEV:GRPZ:PSU:ACTN:HOLD'))
                tres = self.ips.query('SET:DEV:GRPZ:PSU:ACTN:HOLD')
                self.log_saver.log_debug(self.alias, tres)
            elif status == 'to zero':
                # print(self.ips.query('SET:DEV:GRPZ:PSU:ACTN:RTOZ'))
                tres = self.ips.query('SET:DEV:GRPZ:PSU:ACTN:RTOZ')
                self.log_saver.log_debug(self.alias, tres)
        except Exception as e:
            # print(f'set magnet {status} failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set magnet {status} failed because: {repr(e)}')

    def get_current_field(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:SIG:FLD')
            return res[26:-1]
        except Exception as e:
            # print(f'get current field failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get current field failed because: {repr(e)}')
            return self.debug_value

    def set_ips_heater(self, goal):     # goal is 'ON' or 'OFF'
        try:
            res = self.ips.query(f'SET:DEV:GRPZ:PSU:SIG:SWHT:{goal}')

            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set ips heater {goal} failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set ips heater {goal} failed because: {repr(e)}')

    def get_ips_heater(self):
        try:
            res = self.ips.query('READ:DEV:GRPZ:PSU:SIG:SWHT')
            return res[27:]
        except Exception as e:
            # print(f'get ips heater status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get ips heater status failed because: {repr(e)}')
            return self.debug_value

    def get_magnet_temperature(self):
        try:
            res = self.ips.query(f'READ:DEV:{self.db_magnet_temperature}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get magnet field temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet field temperature failed because: {repr(e)}')
            return self.debug_value

    def get_pt1(self):
        try:
            res = self.ips.query(f'READ:DEV:{self.db_pt1}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get magnet field temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet field temperature failed because: {repr(e)}')
            return self.debug_value

    def get_pt2(self):
        try:
            res = self.ips.query(f'READ:DEV:{self.db_pt2}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get magnet field temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get magnet field temperature failed because: {repr(e)}')
            return self.debug_value

    def get_probe_temperature(self):
        try:
            tp = self.tuple_probe_temperature
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get probe temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get probe temperature failed because: {repr(e)}')
            return self.debug_value

    def get_probe_temperature_setpoint(self):
        try:
            tp = self.tuple_probe_temperature
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:TSET')
            return res[31:-1]
        except Exception as e:
            # print(f'get probe temperature set point failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get probe temperature set point failed because: {repr(e)}')
            return self.debug_value

    def set_probe_temperature(self, goal):
        if self.temperature_ls[1] <= goal <= self.temperature_ls[0]:
            try:
                tp = self.tuple_probe_temperature
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:TSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set probe temperature failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set probe temperature failed because: {repr(e)}')
        else:
            # print('设定的probe温度超过阈值，设置失败')
            self.log_saver.error(self.alias, '设定的probe温度超过阈值，设置失败')

    def get_probe_heater_power(self):
        try:
            tp = self.tuple_probe_temperature
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:HSET')
            return res[31:]
        except Exception as e:
            # print(f'get probe heater power failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get probe heater power failed because: {repr(e)}')
            return self.debug_value

    def set_probe_heater_power(self, goal):
        if 0 <= goal <= 100:
            try:
                tp = self.tuple_probe_temperature
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:HSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set probe heater power failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set probe heater power failed because: {repr(e)}')
        else:
            # print('probe heater power 应该在0~100之间')
            self.log_saver.error(self.alias, 'probe heater power 应该在0~100之间')

    def get_probe_heater_auto(self):
        try:
            tp = self.tuple_probe_temperature
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB')
            return res[31:]     # return value is ON/OFF
        except Exception as e:
            # print(f'get probe heater status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get probe heater status failed because: {repr(e)}')
            return self.debug_value

    def set_probe_heater_auto(self, goal):  # goal is ON/OFF
        try:
            tp = self.tuple_probe_temperature
            res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB:{goal}')
            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set probe heater status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set probe heater status failed because: {repr(e)}')

    def get_sorb_temperature(self):
        if self.tuple_sorb is None:
            return self.debug_value

        try:
            tp = self.tuple_sorb
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get vti temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get sorb temperature failed because: {repr(e)}')
            return self.debug_value

    def get_sorb_temperature_setpoint(self):
        if self.tuple_sorb is None:
            return self.debug_value
        try:
            tp = self.tuple_sorb
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:TSET')
            return res[31:-1]
        except Exception as e:
            # print(f'get vti temperature set point failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get sorb temperature set point failed because: {repr(e)}')
            return self.debug_value

    def set_sorb_temperature(self, goal):
        if (self.tuple_sorb is not None) and 0 <= goal <= 40:
            try:
                tp = self.tuple_sorb
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:TSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set vti temperature failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set sorb temperature failed because: {repr(e)}')
        else:
            # print('设定的vti温度超过阈值，设置失败')
            self.log_saver.error(self.alias, '设定的vti温度超过阈值，设置失败')

    def get_sorb_heater_power(self):
        if self.tuple_sorb is None:
            return self.debug_value
        try:
            tp = self.tuple_sorb
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:HSET')
            return res[31:]
        except Exception as e:
            # print(f'get vti heater power failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get sorb heater power failed because: {repr(e)}')
            return self.debug_value

    def set_sorb_heater_power(self, goal):
        if (self.tuple_sorb is not None) and 0 <= goal <= 100:
            try:
                tp = self.tuple_sorb
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:HSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set vti heater power failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set sorb heater power failed because: {repr(e)}')
        else:
            # print('vti heater power 应该在0~100之间')
            self.log_saver.error(self.alias, 'sorb heater power 应该在0~100之间')

    def get_sorb_heater_auto(self):
        if self.tuple_sorb is None:
            return self.debug_value
        try:
            tp = self.tuple_sorb
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB')
            return res[31:]     # return value is ON/OFF
        except Exception as e:
            # print(f'get vti heater auto status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get sorb heater auto status failed because: {repr(e)}')
            return self.debug_value

    def set_sorb_heater_auto(self, goal):  # goal is ON/OFF
        if self.tuple_sorb is not None:
            try:
                tp = self.tuple_sorb
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB:{goal}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set vti heater auto status failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set sorb heater auto status failed because: {repr(e)}')

    def get_vti_temperature(self):
        try:
            tp = self.tuple_vti
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:SIG:TEMP')
            return res[30:-1]
        except Exception as e:
            # print(f'get vti temperature failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get vti temperature failed because: {repr(e)}')
            return self.debug_value

    def get_vti_temperature_setpoint(self):
        try:
            tp = self.tuple_vti
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:TSET')
            return res[31:-1]
        except Exception as e:
            # print(f'get vti temperature set point failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get vti temperature set point failed because: {repr(e)}')
            return self.debug_value

    def set_vti_temperature(self, goal):
        if self.temperature_ls[1] <= goal <= self.temperature_ls[0]:
            try:
                tp = self.tuple_vti
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:TSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set vti temperature failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set vti temperature failed because: {repr(e)}')
        else:
            # print('设定的vti温度超过阈值，设置失败')
            self.log_saver.error(self.alias, '设定的vti温度超过阈值，设置失败')

    def get_vti_heater_power(self):
        try:
            tp = self.tuple_vti
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:HSET')
            return res[31:]
        except Exception as e:
            # print(f'get vti heater power failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get vti heater power failed because: {repr(e)}')
            return self.debug_value

    def set_vti_heater_power(self, goal):
        if 0 <= goal <= 100:
            try:
                tp = self.tuple_vti
                res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:HSET:{goal:.4f}')
                # print(res)
                self.log_saver.log_debug(self.alias, res)
            except Exception as e:
                # print(f'set vti heater power failed because: {repr(e)}')
                self.log_saver.error(self.alias, f'set vti heater power failed because: {repr(e)}')
        else:
            # print('vti heater power 应该在0~100之间')
            self.log_saver.error(self.alias, 'vti heater power 应该在0~100之间')

    def get_vti_heater_auto(self):
        try:
            tp = self.tuple_vti
            res = tp[0].query(f'READ:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB')
            return res[31:]     # return value is ON/OFF
        except Exception as e:
            # print(f'get vti heater auto status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get vti heater auto status failed because: {repr(e)}')
            return self.debug_value

    def set_vti_heater_auto(self, goal):  # goal is ON/OFF
        try:
            tp = self.tuple_vti
            res = tp[0].query(f'SET:DEV:{tp[1]}.T1:TEMP:LOOP:ENAB:{goal}')
            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set vti heater auto status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set vti heater auto status failed because: {repr(e)}')

    def get_1k_pool_pressure(self):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'READ:DEV:{tp[1]}.P1:PRES:SIG:PRES')
            return res[30:-2]
        except Exception as e:
            # print(f'get pressure failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get pressure failed because: {repr(e)}')
            return self.debug_value

    def get_1k_pool_pressure_setpoint(self):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'READ:DEV:{tp[1]}.P1:PRES:LOOP:PRST')
            return res[31:-2]
        except Exception as e:
            # print(f'get pressure set point failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get pressure set point failed because: {repr(e)}')
            return self.debug_value

    def set_1k_pool_pressure(self, goal):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'SET:DEV:{tp[1]}.P1:PRES:LOOP:PRST:{goal:.4f}')
            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set pressure failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set pressure failed because: {repr(e)}')

    def get_1k_pool_nv(self):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'READ:DEV:{tp[1]}.P1:PRES:LOOP:FSET')
            return res[31:]
        except Exception as e:
            # print(f'get N.V. failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get N.V. failed because: {repr(e)}')
            return self.debug_value

    def set_1k_pool_nv(self, goal):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'SET:DEV:{tp[1]}.P1:PRES:LOOP:FSET:{goal:.4f}')
            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set N.V. failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set N.V. failed because: {repr(e)}')

    def get_1k_pool_nv_auto(self):
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'READ:DEV:{tp[1]}.P1:PRES:LOOP:FAUT')
            return res[31:]  # return value is ON/OFF
        except Exception as e:
            # print(f'get N.V. auto status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'get N.V. auto status failed because: {repr(e)}')
            return self.debug_value

    def set_1k_pool_nv_auto(self, goal):  # goal is ON/OFF
        try:
            tp = self.tuple_1k_pool
            res = tp[0].query(f'SET:DEV:{tp[1]}.P1:PRES:LOOP:FAUT:{goal}')
            # print(res)
            self.log_saver.log_debug(self.alias, res)
        except Exception as e:
            # print(f'set N.V. auto status failed because: {repr(e)}')
            self.log_saver.error(self.alias, f'set N.V. auto status failed because: {repr(e)}')
            return self.debug_value


# if __name__ == '__main__':
#     pt_dict = {
#         'alias': 'nanoPublicPT',
#         'field': [7.5, -7.5, 0.2, 0.0001],
#         'temperature': [400.0, 0.1, 2.0, 0.005],
#         'angle': [70.0, -70.0, 10.0, 0.001],
#         'db_setting': [['ITC', 'DB8'], ['ITC', 'DB8'], ['ITC', 'MB1'], ['ITC', 'DB5'], ['None', 'None']],
#         'address': ['IPS = TCPIP0::192.168.1.50::7020::SOCKET',
#                     'ITC = TCPIP0::192.168.1.100::7020::SOCKET',],
#                    # 'HE3 = TCPIP0::192.168.1.30::7020::SOCKET'],
#         'address_ls': [['IPS', 'TCPIP0::192.168.1.50::7020::SOCKET'],
#                        ['ITC', 'TCPIP0::192.168.1.100::7020::SOCKET']],
#                     #   ['HE3', 'TCPIP0::192.168.1.30::7020::SOCKET']],
#         'Tmagnet': [3.7, 3.85]}
#     pt_core = TeslaPTCore(pt_dict)
