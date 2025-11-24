import os
import datetime
from PySide6.QtCore import QObject, QTimer
import matplotlib.pyplot as plt
from collections import deque
import threading


# 设置matplotlib使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 使用黑体，如果不可用则使用DejaVu Sans
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号


class LogSaver(QObject):
    # 定义数据字段名称
    FIELD_NAMES = ['time', 'probe_temp', 'probe_heater', 'vti_temp', 'vti_heater',
                   'nv_angle', 'nv_pressure', 'sorb_temp', 'sorb_heater',
                   'pt1_temp', 'pt2_temp', 'magnet', 'magnet_temp']

    def __init__(self, save_path):
        super().__init__()
        self.save_path = save_path
        self.current_date = datetime.datetime.now().strftime("%Y%m%d")
        self.current_month = datetime.datetime.now().strftime("%Y%m")

        # 创建子文件夹
        self.data_folder = os.path.join(save_path, "data_logs")
        self.error_folder = os.path.join(save_path, "error_logs")
        self.debug_folder = os.path.join(save_path, "debug_logs")

        for folder in [self.data_folder, self.error_folder, self.debug_folder]:
            os.makedirs(folder, exist_ok=True)

        # 数据缓存
        self.data_buffer = deque(maxlen=10000)  # 最多缓存10000条数据
        self.data_lock = threading.Lock()

        # 初始化数据文件
        self.data_file = self._get_data_filename()
        self._write_data_header()

        # 绘图窗口
        self.plot_window = None

        # 定时器用于定期保存数据
        self.save_timer = QTimer()
        self.save_timer.timeout.connect(self._check_date_change)
        self.save_timer.start(60000)  # 每分钟检查一次日期变化

    def _get_data_filename(self):
        """获取当前数据文件名"""
        filename = f"{self.current_date}.txt"
        return os.path.join(self.data_folder, filename)

    def _get_error_filename(self):
        """获取错误日志文件名"""
        filename = f"{self.current_month}_error.txt"
        return os.path.join(self.error_folder, filename)

    def _get_debug_filename(self):
        """获取调试日志文件名"""
        filename = f"{self.current_month}_debug.txt"
        return os.path.join(self.debug_folder, filename)

    def _write_data_header(self):
        """写入数据文件表头"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                header = "\t".join(self.FIELD_NAMES)
                f.write(f"# {header}\n")
        except Exception as e:
            print(f"Write file header error: {e}")

    def _check_date_change(self):
        """检查日期变化，如果需要则创建新文件"""
        current_date = datetime.datetime.now().strftime("%Y%m%d")
        current_month = datetime.datetime.now().strftime("%Y%m")

        if current_date != self.current_date:
            self.current_date = current_date
            self.data_file = self._get_data_filename()
            self._write_data_header()

        if current_month != self.current_month:
            self.current_month = current_month

    def save_data(self, data_tuple):
        """保存数据到文件"""
        try:
            # 检查日期变化
            self._check_date_change()

            # 保存数据到文件
            data_str = "\t".join(str(x) for x in data_tuple)
            with open(self.data_file, 'a', encoding='utf-8') as f:
                f.write(data_str + "\n")

            # 缓存数据用于绘图
            with self.data_lock:
                self.data_buffer.append(data_tuple)

        except Exception as e:
            print(f"Save data error: {e}")

    def error(self, alias, error_str):
        """记录错误日志"""
        self._log_message(alias, error_str, "error")

    def log_debug(self, alias, debug_str):
        """记录调试日志"""
        self._log_message(alias, debug_str, "debug")

    def _log_message(self, alias, message, log_type):
        """通用的日志记录方法"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp}\t{alias}\t{message}\n"

            if log_type == "error":
                filename = self._get_error_filename()
            else:
                filename = self._get_debug_filename()

            with open(filename, 'a', encoding='utf-8') as f:
                f.write(log_entry)

        except Exception as e:
            print(f"Record {log_type} log error: {e}")


