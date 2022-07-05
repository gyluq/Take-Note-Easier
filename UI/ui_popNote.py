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
    QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from NewTextEdit import TextEdit


class Ui_Form1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(434, 163)
        Form.setStyleSheet(u"#frame{\n"
"	border-radius:5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(1950, 161))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color:#FFFFFF;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.textEdit = TextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	color:#3D3D3D;\n"
"	border:1px solid #DCDCDC;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border:none;\n"
"    background-color:#E6E6E6;\n"
"    width:8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #a6a6a6, stop: 0.5 #a6a6a6, stop:1 #a6a6a6);\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #a6a6a6, stop: 0.5 #a6a6a6,  stop:1 #a6a6a6);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  #a6a6a6, stop: 0.5 #a6a6a6,  stop:1 #a6a6a6);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.BtFrame = QFrame(self.frame)
        self.BtFrame.setObjectName(u"BtFrame")
        self.BtFrame.setStyleSheet(u"QPushButton{\n"
"	padding:1 2 1 2;\n"
"	margin:0;\n"
"	border:1px solid #D6DDE0;\n"
"	border-radius:3px;\n"
"	background-color:#F5F5F5;\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid #D7D7D7;\n"
"	background-color:#D7D7D7;\n"
" }\n"
"\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"	border:1px solid #295BBB;\n"
"	background-color:#295BB8;\n"
" }")
        self.BtFrame.setFrameShape(QFrame.StyledPanel)
        self.BtFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.BtFrame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BtTextSend = QPushButton(self.BtFrame)
        self.BtTextSend.setObjectName(u"BtTextSend")
        self.BtTextSend.setMinimumSize(QSize(0, 0))
        self.BtTextSend.setMaximumSize(QSize(16777215, 5222))

        self.verticalLayout.addWidget(self.BtTextSend)

        self.BtTextFormate = QPushButton(self.BtFrame)
        self.BtTextFormate.setObjectName(u"BtTextFormate")
        self.BtTextFormate.setStyleSheet(u"")
        self.BtTextFormate.setCheckable(False)

        self.verticalLayout.addWidget(self.BtTextFormate)

        self.BtFontEnlarge = QPushButton(self.BtFrame)
        self.BtFontEnlarge.setObjectName(u"BtFontEnlarge")

        self.verticalLayout.addWidget(self.BtFontEnlarge)

        self.BtFontShrink = QPushButton(self.BtFrame)
        self.BtFontShrink.setObjectName(u"BtFontShrink")

        self.verticalLayout.addWidget(self.BtFontShrink)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.BtWinExit = QPushButton(self.BtFrame)
        self.BtWinExit.setObjectName(u"BtWinExit")

        self.verticalLayout.addWidget(self.BtWinExit)


        self.horizontalLayout_2.addWidget(self.BtFrame)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtTextSend.setText(QCoreApplication.translate("Form", u"SEND", None))
        self.BtTextFormate.setText(QCoreApplication.translate("Form", u"FORM", None))
        self.BtFontEnlarge.setText(QCoreApplication.translate("Form", u"LAG", None))
        self.BtFontShrink.setText(QCoreApplication.translate("Form", u"SHR", None))
        self.BtWinExit.setText(QCoreApplication.translate("Form", u"EXIT", None))
    # retranslateUi

