# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teslaPTcontrol.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_control(object):
    def setupUi(self, control):
        if not control.objectName():
            control.setObjectName(u"control")
        control.resize(976, 320)
        control.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_7 = QVBoxLayout(control)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_status = QLabel(control)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        self.lb_status.setFont(font)

        self.verticalLayout_7.addWidget(self.lb_status)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.groupBox_3 = QGroupBox(control)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(241, 211))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_magnet_meas_2 = QLabel(self.groupBox_3)
        self.lb_magnet_meas_2.setObjectName(u"lb_magnet_meas_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_magnet_meas_2.sizePolicy().hasHeightForWidth())
        self.lb_magnet_meas_2.setSizePolicy(sizePolicy)
        self.lb_magnet_meas_2.setMinimumSize(QSize(60, 0))
        self.lb_magnet_meas_2.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.lb_magnet_meas_2.setFont(font1)
        self.lb_magnet_meas_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_magnet_meas_2)

        self.rb_ips_heater_on = QRadioButton(self.groupBox_3)
        self.rb_ips_heater_on.setObjectName(u"rb_ips_heater_on")
        self.rb_ips_heater_on.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.rb_ips_heater_on)

        self.rb_ips_heater_off = QRadioButton(self.groupBox_3)
        self.rb_ips_heater_off.setObjectName(u"rb_ips_heater_off")
        self.rb_ips_heater_off.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.rb_ips_heater_off)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setMaximumSize(QSize(90, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.lb_c_field = QLabel(self.groupBox_3)
        self.lb_c_field.setObjectName(u"lb_c_field")
        sizePolicy.setHeightForWidth(self.lb_c_field.sizePolicy().hasHeightForWidth())
        self.lb_c_field.setSizePolicy(sizePolicy)
        self.lb_c_field.setMinimumSize(QSize(80, 0))
        self.lb_c_field.setMaximumSize(QSize(80, 16777215))
        self.lb_c_field.setFont(font1)
        self.lb_c_field.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_c_field)

        self.label1_21 = QLabel(self.groupBox_3)
        self.label1_21.setObjectName(u"label1_21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label1_21.sizePolicy().hasHeightForWidth())
        self.label1_21.setSizePolicy(sizePolicy1)
        self.label1_21.setMinimumSize(QSize(35, 0))
        self.label1_21.setMaximumSize(QSize(35, 16777215))
        self.label1_21.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label1_21)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setMaximumSize(QSize(90, 16777215))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lb_p_field = QLabel(self.groupBox_3)
        self.lb_p_field.setObjectName(u"lb_p_field")
        sizePolicy.setHeightForWidth(self.lb_p_field.sizePolicy().hasHeightForWidth())
        self.lb_p_field.setSizePolicy(sizePolicy)
        self.lb_p_field.setMinimumSize(QSize(80, 0))
        self.lb_p_field.setMaximumSize(QSize(80, 16777215))
        self.lb_p_field.setFont(font1)
        self.lb_p_field.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_p_field)

        self.label1_22 = QLabel(self.groupBox_3)
        self.label1_22.setObjectName(u"label1_22")
        sizePolicy1.setHeightForWidth(self.label1_22.sizePolicy().hasHeightForWidth())
        self.label1_22.setSizePolicy(sizePolicy1)
        self.label1_22.setMinimumSize(QSize(35, 0))
        self.label1_22.setMaximumSize(QSize(35, 16777215))
        self.label1_22.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label1_22)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setMaximumSize(QSize(90, 16777215))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.le_field_set = QLineEdit(self.groupBox_3)
        self.le_field_set.setObjectName(u"le_field_set")
        sizePolicy1.setHeightForWidth(self.le_field_set.sizePolicy().hasHeightForWidth())
        self.le_field_set.setSizePolicy(sizePolicy1)
        self.le_field_set.setMinimumSize(QSize(80, 0))
        self.le_field_set.setMaximumSize(QSize(80, 16777215))
        self.le_field_set.setFont(font2)
        self.le_field_set.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.le_field_set)

        self.label1_20 = QLabel(self.groupBox_3)
        self.label1_20.setObjectName(u"label1_20")
        sizePolicy1.setHeightForWidth(self.label1_20.sizePolicy().hasHeightForWidth())
        self.label1_20.setSizePolicy(sizePolicy1)
        self.label1_20.setMinimumSize(QSize(35, 0))
        self.label1_20.setMaximumSize(QSize(35, 16777215))
        self.label1_20.setFont(font2)

        self.horizontalLayout.addWidget(self.label1_20)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        self.label_3.setMaximumSize(QSize(90, 16777215))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_field_rate = QLineEdit(self.groupBox_3)
        self.le_field_rate.setObjectName(u"le_field_rate")
        sizePolicy1.setHeightForWidth(self.le_field_rate.sizePolicy().hasHeightForWidth())
        self.le_field_rate.setSizePolicy(sizePolicy1)
        self.le_field_rate.setMinimumSize(QSize(80, 0))
        self.le_field_rate.setMaximumSize(QSize(80, 16777215))
        self.le_field_rate.setFont(font2)
        self.le_field_rate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.le_field_rate)

        self.label1_19 = QLabel(self.groupBox_3)
        self.label1_19.setObjectName(u"label1_19")
        sizePolicy1.setHeightForWidth(self.label1_19.sizePolicy().hasHeightForWidth())
        self.label1_19.setSizePolicy(sizePolicy1)
        self.label1_19.setMinimumSize(QSize(35, 0))
        self.label1_19.setMaximumSize(QSize(35, 16777215))
        self.label1_19.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label1_19)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.pb_abort_field = QPushButton(self.groupBox_3)
        self.pb_abort_field.setObjectName(u"pb_abort_field")
        sizePolicy1.setHeightForWidth(self.pb_abort_field.sizePolicy().hasHeightForWidth())
        self.pb_abort_field.setSizePolicy(sizePolicy1)
        self.pb_abort_field.setMaximumSize(QSize(200, 16777215))
        self.pb_abort_field.setFont(font)

        self.horizontalLayout_5.addWidget(self.pb_abort_field)

        self.pb_scan_field = QPushButton(self.groupBox_3)
        self.pb_scan_field.setObjectName(u"pb_scan_field")
        sizePolicy1.setHeightForWidth(self.pb_scan_field.sizePolicy().hasHeightForWidth())
        self.pb_scan_field.setSizePolicy(sizePolicy1)
        self.pb_scan_field.setMaximumSize(QSize(200, 16777215))
        self.pb_scan_field.setFont(font)

        self.horizontalLayout_5.addWidget(self.pb_scan_field)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_25.addWidget(self.groupBox_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_pressure_meas_3 = QLabel(control)
        self.lb_pressure_meas_3.setObjectName(u"lb_pressure_meas_3")
        sizePolicy.setHeightForWidth(self.lb_pressure_meas_3.sizePolicy().hasHeightForWidth())
        self.lb_pressure_meas_3.setSizePolicy(sizePolicy)
        self.lb_pressure_meas_3.setMinimumSize(QSize(100, 0))
        self.lb_pressure_meas_3.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.lb_pressure_meas_3.setFont(font3)
        self.lb_pressure_meas_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.lb_pressure_meas_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(control)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(231, 171))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.rb_itc_heater_off_2 = QRadioButton(self.groupBox_2)
        self.rb_itc_heater_off_2.setObjectName(u"rb_itc_heater_off_2")

        self.horizontalLayout_15.addWidget(self.rb_itc_heater_off_2)

        self.lb_itc_heater_2 = QLabel(self.groupBox_2)
        self.lb_itc_heater_2.setObjectName(u"lb_itc_heater_2")
        sizePolicy.setHeightForWidth(self.lb_itc_heater_2.sizePolicy().hasHeightForWidth())
        self.lb_itc_heater_2.setSizePolicy(sizePolicy)
        self.lb_itc_heater_2.setMinimumSize(QSize(80, 0))
        self.lb_itc_heater_2.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_heater_2.setFont(font1)
        self.lb_itc_heater_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lb_itc_heater_2)

        self.label1_27 = QLabel(self.groupBox_2)
        self.label1_27.setObjectName(u"label1_27")
        sizePolicy1.setHeightForWidth(self.label1_27.sizePolicy().hasHeightForWidth())
        self.label1_27.setSizePolicy(sizePolicy1)
        self.label1_27.setMinimumSize(QSize(40, 0))
        self.label1_27.setMaximumSize(QSize(40, 16777215))
        self.label1_27.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label1_27)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setMaximumSize(QSize(80, 16777215))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.le_itc_heater_set_2 = QLineEdit(self.groupBox_2)
        self.le_itc_heater_set_2.setObjectName(u"le_itc_heater_set_2")
        sizePolicy1.setHeightForWidth(self.le_itc_heater_set_2.sizePolicy().hasHeightForWidth())
        self.le_itc_heater_set_2.setSizePolicy(sizePolicy1)
        self.le_itc_heater_set_2.setMinimumSize(QSize(80, 0))
        self.le_itc_heater_set_2.setMaximumSize(QSize(80, 16777215))
        self.le_itc_heater_set_2.setFont(font2)
        self.le_itc_heater_set_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.le_itc_heater_set_2)

        self.label1_28 = QLabel(self.groupBox_2)
        self.label1_28.setObjectName(u"label1_28")
        sizePolicy1.setHeightForWidth(self.label1_28.sizePolicy().hasHeightForWidth())
        self.label1_28.setSizePolicy(sizePolicy1)
        self.label1_28.setMinimumSize(QSize(40, 0))
        self.label1_28.setMaximumSize(QSize(40, 16777215))
        self.label1_28.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label1_28)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.rb_itc_heater_on_2 = QRadioButton(self.groupBox_2)
        self.rb_itc_heater_on_2.setObjectName(u"rb_itc_heater_on_2")

        self.horizontalLayout_17.addWidget(self.rb_itc_heater_on_2)

        self.lb_itc_temp_2 = QLabel(self.groupBox_2)
        self.lb_itc_temp_2.setObjectName(u"lb_itc_temp_2")
        sizePolicy.setHeightForWidth(self.lb_itc_temp_2.sizePolicy().hasHeightForWidth())
        self.lb_itc_temp_2.setSizePolicy(sizePolicy)
        self.lb_itc_temp_2.setMinimumSize(QSize(80, 0))
        self.lb_itc_temp_2.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_temp_2.setFont(font1)
        self.lb_itc_temp_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lb_itc_temp_2)

        self.label1_29 = QLabel(self.groupBox_2)
        self.label1_29.setObjectName(u"label1_29")
        sizePolicy1.setHeightForWidth(self.label1_29.sizePolicy().hasHeightForWidth())
        self.label1_29.setSizePolicy(sizePolicy1)
        self.label1_29.setMinimumSize(QSize(40, 0))
        self.label1_29.setMaximumSize(QSize(40, 16777215))
        self.label1_29.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label1_29)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_6)

        self.le_itc_temp_set_2 = QLineEdit(self.groupBox_2)
        self.le_itc_temp_set_2.setObjectName(u"le_itc_temp_set_2")
        sizePolicy1.setHeightForWidth(self.le_itc_temp_set_2.sizePolicy().hasHeightForWidth())
        self.le_itc_temp_set_2.setSizePolicy(sizePolicy1)
        self.le_itc_temp_set_2.setMinimumSize(QSize(80, 0))
        self.le_itc_temp_set_2.setMaximumSize(QSize(80, 16777215))
        self.le_itc_temp_set_2.setFont(font2)
        self.le_itc_temp_set_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.le_itc_temp_set_2)

        self.label1_30 = QLabel(self.groupBox_2)
        self.label1_30.setObjectName(u"label1_30")
        sizePolicy1.setHeightForWidth(self.label1_30.sizePolicy().hasHeightForWidth())
        self.label1_30.setSizePolicy(sizePolicy1)
        self.label1_30.setMinimumSize(QSize(40, 0))
        self.label1_30.setMaximumSize(QSize(40, 16777215))
        self.label1_30.setFont(font2)

        self.horizontalLayout_18.addWidget(self.label1_30)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.pb_scan_temp_2 = QPushButton(self.groupBox_2)
        self.pb_scan_temp_2.setObjectName(u"pb_scan_temp_2")
        sizePolicy1.setHeightForWidth(self.pb_scan_temp_2.sizePolicy().hasHeightForWidth())
        self.pb_scan_temp_2.setSizePolicy(sizePolicy1)
        self.pb_scan_temp_2.setMaximumSize(QSize(200, 16777215))
        self.pb_scan_temp_2.setFont(font)

        self.horizontalLayout_19.addWidget(self.pb_scan_temp_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(control)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(231, 171))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rb_itc_heater_off = QRadioButton(self.groupBox)
        self.rb_itc_heater_off.setObjectName(u"rb_itc_heater_off")

        self.horizontalLayout_8.addWidget(self.rb_itc_heater_off)

        self.lb_itc_heater = QLabel(self.groupBox)
        self.lb_itc_heater.setObjectName(u"lb_itc_heater")
        sizePolicy.setHeightForWidth(self.lb_itc_heater.sizePolicy().hasHeightForWidth())
        self.lb_itc_heater.setSizePolicy(sizePolicy)
        self.lb_itc_heater.setMinimumSize(QSize(80, 0))
        self.lb_itc_heater.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_heater.setFont(font1)
        self.lb_itc_heater.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lb_itc_heater)

        self.label1_24 = QLabel(self.groupBox)
        self.label1_24.setObjectName(u"label1_24")
        sizePolicy1.setHeightForWidth(self.label1_24.sizePolicy().hasHeightForWidth())
        self.label1_24.setSizePolicy(sizePolicy1)
        self.label1_24.setMinimumSize(QSize(40, 0))
        self.label1_24.setMaximumSize(QSize(40, 16777215))
        self.label1_24.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label1_24)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.le_itc_heater_set = QLineEdit(self.groupBox)
        self.le_itc_heater_set.setObjectName(u"le_itc_heater_set")
        sizePolicy1.setHeightForWidth(self.le_itc_heater_set.sizePolicy().hasHeightForWidth())
        self.le_itc_heater_set.setSizePolicy(sizePolicy1)
        self.le_itc_heater_set.setMinimumSize(QSize(80, 0))
        self.le_itc_heater_set.setMaximumSize(QSize(80, 16777215))
        self.le_itc_heater_set.setFont(font2)
        self.le_itc_heater_set.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.le_itc_heater_set)

        self.label1_26 = QLabel(self.groupBox)
        self.label1_26.setObjectName(u"label1_26")
        sizePolicy1.setHeightForWidth(self.label1_26.sizePolicy().hasHeightForWidth())
        self.label1_26.setSizePolicy(sizePolicy1)
        self.label1_26.setMinimumSize(QSize(40, 0))
        self.label1_26.setMaximumSize(QSize(40, 16777215))
        self.label1_26.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label1_26)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rb_itc_heater_on = QRadioButton(self.groupBox)
        self.rb_itc_heater_on.setObjectName(u"rb_itc_heater_on")

        self.horizontalLayout_11.addWidget(self.rb_itc_heater_on)

        self.lb_itc_temp = QLabel(self.groupBox)
        self.lb_itc_temp.setObjectName(u"lb_itc_temp")
        sizePolicy.setHeightForWidth(self.lb_itc_temp.sizePolicy().hasHeightForWidth())
        self.lb_itc_temp.setSizePolicy(sizePolicy)
        self.lb_itc_temp.setMinimumSize(QSize(80, 0))
        self.lb_itc_temp.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_temp.setFont(font1)
        self.lb_itc_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lb_itc_temp)

        self.label1_25 = QLabel(self.groupBox)
        self.label1_25.setObjectName(u"label1_25")
        sizePolicy1.setHeightForWidth(self.label1_25.sizePolicy().hasHeightForWidth())
        self.label1_25.setSizePolicy(sizePolicy1)
        self.label1_25.setMinimumSize(QSize(40, 0))
        self.label1_25.setMaximumSize(QSize(40, 16777215))
        self.label1_25.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label1_25)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.le_itc_temp_set = QLineEdit(self.groupBox)
        self.le_itc_temp_set.setObjectName(u"le_itc_temp_set")
        sizePolicy1.setHeightForWidth(self.le_itc_temp_set.sizePolicy().hasHeightForWidth())
        self.le_itc_temp_set.setSizePolicy(sizePolicy1)
        self.le_itc_temp_set.setMinimumSize(QSize(80, 0))
        self.le_itc_temp_set.setMaximumSize(QSize(80, 16777215))
        self.le_itc_temp_set.setFont(font2)
        self.le_itc_temp_set.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.le_itc_temp_set)

        self.label1_23 = QLabel(self.groupBox)
        self.label1_23.setObjectName(u"label1_23")
        sizePolicy1.setHeightForWidth(self.label1_23.sizePolicy().hasHeightForWidth())
        self.label1_23.setSizePolicy(sizePolicy1)
        self.label1_23.setMinimumSize(QSize(40, 0))
        self.label1_23.setMaximumSize(QSize(40, 16777215))
        self.label1_23.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label1_23)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.pb_scan_temp = QPushButton(self.groupBox)
        self.pb_scan_temp.setObjectName(u"pb_scan_temp")
        sizePolicy1.setHeightForWidth(self.pb_scan_temp.sizePolicy().hasHeightForWidth())
        self.pb_scan_temp.setSizePolicy(sizePolicy1)
        self.pb_scan_temp.setMaximumSize(QSize(200, 16777215))
        self.pb_scan_temp.setFont(font)

        self.horizontalLayout_13.addWidget(self.pb_scan_temp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(control)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(231, 171))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.rb_itc_heater_off_3 = QRadioButton(self.groupBox_4)
        self.rb_itc_heater_off_3.setObjectName(u"rb_itc_heater_off_3")

        self.horizontalLayout_20.addWidget(self.rb_itc_heater_off_3)

        self.lb_itc_heater_3 = QLabel(self.groupBox_4)
        self.lb_itc_heater_3.setObjectName(u"lb_itc_heater_3")
        sizePolicy.setHeightForWidth(self.lb_itc_heater_3.sizePolicy().hasHeightForWidth())
        self.lb_itc_heater_3.setSizePolicy(sizePolicy)
        self.lb_itc_heater_3.setMinimumSize(QSize(80, 0))
        self.lb_itc_heater_3.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_heater_3.setFont(font1)
        self.lb_itc_heater_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lb_itc_heater_3)

        self.label1_31 = QLabel(self.groupBox_4)
        self.label1_31.setObjectName(u"label1_31")
        sizePolicy1.setHeightForWidth(self.label1_31.sizePolicy().hasHeightForWidth())
        self.label1_31.setSizePolicy(sizePolicy1)
        self.label1_31.setMinimumSize(QSize(40, 0))
        self.label1_31.setMaximumSize(QSize(40, 16777215))
        self.label1_31.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label1_31)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(80, 0))
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_10)

        self.le_itc_heater_set_3 = QLineEdit(self.groupBox_4)
        self.le_itc_heater_set_3.setObjectName(u"le_itc_heater_set_3")
        sizePolicy1.setHeightForWidth(self.le_itc_heater_set_3.sizePolicy().hasHeightForWidth())
        self.le_itc_heater_set_3.setSizePolicy(sizePolicy1)
        self.le_itc_heater_set_3.setMinimumSize(QSize(80, 0))
        self.le_itc_heater_set_3.setMaximumSize(QSize(80, 16777215))
        self.le_itc_heater_set_3.setFont(font2)
        self.le_itc_heater_set_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.le_itc_heater_set_3)

        self.label1_32 = QLabel(self.groupBox_4)
        self.label1_32.setObjectName(u"label1_32")
        sizePolicy1.setHeightForWidth(self.label1_32.sizePolicy().hasHeightForWidth())
        self.label1_32.setSizePolicy(sizePolicy1)
        self.label1_32.setMinimumSize(QSize(40, 0))
        self.label1_32.setMaximumSize(QSize(40, 16777215))
        self.label1_32.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label1_32)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.rb_itc_heater_on_3 = QRadioButton(self.groupBox_4)
        self.rb_itc_heater_on_3.setObjectName(u"rb_itc_heater_on_3")

        self.horizontalLayout_22.addWidget(self.rb_itc_heater_on_3)

        self.lb_itc_temp_3 = QLabel(self.groupBox_4)
        self.lb_itc_temp_3.setObjectName(u"lb_itc_temp_3")
        sizePolicy.setHeightForWidth(self.lb_itc_temp_3.sizePolicy().hasHeightForWidth())
        self.lb_itc_temp_3.setSizePolicy(sizePolicy)
        self.lb_itc_temp_3.setMinimumSize(QSize(80, 0))
        self.lb_itc_temp_3.setMaximumSize(QSize(80, 16777215))
        self.lb_itc_temp_3.setFont(font1)
        self.lb_itc_temp_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lb_itc_temp_3)

        self.label1_33 = QLabel(self.groupBox_4)
        self.label1_33.setObjectName(u"label1_33")
        sizePolicy1.setHeightForWidth(self.label1_33.sizePolicy().hasHeightForWidth())
        self.label1_33.setSizePolicy(sizePolicy1)
        self.label1_33.setMinimumSize(QSize(40, 0))
        self.label1_33.setMaximumSize(QSize(40, 16777215))
        self.label1_33.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label1_33)


        self.verticalLayout_5.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_7)

        self.le_itc_temp_set_3 = QLineEdit(self.groupBox_4)
        self.le_itc_temp_set_3.setObjectName(u"le_itc_temp_set_3")
        sizePolicy1.setHeightForWidth(self.le_itc_temp_set_3.sizePolicy().hasHeightForWidth())
        self.le_itc_temp_set_3.setSizePolicy(sizePolicy1)
        self.le_itc_temp_set_3.setMinimumSize(QSize(80, 0))
        self.le_itc_temp_set_3.setMaximumSize(QSize(80, 16777215))
        self.le_itc_temp_set_3.setFont(font2)
        self.le_itc_temp_set_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.le_itc_temp_set_3)

        self.label1_34 = QLabel(self.groupBox_4)
        self.label1_34.setObjectName(u"label1_34")
        sizePolicy1.setHeightForWidth(self.label1_34.sizePolicy().hasHeightForWidth())
        self.label1_34.setSizePolicy(sizePolicy1)
        self.label1_34.setMinimumSize(QSize(40, 0))
        self.label1_34.setMaximumSize(QSize(40, 16777215))
        self.label1_34.setFont(font2)

        self.horizontalLayout_23.addWidget(self.label1_34)


        self.verticalLayout_5.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)

        self.pb_scan_temp_3 = QPushButton(self.groupBox_4)
        self.pb_scan_temp_3.setObjectName(u"pb_scan_temp_3")
        sizePolicy1.setHeightForWidth(self.pb_scan_temp_3.sizePolicy().hasHeightForWidth())
        self.pb_scan_temp_3.setSizePolicy(sizePolicy1)
        self.pb_scan_temp_3.setMaximumSize(QSize(200, 16777215))
        self.pb_scan_temp_3.setFont(font)

        self.horizontalLayout_24.addWidget(self.pb_scan_temp_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_25.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.pb_sync = QPushButton(control)
        self.pb_sync.setObjectName(u"pb_sync")
        sizePolicy1.setHeightForWidth(self.pb_sync.sizePolicy().hasHeightForWidth())
        self.pb_sync.setSizePolicy(sizePolicy1)
        self.pb_sync.setMaximumSize(QSize(100, 16777215))
        self.pb_sync.setFont(font)

        self.horizontalLayout_7.addWidget(self.pb_sync)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.retranslateUi(control)

        QMetaObject.connectSlotsByName(control)
    # setupUi

    def retranslateUi(self, control):
        control.setWindowTitle(QCoreApplication.translate("control", u"PT control winodw", None))
        self.lb_status.setText(QCoreApplication.translate("control", u"Ramping", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("control", u"IPS", None))
        self.lb_magnet_meas_2.setText(QCoreApplication.translate("control", u"IPS heater:", None))
        self.rb_ips_heater_on.setText(QCoreApplication.translate("control", u"On", None))
        self.rb_ips_heater_off.setText(QCoreApplication.translate("control", u"Off", None))
        self.label.setText(QCoreApplication.translate("control", u"Field:", None))
        self.lb_c_field.setText(QCoreApplication.translate("control", u"0.000T", None))
        self.label1_21.setText(QCoreApplication.translate("control", u"T", None))
        self.label_4.setText(QCoreApplication.translate("control", u"Magnet", None))
        self.lb_p_field.setText(QCoreApplication.translate("control", u"0.000T", None))
        self.label1_22.setText(QCoreApplication.translate("control", u"T", None))
        self.label_2.setText(QCoreApplication.translate("control", u"Field_set", None))
        self.le_field_set.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_20.setText(QCoreApplication.translate("control", u"T", None))
        self.label_3.setText(QCoreApplication.translate("control", u"Field_rate", None))
        self.le_field_rate.setText(QCoreApplication.translate("control", u"0.1", None))
        self.label1_19.setText(QCoreApplication.translate("control", u"T/min", None))
        self.pb_abort_field.setText(QCoreApplication.translate("control", u"abort", None))
        self.pb_scan_field.setText(QCoreApplication.translate("control", u"To Field Set", None))
        self.lb_pressure_meas_3.setText(QCoreApplication.translate("control", u"ITC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("control", u"VTI", None))
        self.rb_itc_heater_off_2.setText(QCoreApplication.translate("control", u"Manu", None))
        self.lb_itc_heater_2.setText(QCoreApplication.translate("control", u"0.123", None))
        self.label1_27.setText(QCoreApplication.translate("control", u"%", None))
        self.label_9.setText(QCoreApplication.translate("control", u"Power:", None))
        self.le_itc_heater_set_2.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_28.setText(QCoreApplication.translate("control", u"%", None))
        self.rb_itc_heater_on_2.setText(QCoreApplication.translate("control", u"Auto", None))
        self.lb_itc_temp_2.setText(QCoreApplication.translate("control", u"5", None))
        self.label1_29.setText(QCoreApplication.translate("control", u"K", None))
        self.label_6.setText(QCoreApplication.translate("control", u"TEMP_SET", None))
        self.le_itc_temp_set_2.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_30.setText(QCoreApplication.translate("control", u"K", None))
        self.pb_scan_temp_2.setText(QCoreApplication.translate("control", u"To  Set", None))
        self.groupBox.setTitle(QCoreApplication.translate("control", u"Probe", None))
        self.rb_itc_heater_off.setText(QCoreApplication.translate("control", u"Manu", None))
        self.lb_itc_heater.setText(QCoreApplication.translate("control", u"0.123", None))
        self.label1_24.setText(QCoreApplication.translate("control", u"%", None))
        self.label_8.setText(QCoreApplication.translate("control", u"Power:", None))
        self.le_itc_heater_set.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_26.setText(QCoreApplication.translate("control", u"%", None))
        self.rb_itc_heater_on.setText(QCoreApplication.translate("control", u"Auto", None))
        self.lb_itc_temp.setText(QCoreApplication.translate("control", u"5", None))
        self.label1_25.setText(QCoreApplication.translate("control", u"K", None))
        self.label_5.setText(QCoreApplication.translate("control", u"TEMP_SET", None))
        self.le_itc_temp_set.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_23.setText(QCoreApplication.translate("control", u"K", None))
        self.pb_scan_temp.setText(QCoreApplication.translate("control", u"To  Set", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("control", u"1K pool pressure", None))
        self.rb_itc_heater_off_3.setText(QCoreApplication.translate("control", u"Manu", None))
        self.lb_itc_heater_3.setText(QCoreApplication.translate("control", u"0.123", None))
        self.label1_31.setText(QCoreApplication.translate("control", u"%", None))
        self.label_10.setText(QCoreApplication.translate("control", u"N. V.", None))
        self.le_itc_heater_set_3.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_32.setText(QCoreApplication.translate("control", u"%", None))
        self.rb_itc_heater_on_3.setText(QCoreApplication.translate("control", u"Auto", None))
        self.lb_itc_temp_3.setText(QCoreApplication.translate("control", u"2.9", None))
        self.label1_33.setText(QCoreApplication.translate("control", u"mB", None))
        self.label_7.setText(QCoreApplication.translate("control", u"Presure", None))
        self.le_itc_temp_set_3.setText(QCoreApplication.translate("control", u"0", None))
        self.label1_34.setText(QCoreApplication.translate("control", u"mB", None))
        self.pb_scan_temp_3.setText(QCoreApplication.translate("control", u"To  Set", None))
        self.pb_sync.setText(QCoreApplication.translate("control", u"Sync", None))
    # retranslateUi

