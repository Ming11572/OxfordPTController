# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PT_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PTSetting(object):
    def setupUi(self, PTSetting):
        if not PTSetting.objectName():
            PTSetting.setObjectName(u"PTSetting")
        PTSetting.resize(504, 497)
        PTSetting.setMaximumSize(QSize(7500, 5210))
        self.verticalLayout_5 = QVBoxLayout(PTSetting)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox = QGroupBox(PTSetting)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label1_2 = QLabel(self.groupBox)
        self.label1_2.setObjectName(u"label1_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1_2.sizePolicy().hasHeightForWidth())
        self.label1_2.setSizePolicy(sizePolicy)
        self.label1_2.setMinimumSize(QSize(70, 0))
        self.label1_2.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        self.label1_2.setFont(font)

        self.horizontalLayout.addWidget(self.label1_2)

        self.le_field_max = QLineEdit(self.groupBox)
        self.le_field_max.setObjectName(u"le_field_max")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_field_max.sizePolicy().hasHeightForWidth())
        self.le_field_max.setSizePolicy(sizePolicy1)
        self.le_field_max.setMinimumSize(QSize(100, 0))
        self.le_field_max.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.le_field_max.setFont(font1)

        self.horizontalLayout.addWidget(self.le_field_max)

        self.lb_unit_max = QLabel(self.groupBox)
        self.lb_unit_max.setObjectName(u"lb_unit_max")
        sizePolicy.setHeightForWidth(self.lb_unit_max.sizePolicy().hasHeightForWidth())
        self.lb_unit_max.setSizePolicy(sizePolicy)
        self.lb_unit_max.setMinimumSize(QSize(35, 0))
        self.lb_unit_max.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_max.setFont(font)

        self.horizontalLayout.addWidget(self.lb_unit_max)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label1_4 = QLabel(self.groupBox)
        self.label1_4.setObjectName(u"label1_4")
        sizePolicy.setHeightForWidth(self.label1_4.sizePolicy().hasHeightForWidth())
        self.label1_4.setSizePolicy(sizePolicy)
        self.label1_4.setMinimumSize(QSize(70, 0))
        self.label1_4.setMaximumSize(QSize(80, 16777215))
        self.label1_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label1_4)

        self.le_field_min = QLineEdit(self.groupBox)
        self.le_field_min.setObjectName(u"le_field_min")
        sizePolicy1.setHeightForWidth(self.le_field_min.sizePolicy().hasHeightForWidth())
        self.le_field_min.setSizePolicy(sizePolicy1)
        self.le_field_min.setMinimumSize(QSize(100, 0))
        self.le_field_min.setMaximumSize(QSize(100, 16777215))
        self.le_field_min.setFont(font1)

        self.horizontalLayout_2.addWidget(self.le_field_min)

        self.lb_unit_min = QLabel(self.groupBox)
        self.lb_unit_min.setObjectName(u"lb_unit_min")
        sizePolicy.setHeightForWidth(self.lb_unit_min.sizePolicy().hasHeightForWidth())
        self.lb_unit_min.setSizePolicy(sizePolicy)
        self.lb_unit_min.setMinimumSize(QSize(35, 0))
        self.lb_unit_min.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_min.setFont(font)

        self.horizontalLayout_2.addWidget(self.lb_unit_min)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label1_5 = QLabel(self.groupBox)
        self.label1_5.setObjectName(u"label1_5")
        sizePolicy.setHeightForWidth(self.label1_5.sizePolicy().hasHeightForWidth())
        self.label1_5.setSizePolicy(sizePolicy)
        self.label1_5.setMinimumSize(QSize(70, 0))
        self.label1_5.setMaximumSize(QSize(80, 16777215))
        self.label1_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label1_5)

        self.le_field_rate_max = QLineEdit(self.groupBox)
        self.le_field_rate_max.setObjectName(u"le_field_rate_max")
        sizePolicy1.setHeightForWidth(self.le_field_rate_max.sizePolicy().hasHeightForWidth())
        self.le_field_rate_max.setSizePolicy(sizePolicy1)
        self.le_field_rate_max.setMinimumSize(QSize(100, 0))
        self.le_field_rate_max.setMaximumSize(QSize(100, 16777215))
        self.le_field_rate_max.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_field_rate_max)

        self.lb_unit_speed = QLabel(self.groupBox)
        self.lb_unit_speed.setObjectName(u"lb_unit_speed")
        sizePolicy.setHeightForWidth(self.lb_unit_speed.sizePolicy().hasHeightForWidth())
        self.lb_unit_speed.setSizePolicy(sizePolicy)
        self.lb_unit_speed.setMinimumSize(QSize(35, 0))
        self.lb_unit_speed.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_speed.setFont(font)

        self.horizontalLayout_3.addWidget(self.lb_unit_speed)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label1_6 = QLabel(self.groupBox)
        self.label1_6.setObjectName(u"label1_6")
        sizePolicy.setHeightForWidth(self.label1_6.sizePolicy().hasHeightForWidth())
        self.label1_6.setSizePolicy(sizePolicy)
        self.label1_6.setMinimumSize(QSize(70, 0))
        self.label1_6.setMaximumSize(QSize(80, 16777215))
        self.label1_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label1_6)

        self.le_field_step_min = QLineEdit(self.groupBox)
        self.le_field_step_min.setObjectName(u"le_field_step_min")
        sizePolicy1.setHeightForWidth(self.le_field_step_min.sizePolicy().hasHeightForWidth())
        self.le_field_step_min.setSizePolicy(sizePolicy1)
        self.le_field_step_min.setMinimumSize(QSize(100, 0))
        self.le_field_step_min.setMaximumSize(QSize(100, 16777215))
        self.le_field_step_min.setFont(font1)

        self.horizontalLayout_4.addWidget(self.le_field_step_min)

        self.lb_unit_step = QLabel(self.groupBox)
        self.lb_unit_step.setObjectName(u"lb_unit_step")
        sizePolicy.setHeightForWidth(self.lb_unit_step.sizePolicy().hasHeightForWidth())
        self.lb_unit_step.setSizePolicy(sizePolicy)
        self.lb_unit_step.setMinimumSize(QSize(35, 0))
        self.lb_unit_step.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_step.setFont(font)

        self.horizontalLayout_4.addWidget(self.lb_unit_step)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_14.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(PTSetting)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label1_7 = QLabel(self.groupBox_2)
        self.label1_7.setObjectName(u"label1_7")
        sizePolicy.setHeightForWidth(self.label1_7.sizePolicy().hasHeightForWidth())
        self.label1_7.setSizePolicy(sizePolicy)
        self.label1_7.setMinimumSize(QSize(70, 0))
        self.label1_7.setMaximumSize(QSize(80, 16777215))
        self.label1_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label1_7)

        self.le_temp_max = QLineEdit(self.groupBox_2)
        self.le_temp_max.setObjectName(u"le_temp_max")
        sizePolicy1.setHeightForWidth(self.le_temp_max.sizePolicy().hasHeightForWidth())
        self.le_temp_max.setSizePolicy(sizePolicy1)
        self.le_temp_max.setMinimumSize(QSize(100, 0))
        self.le_temp_max.setMaximumSize(QSize(100, 16777215))
        self.le_temp_max.setFont(font1)

        self.horizontalLayout_5.addWidget(self.le_temp_max)

        self.lb_unit_max_2 = QLabel(self.groupBox_2)
        self.lb_unit_max_2.setObjectName(u"lb_unit_max_2")
        sizePolicy.setHeightForWidth(self.lb_unit_max_2.sizePolicy().hasHeightForWidth())
        self.lb_unit_max_2.setSizePolicy(sizePolicy)
        self.lb_unit_max_2.setMinimumSize(QSize(35, 0))
        self.lb_unit_max_2.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_max_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.lb_unit_max_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label1_8 = QLabel(self.groupBox_2)
        self.label1_8.setObjectName(u"label1_8")
        sizePolicy.setHeightForWidth(self.label1_8.sizePolicy().hasHeightForWidth())
        self.label1_8.setSizePolicy(sizePolicy)
        self.label1_8.setMinimumSize(QSize(70, 0))
        self.label1_8.setMaximumSize(QSize(80, 16777215))
        self.label1_8.setFont(font)

        self.horizontalLayout_6.addWidget(self.label1_8)

        self.le_temp_min = QLineEdit(self.groupBox_2)
        self.le_temp_min.setObjectName(u"le_temp_min")
        sizePolicy1.setHeightForWidth(self.le_temp_min.sizePolicy().hasHeightForWidth())
        self.le_temp_min.setSizePolicy(sizePolicy1)
        self.le_temp_min.setMinimumSize(QSize(100, 0))
        self.le_temp_min.setMaximumSize(QSize(100, 16777215))
        self.le_temp_min.setFont(font1)

        self.horizontalLayout_6.addWidget(self.le_temp_min)

        self.lb_unit_min_2 = QLabel(self.groupBox_2)
        self.lb_unit_min_2.setObjectName(u"lb_unit_min_2")
        sizePolicy.setHeightForWidth(self.lb_unit_min_2.sizePolicy().hasHeightForWidth())
        self.lb_unit_min_2.setSizePolicy(sizePolicy)
        self.lb_unit_min_2.setMinimumSize(QSize(35, 0))
        self.lb_unit_min_2.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_min_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.lb_unit_min_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label1_9 = QLabel(self.groupBox_2)
        self.label1_9.setObjectName(u"label1_9")
        sizePolicy.setHeightForWidth(self.label1_9.sizePolicy().hasHeightForWidth())
        self.label1_9.setSizePolicy(sizePolicy)
        self.label1_9.setMinimumSize(QSize(70, 0))
        self.label1_9.setMaximumSize(QSize(80, 16777215))
        self.label1_9.setFont(font)

        self.horizontalLayout_7.addWidget(self.label1_9)

        self.le_temp_rate_max = QLineEdit(self.groupBox_2)
        self.le_temp_rate_max.setObjectName(u"le_temp_rate_max")
        sizePolicy1.setHeightForWidth(self.le_temp_rate_max.sizePolicy().hasHeightForWidth())
        self.le_temp_rate_max.setSizePolicy(sizePolicy1)
        self.le_temp_rate_max.setMinimumSize(QSize(100, 0))
        self.le_temp_rate_max.setMaximumSize(QSize(100, 16777215))
        self.le_temp_rate_max.setFont(font1)

        self.horizontalLayout_7.addWidget(self.le_temp_rate_max)

        self.lb_unit_speed_2 = QLabel(self.groupBox_2)
        self.lb_unit_speed_2.setObjectName(u"lb_unit_speed_2")
        sizePolicy.setHeightForWidth(self.lb_unit_speed_2.sizePolicy().hasHeightForWidth())
        self.lb_unit_speed_2.setSizePolicy(sizePolicy)
        self.lb_unit_speed_2.setMinimumSize(QSize(35, 0))
        self.lb_unit_speed_2.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_speed_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.lb_unit_speed_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label1_10 = QLabel(self.groupBox_2)
        self.label1_10.setObjectName(u"label1_10")
        sizePolicy.setHeightForWidth(self.label1_10.sizePolicy().hasHeightForWidth())
        self.label1_10.setSizePolicy(sizePolicy)
        self.label1_10.setMinimumSize(QSize(70, 0))
        self.label1_10.setMaximumSize(QSize(80, 16777215))
        self.label1_10.setFont(font)

        self.horizontalLayout_8.addWidget(self.label1_10)

        self.le_temp_step_min = QLineEdit(self.groupBox_2)
        self.le_temp_step_min.setObjectName(u"le_temp_step_min")
        sizePolicy1.setHeightForWidth(self.le_temp_step_min.sizePolicy().hasHeightForWidth())
        self.le_temp_step_min.setSizePolicy(sizePolicy1)
        self.le_temp_step_min.setMinimumSize(QSize(100, 0))
        self.le_temp_step_min.setMaximumSize(QSize(100, 16777215))
        self.le_temp_step_min.setFont(font1)

        self.horizontalLayout_8.addWidget(self.le_temp_step_min)

        self.lb_unit_step_2 = QLabel(self.groupBox_2)
        self.lb_unit_step_2.setObjectName(u"lb_unit_step_2")
        sizePolicy.setHeightForWidth(self.lb_unit_step_2.sizePolicy().hasHeightForWidth())
        self.lb_unit_step_2.setSizePolicy(sizePolicy)
        self.lb_unit_step_2.setMinimumSize(QSize(35, 0))
        self.lb_unit_step_2.setMaximumSize(QSize(40, 16777215))
        self.lb_unit_step_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.lb_unit_step_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_14.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.groupBox_4 = QGroupBox(PTSetting)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.part_item_6 = QLabel(self.groupBox_4)
        self.part_item_6.setObjectName(u"part_item_6")
        sizePolicy.setHeightForWidth(self.part_item_6.sizePolicy().hasHeightForWidth())
        self.part_item_6.setSizePolicy(sizePolicy)
        self.part_item_6.setMinimumSize(QSize(130, 0))
        self.part_item_6.setMaximumSize(QSize(130, 16777215))
        self.part_item_6.setFont(font)
        self.part_item_6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.part_item_6)

        self.label1_16 = QLabel(self.groupBox_4)
        self.label1_16.setObjectName(u"label1_16")
        sizePolicy.setHeightForWidth(self.label1_16.sizePolicy().hasHeightForWidth())
        self.label1_16.setSizePolicy(sizePolicy)
        self.label1_16.setMinimumSize(QSize(80, 0))
        self.label1_16.setMaximumSize(QSize(60, 16777215))
        self.label1_16.setFont(font)

        self.horizontalLayout_16.addWidget(self.label1_16)

        self.label1_17 = QLabel(self.groupBox_4)
        self.label1_17.setObjectName(u"label1_17")
        sizePolicy.setHeightForWidth(self.label1_17.sizePolicy().hasHeightForWidth())
        self.label1_17.setSizePolicy(sizePolicy)
        self.label1_17.setMinimumSize(QSize(80, 0))
        self.label1_17.setMaximumSize(QSize(60, 16777215))
        self.label1_17.setFont(font)

        self.horizontalLayout_16.addWidget(self.label1_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.part_item_1 = QLabel(self.groupBox_4)
        self.part_item_1.setObjectName(u"part_item_1")
        sizePolicy.setHeightForWidth(self.part_item_1.sizePolicy().hasHeightForWidth())
        self.part_item_1.setSizePolicy(sizePolicy)
        self.part_item_1.setMinimumSize(QSize(130, 0))
        self.part_item_1.setMaximumSize(QSize(130, 16777215))
        self.part_item_1.setFont(font)
        self.part_item_1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_17.addWidget(self.part_item_1)

        self.part_itc_1 = QComboBox(self.groupBox_4)
        self.part_itc_1.setObjectName(u"part_itc_1")
        self.part_itc_1.setMinimumSize(QSize(80, 0))
        self.part_itc_1.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.part_itc_1)

        self.part_db_1 = QComboBox(self.groupBox_4)
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.addItem("")
        self.part_db_1.setObjectName(u"part_db_1")
        self.part_db_1.setMinimumSize(QSize(80, 0))
        self.part_db_1.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.part_db_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.part_item_2 = QLabel(self.groupBox_4)
        self.part_item_2.setObjectName(u"part_item_2")
        sizePolicy.setHeightForWidth(self.part_item_2.sizePolicy().hasHeightForWidth())
        self.part_item_2.setSizePolicy(sizePolicy)
        self.part_item_2.setMinimumSize(QSize(130, 0))
        self.part_item_2.setMaximumSize(QSize(130, 16777215))
        self.part_item_2.setFont(font)
        self.part_item_2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_18.addWidget(self.part_item_2)

        self.part_itc_2 = QComboBox(self.groupBox_4)
        self.part_itc_2.setObjectName(u"part_itc_2")
        self.part_itc_2.setMinimumSize(QSize(80, 0))
        self.part_itc_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_18.addWidget(self.part_itc_2)

        self.part_db_2 = QComboBox(self.groupBox_4)
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.addItem("")
        self.part_db_2.setObjectName(u"part_db_2")
        self.part_db_2.setMinimumSize(QSize(80, 0))
        self.part_db_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_18.addWidget(self.part_db_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.part_item_3 = QLabel(self.groupBox_4)
        self.part_item_3.setObjectName(u"part_item_3")
        sizePolicy.setHeightForWidth(self.part_item_3.sizePolicy().hasHeightForWidth())
        self.part_item_3.setSizePolicy(sizePolicy)
        self.part_item_3.setMinimumSize(QSize(130, 0))
        self.part_item_3.setMaximumSize(QSize(130, 16777215))
        self.part_item_3.setFont(font)
        self.part_item_3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_19.addWidget(self.part_item_3)

        self.part_itc_3 = QComboBox(self.groupBox_4)
        self.part_itc_3.setObjectName(u"part_itc_3")
        self.part_itc_3.setMinimumSize(QSize(80, 0))
        self.part_itc_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_19.addWidget(self.part_itc_3)

        self.part_db_3 = QComboBox(self.groupBox_4)
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.addItem("")
        self.part_db_3.setObjectName(u"part_db_3")
        self.part_db_3.setMinimumSize(QSize(80, 0))
        self.part_db_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_19.addWidget(self.part_db_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.part_item_4 = QLabel(self.groupBox_4)
        self.part_item_4.setObjectName(u"part_item_4")
        sizePolicy.setHeightForWidth(self.part_item_4.sizePolicy().hasHeightForWidth())
        self.part_item_4.setSizePolicy(sizePolicy)
        self.part_item_4.setMinimumSize(QSize(130, 0))
        self.part_item_4.setMaximumSize(QSize(130, 16777215))
        self.part_item_4.setFont(font)
        self.part_item_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_20.addWidget(self.part_item_4)

        self.part_itc_4 = QComboBox(self.groupBox_4)
        self.part_itc_4.setObjectName(u"part_itc_4")
        self.part_itc_4.setMinimumSize(QSize(80, 0))
        self.part_itc_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_20.addWidget(self.part_itc_4)

        self.part_db_4 = QComboBox(self.groupBox_4)
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.addItem("")
        self.part_db_4.setObjectName(u"part_db_4")
        self.part_db_4.setMinimumSize(QSize(80, 0))
        self.part_db_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_20.addWidget(self.part_db_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.part_item_5 = QLabel(self.groupBox_4)
        self.part_item_5.setObjectName(u"part_item_5")
        sizePolicy.setHeightForWidth(self.part_item_5.sizePolicy().hasHeightForWidth())
        self.part_item_5.setSizePolicy(sizePolicy)
        self.part_item_5.setMinimumSize(QSize(130, 0))
        self.part_item_5.setMaximumSize(QSize(130, 16777215))
        self.part_item_5.setFont(font)

        self.horizontalLayout_24.addWidget(self.part_item_5)

        self.part_itc_5 = QComboBox(self.groupBox_4)
        self.part_itc_5.setObjectName(u"part_itc_5")
        self.part_itc_5.setMinimumSize(QSize(80, 0))
        self.part_itc_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_24.addWidget(self.part_itc_5)

        self.part_db_5 = QComboBox(self.groupBox_4)
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.addItem("")
        self.part_db_5.setObjectName(u"part_db_5")
        self.part_db_5.setMinimumSize(QSize(80, 0))
        self.part_db_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_24.addWidget(self.part_db_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.part_item_8 = QLabel(self.groupBox_4)
        self.part_item_8.setObjectName(u"part_item_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.part_item_8.sizePolicy().hasHeightForWidth())
        self.part_item_8.setSizePolicy(sizePolicy2)
        self.part_item_8.setMinimumSize(QSize(0, 0))
        self.part_item_8.setMaximumSize(QSize(130, 16777215))
        self.part_item_8.setFont(font)

        self.horizontalLayout_26.addWidget(self.part_item_8)

        self.part_ips_magnet_temp = QComboBox(self.groupBox_4)
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.addItem("")
        self.part_ips_magnet_temp.setObjectName(u"part_ips_magnet_temp")
        self.part_ips_magnet_temp.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_26.addWidget(self.part_ips_magnet_temp)

        self.part_ips_pt1 = QComboBox(self.groupBox_4)
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.addItem("")
        self.part_ips_pt1.setObjectName(u"part_ips_pt1")
        self.part_ips_pt1.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_26.addWidget(self.part_ips_pt1)

        self.part_ips_pt2 = QComboBox(self.groupBox_4)
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.addItem("")
        self.part_ips_pt2.setObjectName(u"part_ips_pt2")
        self.part_ips_pt2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_26.addWidget(self.part_ips_pt2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_22.addLayout(self.verticalLayout_4)


        self.horizontalLayout_23.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(PTSetting)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(100, 0))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label1_3 = QLabel(self.groupBox_5)
        self.label1_3.setObjectName(u"label1_3")
        sizePolicy.setHeightForWidth(self.label1_3.sizePolicy().hasHeightForWidth())
        self.label1_3.setSizePolicy(sizePolicy)
        self.label1_3.setMinimumSize(QSize(120, 0))
        self.label1_3.setMaximumSize(QSize(120, 16777215))
        self.label1_3.setFont(font)

        self.verticalLayout_6.addWidget(self.label1_3)

        self.le_field_temp_alarm = QLineEdit(self.groupBox_5)
        self.le_field_temp_alarm.setObjectName(u"le_field_temp_alarm")
        sizePolicy1.setHeightForWidth(self.le_field_temp_alarm.sizePolicy().hasHeightForWidth())
        self.le_field_temp_alarm.setSizePolicy(sizePolicy1)
        self.le_field_temp_alarm.setMinimumSize(QSize(100, 0))
        self.le_field_temp_alarm.setMaximumSize(QSize(100, 16777215))
        self.le_field_temp_alarm.setFont(font1)

        self.verticalLayout_6.addWidget(self.le_field_temp_alarm)

        self.label1_15 = QLabel(self.groupBox_5)
        self.label1_15.setObjectName(u"label1_15")
        sizePolicy.setHeightForWidth(self.label1_15.sizePolicy().hasHeightForWidth())
        self.label1_15.setSizePolicy(sizePolicy)
        self.label1_15.setMinimumSize(QSize(120, 0))
        self.label1_15.setMaximumSize(QSize(120, 16777215))
        self.label1_15.setFont(font)

        self.verticalLayout_6.addWidget(self.label1_15)

        self.le_field_temp_max = QLineEdit(self.groupBox_5)
        self.le_field_temp_max.setObjectName(u"le_field_temp_max")
        sizePolicy1.setHeightForWidth(self.le_field_temp_max.sizePolicy().hasHeightForWidth())
        self.le_field_temp_max.setSizePolicy(sizePolicy1)
        self.le_field_temp_max.setMinimumSize(QSize(100, 0))
        self.le_field_temp_max.setMaximumSize(QSize(100, 16777215))
        self.le_field_temp_max.setFont(font1)

        self.verticalLayout_6.addWidget(self.le_field_temp_max)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_23.addWidget(self.groupBox_5)

        self.horizontalLayout_23.setStretch(0, 6)

        self.verticalLayout_5.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.pb_save_setting = QPushButton(PTSetting)
        self.pb_save_setting.setObjectName(u"pb_save_setting")
        self.pb_save_setting.setFont(font1)

        self.horizontalLayout_10.addWidget(self.pb_save_setting)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.retranslateUi(PTSetting)

        self.part_db_1.setCurrentIndex(9)
        self.part_db_2.setCurrentIndex(9)
        self.part_db_3.setCurrentIndex(1)
        self.part_db_4.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(PTSetting)
    # setupUi

    def retranslateUi(self, PTSetting):
        PTSetting.setWindowTitle(QCoreApplication.translate("PTSetting", u"PT Setting", None))
        self.groupBox.setTitle(QCoreApplication.translate("PTSetting", u"Field", None))
        self.label1_2.setText(QCoreApplication.translate("PTSetting", u"Max Field:", None))
        self.le_field_max.setText(QCoreApplication.translate("PTSetting", u"7.5", None))
        self.lb_unit_max.setText(QCoreApplication.translate("PTSetting", u"T", None))
        self.label1_4.setText(QCoreApplication.translate("PTSetting", u"Min Field:", None))
        self.le_field_min.setText(QCoreApplication.translate("PTSetting", u"-7.5", None))
        self.lb_unit_min.setText(QCoreApplication.translate("PTSetting", u"T", None))
        self.label1_5.setText(QCoreApplication.translate("PTSetting", u"Max Ramp:", None))
        self.le_field_rate_max.setText(QCoreApplication.translate("PTSetting", u"0.2", None))
        self.lb_unit_speed.setText(QCoreApplication.translate("PTSetting", u"T/min", None))
        self.label1_6.setText(QCoreApplication.translate("PTSetting", u"Min Step", None))
        self.le_field_step_min.setText(QCoreApplication.translate("PTSetting", u"0.001", None))
        self.lb_unit_step.setText(QCoreApplication.translate("PTSetting", u"T", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PTSetting", u"Temperature", None))
        self.label1_7.setText(QCoreApplication.translate("PTSetting", u"Max TEM:", None))
        self.le_temp_max.setText(QCoreApplication.translate("PTSetting", u"300", None))
        self.lb_unit_max_2.setText(QCoreApplication.translate("PTSetting", u"K", None))
        self.label1_8.setText(QCoreApplication.translate("PTSetting", u"Min TEM:", None))
        self.le_temp_min.setText(QCoreApplication.translate("PTSetting", u"0.1", None))
        self.lb_unit_min_2.setText(QCoreApplication.translate("PTSetting", u"K", None))
        self.label1_9.setText(QCoreApplication.translate("PTSetting", u"Max Ramp:", None))
        self.le_temp_rate_max.setText(QCoreApplication.translate("PTSetting", u"2", None))
        self.lb_unit_speed_2.setText(QCoreApplication.translate("PTSetting", u"K/min", None))
        self.label1_10.setText(QCoreApplication.translate("PTSetting", u"Min Step", None))
        self.le_temp_step_min.setText(QCoreApplication.translate("PTSetting", u"0.005", None))
        self.lb_unit_step_2.setText(QCoreApplication.translate("PTSetting", u"K", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PTSetting", u"Connect", None))
        self.part_item_6.setText("")
        self.label1_16.setText(QCoreApplication.translate("PTSetting", u"Controller", None))
        self.label1_17.setText(QCoreApplication.translate("PTSetting", u"DB", None))
        self.part_item_1.setText(QCoreApplication.translate("PTSetting", u"Probe Temp Low", None))
        self.part_db_1.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_db_1.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_db_1.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_db_1.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_db_1.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_db_1.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_db_1.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_db_1.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_db_1.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_db_1.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_db_1.setCurrentText(QCoreApplication.translate("PTSetting", u"DB8", None))
        self.part_item_2.setText(QCoreApplication.translate("PTSetting", u"Probe Temp High", None))
        self.part_db_2.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_db_2.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_db_2.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_db_2.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_db_2.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_db_2.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_db_2.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_db_2.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_db_2.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_db_2.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_db_2.setCurrentText(QCoreApplication.translate("PTSetting", u"DB8", None))
        self.part_item_3.setText(QCoreApplication.translate("PTSetting", u"VTI Temp", None))
        self.part_db_3.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_db_3.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_db_3.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_db_3.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_db_3.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_db_3.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_db_3.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_db_3.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_db_3.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_db_3.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_db_3.setCurrentText(QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_item_4.setText(QCoreApplication.translate("PTSetting", u"N.V. out Pressure", None))
        self.part_db_4.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_db_4.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_db_4.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_db_4.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_db_4.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_db_4.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_db_4.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_db_4.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_db_4.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_db_4.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_db_4.setCurrentText(QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_item_5.setText(QCoreApplication.translate("PTSetting", u"Sorb", None))
        self.part_db_5.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_db_5.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_db_5.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_db_5.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_db_5.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_db_5.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_db_5.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_db_5.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_db_5.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_db_5.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_db_5.setCurrentText(QCoreApplication.translate("PTSetting", u"None", None))
        self.part_item_8.setText(QCoreApplication.translate("PTSetting", u"MagnetT/pt1/pt2", None))
        self.part_ips_magnet_temp.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_ips_magnet_temp.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_ips_magnet_temp.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_ips_magnet_temp.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_ips_magnet_temp.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_ips_magnet_temp.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_ips_magnet_temp.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_ips_magnet_temp.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_ips_magnet_temp.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_ips_magnet_temp.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_ips_magnet_temp.setCurrentText(QCoreApplication.translate("PTSetting", u"None", None))
        self.part_ips_pt1.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_ips_pt1.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_ips_pt1.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_ips_pt1.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_ips_pt1.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_ips_pt1.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_ips_pt1.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_ips_pt1.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_ips_pt1.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_ips_pt1.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_ips_pt1.setCurrentText(QCoreApplication.translate("PTSetting", u"None", None))
        self.part_ips_pt2.setItemText(0, QCoreApplication.translate("PTSetting", u"None", None))
        self.part_ips_pt2.setItemText(1, QCoreApplication.translate("PTSetting", u"MB1", None))
        self.part_ips_pt2.setItemText(2, QCoreApplication.translate("PTSetting", u"DB1", None))
        self.part_ips_pt2.setItemText(3, QCoreApplication.translate("PTSetting", u"DB2", None))
        self.part_ips_pt2.setItemText(4, QCoreApplication.translate("PTSetting", u"DB3", None))
        self.part_ips_pt2.setItemText(5, QCoreApplication.translate("PTSetting", u"DB4", None))
        self.part_ips_pt2.setItemText(6, QCoreApplication.translate("PTSetting", u"DB5", None))
        self.part_ips_pt2.setItemText(7, QCoreApplication.translate("PTSetting", u"DB6", None))
        self.part_ips_pt2.setItemText(8, QCoreApplication.translate("PTSetting", u"DB7", None))
        self.part_ips_pt2.setItemText(9, QCoreApplication.translate("PTSetting", u"DB8", None))

        self.part_ips_pt2.setCurrentText(QCoreApplication.translate("PTSetting", u"None", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PTSetting", u"Others", None))
        self.label1_3.setText(QCoreApplication.translate("PTSetting", u"Alarm Field TEM:", None))
        self.le_field_temp_alarm.setText(QCoreApplication.translate("PTSetting", u"4.0", None))
        self.label1_15.setText(QCoreApplication.translate("PTSetting", u"MAX Field TEM", None))
        self.le_field_temp_max.setText(QCoreApplication.translate("PTSetting", u"4.3", None))
        self.pb_save_setting.setText(QCoreApplication.translate("PTSetting", u"Save", None))
    # retranslateUi

