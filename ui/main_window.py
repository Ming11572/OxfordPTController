# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_magnet_meas_2 = QLabel(self.groupBox_3)
        self.lb_magnet_meas_2.setObjectName(u"lb_magnet_meas_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_magnet_meas_2.sizePolicy().hasHeightForWidth())
        self.lb_magnet_meas_2.setSizePolicy(sizePolicy)
        self.lb_magnet_meas_2.setMinimumSize(QSize(90, 0))
        self.lb_magnet_meas_2.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(False)
        self.lb_magnet_meas_2.setFont(font)
        self.lb_magnet_meas_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_magnet_meas_2)

        self.rb_ips_heater_on = QRadioButton(self.groupBox_3)
        self.rb_ips_heater_on.setObjectName(u"rb_ips_heater_on")
        self.rb_ips_heater_on.setMinimumSize(QSize(40, 0))
        self.rb_ips_heater_on.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.rb_ips_heater_on)

        self.rb_ips_heater_off = QRadioButton(self.groupBox_3)
        self.rb_ips_heater_off.setObjectName(u"rb_ips_heater_off")
        self.rb_ips_heater_off.setMinimumSize(QSize(40, 0))
        self.rb_ips_heater_off.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.rb_ips_heater_off)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setMaximumSize(QSize(90, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.lb_switch_field = QLabel(self.groupBox_3)
        self.lb_switch_field.setObjectName(u"lb_switch_field")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_switch_field.sizePolicy().hasHeightForWidth())
        self.lb_switch_field.setSizePolicy(sizePolicy1)
        self.lb_switch_field.setMinimumSize(QSize(100, 0))
        self.lb_switch_field.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lb_switch_field.setFont(font2)
        self.lb_switch_field.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_switch_field)

        self.label1_21 = QLabel(self.groupBox_3)
        self.label1_21.setObjectName(u"label1_21")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label1_21.sizePolicy().hasHeightForWidth())
        self.label1_21.setSizePolicy(sizePolicy2)
        self.label1_21.setMinimumSize(QSize(0, 0))
        self.label1_21.setMaximumSize(QSize(38, 16777215))
        self.label1_21.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label1_21)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setMaximumSize(QSize(90, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lb_magnet_field = QLabel(self.groupBox_3)
        self.lb_magnet_field.setObjectName(u"lb_magnet_field")
        sizePolicy1.setHeightForWidth(self.lb_magnet_field.sizePolicy().hasHeightForWidth())
        self.lb_magnet_field.setSizePolicy(sizePolicy1)
        self.lb_magnet_field.setMinimumSize(QSize(100, 0))
        self.lb_magnet_field.setMaximumSize(QSize(100, 16777215))
        self.lb_magnet_field.setFont(font2)
        self.lb_magnet_field.setStyleSheet(u"")
        self.lb_magnet_field.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_magnet_field)

        self.label1_22 = QLabel(self.groupBox_3)
        self.label1_22.setObjectName(u"label1_22")
        sizePolicy2.setHeightForWidth(self.label1_22.sizePolicy().hasHeightForWidth())
        self.label1_22.setSizePolicy(sizePolicy2)
        self.label1_22.setMinimumSize(QSize(0, 0))
        self.label1_22.setMaximumSize(QSize(38, 16777215))
        self.label1_22.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label1_22)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 0))
        self.label_5.setMaximumSize(QSize(90, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lb_magnet_goal = QLabel(self.groupBox_3)
        self.lb_magnet_goal.setObjectName(u"lb_magnet_goal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_magnet_goal.sizePolicy().hasHeightForWidth())
        self.lb_magnet_goal.setSizePolicy(sizePolicy3)
        self.lb_magnet_goal.setMinimumSize(QSize(100, 0))
        self.lb_magnet_goal.setMaximumSize(QSize(100, 16777215))
        self.lb_magnet_goal.setFont(font2)
        self.lb_magnet_goal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_magnet_goal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_magnet_goal)

        self.label1_20 = QLabel(self.groupBox_3)
        self.label1_20.setObjectName(u"label1_20")
        sizePolicy2.setHeightForWidth(self.label1_20.sizePolicy().hasHeightForWidth())
        self.label1_20.setSizePolicy(sizePolicy2)
        self.label1_20.setMinimumSize(QSize(0, 0))
        self.label1_20.setMaximumSize(QSize(38, 16777215))
        self.label1_20.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label1_20)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        self.label_3.setMaximumSize(QSize(90, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lb_magnet_rate = QLabel(self.groupBox_3)
        self.lb_magnet_rate.setObjectName(u"lb_magnet_rate")
        sizePolicy3.setHeightForWidth(self.lb_magnet_rate.sizePolicy().hasHeightForWidth())
        self.lb_magnet_rate.setSizePolicy(sizePolicy3)
        self.lb_magnet_rate.setMinimumSize(QSize(100, 0))
        self.lb_magnet_rate.setMaximumSize(QSize(100, 16777215))
        self.lb_magnet_rate.setFont(font2)
        self.lb_magnet_rate.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_magnet_rate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_magnet_rate)

        self.label1_19 = QLabel(self.groupBox_3)
        self.label1_19.setObjectName(u"label1_19")
        sizePolicy2.setHeightForWidth(self.label1_19.sizePolicy().hasHeightForWidth())
        self.label1_19.setSizePolicy(sizePolicy2)
        self.label1_19.setMinimumSize(QSize(0, 0))
        self.label1_19.setMaximumSize(QSize(38, 16777215))
        self.label1_19.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label1_19)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_hold = QRadioButton(self.groupBox_3)
        self.rb_hold.setObjectName(u"rb_hold")

        self.horizontalLayout.addWidget(self.rb_hold)

        self.rb_to_set = QRadioButton(self.groupBox_3)
        self.rb_to_set.setObjectName(u"rb_to_set")

        self.horizontalLayout.addWidget(self.rb_to_set)

        self.rb_to_zero = QRadioButton(self.groupBox_3)
        self.rb_to_zero.setObjectName(u"rb_to_zero")

        self.horizontalLayout.addWidget(self.rb_to_zero)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_25.addWidget(self.groupBox_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_pressure_meas_3 = QLabel(self.centralwidget)
        self.lb_pressure_meas_3.setObjectName(u"lb_pressure_meas_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lb_pressure_meas_3.sizePolicy().hasHeightForWidth())
        self.lb_pressure_meas_3.setSizePolicy(sizePolicy4)
        self.lb_pressure_meas_3.setMinimumSize(QSize(0, 0))
        self.lb_pressure_meas_3.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.lb_pressure_meas_3.setFont(font3)

        self.horizontalLayout_14.addWidget(self.lb_pressure_meas_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_probe_temp = QLabel(self.groupBox)
        self.lb_probe_temp.setObjectName(u"lb_probe_temp")
        sizePolicy2.setHeightForWidth(self.lb_probe_temp.sizePolicy().hasHeightForWidth())
        self.lb_probe_temp.setSizePolicy(sizePolicy2)
        self.lb_probe_temp.setMinimumSize(QSize(80, 0))
        self.lb_probe_temp.setMaximumSize(QSize(1000, 16777215))
        self.lb_probe_temp.setFont(font2)
        self.lb_probe_temp.setStyleSheet(u"")
        self.lb_probe_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lb_probe_temp)

        self.label1_32 = QLabel(self.groupBox)
        self.label1_32.setObjectName(u"label1_32")
        sizePolicy4.setHeightForWidth(self.label1_32.sizePolicy().hasHeightForWidth())
        self.label1_32.setSizePolicy(sizePolicy4)
        self.label1_32.setMinimumSize(QSize(30, 0))
        self.label1_32.setMaximumSize(QSize(30, 16777215))
        self.label1_32.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label1_32)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rb_itc_heater_on = QRadioButton(self.groupBox)
        self.rb_itc_heater_on.setObjectName(u"rb_itc_heater_on")
        self.rb_itc_heater_on.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_on.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_11.addWidget(self.rb_itc_heater_on)

        self.lb_probe_temp_goal = QLabel(self.groupBox)
        self.lb_probe_temp_goal.setObjectName(u"lb_probe_temp_goal")
        sizePolicy3.setHeightForWidth(self.lb_probe_temp_goal.sizePolicy().hasHeightForWidth())
        self.lb_probe_temp_goal.setSizePolicy(sizePolicy3)
        self.lb_probe_temp_goal.setMinimumSize(QSize(80, 0))
        self.lb_probe_temp_goal.setMaximumSize(QSize(10000, 16777215))
        self.lb_probe_temp_goal.setFont(font2)
        self.lb_probe_temp_goal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_probe_temp_goal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lb_probe_temp_goal)

        self.label1_25 = QLabel(self.groupBox)
        self.label1_25.setObjectName(u"label1_25")
        sizePolicy4.setHeightForWidth(self.label1_25.sizePolicy().hasHeightForWidth())
        self.label1_25.setSizePolicy(sizePolicy4)
        self.label1_25.setMinimumSize(QSize(30, 0))
        self.label1_25.setMaximumSize(QSize(30, 16777215))
        self.label1_25.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label1_25)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rb_itc_heater_off = QRadioButton(self.groupBox)
        self.rb_itc_heater_off.setObjectName(u"rb_itc_heater_off")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.rb_itc_heater_off.sizePolicy().hasHeightForWidth())
        self.rb_itc_heater_off.setSizePolicy(sizePolicy5)
        self.rb_itc_heater_off.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_off.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_8.addWidget(self.rb_itc_heater_off)

        self.lb_probe_heater = QLabel(self.groupBox)
        self.lb_probe_heater.setObjectName(u"lb_probe_heater")
        sizePolicy3.setHeightForWidth(self.lb_probe_heater.sizePolicy().hasHeightForWidth())
        self.lb_probe_heater.setSizePolicy(sizePolicy3)
        self.lb_probe_heater.setMinimumSize(QSize(80, 0))
        self.lb_probe_heater.setMaximumSize(QSize(10000, 16777215))
        self.lb_probe_heater.setFont(font2)
        self.lb_probe_heater.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_probe_heater.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lb_probe_heater)

        self.label1_24 = QLabel(self.groupBox)
        self.label1_24.setObjectName(u"label1_24")
        sizePolicy4.setHeightForWidth(self.label1_24.sizePolicy().hasHeightForWidth())
        self.label1_24.setSizePolicy(sizePolicy4)
        self.label1_24.setMinimumSize(QSize(30, 0))
        self.label1_24.setMaximumSize(QSize(30, 16777215))
        self.label1_24.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label1_24)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_vti_temp = QLabel(self.groupBox_2)
        self.lb_vti_temp.setObjectName(u"lb_vti_temp")
        sizePolicy2.setHeightForWidth(self.lb_vti_temp.sizePolicy().hasHeightForWidth())
        self.lb_vti_temp.setSizePolicy(sizePolicy2)
        self.lb_vti_temp.setMinimumSize(QSize(80, 0))
        self.lb_vti_temp.setMaximumSize(QSize(1000, 16777215))
        self.lb_vti_temp.setFont(font2)
        self.lb_vti_temp.setStyleSheet(u"")
        self.lb_vti_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lb_vti_temp)

        self.label1_30 = QLabel(self.groupBox_2)
        self.label1_30.setObjectName(u"label1_30")
        sizePolicy4.setHeightForWidth(self.label1_30.sizePolicy().hasHeightForWidth())
        self.label1_30.setSizePolicy(sizePolicy4)
        self.label1_30.setMinimumSize(QSize(30, 0))
        self.label1_30.setMaximumSize(QSize(30, 16777215))
        self.label1_30.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label1_30)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.rb_itc_heater_on_2 = QRadioButton(self.groupBox_2)
        self.rb_itc_heater_on_2.setObjectName(u"rb_itc_heater_on_2")
        self.rb_itc_heater_on_2.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_on_2.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_17.addWidget(self.rb_itc_heater_on_2)

        self.lb_vti_temp_goal = QLabel(self.groupBox_2)
        self.lb_vti_temp_goal.setObjectName(u"lb_vti_temp_goal")
        sizePolicy4.setHeightForWidth(self.lb_vti_temp_goal.sizePolicy().hasHeightForWidth())
        self.lb_vti_temp_goal.setSizePolicy(sizePolicy4)
        self.lb_vti_temp_goal.setMinimumSize(QSize(80, 0))
        self.lb_vti_temp_goal.setMaximumSize(QSize(10000, 16777215))
        self.lb_vti_temp_goal.setFont(font2)
        self.lb_vti_temp_goal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_vti_temp_goal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lb_vti_temp_goal)

        self.label1_29 = QLabel(self.groupBox_2)
        self.label1_29.setObjectName(u"label1_29")
        sizePolicy4.setHeightForWidth(self.label1_29.sizePolicy().hasHeightForWidth())
        self.label1_29.setSizePolicy(sizePolicy4)
        self.label1_29.setMinimumSize(QSize(30, 0))
        self.label1_29.setMaximumSize(QSize(30, 16777215))
        self.label1_29.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label1_29)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.rb_itc_heater_off_2 = QRadioButton(self.groupBox_2)
        self.rb_itc_heater_off_2.setObjectName(u"rb_itc_heater_off_2")
        self.rb_itc_heater_off_2.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_off_2.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_15.addWidget(self.rb_itc_heater_off_2)

        self.lb_vti_heater = QLabel(self.groupBox_2)
        self.lb_vti_heater.setObjectName(u"lb_vti_heater")
        sizePolicy4.setHeightForWidth(self.lb_vti_heater.sizePolicy().hasHeightForWidth())
        self.lb_vti_heater.setSizePolicy(sizePolicy4)
        self.lb_vti_heater.setMinimumSize(QSize(80, 0))
        self.lb_vti_heater.setMaximumSize(QSize(10000, 16777215))
        self.lb_vti_heater.setFont(font2)
        self.lb_vti_heater.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_vti_heater.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lb_vti_heater)

        self.label1_27 = QLabel(self.groupBox_2)
        self.label1_27.setObjectName(u"label1_27")
        sizePolicy4.setHeightForWidth(self.label1_27.sizePolicy().hasHeightForWidth())
        self.label1_27.setSizePolicy(sizePolicy4)
        self.label1_27.setMinimumSize(QSize(30, 0))
        self.label1_27.setMaximumSize(QSize(30, 16777215))
        self.label1_27.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label1_27)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_nv_pressure = QLabel(self.groupBox_4)
        self.lb_nv_pressure.setObjectName(u"lb_nv_pressure")
        sizePolicy2.setHeightForWidth(self.lb_nv_pressure.sizePolicy().hasHeightForWidth())
        self.lb_nv_pressure.setSizePolicy(sizePolicy2)
        self.lb_nv_pressure.setMinimumSize(QSize(80, 0))
        self.lb_nv_pressure.setMaximumSize(QSize(1000, 16777215))
        self.lb_nv_pressure.setFont(font2)
        self.lb_nv_pressure.setStyleSheet(u"")
        self.lb_nv_pressure.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lb_nv_pressure)

        self.label1_34 = QLabel(self.groupBox_4)
        self.label1_34.setObjectName(u"label1_34")
        sizePolicy4.setHeightForWidth(self.label1_34.sizePolicy().hasHeightForWidth())
        self.label1_34.setSizePolicy(sizePolicy4)
        self.label1_34.setMinimumSize(QSize(30, 0))
        self.label1_34.setMaximumSize(QSize(30, 16777215))
        self.label1_34.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label1_34)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.rb_itc_heater_on_3 = QRadioButton(self.groupBox_4)
        self.rb_itc_heater_on_3.setObjectName(u"rb_itc_heater_on_3")
        self.rb_itc_heater_on_3.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_on_3.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_22.addWidget(self.rb_itc_heater_on_3)

        self.lb_nv_pressure_goal = QLabel(self.groupBox_4)
        self.lb_nv_pressure_goal.setObjectName(u"lb_nv_pressure_goal")
        sizePolicy4.setHeightForWidth(self.lb_nv_pressure_goal.sizePolicy().hasHeightForWidth())
        self.lb_nv_pressure_goal.setSizePolicy(sizePolicy4)
        self.lb_nv_pressure_goal.setMinimumSize(QSize(80, 0))
        self.lb_nv_pressure_goal.setMaximumSize(QSize(10000, 16777215))
        self.lb_nv_pressure_goal.setFont(font2)
        self.lb_nv_pressure_goal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_nv_pressure_goal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lb_nv_pressure_goal)

        self.label1_33 = QLabel(self.groupBox_4)
        self.label1_33.setObjectName(u"label1_33")
        sizePolicy4.setHeightForWidth(self.label1_33.sizePolicy().hasHeightForWidth())
        self.label1_33.setSizePolicy(sizePolicy4)
        self.label1_33.setMinimumSize(QSize(30, 0))
        self.label1_33.setMaximumSize(QSize(30, 16777215))
        self.label1_33.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label1_33)


        self.verticalLayout_5.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.rb_itc_heater_off_3 = QRadioButton(self.groupBox_4)
        self.rb_itc_heater_off_3.setObjectName(u"rb_itc_heater_off_3")
        self.rb_itc_heater_off_3.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_off_3.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_20.addWidget(self.rb_itc_heater_off_3)

        self.lb_nv_heater = QLabel(self.groupBox_4)
        self.lb_nv_heater.setObjectName(u"lb_nv_heater")
        sizePolicy4.setHeightForWidth(self.lb_nv_heater.sizePolicy().hasHeightForWidth())
        self.lb_nv_heater.setSizePolicy(sizePolicy4)
        self.lb_nv_heater.setMinimumSize(QSize(80, 0))
        self.lb_nv_heater.setMaximumSize(QSize(10000, 16777215))
        self.lb_nv_heater.setFont(font2)
        self.lb_nv_heater.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_nv_heater.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lb_nv_heater)

        self.label1_31 = QLabel(self.groupBox_4)
        self.label1_31.setObjectName(u"label1_31")
        sizePolicy4.setHeightForWidth(self.label1_31.sizePolicy().hasHeightForWidth())
        self.label1_31.setSizePolicy(sizePolicy4)
        self.label1_31.setMinimumSize(QSize(30, 0))
        self.label1_31.setMaximumSize(QSize(30, 16777215))
        self.label1_31.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label1_31)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_sorb_temp = QLabel(self.groupBox_5)
        self.lb_sorb_temp.setObjectName(u"lb_sorb_temp")
        sizePolicy2.setHeightForWidth(self.lb_sorb_temp.sizePolicy().hasHeightForWidth())
        self.lb_sorb_temp.setSizePolicy(sizePolicy2)
        self.lb_sorb_temp.setMinimumSize(QSize(80, 0))
        self.lb_sorb_temp.setMaximumSize(QSize(1000, 16777215))
        self.lb_sorb_temp.setFont(font2)
        self.lb_sorb_temp.setStyleSheet(u"")
        self.lb_sorb_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lb_sorb_temp)

        self.label1_35 = QLabel(self.groupBox_5)
        self.label1_35.setObjectName(u"label1_35")
        sizePolicy4.setHeightForWidth(self.label1_35.sizePolicy().hasHeightForWidth())
        self.label1_35.setSizePolicy(sizePolicy4)
        self.label1_35.setMinimumSize(QSize(30, 0))
        self.label1_35.setMaximumSize(QSize(30, 16777215))
        self.label1_35.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label1_35)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.rb_itc_heater_on_4 = QRadioButton(self.groupBox_5)
        self.rb_itc_heater_on_4.setObjectName(u"rb_itc_heater_on_4")
        self.rb_itc_heater_on_4.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_on_4.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_23.addWidget(self.rb_itc_heater_on_4)

        self.lb_sorb_goal = QLabel(self.groupBox_5)
        self.lb_sorb_goal.setObjectName(u"lb_sorb_goal")
        sizePolicy4.setHeightForWidth(self.lb_sorb_goal.sizePolicy().hasHeightForWidth())
        self.lb_sorb_goal.setSizePolicy(sizePolicy4)
        self.lb_sorb_goal.setMinimumSize(QSize(80, 0))
        self.lb_sorb_goal.setMaximumSize(QSize(10000, 16777215))
        self.lb_sorb_goal.setFont(font2)
        self.lb_sorb_goal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_sorb_goal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.lb_sorb_goal)

        self.label1_36 = QLabel(self.groupBox_5)
        self.label1_36.setObjectName(u"label1_36")
        sizePolicy4.setHeightForWidth(self.label1_36.sizePolicy().hasHeightForWidth())
        self.label1_36.setSizePolicy(sizePolicy4)
        self.label1_36.setMinimumSize(QSize(30, 0))
        self.label1_36.setMaximumSize(QSize(30, 16777215))
        self.label1_36.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label1_36)


        self.verticalLayout_8.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.rb_itc_heater_off_4 = QRadioButton(self.groupBox_5)
        self.rb_itc_heater_off_4.setObjectName(u"rb_itc_heater_off_4")
        self.rb_itc_heater_off_4.setMinimumSize(QSize(55, 0))
        self.rb_itc_heater_off_4.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_24.addWidget(self.rb_itc_heater_off_4)

        self.lb_sorb_heater = QLabel(self.groupBox_5)
        self.lb_sorb_heater.setObjectName(u"lb_sorb_heater")
        sizePolicy4.setHeightForWidth(self.lb_sorb_heater.sizePolicy().hasHeightForWidth())
        self.lb_sorb_heater.setSizePolicy(sizePolicy4)
        self.lb_sorb_heater.setMinimumSize(QSize(80, 0))
        self.lb_sorb_heater.setMaximumSize(QSize(10000, 16777215))
        self.lb_sorb_heater.setFont(font2)
        self.lb_sorb_heater.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_sorb_heater.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.lb_sorb_heater)

        self.label1_37 = QLabel(self.groupBox_5)
        self.label1_37.setObjectName(u"label1_37")
        sizePolicy4.setHeightForWidth(self.label1_37.sizePolicy().hasHeightForWidth())
        self.label1_37.setSizePolicy(sizePolicy4)
        self.label1_37.setMinimumSize(QSize(30, 0))
        self.label1_37.setMaximumSize(QSize(30, 16777215))
        self.label1_37.setFont(font1)

        self.horizontalLayout_24.addWidget(self.label1_37)


        self.verticalLayout_8.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_2.addWidget(self.groupBox_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 3)

        self.horizontalLayout_25.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_13)

        self.lb_magnetT = QLabel(self.centralwidget)
        self.lb_magnetT.setObjectName(u"lb_magnetT")
        sizePolicy4.setHeightForWidth(self.lb_magnetT.sizePolicy().hasHeightForWidth())
        self.lb_magnetT.setSizePolicy(sizePolicy4)
        self.lb_magnetT.setMinimumSize(QSize(100, 0))
        self.lb_magnetT.setMaximumSize(QSize(100, 16777215))
        self.lb_magnetT.setFont(font1)
        self.lb_magnetT.setStyleSheet(u"")
        self.lb_magnetT.setTextFormat(Qt.PlainText)
        self.lb_magnetT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lb_magnetT)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_11)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_16)

        self.lb_pt1 = QLabel(self.centralwidget)
        self.lb_pt1.setObjectName(u"lb_pt1")
        sizePolicy4.setHeightForWidth(self.lb_pt1.sizePolicy().hasHeightForWidth())
        self.lb_pt1.setSizePolicy(sizePolicy4)
        self.lb_pt1.setMinimumSize(QSize(100, 0))
        self.lb_pt1.setMaximumSize(QSize(100, 16777215))
        self.lb_pt1.setFont(font1)
        self.lb_pt1.setTextFormat(Qt.PlainText)
        self.lb_pt1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lb_pt1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_14)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_2)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_17)

        self.lb_pt2 = QLabel(self.centralwidget)
        self.lb_pt2.setObjectName(u"lb_pt2")
        sizePolicy4.setHeightForWidth(self.lb_pt2.sizePolicy().hasHeightForWidth())
        self.lb_pt2.setSizePolicy(sizePolicy4)
        self.lb_pt2.setMinimumSize(QSize(100, 0))
        self.lb_pt2.setMaximumSize(QSize(100, 16777215))
        self.lb_pt2.setFont(font1)
        self.lb_pt2.setTextFormat(Qt.PlainText)
        self.lb_pt2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lb_pt2)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_18)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer)

        self.pb_warm_up = QPushButton(self.centralwidget)
        self.pb_warm_up.setObjectName(u"pb_warm_up")
        sizePolicy4.setHeightForWidth(self.pb_warm_up.sizePolicy().hasHeightForWidth())
        self.pb_warm_up.setSizePolicy(sizePolicy4)
        self.pb_warm_up.setMaximumSize(QSize(100, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(11)
        self.pb_warm_up.setFont(font4)

        self.horizontalLayout_26.addWidget(self.pb_warm_up)

        self.pb_cool_down = QPushButton(self.centralwidget)
        self.pb_cool_down.setObjectName(u"pb_cool_down")
        sizePolicy4.setHeightForWidth(self.pb_cool_down.sizePolicy().hasHeightForWidth())
        self.pb_cool_down.setSizePolicy(sizePolicy4)
        self.pb_cool_down.setMaximumSize(QSize(100, 16777215))
        self.pb_cool_down.setFont(font4)

        self.horizontalLayout_26.addWidget(self.pb_cool_down)

        self.pb_abort_warm_cool = QPushButton(self.centralwidget)
        self.pb_abort_warm_cool.setObjectName(u"pb_abort_warm_cool")
        sizePolicy4.setHeightForWidth(self.pb_abort_warm_cool.sizePolicy().hasHeightForWidth())
        self.pb_abort_warm_cool.setSizePolicy(sizePolicy4)
        self.pb_abort_warm_cool.setMaximumSize(QSize(100, 16777215))
        self.pb_abort_warm_cool.setFont(font4)

        self.horizontalLayout_26.addWidget(self.pb_abort_warm_cool)

        self.pb_setting = QPushButton(self.centralwidget)
        self.pb_setting.setObjectName(u"pb_setting")
        sizePolicy4.setHeightForWidth(self.pb_setting.sizePolicy().hasHeightForWidth())
        self.pb_setting.setSizePolicy(sizePolicy4)
        self.pb_setting.setMaximumSize(QSize(100, 16777215))
        self.pb_setting.setFont(font4)

        self.horizontalLayout_26.addWidget(self.pb_setting)

        self.pb_logs = QPushButton(self.centralwidget)
        self.pb_logs.setObjectName(u"pb_logs")
        sizePolicy4.setHeightForWidth(self.pb_logs.sizePolicy().hasHeightForWidth())
        self.pb_logs.setSizePolicy(sizePolicy4)
        self.pb_logs.setMaximumSize(QSize(100, 16777215))
        self.pb_logs.setFont(font4)

        self.horizontalLayout_26.addWidget(self.pb_logs)


        self.verticalLayout_2.addLayout(self.horizontalLayout_26)

        self.lb_servers_status = QLabel(self.centralwidget)
        self.lb_servers_status.setObjectName(u"lb_servers_status")
        font5 = QFont()
        font5.setPointSize(9)
        self.lb_servers_status.setFont(font5)

        self.verticalLayout_2.addWidget(self.lb_servers_status)

        self.pte_status = QPlainTextEdit(self.centralwidget)
        self.pte_status.setObjectName(u"pte_status")
        self.pte_status.setEnabled(True)
        self.pte_status.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.pte_status)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(3, 15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"IPS", None))
        self.lb_magnet_meas_2.setText(QCoreApplication.translate("MainWindow", u"IPS heater:", None))
        self.rb_ips_heater_on.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.rb_ips_heater_off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Magnet Switch", None))
        self.lb_switch_field.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label1_21.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Magnet", None))
        self.lb_magnet_field.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label1_22.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Magnet goal", None))
        self.lb_magnet_goal.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_20.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Field_rate", None))
        self.lb_magnet_rate.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_19.setText(QCoreApplication.translate("MainWindow", u"T/min", None))
        self.rb_hold.setText(QCoreApplication.translate("MainWindow", u"hold", None))
        self.rb_to_set.setText(QCoreApplication.translate("MainWindow", u"to set", None))
        self.rb_to_zero.setText(QCoreApplication.translate("MainWindow", u"to zero", None))
        self.lb_pressure_meas_3.setText(QCoreApplication.translate("MainWindow", u"ITC", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Probe", None))
        self.lb_probe_temp.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_32.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_on.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lb_probe_temp_goal.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_25.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_off.setText(QCoreApplication.translate("MainWindow", u"Manu", None))
        self.lb_probe_heater.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_24.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"VTI", None))
        self.lb_vti_temp.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_30.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_on_2.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lb_vti_temp_goal.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_29.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_off_2.setText(QCoreApplication.translate("MainWindow", u"Manu", None))
        self.lb_vti_heater.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_27.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"N.V.", None))
        self.lb_nv_pressure.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_34.setText(QCoreApplication.translate("MainWindow", u"mB", None))
        self.rb_itc_heater_on_3.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lb_nv_pressure_goal.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_33.setText(QCoreApplication.translate("MainWindow", u"mB", None))
        self.rb_itc_heater_off_3.setText(QCoreApplication.translate("MainWindow", u"Manu", None))
        self.lb_nv_heater.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_31.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Sorb", None))
        self.lb_sorb_temp.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_35.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_on_4.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lb_sorb_goal.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_36.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.rb_itc_heater_off_4.setText(QCoreApplication.translate("MainWindow", u"Manu", None))
        self.lb_sorb_heater.setText(QCoreApplication.translate("MainWindow", u"0.123", None))
        self.label1_37.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Magnet T:", None))
        self.lb_magnetT.setText(QCoreApplication.translate("MainWindow", u"1.534", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PT1:", None))
        self.lb_pt1.setText(QCoreApplication.translate("MainWindow", u"10.234", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"PT2:", None))
        self.lb_pt2.setText(QCoreApplication.translate("MainWindow", u"1.534", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.pb_warm_up.setText(QCoreApplication.translate("MainWindow", u"Warm", None))
        self.pb_cool_down.setText(QCoreApplication.translate("MainWindow", u"Cool", None))
        self.pb_abort_warm_cool.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.pb_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.pb_logs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.lb_servers_status.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u8fde\u63a5Oxford Teslatron PT\u3002\u670d\u52a1\u5668\u5df2\u5f00\u542f\uff0c\u76d1\u542c\u7aef\u53e3\uff1a 19020\uff0c\u7b49\u5f85\u8fde\u63a5....", None))
    # retranslateUi

