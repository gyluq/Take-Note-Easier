import win32gui
from PySide6.QtCore import Qt, QTimer, Slot, Signal
from PySide6.QtWidgets import QWidget, QApplication

from UI.ui_popLabel import Ui_Form2
from UI.ui_popNote import Ui_Form1
from Utils.DragToMove import DragToMove


class PopNote(QWidget):
    signal = Signal(str)

    def __init__(self):
        super(PopNote, self).__init__(None, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.initialization()

    def initialization(self):
        self.textLenth = 0
        self.imgNum = 0
        self.detectFlag = True
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.textEdit.setTabStopDistance(40)
        # 拖拽移动
        self.dragToMove = DragToMove()
        self.dragToMove.setUp(self.ui.frame, self)
        # 绑定事件
        self.ui.BtWinExit.clicked.connect(self.close)
        self.ui.BtTextSend.clicked.connect(self.sendTextNote)
        self.ui.BtTextFormate.clicked.connect(self.formateText)
        self.ui.BtTextClear.clicked.connect(lambda x: self.ui.textEdit.clear())

        self.currentFontSize = 9
        self.pop = None

    def formateText(self):
        text = self.ui.textEdit.toHtml()
        newText = text.replace("。", ".") \
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
        # self.fff = QTextEdit
        # self.fff.setHtml
        self.ui.textEdit.setHtml(newText)

    @Slot(str)
    def sendTextNote(self):
        html = self.ui.textEdit.toHtml().replace(f"font-size:{self.currentFontSize}pt;", "font-size:11pt;") \
            .replace(f"width=\"{self.ui.textEdit.width() - 20}\"", "")
        try:
            self.signal.emit(html)
        except Exception:
            self.pop = PopLabel("发送失败", "#CC4040")
            return
        self.pop = PopLabel("发送成功", "#379942")
        self.ui.textEdit.clear()


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
