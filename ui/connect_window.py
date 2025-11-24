# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(406, 278)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label1 = QLabel(Dialog)
        self.label1.setObjectName(u"label1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.label1.setFont(font1)

        self.horizontalLayout.addWidget(self.label1)

        self.le_alias = QLineEdit(Dialog)
        self.le_alias.setObjectName(u"le_alias")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_alias.sizePolicy().hasHeightForWidth())
        self.le_alias.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.le_alias.setFont(font2)

        self.horizontalLayout.addWidget(self.le_alias)

        self.label1_18 = QLabel(Dialog)
        self.label1_18.setObjectName(u"label1_18")
        sizePolicy.setHeightForWidth(self.label1_18.sizePolicy().hasHeightForWidth())
        self.label1_18.setSizePolicy(sizePolicy)
        self.label1_18.setFont(font1)

        self.horizontalLayout.addWidget(self.label1_18)

        self.le_port = QLineEdit(Dialog)
        self.le_port.setObjectName(u"le_port")
        sizePolicy1.setHeightForWidth(self.le_port.sizePolicy().hasHeightForWidth())
        self.le_port.setSizePolicy(sizePolicy1)
        self.le_port.setMinimumSize(QSize(80, 0))
        self.le_port.setMaximumSize(QSize(80, 16777215))
        self.le_port.setFont(font2)

        self.horizontalLayout.addWidget(self.le_port)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_log_addr = QPushButton(Dialog)
        self.pb_log_addr.setObjectName(u"pb_log_addr")

        self.horizontalLayout_2.addWidget(self.pb_log_addr)

        self.le_log_addr = QLineEdit(Dialog)
        self.le_log_addr.setObjectName(u"le_log_addr")
        self.le_log_addr.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_log_addr)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.pte_pt_addr = QPlainTextEdit(Dialog)
        self.pte_pt_addr.setObjectName(u"pte_pt_addr")
        self.pte_pt_addr.setMinimumSize(QSize(0, 65))
        font3 = QFont()
        font3.setPointSize(10)
        self.pte_pt_addr.setFont(font3)

        self.verticalLayout.addWidget(self.pte_pt_addr)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.pb_connect = QPushButton(Dialog)
        self.pb_connect.setObjectName(u"pb_connect")
        self.pb_connect.setFont(font2)

        self.horizontalLayout_15.addWidget(self.pb_connect)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5236\u51b7\u673a\u522b\u540d\u548c\u670d\u52a1\u5668\u7aef\u53e3\u53f7\uff1a", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Alias:", None))
        self.le_alias.setText(QCoreApplication.translate("Dialog", u"nanoPublicPT", None))
        self.label1_18.setText(QCoreApplication.translate("Dialog", u"\u7aef\u53e3\u53f7", None))
        self.le_port.setText(QCoreApplication.translate("Dialog", u"19020", None))
        self.pb_log_addr.setText(QCoreApplication.translate("Dialog", u"Log Addr", None))
        self.le_log_addr.setText(QCoreApplication.translate("Dialog", u".logs", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u63a7\u5236\u5668\uff0c\u5e76\u8f93\u5165\u6b63\u786e\u7684IP", None))
        self.pte_pt_addr.setPlainText(QCoreApplication.translate("Dialog", u"ips = TCPIP0::192.168.1.50::7020::SOCKET\n"
"itc = TCPIP0::192.168.1.100::7020::SOCKET\n"
"he3 = TCPIP0::192.168.1.30::7020::SOCKET", None))
        self.pb_connect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
    # retranslateUi

