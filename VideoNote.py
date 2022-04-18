# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoNote.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(949, 54)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"/*\u6309\u94ae*/\n"
"QPushButton{\n"
"	width: 25px;\n"
"	height:25px;\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"	border:none;\n"
"}\n"
"\n"
"/*\u6309\u94ae\u60ac\u505c*/\n"
"QPushButton:hover{\n"
"	border:1px solid #808080;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"/*\u6309\u94ae\u6309\u4e0b*/\n"
"QPushButton:pressed{\n"
"	background-color:#e1e1e1;\n"
" }\n"
"\n"
"#pushButton1{\n"
"	background-image:url(:/icons/icons/trash.png);\n"
"}\n"
"\n"
"#pushButton2{\n"
"	background-image:url(:/icons/icons/copy.png);\n"
"}\n"
"\n"
"#pushButton3{\n"
"	background-image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"#pushButton4{\n"
"	background-image:url(:/icons/icons/send-01.png);\n"
"}\n"
"\n"
"#pushButton5{\n"
"	background-image:url(:/icons/icons/pin_active.png);\n"
"}\n"
"\n"
"\n"
"/*\u80cc\u666f\u8272*/\n"
"#label_BG{\n"
"	background-color:#FFFFFF;\n"
"	border:1px solid #ffffff;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/*\u63d0\u793a\u4fe1\u606f*/\n"
"#label{\n"
"	padding:3px 1px 3px 1px;\n"
"}\n"
""
                        "\n"
"#comboBox{\n"
"	height:23px;\n"
"	background-color:#F5F5F5;\n"
"	border:1px solid #dadada;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the pop"
                        "up opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(36, 12, 889, 30))
        self.horizontalLayout1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout1.setSpacing(2)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.textEdit1 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setMinimumSize(QSize(60, 25))
        self.textEdit1.setMaximumSize(QSize(60, 25))
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit1.setFont(font1)
        self.textEdit1.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit1.setFocusPolicy(Qt.StrongFocus)
        self.textEdit1.setStyleSheet(u"")
        self.textEdit1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout1.addWidget(self.textEdit1)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout1.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer)

        self.pushButton2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton2.setObjectName(u"pushButton2")

        self.horizontalLayout1.addWidget(self.pushButton2)

        self.pushButton1 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton1.setObjectName(u"pushButton1")

        self.horizontalLayout1.addWidget(self.pushButton1)

        self.pushButton3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton3.setObjectName(u"pushButton3")

        self.horizontalLayout1.addWidget(self.pushButton3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer_2)

        self.textEdit2 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit2.setObjectName(u"textEdit2")
        self.textEdit2.setMinimumSize(QSize(500, 25))
        self.textEdit2.setMaximumSize(QSize(500, 25))
        self.textEdit2.setFont(font1)
        self.textEdit2.setLineWidth(1)
        self.textEdit2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout1.addWidget(self.textEdit2)

        self.pushButton4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton4.setObjectName(u"pushButton4")

        self.horizontalLayout1.addWidget(self.pushButton4)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(65, 0))
        self.label.setMaximumSize(QSize(65, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout1.addWidget(self.label)

        self.pushButton5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton5.setObjectName(u"pushButton5")

        self.horizontalLayout1.addWidget(self.pushButton5)

        self.label_BG = QLabel(Form)
        self.label_BG.setObjectName(u"label_BG")
        self.label_BG.setGeometry(QRect(26, 8, 905, 37))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(8)
        self.label_BG.setFont(font3)
        self.label_BG.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Power", None))
        self.pushButton2.setText("")
        self.pushButton1.setText("")
        self.pushButton3.setText("")
        self.pushButton4.setText("")
        self.label.setText("")
        self.pushButton5.setText("")
        self.label_BG.setText("")
    # retranslateUi

