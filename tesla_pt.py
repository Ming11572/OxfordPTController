from ui.teslaPT import Ui_Form
from ui.teslaPTcontrol import Ui_control
from ui.teslaPT_warm_cool import Ui_WarmCool
from instrument.baseController import BaseController
from instrument.Oxford.teslapt_core import TestraPTCore

from PySide6.QtWidgets import QWidget, QButtonGroup, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, QThread, Qt

import pickle
import numpy as np
import time
import threading
from datetime import datetime
import os.path


# global numbers
global curr_meas_str, now_magnet, nows_magnet_setpoint, now_magnet_rate, now_current_field, nows_magnet_scan_status, \
    nows_ips_heater, now_magnet_temperature, now_probe_temperature, nows_probe_temperature_setpoint, \
    nows_probe_heater_power, nows_probe_heater_auto, now_vti_temperature, nows_vti_temperature_setpoint, \
    nows_vti_heater_power, nows_vti_heater_auto, nows_pool_pressure, nows_pool_pressure_setpoint, nows_pool_nv,\
    nows_pool_nv_auto, min_field_tolerance, min_temperature_tolerance


class TeslaPT(Ui_Form, QWidget, BaseController):

    def __init__(self, resource_name, alias, setting_dict, status_window, global_lock, auto_sens=float(-1), parent=None):
        self.connect_allowed = False
        self.sync_meas_res_lock = threading.Lock()
        self.sync_datas_lock = threading.RLock()
        self.program_closed = False
        self.sweep_forward = 0
        self.sweep_field_started = False
        self.recipe_abort = False
        self.if_all_alarm_clear = True
        Ui_Form.__init__(parent)
        QWidget.__init__(self, parent)
        BaseController.__init__(self, resource_name, alias, setting_dict, status_window, global_lock, auto_sens)
        self.logging_saver = status_window.log_saver
        # connect to ips and itc
        self.pt_core = TestraPTCore(setting_dict, self.logging_saver)
        try:
            if self.pt_core.inst_status:
                self.inst_status = True
            else:
                self.inst_status = False
        except Exception as e:
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, repr(e)])
            self.inst_status = False
            self.if_meter_collect = False

        self.if_instr_writing = True
        temperature = setting_dict['temperature']
        self.max_temperature = temperature[0]
        self.min_temperature = temperature[1]
        self.min_temperature_step = temperature[3]
        self.max_temperature_speed = temperature[2]
        field = setting_dict['field']
        self.max_field = field[0]
        self.min_field = field[1]
        self.min_field_step = field[3]

        self.independent_var_name_dict = {'Tprobe': '_Tprobe', 'Magnet': '_Magnet'}

        global curr_meas_str, now_magnet, nows_magnet_setpoint, now_magnet_rate, now_current_field, nows_magnet_scan_status, \
            nows_ips_heater, now_magnet_temperature, now_probe_temperature, nows_probe_temperature_setpoint, \
            nows_probe_heater_power, nows_probe_heater_auto, now_vti_temperature, nows_vti_temperature_setpoint, \
            nows_vti_heater_power, nows_vti_heater_auto, nows_pool_pressure, nows_pool_pressure_setpoint, nows_pool_nv, \
            nows_pool_nv_auto, min_field_tolerance, min_temperature_tolerance

        min_temperature_tolerance = self.min_temperature_step

        curr_meas_str = ['0', '0', '0', '0', '0', '0', '0', '0']
        now_magnet = -1
        nows_magnet_setpoint = ''
        self.now_magnet_setpoint = 0
        now_magnet_rate = -1
        now_current_field = -1
        nows_magnet_scan_status = 'error'
        nows_ips_heater = 'error'
        now_magnet_temperature = -1

        now_probe_temperature = -1
        nows_probe_temperature_setpoint = '-1'
        nows_probe_heater_power = '-1'
        nows_probe_heater_auto = 'error'

        now_vti_temperature = -1
        nows_vti_temperature_setpoint = '-1'
        nows_vti_heater_power = '-1'
        nows_vti_heater_auto = 'error'

        nows_pool_pressure = '-1'
        nows_pool_pressure_setpoint = '-1'
        nows_pool_nv = '-1'
        nows_pool_nv_auto = 'error'

        min_field_tolerance = self.min_field_step
        self.max_field_speed = field[2]
        # protect
        self.protect_MT_low = setting_dict['Tmagnet'][0]
        self.protect_MT_high = setting_dict['Tmagnet'][1]

        self.if_check_seq_return_error = False

        self.setupUi(self)
        self.defineUi()
        self.meas_channel = ['_Tprobe', '_Magnet', '_Tvti', '_Tmagnet']
        self.curr_meas_res = [0.0, 0.0, 0.0, 0.0]

        self.step_model = False

        self.control = TeslaPTControl(self.pt_core, self)

        self.ui_warmcool = TeslaPTWarmCool(self.pt_core, self)

        self.auto_sync_thread = AutoSyncThread(self.pt_core, self, self.control, self.ui_warmcool)

        self.pause_time_sync_status = 60
        self.pause_time_sync_setpoint = 300

        self.sync_inst_status()

        # self.cb_probe_select.currentIndexChanged.connect(self.slot_pt_probe_select)
        self.cb_if_collect.stateChanged.connect(self.slot_cb_collect_checked)
        self.cb_pause_mode.addItems(['sweep model', 'step model'])
        self.cb_pause_mode.currentIndexChanged.connect(self.slot_pause_mode_checked)
        self.pb_meas.clicked.connect(self.instr_read_and_sync_meas)
        self.pb_control.clicked.connect(self.slot_control_button_clicked)
        self.pb_warm_cool.clicked.connect(self.slot_warm_cool_clicked)

        self.auto_sync_thread.start()

    def start_connect(self, resource_name):
        pass

    def instr_lock_by_recipe(self):
        self.instr_locked_count_by_recipe += 1
        self.pt_core.ips.instr_lock.acquire()
        for itc in self.pt_core.itc_ls:
            itc.instr_lock.acquire()

    def release_instr_lock_by_recipe(self):
        while self.instr_locked_count_by_recipe > 0:
            self.pt_core.ips.instr_lock.release()
            for itc in self.pt_core.itc_ls:
                itc.instr_lock.release()
            self.instr_locked_count_by_recipe -= 1

    def inst_read(self):        # 自动刷新， 频率：每 1 秒一次
        global curr_meas_str, now_magnet, now_probe_temperature, now_vti_temperature, now_magnet_temperature, \
            nows_probe_heater_power, nows_vti_heater_power, nows_pool_nv, nows_pool_pressure, now_current_field

        self.sync_datas_lock.acquire()
        try:
            # probe temperature
            curr_meas_str[0] = self.pt_core.get_probe_temperature()
            now_probe_temperature = float(curr_meas_str[0])
            self.switch_probe_temperature_sensor(now_probe_temperature)
            # magnet
            curr_meas_str[1] = self.pt_core.get_magnet()
            now_magnet = float(curr_meas_str[1])

            now_current_field = float(self.pt_core.get_current_field())

            # vti temperature
            curr_meas_str[2] = self.pt_core.get_vti_temperature()
            now_vti_temperature = float(curr_meas_str[2])
            # magnet temperature
            curr_meas_str[3] = self.pt_core.get_magnet_temperature()
            now_magnet_temperature = float(curr_meas_str[3])
            self.magnet_protect()

            # probe heater
            nows_probe_heater_power = self.pt_core.get_probe_heater_power()
            curr_meas_str[4] = nows_probe_heater_power
            # vti heater
            nows_vti_heater_power = self.pt_core.get_vti_heater_power()
            curr_meas_str[5] = nows_vti_heater_power
            # nv
            nows_pool_nv = self.pt_core.get_1k_pool_nv()
            curr_meas_str[6] = nows_pool_nv
            # pressure
            nows_pool_pressure = self.pt_core.get_1k_pool_pressure()
            curr_meas_str[7] = nows_pool_pressure

            self.logging_saver.append_log('teslatronPT_logging', [time.time()] + curr_meas_str)

        except Exception as e:
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, repr(e)])
            self.inst_status = False
        self.sync_datas_lock.release()
        # self.signal_sync_meas.emit()

    def sync_inst_status(self):     # 自动刷新， 频率：每 1 分钟一次
        global nows_ips_heater, nows_vti_heater_auto, nows_probe_heater_auto, nows_pool_nv_auto, \
            nows_magnet_scan_status, now_magnet_rate
        self.sync_datas_lock.acquire()
        if not self.inst_status:
            return
        nows_ips_heater = self.pt_core.get_ips_heater()
        if nows_ips_heater == 'ON':
            self.meas_Bz.setStyleSheet("color:red")
        else:
            self.meas_Bz.setStyleSheet("color:rgb(128,128,128)")
        nows_vti_heater_auto = self.pt_core.get_vti_heater_auto()
        nows_probe_heater_auto = self.pt_core.get_probe_heater_auto()
        nows_pool_nv_auto = self.pt_core.get_1k_pool_nv_auto()
        nows_magnet_scan_status = self.pt_core.get_magnet_status()

        now_magnet_rate = float(self.pt_core.get_magnet_rate())

        self.instr_read_and_sync_meas()
        self.pause_time_sync_status = 60
        self.sync_datas_lock.release()
        # self.signal_sync_status.emit()

    def get_setpoint_values(self):    # 5min 一更新
        global nows_magnet_setpoint, nows_probe_temperature_setpoint, \
            nows_vti_temperature_setpoint, nows_pool_pressure_setpoint
        self.sync_datas_lock.acquire()
        nows_magnet_setpoint = self.pt_core.get_magnet_setpoint()

        nows_probe_temperature_setpoint = self.pt_core.get_probe_temperature_setpoint()
        nows_vti_temperature_setpoint = self.pt_core.get_probe_temperature_setpoint()
        nows_pool_pressure_setpoint = self.pt_core.get_1k_pool_pressure_setpoint()
        self.sync_inst_status()
        self.pause_time_sync_setpoint = 300
        self.sync_datas_lock.release()
        # self.signal_sync_setpoint.emit()

    def switch_probe_temperature_sensor(self, temp):
        if temp < 5:
            self.pt_core.use_low_temperature_sensor(True)
        elif temp > 15:
            self.pt_core.use_low_temperature_sensor(False)

    def magnet_protect(self):
        if now_magnet_temperature > self.protect_MT_high:
            self.if_all_alarm_clear = False
            if self.auto_sync_thread.block_error <= 0:
                self.signal_fatal_error.emit(2, self.alias, '磁体温度超高，磁场会自动归零')
                self.pt_core.scan_magnet_to_goal(0, 0.1)  # 磁体归零
                self.pt_core.flag_magnet_ready = True
                self.logging_saver.append_log('debug_logging',
                                              [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, '磁体温度超高，磁场会自动归零'])
                self.auto_sync_thread.block_error = 600
        elif now_magnet_temperature > self.protect_MT_low:
            self.if_all_alarm_clear = False
            if self.auto_sync_thread.block_warning <= 0:
                self.signal_fatal_error.emit(1, self.alias, '磁体温度偏高，请注意')
                self.logging_saver.append_log('debug_logging',
                                              [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, '磁体温度偏高，请注意'])
                self.auto_sync_thread.block_warning = 600
        else:
            if not self.if_all_alarm_clear:
                self.pt_core.flag_magnet_ready = False
                self.if_all_alarm_clear = True
                self.signal_fatal_error.emit(0, self.alias, '磁体恢复正常')

    def sync_meas_res(self, meas_var_ls: list = None):

        self.sync_meas_res_lock.acquire()
        global curr_meas_str
        self.meas_probeT.setText(f'{curr_meas_str[0]} K')
        self.meas_Bz.setText(f'{curr_meas_str[1]} T')
        self.meas_vtiT.setText(f'{curr_meas_str[2]} K')
        self.meas_magnetT.setText(f'{curr_meas_str[3]} K')
        self.sync_meas_res_lock.release()

    def parallel_read_part1(self):
        self.pt_core.parallel_query_part1()

    def parallel_read_part2(self) -> list:
        self.curr_meas_res = self.pt_core.parallel_query_part2()
        return self.curr_meas_res

    def set_outp(self, outp_code):
        global now_magnet, min_field_tolerance
        if isinstance(outp_code, list):
            source = outp_code[0]
            goal = float(outp_code[1])
            rate = float(outp_code[2])
            if source == 'Tprobe':
                self.set_probe_temperature(goal, rate)
            elif source == 'Magnet':
                self.now_magnet_setpoint = goal
                if self.step_model:     # step model, outp code 全为 list
                    self.set_field(goal, rate)
                    ramping_time = abs(goal-now_magnet) / rate * 60
                    self.lb_status.setText(f'to {goal:.4f} T, ramping')
                    # time.sleep(ramping_time)
                    now_magnet = float(self.pt_core.get_magnet())
                    overtime = int((20 + ramping_time) * 2.5)
                    # self.lb_status.setText('wait')
                    if_text_not_wait = True
                    for i in range(overtime):
                        if self.recipe_abort:
                            self.lb_status.setText('recipe abort')
                            return

                        if if_text_not_wait and (i > ramping_time * 2.5):
                            self.lb_status.setText(f'to {goal:.4f} T, waiting')
                            if_text_wait = False

                        if abs(goal - now_magnet) <= min_field_tolerance:
                            self.lb_status.setText('reached')
                            break
                        else:
                            time.sleep(0.4)
                        now_magnet = float(self.pt_core.get_magnet())
                    self.curr_meas_res[1] = now_magnet
                else:   # sweep model, outp code 只有第一下为list，设置磁场.
                    now_magnet = float(self.pt_core.get_magnet())
                    if goal - now_magnet > min_field_tolerance:
                        self.sweep_forward = 1
                    elif now_magnet - goal > min_field_tolerance:
                        self.sweep_forward = -1
                    else:
                        self.sweep_forward = 0
                        return
                    self.pt_core.scan_magnet_to_goal(goal, rate)
                    self.lb_status.setText(f'to {goal:.4f} T, rate {rate} T/m')
                    self.sweep_field_started = True
        else:   # sweep model, outp code 之后为Int，设置程序结束条件.
            now_magnet = float(self.pt_core.get_magnet())
            if self.sweep_forward == 1:
                if now_magnet >= self.now_magnet_setpoint:
                    self.status_window.signal_seqs_skip.emit()
                    self.pt_core.set_magnet_status('hold')

                    debug_str = f'field scan finished present={now_magnet}, ' \
                                f'set point = {self.now_magnet_setpoint}, forward'
                    self.logging_saver.append_log('debug_logging',
                                                  [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
                    self.sweep_field_started = False
            elif self.sweep_forward == -1:
                if now_magnet <= self.now_magnet_setpoint:
                    self.status_window.signal_seqs_skip.emit()
                    self.pt_core.set_magnet_status('hold')
                    debug_str = f'field scan finished present={now_magnet}, ' \
                                f'set point = {self.now_magnet_setpoint}, backward'
                    self.logging_saver.append_log('debug_logging',
                                                  [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
                    self.sweep_field_started = False

    def set_probe_temperature(self, goal, rate):
        self.pt_core.set_probe_and_vti_temperature(goal)
        if self.step_model:
            global now_probe_temperature, min_temperature_tolerance
            ramping_time = abs(goal - now_probe_temperature) / rate * 60
            self.lb_status.setText(f'to {goal:.4f} K, ramping')
            # time.sleep(ramping_time)
            now_probe_temperature = float(self.pt_core.get_probe_temperature())
            overtime = int((120 + ramping_time) * 2)
            if_text_not_wait = True
            for i in range(overtime):
                if self.recipe_abort:
                    self.lb_status.setText('aborted')
                    return

                if if_text_not_wait and (i > ramping_time * 2):
                    self.lb_status.setText(f'to {goal:.4f} K, waiting')
                    if_text_wait = False

                if abs(goal - now_probe_temperature) < min_temperature_tolerance:
                    self.lb_status.setText('reached')
                    break
                else:
                    time.sleep(0.5)
                now_probe_temperature = float(self.pt_core.get_probe_temperature())
            self.curr_meas_res[0] = now_probe_temperature

    def set_field(self, goal, rate):
        global now_magnet_rate, nows_magnet_setpoint
        try:
            if rate != now_magnet_rate:
                self.pt_core.set_magnet_rate(rate)
                now_magnet_rate = rate
        except Exception as e:
            debug_str = f'set magnet rate fialed because {repr(e)}'
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])

        try:
            self.pt_core.set_magnet(goal)
            nows_magnet_setpoint = goal
        except Exception as e:
            debug_str = f'set magnet set point fialed because {repr(e)}'
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])

        try:
            time.sleep(0.2)
            self.pt_core.set_magnet_status('to set')
        except Exception as e:
            debug_str = f'set magnet status because {repr(e)}'
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])

    def slot_control_button_clicked(self):
        self.get_setpoint_values()
        if not self.control.lock_thread.isRunning():
            self.control.show()
            self.control.lock_thread.start()
            self.control.sync_setpoint()
            self.control.program_closed = False

    def slot_warm_cool_clicked(self):
        self.sync_inst_status()
        self.ui_warmcool.sync_meas_res()
        self.ui_warmcool.show()

    def close_all_threading(self):
        self.program_closed = True
        self.auto_sync_thread.wait()
        if self.control.lock_thread.isRunning():
            self.control.program_closed = True
            self.control.lock_thread.wait()

    def slot_ramping_status_changed(self, text):
        self.lb_status.setText(text)

    def slot_recipe_abort(self):
        global nows_magnet_scan_status, now_probe_temperature
        if nows_magnet_scan_status != 'hold':
            self.pt_core.set_magnet_status('hold')
            nows_magnet_scan_status = self.pt_core.get_magnet_status()

        self.recipe_abort = True

    def slot_recipe_continue(self, pb):
        self.recipe_abort = False
        if pb == 'continue':
            global now_magnet, nows_magnet_scan_status, min_field_tolerance, nows_magnet_setpoint
            nows_magnet_setpoint = self.pt_core.get_magnet_setpoint()
            if self.now_magnet_setpoint != float(nows_magnet_setpoint):
                debug_str = f'可能在程序暂停过程中，改变了磁场set point, ' \
                            f'为了使程序正常继续，仍然将磁体扫到原来程序设定的磁场{self.now_magnet_setpoint}T'
                self.logging_saver.append_log('debug_logging',
                                              [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
                self.pt_core.set_magnet(self.now_magnet_setpoint)
            if abs(self.now_magnet_setpoint - now_magnet) > min_field_tolerance:
                self.pt_core.set_magnet_status('to set')
                nows_magnet_scan_status = self.pt_core.get_magnet_status()

    def get_now_outp(self, source):
        if source == 'Tprobe':
            return float(self.pt_core.get_probe_temperature())
        elif source == 'Magnet':
            return float(self.pt_core.get_magnet())

    def get_source_channel(self):
        return [[self.alias, 'Tprobe'], [self.alias, 'Magnet']]

    def slot_cb_collect_checked(self, id):
        if id == 0:
            self.if_meter_collect = False
        else:
            self.if_meter_collect = True
        self.collected_changed.emit()

    def slot_pause_mode_checked(self, id):
        if id == 0:
            self.step_model = False
            debug_str = '程序不会自动等待磁场/温度到达稳定'
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
        else:
            self.step_model = True

    def lock_instrument(self, lock_state=None):
        if lock_state is None:
            pass
        else:
            self.if_instrument_locked = lock_state

        if self.if_instrument_locked:
            self.cb_if_collect.setEnabled(False)
            self.cb_pause_mode.setEnabled(False)
        else:
            self.cb_if_collect.setEnabled(True)
            self.cb_pause_mode.setEnabled(True)

    def defineUi(self):
        self.resize(self.width(), self.height()-5)

        self.meas_Bz.setStyleSheet("color:red")
        self.meas_probeT.setStyleSheet("color:red")
        self.meas_magnetT.setStyleSheet("color:red")
        self.lb_alias.setText(self.alias)
        if len(self.resource_name) > 15:
            self.lb_address.setText(f'{self.resource_name[:10]}...')

    def check_seqs(self, source, start, goal, steps, ramp_speed, pause_time):
        global nows_probe_heater_auto, nows_vti_heater_auto, nows_ips_heater
        if self.if_check_seq_return_error:
            return [3, 'cannot start recipe because PT control dialog has locked the recipe']

        flag = 1
        err_str = ''
        if source == 'Tprobe':
            if nows_probe_heater_auto != 'ON' and nows_vti_heater_auto != 'ON':
                return [3, '不能用程序升温度，可能是probe heater处于手动模式']
            if steps > 1:
                flag = 3
                err_str = err_str.join("\t自动升温度步长不能超过1K\n")
            if (goal > self.max_temperature) or (goal < self.min_temperature):
                flag = 3
                err_str = err_str.join("\t温度不能超过%d K或者低于%d k；\n" % (self.max_temperature, self.min_temperature))
            if (ramp_speed > self.max_temperature_speed) or (ramp_speed <= 0):
                flag = 3
                err_str = err_str.join("\t升温速度不能超过%d K/min或者低于0；\n" % self.max_temperature_speed)
            _mod = steps % self.min_temperature_step
            if _mod > self.min_tolerance and abs(_mod - self.min_temperature_step) > self.min_tolerance:
                flag = 3
                err_str = err_str.join("\tSteps不是温度最小步长%.12g的整数倍；\n" % self.min_temperature_step)
        elif source == 'Magnet':
            if nows_ips_heater != 'ON':
                return [3, '不能加磁场，可能是IPS heater 没有打开']
            if (goal > self.max_field) or (goal < self.min_field):
                flag = 3
                err_str = err_str.join("\t磁场不能超过%.12g T或者低于%.12g T；\n" % (self.max_field, self.min_field))
            if (ramp_speed > self.max_field_speed) or (ramp_speed <= 0):
                flag = 3
                err_str = err_str.join("\t升场速度不能超过%.12g T/m或者低于0；\n" % self.max_field_speed)
            _mod = steps % self.min_field_step
            if _mod > self.min_tolerance and abs(_mod - self.min_field_step) > self.min_tolerance:
                flag = 3
                err_str = err_str.join("\tSteps不是磁场最小步长%.12g的整数倍；\n" % self.min_field_step)
        else:
            flag = 3
            err_str = err_str.join("\t不支持%s模式\n" % source)

        res = [flag, err_str]
        if flag > 1:
            return res
        else:
            if not self.step_model and source == 'Magnet':  # if work in sweep mode, pause to magnet to set
                # for magnet sweep model, the magnet code is
                # List[0]: ['Magnet', goal, ramp_speed]
                # List[i>0]: [i-1]
                sweep_seq = [source, goal, ramp_speed]
                wait_time = abs(goal - start) / ramp_speed * 60 * 1.1
                seq_array_code = [sweep_seq]
                for i in range(round(wait_time/pause_time)):
                    seq_array_code.append(i)
                return [flag, seq_array_code]
            else:
                # for temperature or magnet step model, the magnet code is
                # List[i]: [source, step[i], ramp_speed]
                if start >= goal:
                    seq_array = np.arange(start, goal, -1 * steps)
                    seq_array = np.append(seq_array, goal)
                else:
                    seq_array = np.arange(start, goal, steps)
                    seq_array = np.append(seq_array, goal)
                seq_array_code = []
                for sg_seq in seq_array:
                    seq_array_code.append([source, sg_seq, ramp_speed])
                return [flag, seq_array_code]


class AutoSyncThread(QThread):

    def __init__(self, pt_core, ui_widget, control, ui_warmcool):
        super(AutoSyncThread, self).__init__()
        self.pt_core = pt_core

        self.ui_widget = ui_widget
        self.control = control
        self.ui_warmcool = ui_warmcool
        self.sync_meas_stack = 0
        self.block_warning = 0
        self.block_error = 0
        self.stacked_logging = []
        # self.single_log = []
        self.titles = 'Time \t probe_temperature \t magnet \t vti_temperature \t magnet_temperature \t ' \
                      'probe_heater_power \t vti_heater_power \t nv \t pressure \n'
        try:
            with open('.systems/path/pt_logging_path.pkl', 'rb') as file:
                self.logging_path = pickle.load(file)
        except Exception as e:
            _path = self.get_logging_file_path()

            if _path is None:
                self.logging_path = './logging/teslatronPT_logging'
            else:
                self.logging_path = _path

    def get_logging_file_path(self):
        path = QFileDialog.getExistingDirectory(self.ui_widget, "选择teslatron PT logging文件路径", r'./logging/')
        if len(path) > 2:
            logging_path = path
            with open('.systems/path/pt_logging_path.pkl', 'wb') as file:
                pickle.dump(logging_path, file)
            return logging_path
        else:
            return None

    # def append_log(self, single_log):
    #     temp_str = ' \t '.join(single_log)
    #     self.stacked_logging.append(f'{temp_str} \n')
    #     self.save_logging()
    #
    # def save_logging(self):
    #     try:
    #         if len(self.stacked_logging) > 0:
    #             temp_logging = self.stacked_logging[:]
    #
    #             log_file_name = f"{self.logging_path}/{datetime.now().strftime('%Y-%m-%d')}.log"
    #             if os.path.exists(log_file_name):
    #                 with open(log_file_name, 'a') as file:
    #                     for row in temp_logging:
    #                         file.write(row)
    #                         self.stacked_logging.pop(0)
    #             else:
    #                 with open(log_file_name, 'w') as file:
    #                     file.write(self.titles)
    #                     for row in temp_logging:
    #                         file.write(row)
    #                         self.stacked_logging.pop(0)
    #     except Exception as e:
    #         print(e)

    def run(self):
        while True:
            if self.ui_widget.program_closed:
                break
            if self.block_error > 0:
                self.block_error -= 1
            if self.block_warning > 0:
                self.block_warning -= 1
            # print('sync pt')
            if self.ui_widget.pause_time_sync_setpoint == 0:
                self.ui_widget.get_setpoint_values()
                self.control.sync_setpoint()
            elif self.ui_widget.pause_time_sync_status == 0:
                self.ui_widget.sync_inst_status()
                self.ui_widget.sync_meas_res()
                self.control.sync_status()
                self.ui_widget.pause_time_sync_setpoint -= 1
            else:
                self.ui_widget.inst_read()
                self.ui_widget.sync_meas_res()
                self.ui_warmcool.sync_meas_res()
                self.control.sync_meas()
                self.ui_widget.pause_time_sync_setpoint -= 1
                self.ui_widget.pause_time_sync_status -= 1

            self.msleep(1000)


class TeslaPTControl(QWidget, Ui_control):

    def __init__(self, pt_core, ui_widget):
        super(TeslaPTControl, self).__init__()
        self.if_ips_enabled = True
        self.setupUi(self)
        self.program_closed = False
        self.block_close_event = False
        self.sync_control_text_lock = threading.RLock()
        self.ui_widget = ui_widget
        self.logging_saver = ui_widget.log_saver
        self.alias = f"{ui_widget.alias} - control window"

        self.pt_core = pt_core
        self.vti_dict = {
            'pt_core': pt_core,
            'pb_toset': self.pb_scan_temp_2,
            'rb_off': self.rb_itc_heater_off_2,
            'rb_on': self.rb_itc_heater_on_2,
            'manu_res': self.lb_itc_heater_2,
            'manu_set': self.le_itc_heater_set_2,
            'auto_res': self.lb_itc_temp_2,
            'auto_set': self.le_itc_temp_set_2,
            'fun_get_manu': self.pt_core.get_vti_heater_power,
            'fun_set_manu': self.pt_core.set_vti_heater_power,
            'fun_get_auto': self.pt_core.get_vti_temperature_setpoint,
            'fun_get_setpoint': self.pt_core.get_vti_temperature_setpoint,
            'fun_set_auto': self.pt_core.set_vti_temperature,
            'fun_get_auto_status': self.pt_core.get_vti_heater_auto,
            'fun_switch_auto': self.pt_core.set_vti_heater_auto
        }
        self.vti_group = ControlSubGroup(self.vti_dict, self)

        self.probe_dict = {
            'pt_core': pt_core,
            'pb_toset': self.pb_scan_temp,
            'rb_off': self.rb_itc_heater_off,
            'rb_on': self.rb_itc_heater_on,
            'manu_res': self.lb_itc_heater,
            'manu_set': self.le_itc_heater_set,
            'auto_res': self.lb_itc_temp,
            'auto_set': self.le_itc_temp_set,
            'fun_get_manu': self.pt_core.get_probe_heater_power,
            'fun_set_manu': self.pt_core.set_probe_heater_power,
            'fun_get_auto': self.pt_core.get_probe_temperature_setpoint,
            'fun_get_setpoint': self.pt_core.get_probe_temperature_setpoint,
            'fun_set_auto': self.pt_core.set_probe_temperature,
            'fun_get_auto_status': self.pt_core.get_probe_heater_auto,
            'fun_switch_auto': self.pt_core.set_probe_heater_auto
        }
        self.probe_group = ControlSubGroup(self.probe_dict, self)

        self.pool_dict = {
            'pt_core': pt_core,
            'pb_toset': self.pb_scan_temp_3,
            'rb_off': self.rb_itc_heater_off_3,
            'rb_on': self.rb_itc_heater_on_3,
            'manu_res': self.lb_itc_heater_3,
            'manu_set': self.le_itc_heater_set_3,
            'auto_res': self.lb_itc_temp_3,
            'auto_set': self.le_itc_temp_set_3,
            'fun_get_manu': self.pt_core.get_1k_pool_nv,
            'fun_set_manu': self.pt_core.set_1k_pool_nv,
            'fun_get_auto': self.pt_core.get_1k_pool_pressure,
            'fun_get_setpoint': self.pt_core.get_1k_pool_pressure_setpoint,
            'fun_set_auto': self.pt_core.set_1k_pool_pressure,
            'fun_get_auto_status': self.pt_core.get_1k_pool_nv_auto,
            'fun_switch_auto': self.pt_core.set_1k_pool_nv_auto
        }
        self.pool_group = ControlSubGroup(self.pool_dict, self)

        # IPS
        self.ips_heater_group = QButtonGroup(self)
        self.ips_heater_group.addButton(self.rb_ips_heater_on, 1)
        self.ips_heater_group.addButton(self.rb_ips_heater_off, 2)
        self.rb_ips_heater_on.clicked.connect(self.slot_ips_heater_changed)
        self.rb_ips_heater_off.clicked.connect(self.slot_ips_heater_changed)
        self.pb_scan_field.clicked.connect(self.slot_scan_field)
        self.pb_abort_field.clicked.connect(self.slot_abort_field)

        # lock
        self.lock_thread = LockControlWindow(self)
        # self.lock_thread.start()

        self.pb_sync.clicked.connect(self.sync_setpoint_data_and_text)

    def closeEvent(self, event):
        if self.block_close_event:
            event.ignore()
        else:
            self.program_closed = True
            self.lock_thread.wait()
            event.accept()

    def sync_setpoint_data_and_text(self):
        self.ui_widget.get_setpoint_values()
        self.sync_setpoint()

    def slot_ips_heater_changed(self):
        check_id = self.ips_heater_group.checkedId()
        info_str = ''
        if check_id == 1:
            self.pt_core.set_ips_heater('ON')
            info_str = '打开ips heater'
        elif check_id == 2:
            self.pt_core.set_ips_heater('OFF')
            info_str = '关闭ips heater'
        self.lb_status.setText(info_str)
        self.lock_thread.lock_time_ips = 300

    def slot_scan_field(self):
        try:
            global now_magnet_rate, nows_magnet_setpoint
            goal = float(self.le_field_set.text())
            rate = float(self.le_field_rate.text())

            nows_magnet_setpoint = self.pt_core.get_magnet_setpoint()
            now_magnet_rate = float(self.pt_core.get_magnet_rate())

            if goal != float(nows_magnet_setpoint):
                self.pt_core.set_magnet(goal)

            if rate != now_magnet_rate:
                self.pt_core.set_magnet_rate(rate)

            self.pt_core.set_magnet_status('to set')

        except Exception as e:
            debug_str = repr(e)
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])

    def slot_abort_field(self):
        self.pt_core.set_magnet_status('hold')

    def ips_setEnabled(self, flag):
        self.if_ips_enabled = flag
        self.rb_ips_heater_on.setEnabled(flag)
        self.rb_ips_heater_off.setEnabled(flag)
        self.le_field_set.setEnabled(flag)
        self.le_field_rate.setEnabled(flag)
        self.pb_scan_field.setEnabled(flag)
        self.pb_abort_field.setEnabled(flag)

    def sync_ips_meas(self):
        self.sync_control_text_lock.acquire()
        global min_field_tolerance
        global now_current_field, now_magnet
        self.lb_c_field.setText(str(now_current_field))
        self.lb_p_field.setText(str(now_magnet))
        if abs(now_current_field) < min_field_tolerance and abs(now_magnet) < min_field_tolerance:
            if self.if_ips_enabled:
                self.rb_ips_heater_on.setEnabled(True)
                self.rb_ips_heater_off.setEnabled(True)
        else:
            self.rb_ips_heater_on.setEnabled(False)
            self.rb_ips_heater_off.setEnabled(False)
        self.sync_control_text_lock.release()

    def sync_ips_status(self):
        self.rb_ips_heater_on.blockSignals(True)
        self.rb_ips_heater_off.blockSignals(True)
        self.sync_control_text_lock.acquire()
        global nows_ips_heater
        if nows_ips_heater == 'ON':
            self.rb_ips_heater_on.setChecked(True)
            if self.lock_thread.lock_time_ips <= 0:
                if self.if_ips_enabled:
                    self.pb_scan_field.setEnabled(True)
                    self.pb_abort_field.setEnabled(True)
        else:
            self.rb_ips_heater_off.setChecked(True)
            self.pb_scan_field.setEnabled(False)
            self.pb_abort_field.setEnabled(False)
        self.sync_ips_meas()
        self.sync_control_text_lock.release()
        self.rb_ips_heater_on.blockSignals(False)
        self.rb_ips_heater_off.blockSignals(False)

    def sync_ips_setpoint(self):
        self.sync_control_text_lock.acquire()
        global nows_magnet_setpoint, now_magnet_rate
        self.le_field_rate.setText(str(now_magnet_rate))
        self.le_field_set.setText(nows_magnet_setpoint)
        self.sync_ips_status()
        self.sync_control_text_lock.release()

    def sync_itc_setpoint(self):
        self.sync_control_text_lock.acquire()
        global nows_probe_heater_power, now_probe_temperature, nows_probe_heater_auto,  nows_probe_temperature_setpoint,\
            nows_vti_heater_power, now_vti_temperature, nows_vti_heater_auto,  nows_vti_temperature_setpoint, \
            nows_pool_nv, nows_pool_pressure, nows_pool_nv_auto, nows_pool_pressure_setpoint
        self.vti_group.sync_setpoint([nows_vti_heater_power, now_vti_temperature,
                                      nows_vti_heater_auto, nows_vti_temperature_setpoint])
        self.probe_group.sync_setpoint(([nows_probe_heater_power, now_probe_temperature,
                                         nows_probe_heater_auto,  nows_probe_temperature_setpoint]))
        self.pool_group.sync_setpoint(([nows_pool_nv, nows_pool_pressure,
                                        nows_pool_nv_auto, nows_pool_pressure_setpoint]))
        self.sync_control_text_lock.release()

    def sync_itc_status(self):
        self.sync_control_text_lock.acquire()
        global nows_probe_heater_power, now_probe_temperature, nows_probe_heater_auto, nows_probe_temperature_setpoint, \
            nows_vti_heater_power, now_vti_temperature, nows_vti_heater_auto, nows_vti_temperature_setpoint, \
            nows_pool_nv, nows_pool_pressure, nows_pool_nv_auto, nows_pool_pressure_setpoint
        self.vti_group.sync_status([nows_vti_heater_power, now_vti_temperature,
                                    nows_vti_heater_auto])
        self.probe_group.sync_status(([nows_probe_heater_power, now_probe_temperature,
                                       nows_probe_heater_auto]))
        self.pool_group.sync_status(([nows_pool_nv, nows_pool_pressure,
                                      nows_pool_nv_auto]))
        self.sync_control_text_lock.release()

    def sync_itc_meas(self):
        self.sync_control_text_lock.acquire()
        global nows_probe_heater_power, now_probe_temperature, nows_probe_heater_auto, nows_probe_temperature_setpoint, \
            nows_vti_heater_power, now_vti_temperature, nows_vti_heater_auto, nows_vti_temperature_setpoint, \
            nows_pool_nv, nows_pool_pressure, nows_pool_nv_auto, nows_pool_pressure_setpoint
        self.vti_group.sync_meas([nows_vti_heater_power, now_vti_temperature])
        self.probe_group.sync_meas(([nows_probe_heater_power, now_probe_temperature]))
        self.pool_group.sync_meas(([nows_pool_nv, nows_pool_pressure]))
        self.sync_control_text_lock.release()

    def sync_setpoint(self):
        self.sync_ips_setpoint()
        self.sync_itc_setpoint()

    def sync_status(self):
        self.sync_ips_status()
        self.sync_itc_status()

    def sync_meas(self):
        self.sync_ips_meas()
        self.sync_itc_meas()


class ControlSubGroup:

    def __init__(self, group_dict, control):
        self.set_point_object = group_dict['manu_set']
        self.control = control
        self.pt_core = group_dict['pt_core']
        self.group_dict = group_dict
        self.rb_group = QButtonGroup(control)
        self.rb_on = group_dict['rb_on']
        self.rb_off = group_dict['rb_off']
        self.pb_toset = group_dict['pb_toset']
        self.rb_group.addButton(self.rb_on, 1)
        self.rb_group.addButton(self.rb_off, 2)
        self.rb_on.clicked.connect(self.slot_rb_changed)
        self.rb_off.clicked.connect(self.slot_rb_changed)
        self.pb_toset.clicked.connect(self.to_set)
        self.if_itc_enalbed = True
        self.if_auto = True

    def setEnabled(self, flag):
        self.if_itc_enalbed = flag
        self.group_dict['rb_on'].setEnabled(flag)
        self.group_dict['rb_off'].setEnabled(flag)
        self.group_dict['pb_toset'].setEnabled(flag)
        self.group_dict['manu_set'].setEnabled(flag)
        self.group_dict['auto_res'].setEnabled(flag)

    def slot_rb_changed(self):
        checkid = self.rb_group.checkedId()
        if checkid == 1:
            self.group_dict['fun_switch_auto']('ON')
            if self.if_itc_enalbed:
                self.group_dict['auto_set'].setEnabled(True)
            self.group_dict['manu_set'].setEnabled(False)
            self.if_auto = True
            self.set_point_object = self.group_dict['auto_set']
        elif checkid == 2:
            self.group_dict['fun_switch_auto']('OFF')
            self.group_dict['auto_set'].setEnabled(False)
            if self.if_itc_enalbed:
                self.group_dict['manu_set'].setEnabled(True)
            self.if_auto = False
            self.set_point_object = self.group_dict['manu_set']

    def to_set(self):
        goal = float(self.set_point_object.text())
        if self.if_auto:
            self.group_dict['fun_set_auto'](goal)
        else:
            self.group_dict['fun_set_manu'](goal)

    def sync_meas(self, res_ls):
        self.group_dict['manu_res'].setText(str(res_ls[0]))
        self.group_dict['auto_res'].setText(str(res_ls[1]))

    def sync_status(self, res_ls):
        self.rb_on.blockSignals(True)
        self.rb_off.blockSignals(True)
        if res_ls[2] == 'ON':
            self.rb_on.setChecked(True)
            self.if_auto = True
            self.set_point_object = self.group_dict['auto_set']
        elif res_ls[2] == 'OFF':
            self.rb_off.setChecked(True)
            self.if_auto = False
            self.set_point_object = self.group_dict['manu_set']
        self.rb_on.blockSignals(False)
        self.rb_off.blockSignals(False)
        self.sync_meas(res_ls[:2])

    def sync_setpoint(self, res_ls):
        self.group_dict['manu_set'].setText(str(res_ls[0]))
        self.group_dict['auto_set'].setText(str(res_ls[3]))
        self.sync_status(res_ls[:3])


class LockControlWindow(QThread):

    def __init__(self, control):
        super(LockControlWindow, self).__init__()
        self.control = control
        self.lock_time_ips = 0
        self.lock_time_probe = 0
        self.lock_time_vti = 0
        self.lock_time_1k_pool = 0
        self.lock_time_angle = 0
        self.lock_ips = False
        self.lock_probe = False
        self.lock_vti = False
        self.lock_1k_pool = False
        self.lock_angle = False

    def run(self):
        while True:
            if self.control.program_closed:
                break

            if self.lock_time_ips > 0:   # 需要锁定ips
                if not self.lock_ips:   # 如果没有锁定Ips
                    self.control.ips_setEnabled(False)
                    self.control.block_close_event = True
                    self.control.ui_widget.if_check_seq_return_error = True
                    self.lock_ips = True
                self.lock_time_ips -= 1
                self.control.lb_status.setText(f'开关ips heater, 等待 {self.lock_time_ips} s')
            else:
                if self.lock_ips:
                    self.control.ips_setEnabled(True)
                    self.control.block_close_event = False
                    self.control.ui_widget.if_check_seq_return_error = False
                    self.lock_ips = False

            if self.lock_time_probe > 0:
                if not self.lock_probe:
                    self.control.probe_group.setEnabled(False)
                    self.lock_probe = True
                self.lock_time_probe -= 1
            else:
                if self.lock_probe:
                    self.control.probe_group.setEnabled(True)
                    self.lock_probe = False

            if self.lock_time_vti > 0:
                if not self.lock_vti:
                    self.control.vti_group.setEnabled(False)
                    self.lock_vti = True
                self.lock_time_vti -= 1
            else:
                if self.lock_vti:
                    self.control.vti_group.setEnabled(True)
                    self.lock_vti = False

            if self.lock_time_1k_pool > 0:
                if not self.lock_1k_pool:
                    self.control.pool_group.setEnabled(False)
                    self.lock_1k_pool = True
                self.lock_time_1k_pool -= 1
            else:
                if self.lock_1k_pool:
                    self.control.pool_group.setEnabled(True)
                    self.lock_1k_pool = False

            self.sleep(1)


class TeslaPTWarmCool(QWidget, Ui_WarmCool):

    def __init__(self, pt_core, ui_widget):
        super(TeslaPTWarmCool, self).__init__()
        self.sync_meas_lock = threading.Lock()
        self.pt_core = pt_core
        self.ui_widget = ui_widget
        self.logging_saver = ui_widget.log_saver
        self.alias = f"{ui_widget.alias} warm cool widget"

        self.setupUi(self)
        self.le_press_ls = [self.le_press_1, self.le_press_2, self.le_press_3, self.le_press_4, self.le_press_5]
        self.le_heater_ls = [self.le_heater_1, self.le_heater_2, self.le_heater_3, self.le_heater_4, self.le_heater_5]
        self.le_wpress_ls = [self.le_wpress_1, self.le_wpress_2, self.le_wpress_3, self.le_wpress_4, self.le_wpress_5]
        self.defineUi()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.block_close_event = False
        self.abort_warm_cool = False
        self.warm_cool_thread = WarmCoolThread()

        self.pb_abort.clicked.connect(self.slot_abort)
        self.pb_cool.clicked.connect(self.slot_cool_down)
        self.pb_warm.clicked.connect(self.slot_warm_up)
        self.status_Text = ""
        self.meas_ls = [0.0, 0.0, 0.0, 1.0]
        # self.sync_self_thread = AutoSyncWarmCoolDialog(self)
        # self.warm_up_thread = WarmUpThread(self)
        # self.cool_down_thread = CoolDownThread(self)

    def slot_warm_up(self):
        self.warm_cool_thread.default_fun = self.warm_up
        if not self.warm_cool_thread.isRunning():
            self.warm_cool_thread.start()

    def slot_cool_down(self):
        self.warm_cool_thread.default_fun = self.cool_down
        if not self.warm_cool_thread.isRunning():
            self.warm_cool_thread.start()

    def sync_meas_res(self):
        self.sync_meas_lock.acquire()
        global curr_meas_str
        self.meas_probeT.setText(f'{curr_meas_str[0]} K')
        self.meas_Bz.setText(f'{curr_meas_str[1]} T')
        self.meas_vtiT.setText(f'{curr_meas_str[2]} K')
        self.meas_magnetT.setText(f'{curr_meas_str[3]} K')
        self.sync_meas_lock.release()
        self.lb_status.setText(self.status_Text)

    def defineUi(self):
        try:
            with open('./system/teslaPT_warm_cool.pkl', 'rb') as file:
                data_ls = pickle.load(file)
        except FileNotFoundError:
            data_ls = [['20', '10', '10', '10', '2.9'],
                       ['25', '20', '15', '10', '5'],
                       ['0.01', '0.01', '1', '1', '2.9']]
        for i in range(5):
            self.le_press_ls[i].setText(data_ls[0][i])
            self.le_press_ls[i].editingFinished.connect(self.slot_data_ls_changed)
            self.le_heater_ls[i].setText(data_ls[1][i])
            self.le_heater_ls[i].editingFinished.connect(self.slot_data_ls_changed)
            self.le_wpress_ls[i].setText(data_ls[2][i])
            self.le_wpress_ls[i].editingFinished.connect(self.slot_data_ls_changed)

    def set_warm_cool_enabled(self, flag):
        for i in range(5):
            self.le_press_ls[i].setEnabled(flag)
            self.le_heater_ls[i].setEnabled(flag)
            self.le_wpress_ls[i].setEnabled(flag)
        self.pb_cool.setEnabled(flag)
        self.pb_warm.setEnabled(flag)

    def slot_data_ls_changed(self):
        data_ls = [[], [], []]
        for i in range(5):
            data_ls[0].append(self.le_press_ls[i].text())
            data_ls[1].append(self.le_heater_ls[i].text())
            data_ls[2].append(self.le_wpress_ls[i].text())
        with open('./system/teslaPT_warm_cool.pkl', 'wb') as file:
            pickle.dump(data_ls, file)

    def slot_abort(self):
        self.abort_warm_cool = True

    def closeEvent(self, event):
        if self.block_close_event:
            QMessageBox.warning(self, '正在控制设备，不能关闭此窗口', '需要等到程序正常结束，或者abort')
            event.ignore()
        else:
            event.accept()
            # self.calling_window.control_dialog_opening = False

    def warm_up(self):
        self.status_Text = ""
        press_list = []
        heater_list = []
        try:
            for i in range(5):
                heater_list.append(float(self.le_heater_ls[i].text()))
                press_list.append(float(self.le_wpress_ls[i].text()))
        except Exception as e:
            debug_str = repr(e)
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
            self.status_Text = self.status_Text + '输入heater数值有误\n'
            return

        for i in range(10):
            self.status_Text = f'{10-i} s 之后开始升温，按abort 停止'
            if self.abort_warm_cool:
                # 手动结束
                self.status_Text = self.status_Text + '升降温手动结束....\n'
                self.block_close_event = False
                self.set_warm_cool_enabled(True)
                self.abort_warm_cool = False
                return
        self.status_Text = ""

        global now_magnet, now_probe_temperature, now_vti_temperature
        if abs(now_magnet) > 0.001:
            QMessageBox.warning(self, '不能升降温', '磁场没有归零，不能升降温')
            return
        self.status_Text = self.status_Text + '开始升温到300k\n'

        self.block_close_event = True
        debug_str = f"the heater list is: {repr(heater_list)}"
        self.logging_saver.append_log('debug_logging',
                                      [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
        self.set_warm_cool_enabled(False)
        # 开始升温
        self.pt_core.set_probe_heater_auto('OFF')
        self.pt_core.set_vti_heater_auto('OFF')

        counts = 100
        for i in range(400000):
            time.sleep(1)
            if self.abort_warm_cool:
                # 手动结束
                self.status_Text = self.status_Text + '升降温手动结束....\n'
                self.block_close_event = False
                self.set_warm_cool_enabled(True)
                self.abort_warm_cool = False
                return

            if now_vti_temperature >= 290:
                self.pt_core.set_vti_heater_auto('ON')
                self.pt_core.set_vti_temperature(295)
                self.status_Text = self.status_Text + 'probe 温度目标值设定为 300K;\n'
                self.pt_core.set_probe_heater_auto('ON')
                self.pt_core.set_probe_temperature(300)
                self.status_Text = self.status_Text + 'probe 温度目标值设定为 295K;\n'
                break
            elif now_vti_temperature >= 170:
                if counts != 0:
                    counts = 0
                    self.pt_core.set_vti_heater_power(heater_list[counts])
                    self.pt_core.set_probe_heater_power(heater_list[counts])
                    self.status_Text = self.status_Text + 'vti与probe heater功率设置为 %.4f%%;\n' % heater_list[counts]
                    self.pt_core.set_1k_pool_pressure(press_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % press_list[counts]
            elif now_vti_temperature >= 70:
                if counts != 1:
                    counts = 1
                    self.pt_core.set_vti_heater_power(heater_list[counts])
                    self.pt_core.set_probe_heater_power(heater_list[counts])
                    self.status_Text = self.status_Text + 'vti与probe heater功率设置为 %.4f%%;\n' % heater_list[counts]
                    self.pt_core.set_1k_pool_pressure(press_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % press_list[counts]
            elif now_vti_temperature >= 20:
                if counts != 2:
                    counts = 2
                    self.pt_core.set_vti_heater_power(heater_list[counts])
                    self.pt_core.set_probe_heater_power(heater_list[counts])
                    self.status_Text = self.status_Text + 'vti与probe heater功率设置为 %.4f%%;\n' % heater_list[counts]
                    self.pt_core.set_1k_pool_pressure(press_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % press_list[counts]
            elif now_vti_temperature >= 5:
                if counts != 3:
                    counts = 3
                    self.pt_core.set_vti_heater_power(heater_list[counts])
                    self.pt_core.set_probe_heater_power(heater_list[counts])
                    self.status_Text = self.status_Text + 'vti与probe heater功率设置为 %.4f%%;\n' % heater_list[counts]
                    self.pt_core.set_1k_pool_pressure(press_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % press_list[counts]
            else:
                if counts != 4:
                    counts = 4
                    self.pt_core.set_vti_heater_power(heater_list[counts])
                    self.pt_core.set_probe_heater_power(heater_list[counts])
                    self.status_Text = self.status_Text + 'vti与probe heater功率设置为 %.4f%%;\n' % heater_list[counts]
                    self.pt_core.set_1k_pool_pressure(press_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % press_list[counts]

                    break

        self.status_Text = self.status_Text + '升温结束....\n'
        self.block_close_event = False
        self.set_warm_cool_enabled(True)

    def cool_down(self):
        self.status_Text = ""
        cool_list = []
        press_text = [self.le_press_1.text(), self.le_press_2.text(),
                      self.le_press_3.text(), self.le_press_4.text(), self.le_press_5.text()]
        try:
            for text in press_text:
                temp_pressure = float(text)
                cool_list.append(temp_pressure)

        except Exception as e:
            debug_str = repr(e)
            self.logging_saver.append_log('debug_logging',
                                          [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
            self.status_Text = self.status_Text + '输入pressure数值有误....\n'
            return
        self.status_Text = self.status_Text + '开始降温到base....\n'

        self.block_close_event = True

        debug_str = f"the cooling list is: {repr(cool_list)}"
        self.logging_saver.append_log('debug_logging',
                                      [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.alias, debug_str])
        self.set_warm_cool_enabled(False)
        for i in range(10):
            self.status_Text = f'{10-i} s 之后开始降温，按abort 停止'
            if self.abort_warm_cool:
                # 手动结束
                self.status_Text = self.status_Text + '升降温手动结束....\n'
                self.block_close_event = False
                self.set_warm_cool_enabled(True)
                self.abort_warm_cool = False
                return
        self.status_Text = ""

        global now_vti_temperature, now_probe_temperature

        self.pt_core.set_vti_heater_auto('ON')
        self.pt_core.set_vti_temperature(1.2)
        self.status_Text = self.status_Text + 'probe heater 设置为自动, 目标为1.2K;\n'
        self.pt_core.set_probe_heater_auto('ON')
        self.pt_core.set_probe_temperature(1.2)
        self.status_Text = self.status_Text + 'vti heater 设置为自动, 目标为1.2K;\n'
        self.pt_core.set_1k_pool_nv_auto('ON')
        self.status_Text = self.status_Text + '针阀设置为自动....\n'
        counts = 100
        for i in range(400000):
            time.sleep(1)
            if self.abort_warm_cool:
                # 手动结束
                self.status_Text = self.status_Text + '升降温手动结束....\n'
                self.block_close_event = False
                self.set_warm_cool_enabled(True)
                self.abort_warm_cool = False
                return
            if now_vti_temperature >= 170:
                if counts != 0:
                    counts = 0
                    self.pt_core.set_1k_pool_pressure(cool_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % cool_list[counts]
            elif now_vti_temperature >= 70:
                if counts != 1:
                    counts = 1
                    self.pt_core.set_1k_pool_pressure(cool_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % cool_list[counts]
            elif now_vti_temperature >= 20:
                if counts != 2:
                    counts = 2
                    self.pt_core.set_1k_pool_pressure(cool_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % cool_list[counts]
            elif now_vti_temperature >= 5:
                if counts != 3:
                    counts = 3
                    self.pt_core.set_1k_pool_pressure(cool_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % cool_list[counts]
            else:
                if counts != 4:
                    counts = 4
                    self.pt_core.set_1k_pool_pressure(cool_list[counts])
                    self.status_Text = self.status_Text + 'pressure设置为：%.4f mbar;\n' % cool_list[counts]
                    break

        # 降温结束
        self.status_Text = self.status_Text + '降温结束....\n'
        self.block_close_event = False
        self.set_warm_cool_enabled(True)


class WarmCoolThread(QThread):

    def __init__(self):
        super(WarmCoolThread, self).__init__()
        self.default_fun = None

    def run(self):
        if self.default_fun is None:
            return
        else:
            self.default_fun()

        self.default_fun = None



