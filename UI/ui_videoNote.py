# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_videoNote.ui'
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
from .import img_rc
from NewTextEdit import TextEdit

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(942, 819)
        icon1 = QIcon()
        icon1.addFile(u":/new/icons/passion.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon1)
        Form.setStyleSheet(u"#TitleFrame{\n"
"	background-color:#FFFFFF\n"
"}\n"
"\n"
"#ButtonFrame{\n"
"	background-color:#FFFFFF\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TitleFrame = QFrame(self.MainFrame)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setStyleSheet(u"QPushButton{\n"
"	padding:0 0 0 8;\n"
"	margin:0;\n"
"	width:30;\n"
"	height:30;\n"
"	border:none;\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5e5e5;\n"
" }\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#C8C8C8;\n"
" }\n"
"\n"
"#Button_close:hover{\n"
"	background-color:#e81123;\n"
"	background-image:url(:/new/icons/close_ac.png);\n"
"}\n"
"\n"
"#Button_close:pressed{\n"
"	background-color:#f1707a;\n"
"}\n"
"\n"
"#Button_close{\n"
"	background-image:url(:/new/icons/close.png);\n"
"}\n"
"\n"
"#Button_large{\n"
"	background-image:url(:/new/icons/enlarge.png);\n"
"}\n"
"\n"
"#Button_small{\n"
"	background-image:url(:/new/icons/minimize.png);\n"
"}\n"
"\n"
"#Button_large::checked{\n"
"	background-image:url(:/new/icons/enlarge_ac.png);\n"
"}\n"
"\n"
"#icon{\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"	background-image:url(:/new/icons/passion.png)\n"
"}")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.TitleFrame.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.TitleFrame)
        self.icon.setObjectName(u"icon")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(25, 25))
        self.icon.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.icon)

        self.title = QLabel(self.TitleFrame)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 25))
        self.title.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Button_small = QPushButton(self.TitleFrame)
        self.Button_small.setObjectName(u"Button_small")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_small.sizePolicy().hasHeightForWidth())
        self.Button_small.setSizePolicy(sizePolicy1)
        self.Button_small.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.Button_small)

        self.Button_large = QPushButton(self.TitleFrame)
        self.Button_large.setObjectName(u"Button_large")
        sizePolicy1.setHeightForWidth(self.Button_large.sizePolicy().hasHeightForWidth())
        self.Button_large.setSizePolicy(sizePolicy1)
        self.Button_large.setMaximumSize(QSize(16777215, 25))
        self.Button_large.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.Button_large)

        self.Button_close = QPushButton(self.TitleFrame)
        self.Button_close.setObjectName(u"Button_close")
        sizePolicy1.setHeightForWidth(self.Button_close.sizePolicy().hasHeightForWidth())
        self.Button_close.setSizePolicy(sizePolicy1)
        self.Button_close.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.Button_close)


        self.verticalLayout_2.addWidget(self.TitleFrame)

        self.TextFrame = QFrame(self.MainFrame)
        self.TextFrame.setObjectName(u"TextFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TextFrame.sizePolicy().hasHeightForWidth())
        self.TextFrame.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(10)
        self.TextFrame.setFont(font)
        self.TextFrame.setFrameShape(QFrame.NoFrame)
        self.TextFrame.setFrameShadow(QFrame.Raised)
        self.TextFrame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.TextFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = TextEdit(self.TextFrame)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy3)
        self.textEdit.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(11)
        self.textEdit.setFont(font1)
        self.textEdit.setFocusPolicy(Qt.ClickFocus)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	border:none;\n"
"	background-color:#1d1d26;\n"
"	color:white;\n"
"	selection-color: #F0F0F0;\n"
"	selection-background-color:#4388DB;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background:#1d1d26;\n"
"    width: 9px;\n"
"    margin: 3px 0 3px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	border:1px solid rgba(255, 255, 255, 20);\n"
"    background: rgba(255, 255, 255, 60);\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 0px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"/*\n"
"QScrollBar:vertical {\n"
"    border:none;\n"
"    background-color:#1d1d26;\n"
"    width:10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color:#656569;\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background-color:white;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color:white;\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}*/")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.rightPadding = QLabel(self.TextFrame)
        self.rightPadding.setObjectName(u"rightPadding")
        self.rightPadding.setMinimumSize(QSize(3, 0))
        self.rightPadding.setMaximumSize(QSize(3, 16777215))
        self.rightPadding.setStyleSheet(u"background-color: rgb(29, 29, 38);")

        self.horizontalLayout_3.addWidget(self.rightPadding)


        self.verticalLayout_2.addWidget(self.TextFrame)

        self.ButtonFrame = QFrame(self.MainFrame)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-left: 5px solid transparent;\n"
"	text-align:left;\n"
"	padding:2 10 4 21;\n"
"	margin:0;\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#DCDCDC;\n"
" }\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#C8C8C8;\n"
" }\n"
"\n"
"#Button_setting{\n"
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
"#Button_minibox{\n"
"	background-image:url(:/new/icons/box.png);\n"
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
"	background-image:url(:/new/icons/pin_default.png);\n"
"}\n"
"\n"
"#Button_pin::checked{\n"
"	background-image:url(:/new/icons/pin_active.png);\n"
"}\n"
"\n"
"#Button_monitor::checked{"
                        "\n"
"	background-image:url(:/new/icons/monitor_ac.png);\n"
"}\n"
"")
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
        self.Button_monitor.setFocusPolicy(Qt.TabFocus)
        self.Button_monitor.setCheckable(True)
        self.Button_monitor.setFlat(False)

        self.horizontalLayout.addWidget(self.Button_monitor)

        self.Button_setting = QPushButton(self.ButtonFrame)
        self.Button_setting.setObjectName(u"Button_setting")
        self.Button_setting.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.Button_setting)

        self.Button_minibox = QPushButton(self.ButtonFrame)
        self.Button_minibox.setObjectName(u"Button_minibox")

        self.horizontalLayout.addWidget(self.Button_minibox)

        self.Button_pt = QPushButton(self.ButtonFrame)
        self.Button_pt.setObjectName(u"Button_pt")
        self.Button_pt.setStyleSheet(u"#Button_pt{\n"
"	padding:2 10 4 10;\n"
"}\n"
"\n"
"#Button_pt::checked{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"	background-color:#1E89BA;\n"
"}")
        self.Button_pt.setCheckable(True)

        self.horizontalLayout.addWidget(self.Button_pt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.ButtonFrame)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font2)
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
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"Power", None))
        self.Button_small.setText("")
        self.Button_large.setText("")
        self.Button_close.setText("")
        self.rightPadding.setText("")
        self.Button_pin.setText(QCoreApplication.translate("Form", u"Top", None))
        self.Button_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.Button_cut.setText(QCoreApplication.translate("Form", u"Cut", None))
        self.Button_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.Button_monitor.setText(QCoreApplication.translate("Form", u"Monitor", None))
        self.Button_setting.setText(QCoreApplication.translate("Form", u"Setting", None))
        self.Button_minibox.setText(QCoreApplication.translate("Form", u"Mini", None))
        self.Button_pt.setText(QCoreApplication.translate("Form", u"\u53bb\u6362\u884c\u7b26", None))
        self.label.setText(QCoreApplication.translate("Form", u"Note: A Powerful Tool written by MuSen at 2022", None))
    # retranslateUi

