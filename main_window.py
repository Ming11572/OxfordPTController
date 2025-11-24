from threading import Lock
from functools import partial
from datetime import datetime
import pickle
import json

from PySide6.QtWidgets import QLabel, QMessageBox, QButtonGroup
from PySide6.QtGui import QFont, QCloseEvent
from PySide6.QtCore import Qt, Signal, QThread

from My_UItool.resized_window import ResizedMainWindow
from My_UItool.editable_label import EditableLabelHandler
from ui.main_window import Ui_MainWindow
from pt_setting import PTSettingWindow
from teslapt_core import TeslaPTCore
from share_datas import DataCenter
from socket_thread import SocketThread
from plot_window import PlotWindow
from warm_cool import WarmCoolThread


class PtMainWindow(Ui_MainWindow, ResizedMainWindow):
    signal_cmd_logs = Signal(int, str)

    def __init__(self, log_saver, pt_core, itc_alias_ls, port, alias):
        ResizedMainWindow.__init__(self, window_name='pt_controller_window', parent=None)
        Ui_MainWindow.__init__(self)

        self.is_magnet_ready = False  # 决定是否可以远程变化磁场
        self.is_probe_ready = False  # 决定是否可以远程变温
        self.is_ready_lock = Lock()

        self.port = port
        self.alias = alias
        self.pt_core: TeslaPTCore = pt_core
        self.itc_alias_ls = itc_alias_ls
        self.magnet_exciting_tol = 0.001

        self.magnet_goal = 0
        self.magnet_rate = 0
        self.probe_goal = 0

        self.count_status = 0
        self.count_cmds = 0
        self.count_cmd_get_pt_data = 0
        self.count_cmd_get_temp_status = 0
        self.count_cmd_get_field_status = 0

        # init ui and the log savers
        self.setupUi(self)

        self.field_status_group = QButtonGroup()
        self.field_status_group.addButton(self.rb_hold)
        self.field_status_group.addButton(self.rb_to_set)
        self.field_status_group.addButton(self.rb_to_zero)
        self.rb_hold.clicked.connect(partial(self.pt_core.set_magnet_status, status="hold"))
        self.rb_to_set.clicked.connect(partial(self.pt_core.set_magnet_status, status="to set"))
        self.rb_to_zero.clicked.connect(partial(self.pt_core.set_magnet_status, status="to zero"))

        self.ips_heater_group = QButtonGroup()
        self.ips_heater_group.addButton(self.rb_ips_heater_on)
        self.ips_heater_group.addButton(self.rb_ips_heater_off)
        self.rb_ips_heater_on.clicked.connect(partial(self.pt_core.set_ips_heater, goal="ON"))
        self.rb_ips_heater_off.clicked.connect(partial(self.pt_core.set_ips_heater, goal="OFF"))

        self.hd_magnet_goal = EditableLabelHandler(self.lb_magnet_goal)
        self.hd_magnet_goal.valueChanged.connect(self.pt_core.set_magnet)
        self.hd_magnet_rate = EditableLabelHandler(self.lb_magnet_rate)
        self.hd_magnet_rate.valueChanged.connect(self.pt_core.set_magnet_rate)

        self.hd_probe_goal = EditableLabelHandler(self.lb_probe_temp_goal)
        self.hd_probe_goal.valueChanged.connect(self.pt_core.set_probe_temperature)
        self.hd_probe_heater = EditableLabelHandler(self.lb_probe_heater)
        self.hd_probe_heater.valueChanged.connect(self.pt_core.set_probe_heater_power)
        self.probe_group = QButtonGroup()
        self.probe_group.addButton(self.rb_itc_heater_on)
        self.probe_group.addButton(self.rb_itc_heater_off)
        self.rb_itc_heater_on.clicked.connect(partial(self.pt_core.set_probe_heater_auto, goal="ON"))
        self.rb_itc_heater_off.clicked.connect(partial(self.pt_core.set_probe_heater_auto, goal="OFF"))

        self.hd_vti_goal = EditableLabelHandler(self.lb_vti_temp_goal)
        self.hd_vti_goal.valueChanged.connect(self.pt_core.set_vti_temperature)
        self.hd_vti_heater = EditableLabelHandler(self.lb_vti_heater)
        self.hd_vti_heater.valueChanged.connect(self.pt_core.set_vti_heater_power)
        self.vti_group = QButtonGroup()
        self.vti_group.addButton(self.rb_itc_heater_on_2)
        self.vti_group.addButton(self.rb_itc_heater_off_2)
        self.rb_itc_heater_on_2.clicked.connect(partial(self.pt_core.set_vti_heater_auto, goal="ON"))
        self.rb_itc_heater_off_2.clicked.connect(partial(self.pt_core.set_vti_heater_auto, goal="OFF"))

        self.hd_pressure_goal = EditableLabelHandler(self.lb_nv_pressure_goal)
        self.hd_pressure_goal.valueChanged.connect(self.pt_core.set_1k_pool_pressure)
        self.hd_nv_angle = EditableLabelHandler(self.lb_nv_heater)
        self.hd_nv_angle.valueChanged.connect(self.pt_core.set_1k_pool_nv)
        self.nv_group = QButtonGroup()
        self.nv_group.addButton(self.rb_itc_heater_on_3)
        self.nv_group.addButton(self.rb_itc_heater_off_3)
        self.rb_itc_heater_on_3.clicked.connect(partial(self.pt_core.set_1k_pool_nv_auto, goal="ON"))
        self.rb_itc_heater_off_3.clicked.connect(partial(self.pt_core.set_1k_pool_nv_auto, goal="OFF"))

        self.hd_sorb_goal = EditableLabelHandler(self.lb_sorb_goal)
        self.hd_sorb_goal.valueChanged.connect(self.pt_core.set_sorb_temperature)
        self.hd_sorb_heater = EditableLabelHandler(self.lb_sorb_heater)
        self.hd_sorb_heater.valueChanged.connect(self.pt_core.set_sorb_heater_power)
        self.sorb_group = QButtonGroup()
        self.sorb_group.addButton(self.rb_itc_heater_on_4)
        self.sorb_group.addButton(self.rb_itc_heater_off_4)
        self.rb_itc_heater_on_4.clicked.connect(partial(self.pt_core.set_sorb_heater_auto, goal="ON"))
        self.rb_itc_heater_off_4.clicked.connect(partial(self.pt_core.set_sorb_heater_auto, goal="OFF"))

        font = QFont()
        font.setPointSize(9)

        self.lb_status_1 = QLabel('')
        self.lb_status_1.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_status_1.setFont(font)
        self.statusBar.addWidget(self.lb_status_1)
        self.lb_status_2 = QLabel('')
        self.lb_status_2.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_status_2.setFont(font)
        self.statusBar.addWidget(self.lb_status_2)
        self.lb_status_3 = QLabel('')
        self.lb_status_3.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_status_3.setFont(font)
        self.statusBar.addWidget(self.lb_status_3)
        self.lb_cmd_ls = [self.lb_status_1, self.lb_status_2, self.lb_status_3]

        self.init_window_size_and_pos()
        self.count_status = 0

        # setting windows
        self.pt_setting_window = PTSettingWindow(self.itc_alias_ls)
        self.pt_setting_window.signal_pt_setting_changed.connect(self.init_pt_settings)
        pt_settings = self.pt_setting_window.get_pt_settings()
        # self.pt_setting_window.show()
        self.magnet_alarm_temp = pt_settings["alarm_field_temp"]
        self.magnet_max_temp = pt_settings["max_field_temp"]
        self.shared_datas = DataCenter(self.pt_core)
        self.init_pt_settings(pt_settings)

        # 绑定画图窗口
        self.log_saver = log_saver
        self.shared_datas.signal_system_datas.connect(self.log_saver.save_data)
        self.plot_window = PlotWindow(self.log_saver)
        self.pb_logs.clicked.connect(self.show_plot_windows)

        self.ui_status_syncer = SyncUIThread(self)
        self.ui_status_syncer.signal_sync_main_ui.connect(self.sync_UI)
        self.signal_cmd_logs.connect(self.sync_cmd_logs)
        self.ui_status_syncer.start()
        self.pb_setting.clicked.connect(self.slot_setting_clicked)

        # 创建socket对象
        self.thread_socket = SocketThread('localhost', self.port)
        self.thread_socket.signal_client_called.connect(self.handle_client)
        self.thread_socket.signal_log.connect(self.sync_cmd_logs)
        self.thread_socket.start()
        self.lb_servers_status.setText(f"已连接Oxford Teslatron PT。服务器已开启，监听端口： {self.port}，等待连接....")

        # warm cool thread
        self.warm_cool_thread = WarmCoolThread(self.pt_core, self.shared_datas, self)
        self.warm_cool_thread.signal_logs.connect(self.append_status)
        self.warm_cool_thread.signal_warm_cool_finished.connect(self.set_warm_cool_enabled)
        self.pb_warm_up.clicked.connect(self.slot_warm_up)
        self.pb_cool_down.clicked.connect(self.slot_cool_down)
        self.pb_abort_warm_cool.clicked.connect(self.slot_abort_warm_cool)
        self.pb_abort_warm_cool.setEnabled(False)

        self.thread_ls = [self.thread_socket, self.shared_datas, self.ui_status_syncer, self.warm_cool_thread]
        self.window_ls = [self.plot_window, self.pt_setting_window]

    def slot_warm_up(self):
        is_closed, err_str = self.shared_datas.is_magnet_closed()
        if is_closed:
            reply = QMessageBox.question(self, '确认？', '是否开始一键升温',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.warm_cool_thread.set_fun('warm')
                self.warm_cool_thread.start()
                self.pb_warm_up.setEnabled(False)
                self.pb_cool_down.setEnabled(False)
                self.pb_abort_warm_cool.setEnabled(True)
        else:
            QMessageBox.warning(self, 'error', err_str)

    def slot_cool_down(self):
        is_closed, err_str = self.shared_datas.is_magnet_closed()
        if is_closed:
            reply = QMessageBox.question(self, '确认？', '是否开始一键降温',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.warm_cool_thread.set_fun('cool')
                self.warm_cool_thread.start()
                self.pb_warm_up.setEnabled(False)
                self.pb_cool_down.setEnabled(False)
                self.pb_abort_warm_cool.setEnabled(True)

        else:
            QMessageBox.warning(self, 'error', err_str)

    def slot_abort_warm_cool(self):
        self.warm_cool_thread.quit_thread()
        self.set_warm_cool_enabled()

    def set_warm_cool_enabled(self):
        # pass
        self.pb_warm_up.setEnabled(True)
        self.pb_cool_down.setEnabled(True)
        self.pb_abort_warm_cool.setEnabled(False)

    def show_plot_windows(self):
        self.plot_window.show()
        self.plot_window.activateWindow()

    def enable_ips_heater(self, flag):
        self.rb_ips_heater_on.setEnabled(flag)
        self.rb_ips_heater_off.setEnabled(flag)

    def slot_setting_clicked(self):
        self.pt_setting_window.show()
        self.pt_setting_window.activateWindow()

    def init_pt_settings(self, settings):
        # print(settings)
        flag, err_str = self.pt_core.init_pt_core(settings)

        self.magnet_alarm_temp = settings["alarm_field_temp"]
        self.magnet_max_temp = settings["max_field_temp"]
        if flag and (not self.shared_datas.running):
            self.shared_datas.start()
        else:
            self.pt_setting_window.show()
            print(err_str)

    def sync_UI(self):
        mag_temp, vti_temp, probe_temp, pt1, pt2, magnet, switch_magnet, magnet_goal, magnet_rate, \
            probe_goal, probe_power, vti_goal, vti_power, nv_pressure, nv_goal, nv_angle, \
            sorb_temp, sorb_goal, sorb_heater = self.shared_datas.get_temperature_and_magnet()

        if magnet_goal != self.magnet_goal:
            self.magnet_goal = magnet_goal
        if self.magnet_rate != magnet_rate:
            self.magnet_rate = magnet_rate
        if self.probe_goal != probe_goal:
            self.probe_goal = probe_goal

        self.lb_magnetT.setText(f"{mag_temp}")
        self.lb_vti_temp.setText(f"{vti_temp}")
        self.lb_probe_temp.setText(f"{probe_temp}")
        self.lb_pt1.setText(f"{pt1}")
        self.lb_pt2.setText(f"{pt2}")
        self.lb_magnet_field.setText(f"{magnet}")
        self.lb_switch_field.setText(f"{switch_magnet}")
        self.lb_magnet_goal.setText(f"{magnet_goal}")
        self.lb_magnet_rate.setText(f"{magnet_rate}")
        self.lb_probe_temp_goal.setText(f"{probe_goal}")
        self.lb_probe_heater.setText(f"{probe_power}")
        self.lb_vti_temp_goal.setText(f"{vti_goal}")
        self.lb_vti_heater.setText(f"{vti_power}")
        self.lb_nv_pressure.setText(f"{nv_pressure}")
        self.lb_nv_pressure_goal.setText(f"{nv_goal}")
        self.lb_nv_heater.setText(f"{nv_angle}")
        self.lb_sorb_heater.setText(f"{sorb_heater}")
        self.lb_sorb_goal.setText(f"{sorb_goal}")
        self.lb_sorb_temp.setText(f"{sorb_temp}")

        # sync rb buttons
        self.block_signals(True)
        magnet_status, ips_status, probe_status, vti_status, nv_status, sorb_status = self.shared_datas.get_magnet_and_heater_status()
        if magnet_status == 'hold':
            self.rb_hold.setChecked(True)
        elif magnet_status == 'to set':
            self.rb_to_set.setChecked(True)
        else:
            self.rb_to_zero.setChecked(True)
        if ips_status == "OFF":
            self.rb_ips_heater_off.setChecked(True)
            self.hd_magnet_goal.set_editable(False)
            self.hd_magnet_rate.set_editable(False)
        else:
            self.rb_ips_heater_on.setChecked(True)
            self.hd_magnet_goal.set_editable(True)
            self.hd_magnet_rate.set_editable(True)
        if probe_status == "ON":
            self.rb_itc_heater_on.setChecked(True)
            self.hd_probe_goal.set_editable(True)
            self.hd_probe_heater.set_editable(False)
        else:
            self.rb_itc_heater_off.setChecked(True)
            self.hd_probe_goal.set_editable(False)
            self.hd_probe_heater.set_editable(True)

        if vti_status == "ON":
            self.rb_itc_heater_on_2.setChecked(True)
            self.hd_vti_goal.set_editable(True)
            self.hd_vti_heater.set_editable(False)
        else:
            self.rb_itc_heater_off_2.setChecked(True)
            self.hd_vti_goal.set_editable(False)
            self.hd_vti_heater.set_editable(True)
        if nv_status == "ON":
            self.rb_itc_heater_on_3.setChecked(True)
            self.hd_pressure_goal.set_editable(True)
            self.hd_nv_angle.set_editable(False)
        else:
            self.rb_itc_heater_off_3.setChecked(True)
            self.hd_pressure_goal.set_editable(False)
            self.hd_nv_angle.set_editable(True)
        if sorb_status == "ON":
            self.rb_itc_heater_on_4.setChecked(True)
            self.hd_sorb_goal.set_editable(True)
            self.hd_sorb_heater.set_editable(False)
        else:
            self.rb_itc_heater_off_4.setChecked(True)
            self.hd_sorb_goal.set_editable(False)
            self.hd_sorb_heater.set_editable(True)
        self.block_signals(False)

        flag_magnet_temp_high = False
        if mag_temp > self.magnet_max_temp:
            self.lb_magnetT.setStyleSheet("background-color: rgb(255, 255, 0); color:red")
            flag_magnet_temp_high = True
            self.__set_magnet_ready(False)
            self.rb_ips_heater_on.setEnabled(False)
            self.hd_magnet_goal.set_editable(False)
            if abs(switch_magnet - magnet) <= self.magnet_exciting_tol:
                self.rb_ips_heater_off.setEnabled(True)
            else:
                self.rb_ips_heater_off.setEnabled(False)
        elif mag_temp > self.magnet_alarm_temp:
            self.lb_magnetT.setStyleSheet("background-color: rgb(255, 255, 0); color:red")

        else:
            self.lb_magnetT.setStyleSheet("background-color: rgb(240, 240, 240); color:black")
        if not flag_magnet_temp_high:
            if abs(switch_magnet - magnet) <= self.magnet_exciting_tol:
                self.rb_ips_heater_off.setEnabled(True)
                self.rb_ips_heater_on.setEnabled(True)
            else:
                self.rb_ips_heater_off.setEnabled(False)
                self.rb_ips_heater_on.setEnabled(False)

            if ips_status == "ON":
                self.__set_magnet_ready(True)
            else:
                self.__set_magnet_ready(False)

        if probe_status == "ON" and vti_status == "ON":
            self.__set_probe_ready(True)
        else:
            self.__set_probe_ready(False)

    def __set_magnet_ready(self, flag):
        with self.is_ready_lock:
            self.is_magnet_ready = flag

    def __get_magnet_ready(self):
        with self.is_ready_lock:
            return self.is_magnet_ready

    def __set_probe_ready(self, flag):
        with self.is_ready_lock:
            self.is_probe_ready = flag

    def get_probe_ready(self):
        with self.is_ready_lock:
            return self.is_probe_ready

    def block_signals(self, flag):
        # flag = True, block signal
        # flag = False, unblock signal
        self.rb_ips_heater_on.blockSignals(flag)
        self.rb_ips_heater_off.blockSignals(flag)
        self.rb_hold.blockSignals(flag)
        self.rb_to_set.blockSignals(flag)
        self.rb_to_zero.blockSignals(flag)
        self.rb_itc_heater_off.blockSignals(flag)
        self.rb_itc_heater_on.blockSignals(flag)
        self.rb_itc_heater_on_2.blockSignals(flag)
        self.rb_itc_heater_off_2.blockSignals(flag)
        self.rb_itc_heater_off_3.blockSignals(flag)
        self.rb_itc_heater_on_3.blockSignals(flag)

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, '确认关闭窗口？', '确认所有客户端程序已经关闭！！！',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:

            for _td in self.thread_ls:
                if _td.running:
                    _td.quit_thread()
                    _td.wait()

            for win in self.window_ls:
                win.close()
            event.accept()
        else:
            event.ignore()

    # 用于处理客户端请求
    def handle_client(self, conn, addr):
        """
                一共有四种请求：
                    get_temperature, get_field
                    set_temperature, set_field
                :param conn:
                :param addr:
                :return:
                """
        try:
            # 接收请求
            data = conn.recv(1024).decode()
            if data:
                # 解析请求
                request = json.loads(data)
                action = request.get("action")
                # params = request.get("params", [])
                # 执行相应操作
                if action == "get_temperature":
                    result = self.__get_probe_temperature()
                    # self.log_saver.log_debug(addr[0], "Get Temperature")
                    self.signal_cmd_logs.emit(0, f"{addr[0]} [Get Temp] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "get_magnet":
                    result = self.__get_magnet()
                    self.signal_cmd_logs.emit(0, f"{addr[0]} [Get Magnet] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "get_temp_magnet":
                    result = self.__get_probe_temp_and_magnet()
                    self.signal_cmd_logs.emit(0, f"{addr[0]} [Get Temp and Magnet] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "get_pt_setting":
                    result = self.pt_core.get_pt_setting()
                    self.signal_cmd_logs.emit(0, f"{addr[0]} [Get PT setting] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "get_magnet_temperature":
                    result = self.__get_magnet_temperature()
                    self.signal_cmd_logs.emit(0, f"{addr[0]} [Get Mag Temp] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "is_magnet_reached":
                    result = self.__is_magnet_reached()
                    self.signal_cmd_logs.emit(1, f"{addr[0]} [is Mag Reach] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "is_magnet_ready":
                    result = self.__get_magnet_ready()
                    self.signal_cmd_logs.emit(1, f"{addr[0]} [is Mag Reach] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "is_probe_ready":
                    result = self.get_probe_ready()
                    self.signal_cmd_logs.emit(1, f"{addr[0]} [is Mag Reach] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": result}

                elif action == "set_temperature":
                    params = request.get("params", [])
                    if len(params) < 1:
                        result = "Failed, 温度输入为空"
                    else:
                        self.log_saver.log_debug(f"{addr[0]}", "Set Temperature")
                        self.__set_probe_temp(*params)
                        result = "Succeed"
                    response = {"result": result}

                elif action == "set_magnet":
                    params = request.get("params", [])
                    if len(params) < 1:
                        result = "Failed, 磁场输入为空"
                    else:
                        self.log_saver.log_debug(f"{addr[0]}", "Set Magnet")
                        self.__set_magnet(*params)
                        result = "Succeed"
                    response = {"result": result}

                elif action == "pause_magnet":
                    self.__pause_magnet()
                    self.signal_cmd_logs.emit(1, f"{addr[0]} [is Mag Reach] at {datetime.now().strftime('%H:%M:%S')}")
                    response = {"result": "Succeed"}

                else:
                    response = {"error": "Invalid action"}
                # 发送响应
                conn.sendall(json.dumps(response).encode())
        finally:
            conn.close()

    # socket 调用
    def __set_probe_temp(self, goal):
        self.pt_core.set_probe_and_vti_temperature(goal)

    def __set_magnet(self, goal, rate=None):
        if rate == self.magnet_rate:
            rate = None
        self.shared_datas.update_magnet_goal(goal)
        self.pt_core.scan_magnet_to_goal(goal, rate)

    def __pause_magnet(self):
        self.pt_core.set_magnet_status('hold')
        self.rb_hold.setChecked(True)

    def __get_probe_temp_and_magnet(self):
        return self.shared_datas.get_probe_and_magnet()

    def __get_magnet_temperature(self):
        return self.shared_datas.get_magnet_temperature()

    def __get_probe_temperature(self):
        return self.shared_datas.get_probe_temp()

    def __get_magnet(self):
        return self.shared_datas.get_magnet()

    def __is_magnet_reached(self):
        return self.shared_datas.is_magnet_reached()

    def sync_cmd_logs(self, _id, cmd_logs):
        if _id > len(self.lb_cmd_ls):
            self.lb_cmd_ls[-1].setText(cmd_logs)
        else:
            self.lb_cmd_ls[_id].setText(cmd_logs)

    # program logs
    def append_status(self, text):
        if self.count_status <= 100:
            self.count_status += 1
        else:
            self.pte_status.clear()
            self.count_status = 0
        self.pte_status.appendPlainText(text)


class SyncUIThread(QThread):
    signal_sync_main_ui = Signal()
    signal_sync_cmd_logs = Signal(tuple)
    signal_sync_status = Signal(str)

    def __init__(self, caller):
        super(SyncUIThread, self).__init__()
        self.running = False
        self.thread_lock = Lock()
        self.cmd_logs = None
        self.pt_data_logs = None
        self.pt_temp_logs = None
        self.pt_magnet_logs = None
        self.status_logs = None

    def quit_thread(self):
        with self.thread_lock:
            self.running = False

    def run(self) -> None:
        self.running = True

        while self.running:
            try:
                self.signal_sync_main_ui.emit()
            except:
                pass

            self.msleep(1000)





