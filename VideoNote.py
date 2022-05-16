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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from TextEdit import TextEdit
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(309, 255)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"QTextEdit{\n"
"	border-left:1px solid #ffffff;\n"
"	border-bottom:1px solid #ffffff;\n"
"	border-right:1px solid #ffffff;\n"
"	border-top:1px solid #E6E6E6;\n"
"	border-bottom-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"	background-color:#F6F6F6 ;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"#frame_2{\n"
"	background-color:white;\n"
"	border-top-left-radius:6px;\n"
"	border-top-right-radius:6px;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"QPushButton{\n"
"	width: 25px;\n"
"	height:25px;\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid #808080;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#e1e1e1;\n"
" }\n"
"\n"
"#Button_copy{\n"
"	background-image:url(:/new/icons/copy.png);\n"
"}\n"
"\n"
"#Button_cut{\n"
"	background-image:url(:/new/icons/cut.p"
                        "ng);\n"
"}\n"
"\n"
"#Button_clear{\n"
"	background-image:url(:/new/icons/trash.png);\n"
"}\n"
"\n"
"#Button_shrink{\n"
"	background-image:url(:/new/icons/shrink.png);\n"
"}\n"
"\n"
"#Button_monitor{\n"
"	background-image:url(:/new/icons/monitor.png);\n"
"}\n"
"\n"
"#Button_close{\n"
"	background-image:url(:/new/icons/close.png);\n"
"}\n"
"\n"
"#Button_pin{\n"
"	background-image:url(:/new/icons/pin_default.png);\n"
"}\n"
"\n"
"#Button_shrink::checked{\n"
"	background-image:url(:/new/icons/expand.png);\n"
"}\n"
"\n"
"#Button_monitor::checked{\n"
"	background-color:#80FFC9DB;\n"
"	border:1px solid #808080;\n"
"	border-radius:4px;\n"
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
"    "
                        "subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 12px;\n"
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
"")
        self.frame_1 = QFrame(Form)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(4, 2, 300, 250))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setMinimumSize(QSize(300, 250))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(242, 33))
        self.frame_2.setMaximumSize(QSize(16777215, 33))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 2, 2, 2)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(73, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.Button_copy = QPushButton(self.frame_2)
        self.Button_copy.setObjectName(u"Button_copy")

        self.horizontalLayout_2.addWidget(self.Button_copy)

        self.Button_cut = QPushButton(self.frame_2)
        self.Button_cut.setObjectName(u"Button_cut")

        self.horizontalLayout_2.addWidget(self.Button_cut)

        self.Button_clear = QPushButton(self.frame_2)
        self.Button_clear.setObjectName(u"Button_clear")

        self.horizontalLayout_2.addWidget(self.Button_clear)

        self.Button_shrink = QPushButton(self.frame_2)
        self.Button_shrink.setObjectName(u"Button_shrink")
        self.Button_shrink.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.Button_shrink)

        self.Button_monitor = QPushButton(self.frame_2)
        self.Button_monitor.setObjectName(u"Button_monitor")
        self.Button_monitor.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.Button_monitor)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Button_close = QPushButton(self.frame_2)
        self.Button_close.setObjectName(u"Button_close")

        self.horizontalLayout_2.addWidget(self.Button_close)

        self.Button_pin = QPushButton(self.frame_2)
        self.Button_pin.setObjectName(u"Button_pin")

        self.horizontalLayout_2.addWidget(self.Button_pin)

        self.comboBox.raise_()
        self.Button_copy.raise_()
        self.Button_clear.raise_()
        self.Button_monitor.raise_()
        self.Button_close.raise_()
        self.Button_pin.raise_()
        self.Button_cut.raise_()
        self.Button_shrink.raise_()

        self.verticalLayout.addWidget(self.frame_2)

        self.textEdit = TextEdit(self.frame_1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 200))
        self.textEdit.setMaximumSize(QSize(200000, 2500))
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit.setFont(font1)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textEdit.setFocusPolicy(Qt.StrongFocus)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Power", None))
        self.Button_copy.setText("")
        self.Button_cut.setText("")
        self.Button_clear.setText("")
        self.Button_shrink.setText("")
        self.Button_monitor.setText("")
        self.Button_close.setText("")
        self.Button_pin.setText("")
    # retranslateUi

