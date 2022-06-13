# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoNote.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)

from .NewTextEdit import TextEdit
from . import img_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(721, 653)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"QPushButton{\n"
                                     "	border-left:1px solid #808080;\n"
                                     "	border-bottom:1px solid #808080;\n"
                                     "	border-top:1px solid #808080;\n"
                                     "	text-align:left;\n"
                                     "	padding:2 0 4 19;\n"
                                     "	margin:0;\n"
                                     "	background-repeat:none;\n"
                                     "	background-position:left;\n"
                                     "	background-color:#E6E6E6;\n"
                                     "	min-width:50px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "	background-color:#C8C8C8;\n"
                                     " }\n"
                                     "\n"
                                     "#Button_setting{\n"
                                     "	border-right:1px solid #808080;\n"
                                     "	border-top-right-radius:3px;\n"
                                     "	border-bottom-right-radius:3px;\n"
                                     "	background-image:url(:/new/icons/setting.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_copy{\n"
                                     "	background-image:url(:/new/icons/copy.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_cut{\n"
                                     "	background-image:url(:/new/icons/cut.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_clear{\n"
                                     "	background-image:url(:/new/icons/trash.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_monitor{\n"
                                     "	background-image:url(:/new/icons/monitor.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_pin{\n"
                                     "	border-top-left-radius:3px;\n"
                                     "	border-bottom-left-radius:3px;\n"
                                     "	background-image:url(:/new/icons/pin_default.png);\n"
                                     ""
                                     "}\n"
                                     "\n"
                                     "#Button_pin::checked{\n"
                                     "	background-image:url(:/new/icons/pin_active.png);\n"
                                     "}\n"
                                     "\n"
                                     "#Button_monitor::checked{\n"
                                     "	background-image:url(:/new/icons/monitor_ac.png);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TextFrame = QFrame(self.MainFrame)
        self.TextFrame.setObjectName(u"TextFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextFrame.sizePolicy().hasHeightForWidth())
        self.TextFrame.setSizePolicy(sizePolicy)
        self.TextFrame.setFrameShape(QFrame.StyledPanel)
        self.TextFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.TextFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = TextEdit(self.TextFrame)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
                                    "	border:none;\n"
                                    "	background-color:#F6F6F6 ;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar:vertical {\n"
                                    "    border:none;\n"
                                    "    background-color:#C7C7C7;\n"
                                    "    width:10px;\n"
                                    "    margin: 0px 0px 0px 0px;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::handle:vertical {\n"
                                    "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                    "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
                                    "    min-height: 0px;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::add-line:vertical {\n"
                                    "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                    "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                                    "    height: 0px;\n"
                                    "    subcontrol-position: bottom;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::sub-line:vertical {\n"
                                    "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                    "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                                    "    height: 0 px;\n"
                                    "    subcontrol-position: top;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}")
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalLayout_2.addWidget(self.TextFrame)

        self.ButtonFrame = QFrame(self.MainFrame)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setStyleSheet(u"")
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 1, 3, 1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Button_pin = QPushButton(self.ButtonFrame)
        self.Button_pin.setObjectName(u"Button_pin")
        self.Button_pin.setCheckable(True)

        self.horizontalLayout.addWidget(self.Button_pin)

        self.Button_copy = QPushButton(self.ButtonFrame)
        self.Button_copy.setObjectName(u"Button_copy")

        self.horizontalLayout.addWidget(self.Button_copy)

        self.Button_cut = QPushButton(self.ButtonFrame)
        self.Button_cut.setObjectName(u"Button_cut")

        self.horizontalLayout.addWidget(self.Button_cut)

        self.Button_clear = QPushButton(self.ButtonFrame)
        self.Button_clear.setObjectName(u"Button_clear")

        self.horizontalLayout.addWidget(self.Button_clear)

        self.Button_monitor = QPushButton(self.ButtonFrame)
        self.Button_monitor.setObjectName(u"Button_monitor")
        self.Button_monitor.setCheckable(True)

        self.horizontalLayout.addWidget(self.Button_monitor)

        self.Button_setting = QPushButton(self.ButtonFrame)
        self.Button_setting.setObjectName(u"Button_setting")

        self.horizontalLayout.addWidget(self.Button_setting)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addWidget(self.ButtonFrame)

        self.verticalLayout.addWidget(self.MainFrame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Button_pin.setText(QCoreApplication.translate("Form", u"Top", None))
        self.Button_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.Button_cut.setText(QCoreApplication.translate("Form", u"Cut", None))
        self.Button_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.Button_monitor.setText(QCoreApplication.translate("Form", u"Monitor", None))
        self.Button_setting.setText(QCoreApplication.translate("Form", u"Setting", None))
    # retranslateUi
