from PySide6.QtCore import QThread, Signal
from threading import Lock
from datetime import datetime

from teslapt_core import TeslaPTCore


class WarmCoolThread(QThread):
    signal_logs = Signal(str)
    signal_warm_cool_finished = Signal()

    def __init__(self, pt_core, shared_datas, caller):
        super(WarmCoolThread, self).__init__()
        self.pt_core: TeslaPTCore = pt_core
        self.shared_datas = shared_datas
        self.caller = caller
        self.max_magnet_temp = 4.8
        self.thread_lock = Lock()
        self.running = False

        self._fun = None

    def set_max_magnet_temp(self, temp):
        self.max_magnet_temp = temp

    def quit_thread(self):
        self.signal_logs.emit(
            f"{datetime.now().strftime('%H:%M:%S')} 手动退出升降温")
        with self.thread_lock:
            self.running = False

    def set_fun(self, flag: str):
        if flag == "cool":
            self._fun = self.cool_down
        elif flag == 'warm':
            self._fun = self.warm_up

    def run(self) -> None:
        if self._fun is not None:
            self._fun()

    def warm_up(self):
        self.running = True
        self.signal_logs.emit(
            f"{datetime.now().strftime('%H:%M:%S')} 开始升温，如果使用的是He3杆， 请先将probe升温到1.5K以上")
        self.pt_core.set_probe_heater_auto("ON")
        self.pt_core.set_vti_heater_auto("ON")

        self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 打开vti/probe/自动控温")

        # 关针阀
        self.pt_core.set_1k_pool_pressure(0)
        self.pt_core.set_1k_pool_nv_auto("OFF")
        self.pt_core.set_1k_pool_nv(0)
        self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 关闭针阀")

        probe_temp = self.shared_datas.get_probe_temp()
        count_reset_temp = 20

        while self.running and probe_temp <= 299:
            probe_temp, vti_temp, probe_goal, vti_goal, probe_power, vti_power = self.shared_datas.get_warm_up_datas()

            if count_reset_temp >= 20:  # 每10s调一下
                if probe_power > 85:  # probe 最大功率为85
                    self.pt_core.set_probe_heater_auto("OFF")
                    self.pt_core.set_probe_heater_power(85)
                    self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 关闭probe自动控温，设置加热器功率为85")
                elif probe_power < 85:
                    if probe_goal - probe_temp <= 5 and probe_goal <= 300:
                        new_probe_goal = max(probe_goal, probe_temp) + 0.5
                        self.pt_core.set_probe_temperature(new_probe_goal)
                        self.signal_logs.emit(
                            f"{datetime.now().strftime('%H:%M:%S')} 设置probe温度：{new_probe_goal:.4f} K")

                if vti_power > 80:
                    self.pt_core.set_vti_heater_auto("OFF")
                    self.pt_core.set_vti_heater_power(80)
                    self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 关闭VTI自动控温，设置加热器功率为80")
                elif vti_power < 80:
                    if vti_goal - vti_temp <= 5 and vti_goal < 295:
                        new_vti_goal = max(vti_goal, vti_temp) + 0.5
                        self.pt_core.set_vti_temperature(new_vti_goal)
                        self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 设置VTI温度：{new_vti_goal:.4f} K")
                else:
                    if vti_temp >= 295:
                        self.pt_core.set_vti_heater_auto("ON")
                        self.pt_core.set_vti_temperature(295)

                count_reset_temp = 0

            self.msleep(500)
            count_reset_temp += 1

        if self.running:
            self.pt_core.set_probe_heater_auto("ON")
            self.pt_core.set_vti_heater_auto("ON")
            self.pt_core.set_probe_and_vti_temperature(300)
            self.signal_warm_cool_finished.emit()
            self.signal_logs.emit(
                f"{datetime.now().strftime('%H:%M:%S')} 升温结束")
        self.running = False

    def cool_down(self):
        self.running = True
        self.pt_core.set_probe_heater_auto("ON")
        self.pt_core.set_vti_heater_auto("ON")
        self.pt_core.set_probe_and_vti_temperature(1.5)
        self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 开始降温，打开VTI/Probe的自动控温, 将目标温度设定为1.4K\n"
                              f"\t如果是He3杆，请将最终probe/vti温度改为10K")

        self.pt_core.set_1k_pool_nv_auto("ON")
        self.pt_core.set_1k_pool_pressure(10)
        self.signal_logs.emit(f"{datetime.now().strftime('%H:%M:%S')} 针阀设置为自动控制模式")

        probe_temp = self.shared_datas.get_probe_temp()
        # print(probe_temp)
        count_reset_temp = 20

        while self.running and probe_temp > 10:
            probe_temp, magnet_temp, pressure_goal = self.shared_datas.get_cool_down_datas()

            if count_reset_temp >= 20:  # 每10s调节一次针阀，如果磁体温度没有超过极限，增加Pressure；否则减小。
                if magnet_temp > self.max_magnet_temp:
                    self.pt_core.set_1k_pool_pressure(pressure_goal - 0.5)
                    self.signal_logs.emit(
                        f"{datetime.now().strftime('%H:%M:%S')}  SET Pressure {pressure_goal - 0.5} mbar")
                else:
                    if pressure_goal <= 29.5:
                        self.pt_core.set_1k_pool_pressure(pressure_goal + 0.5)
                        self.signal_logs.emit(
                            f"{datetime.now().strftime('%H:%M:%S')}  SET Pressure {pressure_goal + 0.5} mbar")
                    else:   # 针阀最大开到 P = 30 mbar
                        if pressure_goal != 30:
                            self.pt_core.set_1k_pool_pressure(30)
                            self.signal_logs.emit(
                                f"{datetime.now().strftime('%H:%M:%S')} SET Pressure 30 mbar")

                count_reset_temp = 0

            self.msleep(500)
            count_reset_temp += 1

        if self.running:
            self.pt_core.set_1k_pool_pressure(5)
            self.signal_logs.emit(
                f"{datetime.now().strftime('%H:%M:%S')} 降温结束, 气压设置为5mbar")
            self.signal_warm_cool_finished.emit()

        self.running = False





