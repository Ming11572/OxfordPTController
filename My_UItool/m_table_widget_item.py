from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, Signal
from copy import deepcopy


class BaseTableItem(QTableWidgetItem):

    def __init__(self, text: str, flag_read_only: bool):
        QTableWidgetItem.__init__(self, text)
        self.read_only(flag_read_only)
        self.value = None

    def set_value(self, value):
        self.value = value
        self.setText(value)

    def get_value(self):
        pass

    def item_text_changed(self) -> bool:
        return True

    def read_only(self, flag):
        if flag:
            self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)


class TextItem(BaseTableItem):

    def __init__(self, text: str, flag_read_only: bool):
        text = str(text)
        BaseTableItem.__init__(self, text, flag_read_only)
        self.value = text
        self.item_text_changed()

    def set_value(self, value):
        self.value = str(value)
        self.setText(self.value)

    def get_value(self):
        return deepcopy(self.value)

    def item_text_changed(self) -> bool:
        self.value = self.text()
        return True


class TextItemNoNull(TextItem):

    def __init__(self, text, flag_read_only: bool):
        if (text is None) or (text == ''):
            raise ValueError("input error for text item")
        TextItem.__init__(self, text, flag_read_only)

    def set_value(self, value):
        if value is None or value == '':
            return
        self.value = str(value)
        self.setText(self.value)

    def item_text_changed(self) -> bool:
        text = self.text()
        if (text is None) or (text == ''):
            self.setText(self.value)
            return False
        else:
            self.value = text
            return True


class FloatItem(BaseTableItem):
    def __init__(self, value, flag_read_only: bool):
        self.value = float(value)
        BaseTableItem.__init__(self, self.get_v_str(), flag_read_only)

    def get_v_str(self):
        return f"{self.value:.12g}"

    def item_text_changed(self) -> bool:
        text = self.text()
        try:
            self.value = float(text)
            return True
        except Exception as e:
            print(e)
            self.setText(self.get_v_str())
            return False

    def set_value(self, value):
        self.value = float(value)
        self.setText(self.get_v_str())

    def get_value(self):
        return deepcopy(self.value)


class FloatItemE(FloatItem):

    def get_v_str(self):
        if abs(self.value) >= 10000:
            v_str = f"{self.value:.3e}"
        else:
            v_str = f"{self.value:.3f}"
        return v_str


class CheckItem(BaseTableItem):
    def __init__(self, check_id, flag_read_only: bool):
        BaseTableItem.__init__(self, '', flag_read_only)
        if isinstance(check_id, bool):
            self.value = check_id
        elif isinstance(check_id, int):
            if check_id == 0:
                self.value = False
            else:
                self.value = True
        elif isinstance(check_id, float):
            if check_id == 0.0:
                self.value = False
            else:
                self.value = True
        elif isinstance(check_id, str):
            if check_id == '0' or check_id == 'False':
                self.value = False
            else:
                self.value = True
        elif isinstance(check_id, Qt.CheckState):
            if check_id == Qt.CheckState.Unchecked:
                self.value = False
            else:
                self.value = True
        else:
            raise ValueError("input error for check item")

        if self.value:
            self.setCheckState(Qt.CheckState.Checked)
        else:
            self.setCheckState(Qt.CheckState.Unchecked)

    def set_value(self, value: bool):
        self.value = value
        if self.value:
            self.setCheckState(Qt.CheckState.Checked)
        else:
            self.setCheckState(Qt.CheckState.Unchecked)

    def get_value(self):
        return deepcopy(self.value)

    def item_text_changed(self) -> bool:
        if self.checkState() == Qt.CheckState.Unchecked:
            self.value = False
        else:
            self.value = True
        return True


item_dict = {
    'TEXT': TextItem,
    'TEXT NOT NULL': TextItemNoNull,
    'FLOAT': FloatItem,
    'FLOATE': FloatItemE,
    'BOOL': CheckItem
}
