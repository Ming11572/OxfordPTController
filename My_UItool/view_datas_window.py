from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui.view_data_widget import Ui_Form

import pandas as pd


class ViewDataWindow(QWidget, Ui_Form):
    signal_view_data_window_delete = Signal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self)
        # super(ViewDataWindow, self).__init__(parent)
        self.setupUi(self)
        self.tb_name = None
        self.df = None

    def set_datas(self, tb_name, df: pd.DataFrame, run_name: str):
        self.tb_name = tb_name
        self.df = df

        self.setWindowTitle(f"{tb_name}__{run_name}")

        col_dict = {}
        read_only_ls = []
        for name in df.columns:
            col_dict[name] = ('FLOAT', 0.0)
            read_only_ls.append(True)

        read_only_ls = tuple(read_only_ls)

        self.tb_datas.init_table('view_datas_temp_table', col_dict, read_only_ls)
        self.tb_datas.df_to_table(df)

    def closeEvent(self, event) -> None:
        self.signal_view_data_window_delete.emit(self.tb_name)
