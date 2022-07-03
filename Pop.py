import win32gui
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QApplication

from Utils.DragToMove import DragToMove
from UI.ui_popNote import Ui_Form1
from UI.ui_popLabel import Ui_Form2


class PopNote(QWidget):
    def __init__(self):
        super(PopNote, self).__init__(None, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.initialization()

    def initialization(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 拖拽移动
        self.dragToMove = DragToMove()
        self.dragToMove.setUp(self.ui.frame, self)
        # 检测剪切板
        self.clip = QGuiApplication.clipboard()
        self.clip.dataChanged.connect(self.getTextFromClipboard)
        # 绑定事件
        self.ui.BtExit.clicked.connect(self.close)

    def getTextFromClipboard(self):
        text = self.clip.text().replace("。", ".") \
            .replace("，", ",") \
            .replace("‘", "'") \
            .replace("’", "'") \
            .replace("”", "\"") \
            .replace("“", "\"") \
            .replace("；", ";") \
            .replace("）", ")") \
            .replace("（", "(") \
            .replace("【", "[") \
            .replace("】", "]") \
            .replace("》", ">") \
            .replace("《", "<") \
            .replace("？", "?")
        self.ui.textEdit.append(text)


class PopLabel(QWidget):
    flag = None

    def __init__(self, text, color=None):
        super(PopLabel, self).__init__(None, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.ui.label.setWordWrap(True)
        self.ui.label.setText(text)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.ClickFocus)
        if color is not None:
            self.ui.label.setStyleSheet(f"background-color:{color}")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(600)
        self.show()

    def showMe(self):
        window = win32gui.FindWindow(None, "Form")
        win32gui.SetForegroundWindow(window)


if __name__ == "__main__":
    app = QApplication([])
    showit = PopNote()
    showit.show()
    app.exec()
