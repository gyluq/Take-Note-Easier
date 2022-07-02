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
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(190, 140)
        Form.setStyleSheet(u"#frame{\n"
"	border-radius:5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(190, 140))
        self.frame.setMaximumSize(QSize(190, 140))
        self.frame.setStyleSheet(u"QPushButton{\n"
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
" }\n"
"\n"
"QTextEdit{\n"
"	border:1px solid #C4C7C9;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color:#FFFFFF;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BtExit = QPushButton(self.frame_2)
        self.BtExit.setObjectName(u"BtExit")

        self.horizontalLayout.addWidget(self.BtExit)

        self.BtSend = QPushButton(self.frame_2)
        self.BtSend.setObjectName(u"BtSend")
        self.BtSend.setMinimumSize(QSize(0, 20))
        self.BtSend.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.BtSend)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtExit.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.BtSend.setText(QCoreApplication.translate("Form", u"SEND", None))
    # retranslateUi

