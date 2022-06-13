# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoNote.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from .NewTextEdit import TextEdit
from .import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(713, 653)
        icon = QIcon()
        icon.addFile(u":/new/icons/passion.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"QPushButton{\n"
"	/*border-left:1px solid #808080;\n"
"	border-bottom:1px solid #808080;\n"
"	border-top:1px solid #808080;*/\n"
"	border:none;\n"
"	text-align:left;\n"
"	padding:2 13 4 21;\n"
"	margin:0;\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#C8C8C8;\n"
" }\n"
"\n"
"#Button_setting{\n"
"	/*border-right:1px solid #808080;\n"
"	border-top-right-radius:3px;\n"
"	border-bottom-right-radius:3px;*/\n"
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
"	/*border-top-left-radius:3px;\n"
"	border-bottom-left-radius:3px;*/\n"
"	background-image:url(:/new/icons/pin_default.png);\n"
"}\n"
"\n"
"#Butto"
                        "n_pin::checked{\n"
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
        font = QFont()
        font.setPointSize(10)
        self.TextFrame.setFont(font)
        self.TextFrame.setFrameShape(QFrame.NoFrame)
        self.TextFrame.setFrameShadow(QFrame.Raised)
        self.TextFrame.setLineWidth(1)
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
        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(Qt.ClickFocus)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	border:none;\n"
"	background-color:#FFFFFF;\n"
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
        self.horizontalLayout.setContentsMargins(10, 1, 10, 1)
        self.Button_pin = QPushButton(self.ButtonFrame)
        self.Button_pin.setObjectName(u"Button_pin")
        self.Button_pin.setFocusPolicy(Qt.ClickFocus)
        self.Button_pin.setCheckable(True)

        self.horizontalLayout.addWidget(self.Button_pin)

        self.Button_copy = QPushButton(self.ButtonFrame)
        self.Button_copy.setObjectName(u"Button_copy")
        self.Button_copy.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.Button_copy)

        self.Button_cut = QPushButton(self.ButtonFrame)
        self.Button_cut.setObjectName(u"Button_cut")
        self.Button_cut.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.Button_cut)

        self.Button_clear = QPushButton(self.ButtonFrame)
        self.Button_clear.setObjectName(u"Button_clear")
        self.Button_clear.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.Button_clear)

        self.Button_monitor = QPushButton(self.ButtonFrame)
        self.Button_monitor.setObjectName(u"Button_monitor")
        self.Button_monitor.setFocusPolicy(Qt.ClickFocus)
        self.Button_monitor.setCheckable(True)

        self.horizontalLayout.addWidget(self.Button_monitor)

        self.Button_setting = QPushButton(self.ButtonFrame)
        self.Button_setting.setObjectName(u"Button_setting")
        self.Button_setting.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.Button_setting)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.ButtonFrame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:#969696;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


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
        self.label.setText(QCoreApplication.translate("Form", u"Note: A Powerful Tool written by MuSen at 2022", None))
    # retranslateUi

