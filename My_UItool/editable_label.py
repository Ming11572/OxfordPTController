from PySide6.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt, Signal, QObject, QEvent
from PySide6.QtGui import QCursor


class EditableLabelHandler(QObject):
    # 定义信号，当确认修改时会发射这个信号，参数为修改后的值
    valueChanged = Signal(float)

    def __init__(self, label: QLabel):
        super().__init__()
        self.label = label
        self.original_value = label.text()
        self.editable = True  # 默认开启编辑功能

        # 设置初始鼠标悬停提示
        self.update_tooltip()

        # 启用鼠标跟踪
        self.label.setMouseTracking(True)

        # 安装事件过滤器来捕获鼠标事件
        self.label.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.label:
            # 鼠标进入事件
            if event.type() == QEvent.Enter:
                if self.editable:
                    self.label.setCursor(QCursor(Qt.PointingHandCursor))
                else:
                    self.label.setCursor(QCursor(Qt.ArrowCursor))
                return True

            # 鼠标离开事件
            elif event.type() == QEvent.Leave:
                self.label.setCursor(QCursor(Qt.ArrowCursor))
                return True

            # 鼠标双击事件 - 只在可编辑时响应
            elif event.type() == QEvent.MouseButtonDblClick:
                if event.button() == Qt.LeftButton and self.editable:
                    self.show_edit_dialog()
                    return True

        return super().eventFilter(obj, event)

    def show_edit_dialog(self):
        """显示编辑对话框"""
        dialog = QDialog(self.label)
        dialog.setWindowTitle("修改数值")
        dialog.setModal(True)
        dialog.setFixedSize(300, 150)

        # 创建布局
        layout = QVBoxLayout()

        # 创建输入框，显示当前值
        line_edit = QLineEdit()
        line_edit.setText(self.label.text())
        line_edit.selectAll()  # 选中所有文本方便修改
        layout.addWidget(line_edit)

        # 创建按钮布局
        button_layout = QVBoxLayout()

        # 确认按钮
        confirm_btn = QPushButton("确认")

        # 取消按钮
        cancel_btn = QPushButton("取消")

        button_layout.addWidget(confirm_btn)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)
        dialog.setLayout(layout)

        # 连接按钮信号
        def on_confirm():
            new_value = line_edit.text().strip()
            try:
                self.valueChanged.emit(float(new_value))
                self.label.setText(new_value)
                dialog.accept()
            except:
                QMessageBox.warning(dialog, "警告", "需要输入数值")

        confirm_btn.clicked.connect(on_confirm)
        cancel_btn.clicked.connect(dialog.reject)

        # 设置回车键确认
        line_edit.returnPressed.connect(on_confirm)

        # 显示对话框
        dialog.exec()

    def set_editable(self, editable: bool):
        """设置是否可编辑"""
        self.editable = editable
        self.update_tooltip()

    def update_tooltip(self):
        """更新悬停提示文本"""
        if self.editable:
            self.label.setToolTip("双击修改数值")
        else:
            self.label.setToolTip("无法修改当前数值")

    def toggle_editable(self):
        """切换编辑状态"""
        self.set_editable(not self.editable)

    def is_editable(self):
        """返回当前是否可编辑"""
        return self.editable


# 使用示例
if __name__ == "__main__":
    app = QApplication([])

    # 创建一个测试用的QLabel
    label = QLabel("100")
    label.resize(200, 50)
    label.show()

    # 创建我们的处理器
    handler = EditableLabelHandler(label)

    # 连接信号，处理数值改变
    handler.valueChanged.connect(lambda new_value: print(f"数值已修改为: {new_value}"))

    # 演示开关功能
    # 5秒后关闭编辑功能
    from PySide6.QtCore import QTimer


    def disable_editing():
        handler.set_editable(False)
        print("编辑功能已关闭")


    QTimer.singleShot(5000, disable_editing)


    # 10秒后重新开启编辑功能
    def enable_editing():
        handler.set_editable(True)
        print("编辑功能已开启")


    QTimer.singleShot(10000, enable_editing)

    app.exec()