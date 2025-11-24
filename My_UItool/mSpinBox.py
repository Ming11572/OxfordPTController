from PySide6.QtCore import QObject, Signal, QSize


class MSpinBox(QObject):
    textChanged = Signal(str)
    valueChanged = Signal(float)

    def __init__(self, display_value, pb_up, pb_down):
        super(MSpinBox, self).__init__()
        self.display_value = display_value
        self.pb_up = pb_up
        self.pb_down = pb_down
        self.current_var = 0.0
        self.Decimals = 6
        self.format_str = '%.3f'
        self.singleStep = 0.0001
        self.minimum = 0
        self.maxnimum = 1
        self.pb_up.clicked.connect(self.slot_pb_up_clicked)
        self.pb_down.clicked.connect(self.slot_pb_down_clicked)
        self.display_value.signal_mouse_wheel.connect(self.slot_wheel_event)
        # init value
        self.setValue(self.current_var)
        self.pb_up.setMinimumSize(QSize(20, 12))
        self.pb_down.setMaximumSize(QSize(20, 12))

    def setDecimals(self, Decimals):
        self.Decimals = Decimals
        self.format_str = '%.' + str(Decimals) + 'f'

    def setValue(self, val, flag_emit_signal=False):
        if val < self.minimum:
            val = self.minimum
        elif val > self.maxnimum:
            val = self.maxnimum
        self.current_var = val
        new_text = self.format_str % val
        self.display_value.setText(new_text)

        if flag_emit_signal:
            self.valueChanged.emit(val)
            self.textChanged.emit(new_text)

    def slot_wheel_event(self, dely):
        if dely > 0:
            self.slot_pb_up_clicked()
        elif dely < 0:
            self.slot_pb_down_clicked()

    def slot_pb_up_clicked(self):
        self.setValue(val=(self.current_var + self.singleStep), flag_emit_signal=True)

    def slot_pb_down_clicked(self):
        self.setValue(val=(self.current_var - self.singleStep), flag_emit_signal=True)

    def setSingleStep(self, step):
        self.singleStep = step

    def setMaximum(self, max):
        self.maxnimum = max

    def setMinimum(self, min):
        self.minimum = min

    def setStyleSheet(self, style):
        self.display_value.setStyleSheet("background-color: rgb(255, 255, 255);" + style)

    def setEnabled(self, flag):
        self.display_value.setEnabled(flag)
        self.pb_up.setEnabled(flag)
        self.pb_down.setEnabled(flag)
        if flag:
            self.setStyleSheet("background-color: rgb(255, 255, 255); color:black")
        else:
            self.display_value.setStyleSheet("background-color: rgb(220, 220, 220); color:rgb(128, 128, 128)")


