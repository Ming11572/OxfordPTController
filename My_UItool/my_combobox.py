from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QComboBox, QApplication, QSizePolicy
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QFont


class MyComboBox(QWidget):
    signal_current_text_changed = Signal()

    def __init__(self, obj_name, var_name_ls=None):
        super(MyComboBox, self).__init__(parent=None)
        self.resize(250, 40)
        self.setMinimumSize(150, 35)
        self.obj_name = obj_name
        self.flag_emit_signal = True

        h_layout = QHBoxLayout(self)

        # self.setLayout(h_layout)

        font1 = QFont()
        font1.setPointSize(10)

        font2 = QFont()
        font2.setPointSize(11)

        self.label = QLabel(obj_name, self)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setMinimumSize(QSize(70, 25))
        self.label.setMaximumSize(QSize(70, 40))

        h_layout.addWidget(self.label)

        self.cb_var = QComboBox(self)
        self.cb_var.setObjectName(u"cb_var")
        self.cb_var.setFont(font2)
        self.cb_var.setMinimumSize(QSize(100, 30))
        self.cb_var.setMaximumSize(QSize(16777215, 40))
        # self.cb_var.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        h_layout.addWidget(self.cb_var)
        h_layout.setSpacing(0)

        self.cb_var.currentTextChanged.connect(self.slot_cb_text_changed)

        if var_name_ls is not None:
            self.set_combox_items(var_name_ls)

    def current_text(self):
        return self.cb_var.currentText()

    def set_combox_items(self, var_name_ls):
        _flag = True
        self.flag_emit_signal = False
        ori_text = self.cb_var.currentText()
        self.cb_var.clear()
        self.cb_var.addItem('None')
        for var_name in var_name_ls:
            self.cb_var.addItem(var_name)
        try:
            self.cb_var.setCurrentText(ori_text)
        except Exception as e:
            self.cb_var.setCurrentIndex(0)
            self.signal_current_text_changed.emit()
            _flag = False

        self.flag_emit_signal = True
        return _flag

    def slot_cb_text_changed(self, new_text):
        if self.flag_emit_signal:
            self.signal_current_text_changed.emit()


if __name__ == '__main__':
    app = QApplication([])

    name = 'str1'
    var_ls = ['a1', 'a2', 'a3']

    temp_combo = MyComboBox(name, var_ls)
    temp_combo.show()

    app.exec()

