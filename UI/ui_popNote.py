# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_popNote.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from NewTextEdit import TextEdit

class Ui_Form1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(195, 161)
        Form.setStyleSheet(u"#frame{\n"
"	border-radius:5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(195, 161))
        self.frame.setMaximumSize(QSize(195, 161))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color:#FFFFFF;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.textEdit = TextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	color:#858383;\n"
"	border:1px solid #C4C7C9;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border:none;\n"
"    background-color:#C4C9F2;\n"
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

        self.verticalLayout.addWidget(self.textEdit)

        self.BtFrame = QFrame(self.frame)
        self.BtFrame.setObjectName(u"BtFrame")
        self.BtFrame.setStyleSheet(u"QPushButton{\n"
"	padding:0;\n"
"	margin:0;\n"
"	border:1px solid #C4C7C9;\n"
"	background-color:#EEEEEE;\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#E6E6E6;\n"
" }\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#DCDCDC;\n"
" }")
        self.BtFrame.setFrameShape(QFrame.StyledPanel)
        self.BtFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.BtFrame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BtExit = QPushButton(self.BtFrame)
        self.BtExit.setObjectName(u"BtExit")

        self.horizontalLayout.addWidget(self.BtExit)

        self.BtStop = QPushButton(self.BtFrame)
        self.BtStop.setObjectName(u"BtStop")
        self.BtStop.setStyleSheet(u"QPushButton:checked{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"	background-color:#295BB8;\n"
"	border:1px solid #295BBB;\n"
"}")
        self.BtStop.setCheckable(True)

        self.horizontalLayout.addWidget(self.BtStop)

        self.BtSend = QPushButton(self.BtFrame)
        self.BtSend.setObjectName(u"BtSend")
        self.BtSend.setMinimumSize(QSize(0, 20))
        self.BtSend.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.BtSend)


        self.verticalLayout.addWidget(self.BtFrame)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtExit.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.BtStop.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.BtSend.setText(QCoreApplication.translate("Form", u"SEND", None))
    # retranslateUi

