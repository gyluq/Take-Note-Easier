import win32gui
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QApplication

from .popLabel import Ui_Form


class PopLabel(QWidget):
    flag = None

    def __init__(self, text):
        super(PopLabel, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.ClickFocus)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setWordWrap(True)
        self.ui.label.setText(text)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.close)  # 计时结束调用operate()方法
        self.timer.start(600)  # 设置计时间隔并启动 2s后关闭窗口

        self.show()

    def showMe(self):
        window = win32gui.FindWindow(None, "Form")
        win32gui.SetForegroundWindow(window)


if __name__ == '__main__':
    app = QApplication([])
    a = PopLabel("hhh")
    app.exec()
