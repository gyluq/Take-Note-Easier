import sys

import keyboard
from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QWidget
from system_hotkey import SystemHotkey

from Screenshot import CaptureScreen
from VideoNote import Ui_Form
from pyperclip import paste


class yes(QWidget, Ui_Form):
    cap = None
    exit_time = 0
    clear_time = 0
    signal3 = Signal()

    def __init__(self):
        super(yes, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定事件
        self.ui.pushButton1.clicked.connect(self.clearTextEdit1)
        self.ui.pushButton2.clicked.connect(self.copyAll)
        self.ui.pushButton3.clicked.connect(self.exit)
        self.ui.pushButton4.clicked.connect(self.sendNote)
        self.ui.pushButton5.clicked.connect(self.sendClipboard)

        # 无边框,背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

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
        self.hk_start.register(('f4', ), callback=lambda x: self.send_key_event())

    '''
    设置了快捷键Ctrl+1,调用截图
    '''

    def send_key_event(self):
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
        yes.cap = CaptureScreen()
        yes.cap.show()
        yes.cap.signal.connect(self.appendImage)
        yes.cap.signal2.connect(self.lastImageSize)

    def clearTextEdit1(self):
        yes.exit_time = 0
        self.ui.label.setStyleSheet("color:red;font-weight:bold")
        yes.clear_time += 1
        if yes.clear_time == 1:
            self.ui.label.setText("确认清空?")
        elif yes.clear_time == 2:
            self.ui.label.setText("再点一次")
        else:
            self.ui.textEdit1.clear()
            self.ui.label.setText("清空了")

    '''
    复制到剪切板
    '''

    def copyAll(self):
        yes.exit_time = 0
        yes.clear_time = 0
        self.ui.label.setText("")
        self.ui.textEdit1.setFocus()
        self.ui.textEdit1.selectAll()
        keyboard.press_and_release("ctrl+c")

    '''
    退出程序
    '''

    def exit(self):
        yes.clear_time = 0
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
        yes.clear_time = 0
        self.ui.label.setText("")
        self.ui.textEdit1.append(self.ui.textEdit2.toPlainText())
        self.ui.textEdit2.clear()

    def sendClipboard(self):
        self.ui.label.setText("")
        self.ui.textEdit1.append(paste())
        self.ui.textEdit2.clear()

    '''
    槽函数,接受截图数据
    '''

    @Slot(str)
    def appendImage(self, imageBase64):
        self.ui.textEdit1.append(f"<img src=data:image/png;base64,{imageBase64}/>")

    '''
    槽函数,检测图片大小,提醒用户是否截图成功
    '''

    @Slot(int, int)
    def lastImageSize(self, width, height):
        if width < 50 or height < 50:
            self.ui.label.setStyleSheet("color:red;font-weight:bold")
            self.ui.label.setText("小于50px")
        else:
            self.ui.label.setStyleSheet("color:green;font-weight:bold")
            self.ui.label.setText(f"{width}×{height}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = yes()
    mainWin.move(400, 5)
    mainWin.show()
    sys.exit(app.exec())
