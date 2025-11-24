from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QWheelEvent
from PySide6.QtCore import Signal


class MQLabel(QLabel):
    signal_mouse_wheel = Signal(int)

    def __init__(self, parent):
        super(MQLabel, self).__init__(parent)

    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta()
        # print(delta.y())
        self.signal_mouse_wheel.emit(delta.y())

    def enterEvent(self, event):
        if self.isEnabled():
            self.setStyleSheet("background-color: rgb(255, 255, 255); color:green")

    def leaveEvent(self, event):
        if self.isEnabled():
            self.setStyleSheet("background-color: rgb(255, 255, 255); color:black")

