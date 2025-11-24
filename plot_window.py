# plot_widget.py
import os
import datetime
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QCheckBox,
                               QPushButton, QGroupBox, QScrollArea)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import numpy as np
from collections import deque
import threading

# 设置matplotlib使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 使用黑体，如果不可用则使用DejaVu Sans
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号


class PlotWindow(QMainWindow):
    def __init__(self, log_saver):
        super().__init__()
        self.log_saver = log_saver
        self.data_cache = []
        self.update_timer = QTimer()
        self.is_zoomed = False

        self.init_ui()
        self.setup_plot()
        self.start_update_timer()

    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("Data Monitoring Chart")
        self.setGeometry(100, 100, 1400, 900)

        # 中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 主布局
        main_layout = QHBoxLayout(central_widget)

        # 左侧控制面板
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel)

        # 右侧绘图区域
        plot_widget = QWidget()
        plot_layout = QVBoxLayout(plot_widget)

        # 创建matplotlib图形
        self.figure = Figure(figsize=(10, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

        main_layout.addWidget(plot_widget, 1)

        # 连接鼠标事件
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('draw_event', self.on_draw)

    def create_control_panel(self):
        """创建控制面板"""
        panel = QWidget()
        panel.setMaximumWidth(300)
        layout = QVBoxLayout(panel)

        # 时间范围选择
        time_group = QGroupBox("Time Range")
        time_layout = QVBoxLayout(time_group)

        self.time_buttons = {}
        time_periods = ['1 Day', '1 Week', '1 Month', '1 Year']

        for period in time_periods:
            btn = QPushButton(period)
            btn.setCheckable(True)
            btn.clicked.connect(self.create_time_button_handler(period))
            time_layout.addWidget(btn)
            self.time_buttons[period] = btn

        self.time_buttons['1 Day'].setChecked(True)
        layout.addWidget(time_group)

        # 变量选择
        var_group = QGroupBox("Display Variables")
        var_layout = QVBoxLayout(var_group)

        self.var_checkboxes = {}
        variables = self.log_saver.FIELD_NAMES[1:]  # 排除time

        # 创建滚动区域
        scroll = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for var in variables:
            cb = QCheckBox(var)
            cb.setChecked(True)
            cb.stateChanged.connect(self.on_variables_changed)
            scroll_layout.addWidget(cb)
            self.var_checkboxes[var] = cb

        scroll.setWidget(scroll_widget)
        scroll.setMaximumHeight(400)
        var_layout.addWidget(scroll)
        layout.addWidget(var_group)

        # 实时更新控制
        update_group = QGroupBox("Update Settings")
        update_layout = QVBoxLayout(update_group)

        self.update_btn = QPushButton("Pause Update")
        self.update_btn.setCheckable(True)
        self.update_btn.clicked.connect(self.toggle_update)
        update_layout.addWidget(self.update_btn)

        layout.addWidget(update_group)
        layout.addStretch()

        return panel

    def create_time_button_handler(self, period):
        """创建时间按钮处理器"""

        def handler(checked):
            self.on_time_period_changed(period)

        return handler

    def setup_plot(self):
        """设置绘图区域"""
        self.axes = self.figure.add_subplot(111)
        self.lines = {}  # 存储每个变量的线条对象
        self.current_time_range = '1 Day'
        self.load_data()
        self.update_plot()

    def load_data(self, time_range=None):
        """加载数据"""
        if time_range is None:
            time_range = self.current_time_range

        end_time = datetime.datetime.now()

        if time_range == '1 Day':
            start_time = end_time - datetime.timedelta(days=1)
        elif time_range == '1 Week':
            start_time = end_time - datetime.timedelta(weeks=1)
        elif time_range == '1 Month':
            start_time = end_time - datetime.timedelta(days=30)
        else:  # 1 Year
            start_time = end_time - datetime.timedelta(days=365)

        # 从缓存和文件加载数据
        self.data_cache.clear()

        # 首先从缓存加载
        with self.log_saver.data_lock:
            for data in self.log_saver.data_buffer:
                timestamp = datetime.datetime.fromtimestamp(data[0])
                if start_time <= timestamp <= end_time:
                    self.data_cache.append(data)

        # 如果缓存数据不足，从文件加载
        if len(self.data_cache) < 100:  # 阈值可以根据需要调整
            self.load_data_from_files(start_time, end_time)

    def load_data_from_files(self, start_time, end_time):
        """从文件加载数据"""
        current_date = start_time.date()
        end_date = end_time.date()

        while current_date <= end_date:
            filename = os.path.join(self.log_saver.data_folder,
                                    current_date.strftime("%Y%m%d.txt"))
            if os.path.exists(filename):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith('#'):
                                continue
                            try:
                                data = tuple(float(x) for x in line.strip().split('\t'))
                                timestamp = datetime.datetime.fromtimestamp(data[0])
                                if start_time <= timestamp <= end_time:
                                    self.data_cache.append(data)
                            except ValueError:
                                continue
                except Exception as e:
                    print(f"Read file {filename} error: {e}")

            current_date += datetime.timedelta(days=1)

    def update_plot(self):
        """更新图表"""
        if self.is_zoomed:
            return

        # 清除所有现有线条
        for line in self.lines.values():
            if line in self.axes.lines:
                line.remove()
        self.lines.clear()

        # 清除坐标轴
        self.axes.clear()

        if not self.data_cache:
            self.axes.text(0.5, 0.5, 'No Data Available', transform=self.axes.transAxes,
                           ha='center', va='center')
            self.canvas.draw()
            return

        # 准备数据
        times = [datetime.datetime.fromtimestamp(data[0]) for data in self.data_cache]

        # 绘制选中的变量
        colors = plt.cm.tab10(np.linspace(0, 1, len(self.var_checkboxes)))
        color_idx = 0

        for i, (var_name, checkbox) in enumerate(self.var_checkboxes.items()):
            if checkbox.isChecked():
                var_index = self.log_saver.FIELD_NAMES.index(var_name)
                values = [data[var_index] for data in self.data_cache]

                # 数据降采样以提高性能
                if len(times) > 1000:
                    step = len(times) // 1000
                    times_plot = times[::step]
                    values_plot = values[::step]
                else:
                    times_plot = times
                    values_plot = values

                line, = self.axes.plot(times_plot, values_plot,
                                       color=colors[color_idx], label=var_name, linewidth=1)
                self.lines[var_name] = line
                color_idx += 1

        # 只有当有选中的变量时才添加图例和标签
        if self.lines:
            self.axes.legend(loc='upper left', bbox_to_anchor=(1, 1))
            self.axes.set_xlabel('Time')
            self.axes.set_ylabel('Value')
            self.axes.grid(True, alpha=0.3)

            # 设置时间格式
            self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            if self.current_time_range in ['1 Month', '1 Year']:
                self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

            self.figure.autofmt_xdate()

        self.canvas.draw()

    def on_time_period_changed(self, period):
        """时间范围改变事件"""
        for btn in self.time_buttons.values():
            btn.setChecked(False)
        self.time_buttons[period].setChecked(True)

        self.current_time_range = period
        self.load_data(period)
        self.update_plot()

    def on_variables_changed(self):
        """变量选择改变事件"""
        # 直接调用update_plot来更新显示
        self.update_plot()

    def toggle_update(self):
        """切换更新状态"""
        if self.update_btn.isChecked():
            self.update_btn.setText("Resume Update")
            self.update_timer.stop()
        else:
            self.update_btn.setText("Pause Update")
            self.start_update_timer()

    def start_update_timer(self):
        """启动更新定时器"""
        # 先断开之前的连接，避免重复连接
        try:
            self.update_timer.timeout.disconnect()
        except:
            pass
        self.update_timer.timeout.connect(self.on_timer_update)
        self.update_timer.start(10000)  # 10秒更新一次

    def on_timer_update(self):
        """定时器更新"""
        if not self.is_zoomed:
            self.load_data()
            self.update_plot()

    def on_click(self, event):
        """鼠标点击事件"""
        if event.button == 3:  # 右键
            self.is_zoomed = False
            self.load_data()
            self.update_plot()

    def on_draw(self, event):
        """绘制事件，用于检测缩放状态"""
        if hasattr(self.axes, 'viewLim'):
            xlim = self.axes.get_xlim()
            if len(self.data_cache) > 0:
                times = [data[0] for data in self.data_cache]
                data_range = max(times) - min(times)
                current_range = xlim[1] - xlim[0]
                self.is_zoomed = current_range < data_range * 0.9

    def closeEvent(self, event):
        """关闭事件，确保定时器停止"""
        self.update_timer.stop()
        event.accept()