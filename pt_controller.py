from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6 import QtCore, QtQuick
from connect_pt import Connector

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    QtQuick.QQuickWindow.setGraphicsApi(QtQuick.QSGRendererInterface.OpenGLRhi)
    app = QApplication([])

    con = Connector()
    con.show()

    app.exec()

