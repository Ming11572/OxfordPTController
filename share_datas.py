from threading import Lock
from PySide6.QtCore import Signal, QObject, QThread, Slot
from teslapt_core import TeslaPTCore
from time import time


class DataCenter(QThread):
    signal_magnet_temp_alarmed = Signal(int)    # 磁场温度超过预警时发送，1为alarm，需要注意，2为达到max，需要立即，缓慢地降磁场。
    signal_magnet_exciting_error = Signal(bool)     # 当磁场开关与线圈磁场数值相差太大时，会disable ips heater 开关
    signal_system_datas = Signal(tuple)
    signal_logs = Signal(str)

    def __init__(self, pt_core):
        super().__init__()
        self.pt_core: TeslaPTCore = pt_core  # 用于与设备通讯，读取或写入设备状态
        self.lock_optimally_code = Lock()
        self.flag_optimally_code = False
        self.min_field_tol = self.pt_core.magnet_ls[-1]

        self.probe_sensor = 'high'

        self.thread_lock = Lock()
        self.running = False
        self.max_errors = 100

        self.data_lock = Lock()     #
        self._pt_datas = {      # 制冷机实现参数，磁场，温度等，使用较高的同步速率 （~0.2s一次 ）
            "magnet": 0.0,      # 磁场， 单位为T
            "switch_magnet": 0.0,  # 磁体开关电流对应的磁场
            "magnet_status": "hold",    # 磁场状态，hold, to set, to zero
            "magnet_temperature": 3.3,  # 磁体温度
            "probe_temperature": 3.3,   # 样品杆温度
            "vti_temperature": 3.3,     # vti温度
        }

        self.setpoint_lock = Lock()
        self._pt_setpoints = {  # 制冷机设定参数，如磁场设定，温度设定等，同步速率稍慢（大于1.2s一次）
            "magnet_goal": 0,
            "magnet_rate": 0.2,     # 单位为T/min
            "ips_heater_status": "OFF",   # ON / OFF
            "probe_goal": 1.7,          # 样品杆设定温度
            "probe_heater_power": 0.2,  # 样品杆加热功率
            "probe_heater_status": "A", # 样品杆加热器状态，A为自动，M为手动
            "vti_goal": 1.7,            # vti，下同
            "vti_heater_power": 0.2,
            "vti_heater_status": "A",
            "nv_pressure": 5,       # nv当前气压，单位mbar
            "nv_pressure_goal": 5,  # nv pressure 设定值，单位mbar
            "nv_angle": 10,         # nv开角
            "nv_status": "A",       # nv出口出气调节方式，A为自动，M为手动
            "sorb_temperature": 10.0,
            "sorb_goal": 1.0,
            "sorb_heater": 1.0,
            "sorb_status": "A",
            "pt1_temperature": 3.3, #
            "pt2_temperature": 3.3,
        }

    def update_probe_temp_and_magnet(self):
        with self.data_lock:
            probe_data = float(self.pt_core.get_probe_temperature())
            self._pt_datas["probe_temperature"] = probe_data
            self._pt_datas["magnet"] = float(self.pt_core.get_magnet())
            self._pt_datas["switch_magnet"] = float(self.pt_core.get_current_field())

        if probe_data < 1.45 and self.probe_sensor == "high":
            self.pt_core.use_low_temperature_sensor(True)
            self.probe_sensor = 'low'
        if probe_data > 1.5 and self.probe_sensor == 'low':
            self.pt_core.use_low_temperature_sensor(False)
            self.probe_sensor = 'high'

    def optimally_code_passed(self, flag):
        with self.lock_optimally_code:
            self.flag_optimally_code = flag

    def update_other_pt_datas(self):
        with self.data_lock:
            self._pt_datas["magnet_temperature"] = float(self.pt_core.get_magnet_temperature())
            self._pt_datas["magnet_status"] = self.pt_core.get_magnet_status()
            self._pt_datas["vti_temperature"] = float(self.pt_core.get_vti_temperature())

    def update_pt_setpoints(self):
        with self.setpoint_lock:
            self._pt_setpoints["magnet_goal"] = float(self.pt_core.get_magnet_setpoint())
            self._pt_setpoints["magnet_rate"] = float(self.pt_core.get_magnet_rate())
            self._pt_setpoints["ips_heater_status"] = self.pt_core.get_ips_heater()  # ON / OFF
            with self.lock_optimally_code:
                if self.flag_optimally_code:
                    return
            self._pt_setpoints["probe_goal"] = float(self.pt_core.get_probe_temperature_setpoint())
            self._pt_setpoints["probe_heater_power"] = float(self.pt_core.get_probe_heater_power())
            self._pt_setpoints["probe_heater_status"] = self.pt_core.get_probe_heater_auto()  # ON / OFF
            with self.lock_optimally_code:
                if self.flag_optimally_code:
                    return
            self._pt_setpoints["vti_goal"] = float(self.pt_core.get_vti_temperature_setpoint())
            self._pt_setpoints["vti_heater_power"] = float(self.pt_core.get_vti_heater_power())
            self._pt_setpoints["vti_heater_status"] = self.pt_core.get_vti_heater_auto()  # ON / OFF
            with self.lock_optimally_code:
                if self.flag_optimally_code:
                    return
            self._pt_setpoints["nv_pressure"] = float(self.pt_core.get_1k_pool_pressure())
            self._pt_setpoints["nv_pressure_goal"] = float(self.pt_core.get_1k_pool_pressure_setpoint())
            self._pt_setpoints["nv_angle"] = float(self.pt_core.get_1k_pool_nv())
            self._pt_setpoints["nv_status"] = self.pt_core.get_1k_pool_nv_auto()  # ON / OFF
            with self.lock_optimally_code:
                if self.flag_optimally_code:
                    return
            self._pt_setpoints["sorb_temperature"] = float(self.pt_core.get_sorb_temperature())
            self._pt_setpoints["sorb_goal"] = float(self.pt_core.get_sorb_temperature_setpoint())
            self._pt_setpoints["sorb_heater"] = float(self.pt_core.get_sorb_heater_power())
            self._pt_setpoints["sorb_status"] = self.pt_core.get_sorb_heater_auto()
            with self.lock_optimally_code:
                if self.flag_optimally_code:
                    return
            self._pt_setpoints["pt1_temperature"] = float(self.pt_core.get_pt1())
            self._pt_setpoints["pt2_temperature"] = float(self.pt_core.get_pt2())

    # 获取所有vti, probe, 磁体温度，主要升降温的时候需要用到
    def get_temperature_and_magnet(self):
        with self.data_lock and self.setpoint_lock:
            return (self._pt_datas["magnet_temperature"], self._pt_datas["vti_temperature"],
                    self._pt_datas["probe_temperature"], self._pt_setpoints["pt1_temperature"],
                    self._pt_setpoints["pt2_temperature"], self._pt_datas["magnet"], self._pt_datas["switch_magnet"],
                    self._pt_setpoints["magnet_goal"], self._pt_setpoints["magnet_rate"],
                    self._pt_setpoints["probe_goal"], self._pt_setpoints["probe_heater_power"],
                    self._pt_setpoints["vti_goal"], self._pt_setpoints["vti_heater_power"],
                    self._pt_setpoints["nv_pressure"], self._pt_setpoints["nv_pressure_goal"],
                    self._pt_setpoints["nv_angle"], self._pt_setpoints["sorb_temperature"],
                    self._pt_setpoints["sorb_goal"], self._pt_setpoints["sorb_heater"])

    def get_magnet_and_heater_status(self):
        with self.data_lock and self.setpoint_lock:
            return (self._pt_datas["magnet_status"], self._pt_setpoints["ips_heater_status"],
                    self._pt_setpoints["probe_heater_status"], self._pt_setpoints["vti_heater_status"],
                    self._pt_setpoints["nv_status"], self._pt_setpoints["sorb_status"])

    def get_magnet_temperature(self):
        with self.data_lock:
            return self._pt_datas["magnet_temperature"]

    def get_probe_and_magnet(self):
        with self.data_lock:
            return self._pt_datas["probe_temperature"], self._pt_datas["magnet"]

    def get_probe_temp(self):
        with self.data_lock:
            return self._pt_datas["probe_temperature"]

    def get_warm_up_datas(self):
        with self.data_lock and self.setpoint_lock:
            return self._pt_datas["probe_temperature"], self._pt_datas["vti_temperature"], \
                   self._pt_setpoints["probe_goal"], self._pt_setpoints["vti_goal"], \
                   self._pt_setpoints["probe_heater_power"], self._pt_setpoints["vti_heater_power"]

    def get_cool_down_datas(self):
        with self.data_lock and self.setpoint_lock:
            return self._pt_datas["probe_temperature"], self._pt_datas["magnet_temperature"], \
                   self._pt_setpoints["nv_pressure_goal"]

    def get_nv_pressure_goal(self):
        with self.setpoint_lock:
            return self._pt_setpoints["nv_pressure_goal"]

    def get_magnet(self):
        with self.data_lock:
            return self._pt_datas["magnet"]

    def is_magnet_reached(self):
        with self.data_lock and self.setpoint_lock:
            if abs(self._pt_datas["magnet"] - self._pt_setpoints["magnet_goal"]) <= self.min_field_tol * 3:
                return True
            else:
                return False

    def is_magnet_closed(self):
        with self.data_lock and self.setpoint_lock:
            magnet_goal = self._pt_setpoints["magnet_goal"]
            ips_heater = self._pt_setpoints["ips_heater_status"]
            magnet = self._pt_datas["magnet"]

        is_closed = 0
        err_str_ls = []
        if abs(magnet) > self.min_field_tol * 3:
            is_closed += 1
            err_str_ls.append("当前磁场没有完全归零，请打开IPS heater之后，点一下to zero将磁场归零，再关闭IPS heater")

        if abs(magnet_goal) > self.min_field_tol:
            is_closed += 1
            err_str_ls.append("需要将磁场目标值设置为零之后再升/降温")

        if ips_heater == "ON":
            is_closed += 1
            err_str_ls.append("升降温之前需要先关闭IPS heater")
        err_str = '\n'.join(err_str_ls)

        if is_closed > 0:
            return False, err_str
        else:
            return True, err_str

    def saver_system_datas(self):
        with self.data_lock and self.setpoint_lock:
            datas = (time(),
                     self._pt_datas["probe_temperature"], self._pt_setpoints["probe_heater_power"],
                     self._pt_datas["vti_temperature"], self._pt_setpoints["vti_heater_power"],
                     self._pt_setpoints["nv_angle"], self._pt_setpoints["nv_pressure"],
                     self._pt_setpoints["sorb_temperature"], self._pt_setpoints["sorb_heater"],
                     self._pt_setpoints["pt1_temperature"], self._pt_setpoints["pt2_temperature"],
                     self._pt_datas["magnet"], self._pt_datas["magnet_temperature"])
        self.signal_system_datas.emit(datas)

    def update_magnet_goal(self, goal):
        with self.setpoint_lock:
            self._pt_setpoints["magnet_goal"] = goal

    def quit_thread(self):
        with self.thread_lock:
            self.running = False

    def run(self):
        self.running = True

        count = 0
        err_count = 0
        while self.running:
            try:
                self.update_probe_temp_and_magnet()
            except Exception as e:
                print(repr(e))
                err_count += 1

            if count % 5 == 0:
                try:
                    self.update_other_pt_datas()
                except Exception as e:
                    print(repr(e))
                    err_count += 1

            if count % 10 == 0:
                try:
                    self.update_pt_setpoints()
                    self.saver_system_datas()
                except Exception as e:
                    print(repr(e))
                    err_count += 1

            if err_count >= self.max_errors:
                with self.thread_lock:
                    self.running = False

            if count >= 1000:
                count = 0

            self.msleep(100)
            count += 1







