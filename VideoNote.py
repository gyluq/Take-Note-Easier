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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(694, 44)
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
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"#pushButton{\n"
"	background-image:url(:/icons/icons/copy.png);\n"
"}\n"
"\n"
"#pushButton1{\n"
"	background-image:url(:/icons/icons/trash.png);\n"
"}\n"
"\n"
"#pushButton2{\n"
"	background-image:url(:/icons/icons/cut.png);\n"
"}\n"
"\n"
"#pushButton3{\n"
"	background-image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"#pushButton4{\n"
"	background-image:url(:/icons/icons/send.png);\n"
"}\n"
"\n"
"#pushButton5{\n"
"	background-image:url(:/icons/icons/pin_active.png);\n"
"}\n"
"\n"
"#pushButton6{\n"
"	background-image:url(:/icons/icons/m"
                        "onitor.png);\n"
"}\n"
"\n"
"#pushButton6::checked{\n"
"	background-color:#80C698F0;\n"
"	border:1px solid #808080;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"#label_BG{\n"
"	background-color:#FFFFFF;\n"
"	border:1px solid #ffffff;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#label{\n"
"	padding:3px 1px 3px 1px;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"QTextEdit{\n"
"	border:1px solid #808080;\n"
"	border-radius:3px;\n"
"	background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------*/\n"
"\n"
"QComboBox {\n"
"	height:23px;\n"
"    border: 1px solid darkgray;\n"
"    border-radius: 3px;\n"
"	background-color:#FAFAFA;\n"
"    padding: 1px 8px 1px 3px;\n"
"    min-width: 4em;\n"
"}\n"
"\n"
"/*\u53f3\u4fa7\u7684\u5c55\u793a\u6309\u94ae*/\n"
"QComboBox::drop-down {\n"
"    subcontrol-origi"
                        "n: padding;\n"
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
"    image: url(:/icons/icons/sort-left.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    width: 9px;  \n"
"    height: 9px;   \n"
"    image: url(:/icons/icons/sort-down.png);\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(12, 8, 671, 30))
        self.horizontalLayout1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout1.setSpacing(2)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.textEdit1 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setMinimumSize(QSize(200, 25))
        self.textEdit1.setMaximumSize(QSize(200, 25))
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
        self.comboBox.setMinimumSize(QSize(73, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout1.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout1.addWidget(self.pushButton)

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
        self.textEdit2.setMinimumSize(QSize(150, 25))
        self.textEdit2.setMaximumSize(QSize(150, 25))
        self.textEdit2.setFont(font1)
        self.textEdit2.setLineWidth(1)
        self.textEdit2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout1.addWidget(self.textEdit2)

        self.pushButton4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton4.setObjectName(u"pushButton4")

        self.horizontalLayout1.addWidget(self.pushButton4)

        self.pushButton6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setCheckable(True)

        self.horizontalLayout1.addWidget(self.pushButton6)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 16777215))
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
        self.label_BG.setGeometry(QRect(4, 6, 683, 33))
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
        self.pushButton.setText("")
        self.pushButton2.setText("")
        self.pushButton1.setText("")
        self.pushButton3.setText("")
        self.pushButton4.setText("")
        self.pushButton6.setText("")
        self.label.setText("")
        self.pushButton5.setText("")
        self.label_BG.setText("")
    # retranslateUi

