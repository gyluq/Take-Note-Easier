import win32gui
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QApplication

from .popLabel import Ui_Form


class PopLabel(QWidget):
    flag = None

    def __init__(self, text, color=None):
        super(PopLabel, self).__init__(None, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form()
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


if __name__ == '__main__':
    app = QApplication([])
    a = PopLabel("hhh")
    app.exec()
