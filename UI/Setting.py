# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 216)
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
        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 1, 1, 1)

        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")

        self.gridLayout.addWidget(self.label5, 4, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 1, 1, 1)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")

        self.gridLayout.addWidget(self.label4, 3, 1, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.Color_mainwindow = QPushButton(self.groupBox)
        self.Color_mainwindow.setObjectName(u"Color_mainwindow")

        self.gridLayout.addWidget(self.Color_mainwindow, 0, 3, 1, 1)

        self.Color_textedit = QPushButton(self.groupBox)
        self.Color_textedit.setObjectName(u"Color_textedit")

        self.gridLayout.addWidget(self.Color_textedit, 1, 3, 1, 1)

        self.Color_border = QPushButton(self.groupBox)
        self.Color_border.setObjectName(u"Color_border")

        self.gridLayout.addWidget(self.Color_border, 3, 3, 1, 1)

        self.Color_dot = QPushButton(self.groupBox)
        self.Color_dot.setObjectName(u"Color_dot")

        self.gridLayout.addWidget(self.Color_dot, 4, 3, 1, 1)

        self.Color_mask = QPushButton(self.groupBox)
        self.Color_mask.setObjectName(u"Color_mask")

        self.gridLayout.addWidget(self.Color_mask, 2, 3, 1, 1)

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
        self.label2.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u6846\u80cc\u666f\u8272", None))
        self.label5.setText(QCoreApplication.translate("Form", u"\u622a\u56fe\u7aef\u70b9", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\u7a97\u4f53\u80cc\u666f\u8272", None))
        self.label4.setText(QCoreApplication.translate("Form", u"\u8fb9\u6846", None))
        self.label3.setText(QCoreApplication.translate("Form", u"\u906e\u7f69\u5c42", None))
        self.Color_mainwindow.setText("")
        self.Color_textedit.setText("")
        self.Color_border.setText("")
        self.Color_dot.setText("")
        self.Color_mask.setText("")
        self.Button_apply.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi
