import sys

import keyboard
from PySide6.QtCore import Slot, Qt, Signal, QSettings
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QWidget
from system_hotkey import SystemHotkey

from Screenshot import CaptureScreen
from VideoNote import Ui_Form


class yes(QWidget, Ui_Form):
    cap = None
    exit_time = 0
    signal3 = Signal()
    setting = None

    def __init__(self):
        super(yes, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # QPushButton按钮事件
        self.ui.pushButton2.clicked.connect(self.copyAll)
        self.ui.pushButton3.clicked.connect(self.exit)
        self.ui.pushButton4.clicked.connect(self.sendNote)

        # QRadioButton切换事件
        self.ui.radioButton1.setChecked(True)
        self.ui.radioButton1.toggled.connect(lambda: self.ctrlPicSize("rbt1"))
        self.ui.radioButton2.toggled.connect(lambda: self.ctrlPicSize("rbt2"))
        self.ui.radioButton3.toggled.connect(lambda: self.ctrlPicSize("rbt3"))
        self.ui.radioButton4.toggled.connect(lambda: self.ctrlPicSize("rbt4"))
        self.ui.radioButton5.toggled.connect(lambda: self.ctrlPicSize("rbt5"))
        self.ui.radioButton6.toggled.connect(lambda: self.ctrlPicSize("rbt6"))

        # QCheckBox切换事件
        self.ui.checkBox1.toggled.connect(self.stopVideoOrNot)

        # 无边框,背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 读取配置文件
        self.setting = QSettings("config.ini", QSettings.IniFormat)
        bg = self.setting.value("UI/background_color")
        self.ui.label_BG.setStyleSheet(f"background-color:{bg}")

        # 窗口置顶
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # 拖拽移动
        self.m_flag = False
        self.m_Position = 0

        # 连接信号与槽
        self.signal3.connect(self.startScreen)
        # 初始化一个热键
        self.hk_start = SystemHotkey()
        # 绑定快捷键和对应的信号发送函数
        self.hk_start.register(('f4',), callback=lambda x: self.send_key_event())

        # 截图的默认最大宽度
        self.maxWidth = 1300

        # 默认不暂停视频
        self.stopOrNot = False

    '''
    设置了快捷键f4,调用截图
    '''

    def send_key_event(self):
        if self.stopOrNot:
            keyboard.press_and_release("space")
        self.signal3.emit()

    '''
    鼠标点击事件
    '''

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPosition().toPoint() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    '''
    鼠标移动事件
    '''

    def mouseMoveEvent(self, QMouseEvent):
        if self.m_flag:
            self.move(QMouseEvent.globalPosition().toPoint() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    '''
    鼠标释放事件
    '''

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    '''
    开始截图
    '''

    def startScreen(self):
        yes.cap = CaptureScreen(self.maxWidth, self.stopOrNot)
        yes.cap.show()
        yes.cap.signal.connect(self.appendImage)
        yes.cap.signal2.connect(self.lastImageSize)

    '''
    复制到剪切板
    '''

    def copyAll(self):
        yes.exit_time = 0
        self.ui.label.setText("")
        self.ui.textEdit1.setFocus()
        self.ui.textEdit1.selectAll()
        keyboard.press_and_release("ctrl+x")

    '''
    退出程序
    '''

    def exit(self):
        self.ui.label.setStyleSheet("color:purple;font-weight:bold")
        yes.exit_time += 1
        if yes.exit_time == 1:
            self.ui.label.setText("确认退出?")
        elif yes.exit_time == 2:
            self.ui.label.setText("再点一次")
        else:
            self.close()

    '''
    添加笔记
    '''

    def sendNote(self):
        yes.exit_time = 0
        self.ui.label.setText("")
        self.ui.textEdit1.append(self.ui.textEdit2.toPlainText())
        self.ui.textEdit2.clear()

    '''
    控制截图的最大宽度
    '''

    def ctrlPicSize(self, rbt):
        if rbt == "rbt1" and self.ui.radioButton1.isChecked():
            self.maxWidth = 1300
        elif rbt == "rbt2" and self.ui.radioButton2.isChecked():
            self.maxWidth = 1100
        elif rbt == "rbt3" and self.ui.radioButton3.isChecked():
            self.maxWidth = 1000
        elif rbt == "rbt4" and self.ui.radioButton4.isChecked():
            self.maxWidth = 900
        elif rbt == "rbt5" and self.ui.radioButton5.isChecked():
            self.maxWidth = 700
        elif rbt == "rbt6" and self.ui.radioButton6.isChecked():
            self.maxWidth = 500

    def stopVideoOrNot(self):
        self.stopOrNot = not self.stopOrNot

    '''
    槽函数,接受截图数据
    '''

    @Slot(str)
    def appendImage(self, imageBase64):
        self.ui.textEdit1.append(f"<img src=data:image/png;base64,{imageBase64}/>")
        self.ui.textEdit1.append("")

    '''
    槽函数,检测图片大小,提醒用户是否截图成功
    '''

    @Slot(int, int)
    def lastImageSize(self, width, height):
        if width < 50 and height < 50:
            self.ui.label.setStyleSheet("color:red;font-weight:bold")
            self.ui.label.setText("小于50px")
        else:
            self.ui.label.setStyleSheet("color:green;font-weight:bold")
            self.ui.label.setText(f"{width}×{height}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = yes()
    mainWin.move(500, 27)
    mainWin.show()
    sys.exit(app.exec())
