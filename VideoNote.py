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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(872, 316)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid #ffffff;\n"
"	color:white;\n"
"	font-weight:bold;\n"
"	background-color: #8800C2;\n"
"	border-radius:2px;\n"
"	padding: 3px 5px 3px 5px;\n"
"	margin:1px 2px 1px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #A34EC9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:#104CC4;\n"
"	border: 1px solid #104CC4;\n"
"	color:white;\n"
" }\n"
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
"#pushButton3{\n"
"	background-color: #C2002F;\n"
"}")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(23, 8, 793, 30))
        self.horizontalLayout1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout1.setSpacing(0)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.textEdit1 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setMinimumSize(QSize(80, 25))
        self.textEdit1.setMaximumSize(QSize(80, 25))
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit1.setFont(font1)
        self.textEdit1.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit1.setFocusPolicy(Qt.StrongFocus)
        self.textEdit1.setStyleSheet(u"")
        self.textEdit1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout1.addWidget(self.textEdit1)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(65, 0))
        self.label.setMaximumSize(QSize(65, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout1.addWidget(self.label)

        self.pushButton2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton2.setObjectName(u"pushButton2")

        self.horizontalLayout1.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton3.setObjectName(u"pushButton3")

        self.horizontalLayout1.addWidget(self.pushButton3)

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

        self.label_BG = QLabel(Form)
        self.label_BG.setObjectName(u"label_BG")
        self.label_BG.setGeometry(QRect(14, 4, 805, 67))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(8)
        self.label_BG.setFont(font3)
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(350, 42, 97, 23))
        self.horizontalLayout2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.checkBox1 = QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox1.setObjectName(u"checkBox1")

        self.horizontalLayout2.addWidget(self.checkBox1)

        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(22, 42, 321, 23))
        self.horizontalLayout3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout3.addWidget(self.label_2)

        self.radioButton2 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton2.setObjectName(u"radioButton2")

        self.horizontalLayout3.addWidget(self.radioButton2)

        self.radioButton1 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton1.setObjectName(u"radioButton1")

        self.horizontalLayout3.addWidget(self.radioButton1)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout3.addWidget(self.radioButton)

        self.label_BG.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.pushButton2.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.pushButton3.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.pushButton4.setText(QCoreApplication.translate("Form", u"Send", None))
        self.label_BG.setText("")
        self.checkBox1.setText(QCoreApplication.translate("Form", u"\u6682\u505c\u529f\u80fd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5c3a\u5bf8\u9009\u62e9 :", None))
        self.radioButton2.setText(QCoreApplication.translate("Form", u"1300px", None))
        self.radioButton1.setText(QCoreApplication.translate("Form", u"1000px", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"700px", None))
    # retranslateUi

