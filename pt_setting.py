from ui.PT_setting import Ui_PTSetting

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Qt

import pickle


class PTSettingWindow(QWidget, Ui_PTSetting):
    signal_pt_setting_changed = Signal(dict)

    def __init__(self, itc_alias_ls):
        super(PTSettingWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        self.cb_itc_ls = [self.part_itc_1, self.part_itc_2, self.part_itc_3, self.part_itc_4, self.part_itc_5]
        self.cb_db_ls = [self.part_db_1, self.part_db_2, self.part_db_3, self.part_db_4, self.part_db_5]

        self.itc_alias_ls = itc_alias_ls
        for cb in self.cb_itc_ls:
            cb.addItems(itc_alias_ls)

        try:
            with open("./.systems/pt_setting.pkl", "rb") as f:
                self.pt_settings = pickle.load(f)
                # print(self.pt_settings)
        except:
            self.pt_settings = {
                "temp_set": [300, 0.1, 2, 0.005],
                "magnet_set": [7.5, -7.5, 0.2, 1e-4],
                "itc_set":['itc', 'itc', 'itc', 'itc', 'itc'],
                "db_set":['DB8', 'DB8', 'MB1', 'DB4', 'None'],
                "alarm_field_temp": 4.0,
                "max_field_temp": 4.3,
                "db_magnet_temp": "DB1",
                "db_pt1": "DB2",
                "db_pt2": "DB3",
            }
        magnet_set = self.pt_settings['magnet_set']
        self.le_field_max.setText(str(magnet_set[0]))
        self.le_field_min.setText(str(magnet_set[1]))
        self.le_field_rate_max.setText(str(magnet_set[2]))
        self.le_field_step_min.setText(str(magnet_set[3]))

        temp_set = self.pt_settings['temp_set']
        self.le_temp_max.setText(str(temp_set[0]))
        self.le_temp_min.setText(str(temp_set[1]))
        self.le_temp_rate_max.setText(str(temp_set[2]))
        self.le_temp_step_min.setText(str(temp_set[3]))

        self.le_field_temp_alarm.setText(str(self.pt_settings['alarm_field_temp']))
        self.le_field_temp_max.setText(str(self.pt_settings['max_field_temp']))

        for i in range(len(self.cb_itc_ls)):
            temp_itc = self.pt_settings["itc_set"][i]
            temp_db = self.pt_settings["db_set"][i]
            # print(f"{temp_itc}: {temp_db}")
            if temp_itc in self.itc_alias_ls:
                self.cb_itc_ls[i].setCurrentText(temp_itc)
                self.cb_db_ls[i].setCurrentText(temp_db)
            else:
                self.cb_itc_ls[i].setCurrentIndex(0)
                self.cb_db_ls[i].setCurrentText('None')
        self.part_ips_magnet_temp.setCurrentText(self.pt_settings["db_magnet_temp"])
        self.part_ips_pt1.setCurrentText(self.pt_settings["db_pt1"])
        self.part_ips_pt2.setCurrentText(self.pt_settings["db_pt2"])

        self.pb_save_setting.clicked.connect(self.save_pt_settings)

    def get_pt_settings(self):
        db_set_ls = []
        itc_set_ls = []
        for i in range(5):
            db_set_ls.append(self.cb_db_ls[i].currentText())
            itc_set_ls.append(self.cb_itc_ls[i].currentText())

        field_set = [float(self.le_field_max.text()), float(self.le_field_min.text()),
                     float(self.le_field_rate_max.text()), float(self.le_field_step_min.text())]

        temp_set = [float(self.le_temp_max.text()), float(self.le_temp_min.text()),
                    float(self.le_temp_rate_max.text()), float(self.le_temp_step_min.text())]

        pt_settings = {
            "temp_set": temp_set,
            "magnet_set": field_set,
            "itc_set": itc_set_ls,
            "db_set": db_set_ls,
            "alarm_field_temp": float(self.le_field_temp_alarm.text()),
            "max_field_temp": float(self.le_field_temp_max.text()),
            "db_magnet_temp": self.part_ips_magnet_temp.currentText(),
            "db_pt1": self.part_ips_pt1.currentText(),
            "db_pt2": self.part_ips_pt2.currentText(),
        }

        return pt_settings

    def save_pt_settings(self):
        try:
            self.pt_settings = self.get_pt_settings()
            with open("./.systems/pt_setting.pkl", 'wb') as file:
                pickle.dump(self.pt_settings, file)

            self.signal_pt_setting_changed.emit(self.pt_settings)

            self.hide()
        except Exception as e:
            print(repr(e))

