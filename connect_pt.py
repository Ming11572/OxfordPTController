import pickle
import os.path

from ui.connect_window import Ui_Dialog
from teslapt_core import connect_to_tesla_pt
from log_saver import LogSaver
from main_window import PtMainWindow

from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import Qt


class Connector(QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        super(Connector, self).__init__(parent)
        self.setupUi(self)

        self.ips_addr = ""
        self.itc_ls = []
        self.itc_alias_ls = []
        self.controller_window = None

        try:
            with open("./.systems/connect_settings.pkl", "rb") as f:
                self.settings = pickle.load(f)
        except:
            self.settings = {
                "alias": "nanoPublicPT",
                "port": 19020,
                "log_addr": '...',
                "pt_addr": "ips=TCPIP0::192.168.1.50::7020::SOCKET\nitc=TCPIP0::192.168.1.100::7020::SOCKET\nhe3=TCPIP0::192.168.1.30::7020::SOCKET"
            }
        self.le_alias.setText(self.settings["alias"])
        self.le_port.setText(str(self.settings["port"]))
        self.le_log_addr.setText(self.settings["log_addr"])
        self.pte_pt_addr.setPlainText(self.settings["pt_addr"])

        self.pb_connect.clicked.connect(self.start_connect)
        self.pb_log_addr.clicked.connect(self.new_dir)

    def check_inputs(self):
        alias = self.le_alias.text()
        if alias == "":
            QMessageBox.warning(self, "Warning", "Please enter alias.")
            return False

        port = self.le_port.text()
        try:
            port = int(port)
        except:
            QMessageBox.warning(self, "Warning", "Please enter port number.")
            return False

        log_addr = self.le_log_addr.text()
        if not os.path.isdir(log_addr):
            QMessageBox.warning(self, "Warning", "log directory does not exist.")
            return False

        pt_addr = self.pte_pt_addr.toPlainText()
        pt_addr_ls = pt_addr.split("\n")
        itc_ls = []
        itc_alias = []
        ips = None
        for resource in pt_addr_ls:
            if "ips" in resource:
                ips = resource.split("=")[1]
            else:
                _alias, _addr = resource.split("=")
                itc_ls.append(_addr)
                itc_alias.append(_alias)
        if ips is None:
            QMessageBox.warning(self, "Warning", "Please enter ips address.")
            return False

        self.ips_addr = ips
        self.itc_ls = itc_ls
        self.itc_alias_ls = itc_alias

        self.settings.update({"alias": alias, "port": port, "log_addr": log_addr, "pt_addr": pt_addr})
        with open("./.systems/connect_settings.pkl", "wb") as f:
            pickle.dump(self.settings, f)
        return True

    def new_dir(self):
        path = QFileDialog.getExistingDirectory(None, "select dir for log files", r'./.logs/')
        if len(path) > 2:
            logging_path = path
        else:
            logging_path = './.logs'
        self.le_log_addr.setText(logging_path)

    def start_connect(self):
        """
        1. check_inputs
        2. connect to tesla PT
        3. open the main window
        :return:
        """
        if self.check_inputs():
            # connect to log_saver
            log_saver = LogSaver(self.settings["log_addr"])

            info_ls = [f"ips\t{self.ips_addr}"]
            for i in range(len(self.itc_ls)):
                info_ls.append(f"{self.itc_alias_ls[i]}\t{self.itc_ls[i]}")
            info = "\n".join(info_ls)
            reply = QMessageBox.question(self, "Check", f"Connect to the following controller:\n{info}",
                                        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Ok:
                flag, pt_core = connect_to_tesla_pt(log_saver, self.ips_addr, self.itc_ls, self.itc_alias_ls)
                if flag:
                    self.controller_window = PtMainWindow(log_saver, pt_core, self.itc_alias_ls,
                                                          self.settings["port"], self.settings["alias"])
                    self.controller_window.show()
                    self.hide()
                else:
                    QMessageBox.warning(self, "Warning", f"Failed to connect.. \n{pt_core}")


