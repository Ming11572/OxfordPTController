# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teslaPT_warm_cool.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WarmCool(object):
    def setupUi(self, WarmCool):
        if not WarmCool.objectName():
            WarmCool.setObjectName(u"WarmCool")
        WarmCool.resize(690, 350)
        WarmCool.setMinimumSize(QSize(690, 350))
        WarmCool.setMaximumSize(QSize(690, 350))
        self.horizontalLayout_18 = QHBoxLayout(WarmCool)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(WarmCool)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(35, 0))
        self.label_9.setMaximumSize(QSize(35, 16777215))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)

        self.label_8 = QLabel(WarmCool)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_8)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)

        self.label_10 = QLabel(WarmCool)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(120, 16777215))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(WarmCool)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(35, 0))
        self.label_2.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.le_press_1 = QLineEdit(WarmCool)
        self.le_press_1.setObjectName(u"le_press_1")
        sizePolicy1.setHeightForWidth(self.le_press_1.sizePolicy().hasHeightForWidth())
        self.le_press_1.setSizePolicy(sizePolicy1)
        self.le_press_1.setMinimumSize(QSize(60, 0))
        self.le_press_1.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.le_press_1)

        self.label_11 = QLabel(WarmCool)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(10, 0))
        self.label_11.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.le_heater_1 = QLineEdit(WarmCool)
        self.le_heater_1.setObjectName(u"le_heater_1")
        sizePolicy1.setHeightForWidth(self.le_heater_1.sizePolicy().hasHeightForWidth())
        self.le_heater_1.setSizePolicy(sizePolicy1)
        self.le_heater_1.setMinimumSize(QSize(60, 0))
        self.le_heater_1.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.le_heater_1)

        self.label_12 = QLabel(WarmCool)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(10, 0))
        self.label_12.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.le_wpress_1 = QLineEdit(WarmCool)
        self.le_wpress_1.setObjectName(u"le_wpress_1")
        sizePolicy1.setHeightForWidth(self.le_wpress_1.sizePolicy().hasHeightForWidth())
        self.le_wpress_1.setSizePolicy(sizePolicy1)
        self.le_wpress_1.setMinimumSize(QSize(60, 0))
        self.le_wpress_1.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.le_wpress_1)

        self.label_24 = QLabel(WarmCool)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(10, 0))
        self.label_24.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_6.addWidget(self.label_24)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(WarmCool)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(35, 0))
        self.label_3.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.le_press_2 = QLineEdit(WarmCool)
        self.le_press_2.setObjectName(u"le_press_2")
        sizePolicy1.setHeightForWidth(self.le_press_2.sizePolicy().hasHeightForWidth())
        self.le_press_2.setSizePolicy(sizePolicy1)
        self.le_press_2.setMinimumSize(QSize(60, 0))
        self.le_press_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.le_press_2)

        self.label_13 = QLabel(WarmCool)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(10, 0))
        self.label_13.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.le_heater_2 = QLineEdit(WarmCool)
        self.le_heater_2.setObjectName(u"le_heater_2")
        sizePolicy1.setHeightForWidth(self.le_heater_2.sizePolicy().hasHeightForWidth())
        self.le_heater_2.setSizePolicy(sizePolicy1)
        self.le_heater_2.setMinimumSize(QSize(60, 0))
        self.le_heater_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.le_heater_2)

        self.label_14 = QLabel(WarmCool)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(10, 0))
        self.label_14.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.le_wpress_2 = QLineEdit(WarmCool)
        self.le_wpress_2.setObjectName(u"le_wpress_2")
        sizePolicy1.setHeightForWidth(self.le_wpress_2.sizePolicy().hasHeightForWidth())
        self.le_wpress_2.setSizePolicy(sizePolicy1)
        self.le_wpress_2.setMinimumSize(QSize(60, 0))
        self.le_wpress_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.le_wpress_2)

        self.label_26 = QLabel(WarmCool)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(10, 0))
        self.label_26.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_7.addWidget(self.label_26)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(WarmCool)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(35, 0))
        self.label_6.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_12.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.le_press_3 = QLineEdit(WarmCool)
        self.le_press_3.setObjectName(u"le_press_3")
        sizePolicy1.setHeightForWidth(self.le_press_3.sizePolicy().hasHeightForWidth())
        self.le_press_3.setSizePolicy(sizePolicy1)
        self.le_press_3.setMinimumSize(QSize(60, 0))
        self.le_press_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.le_press_3)

        self.label_15 = QLabel(WarmCool)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(10, 0))
        self.label_15.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_10.addWidget(self.label_15)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.le_heater_3 = QLineEdit(WarmCool)
        self.le_heater_3.setObjectName(u"le_heater_3")
        sizePolicy1.setHeightForWidth(self.le_heater_3.sizePolicy().hasHeightForWidth())
        self.le_heater_3.setSizePolicy(sizePolicy1)
        self.le_heater_3.setMinimumSize(QSize(60, 0))
        self.le_heater_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.le_heater_3)

        self.label_16 = QLabel(WarmCool)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(10, 0))
        self.label_16.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_10.addWidget(self.label_16)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)

        self.le_wpress_3 = QLineEdit(WarmCool)
        self.le_wpress_3.setObjectName(u"le_wpress_3")
        sizePolicy1.setHeightForWidth(self.le_wpress_3.sizePolicy().hasHeightForWidth())
        self.le_wpress_3.setSizePolicy(sizePolicy1)
        self.le_wpress_3.setMinimumSize(QSize(60, 0))
        self.le_wpress_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.le_wpress_3)

        self.label_27 = QLabel(WarmCool)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(10, 0))
        self.label_27.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_10.addWidget(self.label_27)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(WarmCool)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(35, 0))
        self.label_5.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_11.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.le_press_4 = QLineEdit(WarmCool)
        self.le_press_4.setObjectName(u"le_press_4")
        sizePolicy1.setHeightForWidth(self.le_press_4.sizePolicy().hasHeightForWidth())
        self.le_press_4.setSizePolicy(sizePolicy1)
        self.le_press_4.setMinimumSize(QSize(60, 0))
        self.le_press_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_13.addWidget(self.le_press_4)

        self.label_17 = QLabel(WarmCool)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(10, 0))
        self.label_17.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_13.addWidget(self.label_17)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.le_heater_4 = QLineEdit(WarmCool)
        self.le_heater_4.setObjectName(u"le_heater_4")
        sizePolicy1.setHeightForWidth(self.le_heater_4.sizePolicy().hasHeightForWidth())
        self.le_heater_4.setSizePolicy(sizePolicy1)
        self.le_heater_4.setMinimumSize(QSize(60, 0))
        self.le_heater_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_13.addWidget(self.le_heater_4)

        self.label_18 = QLabel(WarmCool)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(10, 0))
        self.label_18.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_13.addWidget(self.label_18)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.le_wpress_4 = QLineEdit(WarmCool)
        self.le_wpress_4.setObjectName(u"le_wpress_4")
        sizePolicy1.setHeightForWidth(self.le_wpress_4.sizePolicy().hasHeightForWidth())
        self.le_wpress_4.setSizePolicy(sizePolicy1)
        self.le_wpress_4.setMinimumSize(QSize(60, 0))
        self.le_wpress_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_13.addWidget(self.le_wpress_4)

        self.label_28 = QLabel(WarmCool)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(10, 0))
        self.label_28.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_13.addWidget(self.label_28)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_7 = QLabel(WarmCool)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(35, 0))
        self.label_7.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_16.addWidget(self.label_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.le_press_5 = QLineEdit(WarmCool)
        self.le_press_5.setObjectName(u"le_press_5")
        sizePolicy1.setHeightForWidth(self.le_press_5.sizePolicy().hasHeightForWidth())
        self.le_press_5.setSizePolicy(sizePolicy1)
        self.le_press_5.setMinimumSize(QSize(60, 0))
        self.le_press_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.le_press_5)

        self.label_19 = QLabel(WarmCool)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(10, 0))
        self.label_19.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_14.addWidget(self.label_19)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.le_heater_5 = QLineEdit(WarmCool)
        self.le_heater_5.setObjectName(u"le_heater_5")
        sizePolicy1.setHeightForWidth(self.le_heater_5.sizePolicy().hasHeightForWidth())
        self.le_heater_5.setSizePolicy(sizePolicy1)
        self.le_heater_5.setMinimumSize(QSize(60, 0))
        self.le_heater_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.le_heater_5)

        self.label_20 = QLabel(WarmCool)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(10, 0))
        self.label_20.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_14.addWidget(self.label_20)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.le_wpress_5 = QLineEdit(WarmCool)
        self.le_wpress_5.setObjectName(u"le_wpress_5")
        sizePolicy1.setHeightForWidth(self.le_wpress_5.sizePolicy().hasHeightForWidth())
        self.le_wpress_5.setSizePolicy(sizePolicy1)
        self.le_wpress_5.setMinimumSize(QSize(60, 0))
        self.le_wpress_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.le_wpress_5)

        self.label_29 = QLabel(WarmCool)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(10, 0))
        self.label_29.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_14.addWidget(self.label_29)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_21 = QLabel(WarmCool)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(35, 0))
        self.label_21.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_17.addWidget(self.label_21)

        self.label_25 = QLabel(WarmCool)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(10, 0))
        self.label_25.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_17.addWidget(self.label_25)

        self.label_23 = QLabel(WarmCool)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(10, 0))
        self.label_23.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_17.addWidget(self.label_23)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_19)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label1_3 = QLabel(WarmCool)
        self.label1_3.setObjectName(u"label1_3")
        sizePolicy1.setHeightForWidth(self.label1_3.sizePolicy().hasHeightForWidth())
        self.label1_3.setSizePolicy(sizePolicy1)
        self.label1_3.setMinimumSize(QSize(55, 0))
        self.label1_3.setMaximumSize(QSize(55, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.label1_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label1_3)

        self.meas_probeT = QLabel(WarmCool)
        self.meas_probeT.setObjectName(u"meas_probeT")
        self.meas_probeT.setMinimumSize(QSize(80, 0))
        self.meas_probeT.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.meas_probeT.setFont(font2)

        self.horizontalLayout.addWidget(self.meas_probeT)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label1_4 = QLabel(WarmCool)
        self.label1_4.setObjectName(u"label1_4")
        sizePolicy1.setHeightForWidth(self.label1_4.sizePolicy().hasHeightForWidth())
        self.label1_4.setSizePolicy(sizePolicy1)
        self.label1_4.setMinimumSize(QSize(55, 0))
        self.label1_4.setMaximumSize(QSize(55, 16777215))
        self.label1_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label1_4)

        self.meas_vtiT = QLabel(WarmCool)
        self.meas_vtiT.setObjectName(u"meas_vtiT")
        self.meas_vtiT.setMinimumSize(QSize(80, 0))
        self.meas_vtiT.setMaximumSize(QSize(120, 16777215))
        self.meas_vtiT.setFont(font2)

        self.horizontalLayout_2.addWidget(self.meas_vtiT)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label1_7 = QLabel(WarmCool)
        self.label1_7.setObjectName(u"label1_7")
        sizePolicy1.setHeightForWidth(self.label1_7.sizePolicy().hasHeightForWidth())
        self.label1_7.setSizePolicy(sizePolicy1)
        self.label1_7.setMinimumSize(QSize(55, 0))
        self.label1_7.setMaximumSize(QSize(55, 16777215))
        self.label1_7.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label1_7)

        self.meas_magnetT = QLabel(WarmCool)
        self.meas_magnetT.setObjectName(u"meas_magnetT")
        self.meas_magnetT.setMinimumSize(QSize(80, 0))
        self.meas_magnetT.setMaximumSize(QSize(120, 16777215))
        self.meas_magnetT.setFont(font2)

        self.horizontalLayout_4.addWidget(self.meas_magnetT)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label1_5 = QLabel(WarmCool)
        self.label1_5.setObjectName(u"label1_5")
        sizePolicy1.setHeightForWidth(self.label1_5.sizePolicy().hasHeightForWidth())
        self.label1_5.setSizePolicy(sizePolicy1)
        self.label1_5.setMinimumSize(QSize(55, 0))
        self.label1_5.setMaximumSize(QSize(55, 16777215))
        self.label1_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label1_5)

        self.meas_Bz = QLabel(WarmCool)
        self.meas_Bz.setObjectName(u"meas_Bz")
        self.meas_Bz.setMinimumSize(QSize(80, 0))
        self.meas_Bz.setMaximumSize(QSize(120, 16777215))
        self.meas_Bz.setFont(font2)

        self.horizontalLayout_3.addWidget(self.meas_Bz)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pb_cool = QPushButton(WarmCool)
        self.pb_cool.setObjectName(u"pb_cool")
        sizePolicy1.setHeightForWidth(self.pb_cool.sizePolicy().hasHeightForWidth())
        self.pb_cool.setSizePolicy(sizePolicy1)
        self.pb_cool.setMinimumSize(QSize(80, 0))
        self.pb_cool.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        self.pb_cool.setFont(font3)

        self.verticalLayout_4.addWidget(self.pb_cool)

        self.pb_cool_10 = QPushButton(WarmCool)
        self.pb_cool_10.setObjectName(u"pb_cool_10")
        sizePolicy1.setHeightForWidth(self.pb_cool_10.sizePolicy().hasHeightForWidth())
        self.pb_cool_10.setSizePolicy(sizePolicy1)
        self.pb_cool_10.setMinimumSize(QSize(80, 0))
        self.pb_cool_10.setMaximumSize(QSize(80, 16777215))
        self.pb_cool_10.setFont(font3)

        self.verticalLayout_4.addWidget(self.pb_cool_10)

        self.pb_abort = QPushButton(WarmCool)
        self.pb_abort.setObjectName(u"pb_abort")

        self.verticalLayout_4.addWidget(self.pb_abort)

        self.pb_warm = QPushButton(WarmCool)
        self.pb_warm.setObjectName(u"pb_warm")
        sizePolicy1.setHeightForWidth(self.pb_warm.sizePolicy().hasHeightForWidth())
        self.pb_warm.setSizePolicy(sizePolicy1)
        self.pb_warm.setMinimumSize(QSize(80, 0))
        self.pb_warm.setMaximumSize(QSize(80, 16777215))
        self.pb_warm.setFont(font3)

        self.verticalLayout_4.addWidget(self.pb_warm)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.label_22 = QLabel(WarmCool)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_3.addWidget(self.label_22)

        self.lb_status = QLabel(WarmCool)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(0, 200))
        self.lb_status.setFont(font1)
        self.lb_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.lb_status)


        self.horizontalLayout_18.addLayout(self.verticalLayout_3)


        self.retranslateUi(WarmCool)

        QMetaObject.connectSlotsByName(WarmCool)
    # setupUi

    def retranslateUi(self, WarmCool):
        WarmCool.setWindowTitle(QCoreApplication.translate("WarmCool", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("WarmCool", u"vti_T", None))
        self.label_8.setText(QCoreApplication.translate("WarmCool", u"pressure", None))
        self.label_10.setText(QCoreApplication.translate("WarmCool", u"heater/Pressure", None))
        self.label_2.setText(QCoreApplication.translate("WarmCool", u"300K", None))
        self.le_press_1.setText(QCoreApplication.translate("WarmCool", u"20", None))
        self.label_11.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.le_heater_1.setText(QCoreApplication.translate("WarmCool", u"25", None))
        self.label_12.setText(QCoreApplication.translate("WarmCool", u"%", None))
        self.le_wpress_1.setText(QCoreApplication.translate("WarmCool", u"0.01", None))
        self.label_24.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.label_3.setText(QCoreApplication.translate("WarmCool", u"170K", None))
        self.le_press_2.setText(QCoreApplication.translate("WarmCool", u"10", None))
        self.label_13.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.le_heater_2.setText(QCoreApplication.translate("WarmCool", u"20", None))
        self.label_14.setText(QCoreApplication.translate("WarmCool", u"%", None))
        self.le_wpress_2.setText(QCoreApplication.translate("WarmCool", u"0.01", None))
        self.label_26.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.label_6.setText(QCoreApplication.translate("WarmCool", u"70K", None))
        self.le_press_3.setText(QCoreApplication.translate("WarmCool", u"10", None))
        self.label_15.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.le_heater_3.setText(QCoreApplication.translate("WarmCool", u"10", None))
        self.label_16.setText(QCoreApplication.translate("WarmCool", u"%", None))
        self.le_wpress_3.setText(QCoreApplication.translate("WarmCool", u"1", None))
        self.label_27.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.label_5.setText(QCoreApplication.translate("WarmCool", u"20K", None))
        self.le_press_4.setText(QCoreApplication.translate("WarmCool", u"10", None))
        self.label_17.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.le_heater_4.setText(QCoreApplication.translate("WarmCool", u"10", None))
        self.label_18.setText(QCoreApplication.translate("WarmCool", u"%", None))
        self.le_wpress_4.setText(QCoreApplication.translate("WarmCool", u"1", None))
        self.label_28.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.label_7.setText(QCoreApplication.translate("WarmCool", u"5K", None))
        self.le_press_5.setText(QCoreApplication.translate("WarmCool", u"2.9", None))
        self.label_19.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.le_heater_5.setText(QCoreApplication.translate("WarmCool", u"5", None))
        self.label_20.setText(QCoreApplication.translate("WarmCool", u"%", None))
        self.le_wpress_5.setText(QCoreApplication.translate("WarmCool", u"2.9", None))
        self.label_29.setText(QCoreApplication.translate("WarmCool", u"mB", None))
        self.label_21.setText(QCoreApplication.translate("WarmCool", u"1.2K", None))
        self.label_25.setText("")
        self.label_23.setText("")
        self.label1_3.setText(QCoreApplication.translate("WarmCool", u"probe_T:", None))
        self.meas_probeT.setText(QCoreApplication.translate("WarmCool", u"1.732K", None))
        self.label1_4.setText(QCoreApplication.translate("WarmCool", u"VTI_T:", None))
        self.meas_vtiT.setText(QCoreApplication.translate("WarmCool", u"1.732K", None))
        self.label1_7.setText(QCoreApplication.translate("WarmCool", u"MagnetT:", None))
        self.meas_magnetT.setText(QCoreApplication.translate("WarmCool", u"3.9K", None))
        self.label1_5.setText(QCoreApplication.translate("WarmCool", u"Magnet:", None))
        self.meas_Bz.setText(QCoreApplication.translate("WarmCool", u"1.000T", None))
        self.pb_cool.setText(QCoreApplication.translate("WarmCool", u"\u964d\u52301.5k", None))
        self.pb_cool_10.setText(QCoreApplication.translate("WarmCool", u"\u964d\u523010k", None))
        self.pb_abort.setText(QCoreApplication.translate("WarmCool", u"abort", None))
        self.pb_warm.setText(QCoreApplication.translate("WarmCool", u"\u5347\u5230300k", None))
        self.label_22.setText(QCoreApplication.translate("WarmCool", u"Status:", None))
        self.lb_status.setText(QCoreApplication.translate("WarmCool", u"1....", None))
    # retranslateUi

