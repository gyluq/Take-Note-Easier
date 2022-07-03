import win32gui
from PySide6.QtCore import Qt, QTimer, Slot, Signal
from PySide6.QtGui import QGuiApplication, QTextCursor
from PySide6.QtWidgets import QWidget, QApplication, QTextEdit

from Utils.DragToMove import DragToMove
from UI.ui_popNote import Ui_Form1
from UI.ui_popLabel import Ui_Form2


class PopNote(QWidget):
    signal = Signal(str, tuple)

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
        self.ui.BtStop.setChecked(True)
        # 拖拽移动
        self.dragToMove = DragToMove()
        self.dragToMove.setUp(self.ui.frame, self)
        # 检测剪切板
        self.clip = QGuiApplication.clipboard()
        self.clip.dataChanged.connect(self.getDataFromClipboard)
        # 绑定事件
        self.ui.BtExit.clicked.connect(self.close)
        self.ui.BtSend.clicked.connect(self.sendTextNote)
        self.ui.BtStop.clicked.connect(self.stopMonitor)

    def getDataFromClipboard(self):
        self.ui.textEdit.append("")
        if self.clip.mimeData().hasImage():
            pixmap = self.clip.image()
            self.ui.textEdit.insertImage(pixmap, True, 165)
            self.imgNum += 1
        else:
            newText = self.clip.text().replace("。", ".") \
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
            self.ui.textEdit.append(newText)
            cursor = self.ui.textEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.ui.textEdit.setTextCursor(cursor)
            self.textLenth += len(newText)

    @Slot(str, tuple)
    def sendTextNote(self):
        text = self.ui.textEdit.toHtml().replace(" width=\"165\"", "") \
            .replace(f"; font-size:9pt", "; font-size:11pt")
        self.signal.emit(text, (self.textLenth, self.imgNum))
        self.ui.textEdit.clear()

    @Slot()
    def stopMonitor(self):
        if self.detectFlag:
            self.clip.dataChanged.disconnect(self.getDataFromClipboard)
            self.detectFlag = False
        else:
            self.clip.dataChanged.connect(self.getDataFromClipboard)
            self.detectFlag = True


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
