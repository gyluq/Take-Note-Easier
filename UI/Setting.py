# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)
from . import img_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(335, 262)
        icon = QIcon()
        icon.addFile(u":/new/icons/passion.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QPushButton{\n"
                           "	border:1px solid #abadb3;\n"
                           "	background-color:#FFFFFF;\n"
                           "	padding:3 5 3 5;\n"
                           "	width:70px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "	background-color:#EBEBEB;\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed{\n"
                           "	background-color:#C9C4C4;\n"
                           "}\n"
                           "\n"
                           "QPushButton#Button_apply{\n"
                           "	border:1px solid #abadb3;\n"
                           "	background-color:#E8E8E8;\n"
                           "	padding:3 5 3 5;\n"
                           "	width:70px;\n"
                           "}\n"
                           "\n"
                           "QPushButton#Button_apply:hover{\n"
                           "	background-color:#F0E3E3;\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QPushButton#Button_apply:pressed{\n"
                           "	background-color:#D1C1C1;\n"
                           "}\n"
                           "\n"
                           "/*----------------------------------------------------------------------------------*/\n"
                           "\n"
                           "QComboBox {\n"
                           "	height:23px;\n"
                           "    border: 1px solid #BEBEBE;\n"
                           "    border-radius: 3px;\n"
                           "	background-color:#FAFAFA;\n"
                           "    padding: 1px 8px 1px 3px;\n"
                           "    min-width: 4em;\n"
                           "}\n"
                           "\n"
                           "/*\u53f3\u4fa7\u7684\u5c55\u793a\u6309\u94ae*/\n"
                           "QComboBox::drop-down {\n"
                           "    subcontrol-origin: padding;\n"
                           "    subcontrol-position: top right;\n"
                           "    width: 1"
                           "2px;\n"
                           "	border-left:1px solid darkgray;\n"
                           "	border-top-right-radius: 3px;\n"
                           "    border-bottom-right-radius: 3px;\n"
                           "}\n"
                           "\n"
                           "QComboBox::down-arrow \n"
                           "{\n"
                           "    width: 9px;  \n"
                           "    height: 9px;   \n"
                           "    image: url(:/new/icons/sort-left.png);\n"
                           "}\n"
                           "\n"
                           "QComboBox::down-arrow:on\n"
                           "{\n"
                           "    width: 9px;  \n"
                           "    height: 9px;   \n"
                           "    image: url(:/new/icons/sort-down.png);\n"
                           "}\n"
                           "\n"
                           "\n"
                           "\n"
                           "")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Color_dot = QPushButton(self.groupBox)
        self.Color_dot.setObjectName(u"Color_dot")

        self.gridLayout.addWidget(self.Color_dot, 4, 3, 1, 1)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")

        self.gridLayout.addWidget(self.label4, 3, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(73, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.comboBox, 5, 3, 1, 1)

        self.label1_2 = QLabel(self.groupBox)
        self.label1_2.setObjectName(u"label1_2")

        self.gridLayout.addWidget(self.label1_2, 5, 1, 1, 1)

        self.Color_mainwindow = QPushButton(self.groupBox)
        self.Color_mainwindow.setObjectName(u"Color_mainwindow")

        self.gridLayout.addWidget(self.Color_mainwindow, 0, 3, 1, 1)

        self.Color_border = QPushButton(self.groupBox)
        self.Color_border.setObjectName(u"Color_border")

        self.gridLayout.addWidget(self.Color_border, 3, 3, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 2, 1, 1, 1)

        self.Color_mask = QPushButton(self.groupBox)
        self.Color_mask.setObjectName(u"Color_mask")

        self.gridLayout.addWidget(self.Color_mask, 2, 3, 1, 1)

        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")

        self.gridLayout.addWidget(self.label5, 4, 1, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 1, 1, 1)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 1, 1, 1)

        self.Color_textedit = QPushButton(self.groupBox)
        self.Color_textedit.setObjectName(u"Color_textedit")

        self.gridLayout.addWidget(self.Color_textedit, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Button_apply = QPushButton(Form)
        self.Button_apply.setObjectName(u"Button_apply")

        self.horizontalLayout.addWidget(self.Button_apply)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u80cc\u666f\u8272", None))
        self.Color_dot.setText("")
        self.label4.setText(QCoreApplication.translate("Form", u"\u622a\u56fe\u8fb9\u6846", None))
        self.label1_2.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u6700\u5927\u5bbd\u5ea6", None))
        self.Color_mainwindow.setText("")
        self.Color_border.setText("")
        self.label3.setText(QCoreApplication.translate("Form", u"\u622a\u56fe\u906e\u7f69\u5c42", None))
        self.Color_mask.setText("")
        self.label5.setText(QCoreApplication.translate("Form", u"\u622a\u56fe\u7aef\u70b9", None))
        self.label2.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91\u5668\u80cc\u666f\u8272", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\u7a97\u4f53\u80cc\u666f\u8272", None))
        self.Color_textedit.setText("")
        self.Button_apply.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi
