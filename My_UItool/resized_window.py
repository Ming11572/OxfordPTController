from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QFont
import pickle


class ResizedMainWindow(QMainWindow):

    def __init__(self, window_name, parent=None):
        # super().__init__()
        # self.window_name = window_name
        QMainWindow.__init__(self)
        # super(ResizedMainWindow, self).__init__(parent=parent)
        self.title_block_height = self.frameGeometry().height() - self.geometry().height()
        self.file_path_size_pos = f'.systems/size_and_pos/{window_name}_size_pos.pkl'

        # 字体
        self.font_selected = QFont(u"Times New Roman", pointSize=11)
        self.font_selected.setBold(True)
        self.font_unselected = QFont(u"Times New Roman", pointSize=10)
        self.font_unselected.setBold(False)

    def init_window_size_and_pos(self):
        # print(self.file_path_size_pos)
        try:
            with open(self.file_path_size_pos, 'rb') as file:
                size, pos = pickle.load(file)
                self.move(pos.x(), pos.y() - self.title_block_height)
                self.resize(size)
        except Exception as e:
            print(e)

    def resizeEvent(self, event) -> None:
        with open(self.file_path_size_pos, 'wb') as file:
            win_size = self.size()
            win_pos = self.pos()
            pickle.dump((win_size, win_pos), file)

    def moveEvent(self, event) -> None:
        with open(self.file_path_size_pos, 'wb') as file:
            win_size = self.size()
            win_pos = self.pos()
            pickle.dump((win_size, win_pos), file)


class ResizedDialog(QWidget):

    def __init__(self, window_name, parent=None):
        QWidget.__init__(self)
        # super(ResizedMainWindow, self).__init__(parent=parent)
        self.title_block_height = self.frameGeometry().height() - self.geometry().height()
        self.file_path_size_pos = f'.systems/size_and_pos/{window_name}_size_pos.pkl'

        # 字体
        self.font_selected = QFont(u"Times New Roman", pointSize=11)
        self.font_selected.setBold(True)
        self.font_unselected = QFont(u"Times New Roman", pointSize=10)
        self.font_unselected.setBold(False)

    def init_window_size_and_pos(self):
        # print(self.file_path_size_pos)
        try:
            with open(self.file_path_size_pos, 'rb') as file:
                size, pos = pickle.load(file)
                self.move(pos.x(), pos.y() - self.title_block_height)
                self.resize(size)
        except Exception as e:
            print(e)

    def resizeEvent(self, event) -> None:
        with open(self.file_path_size_pos, 'wb') as file:
            win_size = self.size()
            win_pos = self.pos()
            pickle.dump((win_size, win_pos), file)

    def moveEvent(self, event) -> None:
        with open(self.file_path_size_pos, 'wb') as file:
            win_size = self.size()
            win_pos = self.pos()
            pickle.dump((win_size, win_pos), file)

