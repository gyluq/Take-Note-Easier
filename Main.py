import os
import sys

import win32con
import win32gui
from PySide6.QtCore import Slot, Qt, Signal, QSettings, QMimeData
from PySide6.QtGui import QPixmap, QGuiApplication, QTextCursor
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget
from system_hotkey import SystemHotkey

from Screenshot import CaptureScreen
from UI.VideoNote import Ui_Form
from Settings import Setting


class NoteWindow(QWidget):
    cap = None
    screenSignal = Signal()
    stayOnTopFlag = False

    def __init__(self):
        super(NoteWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.screenSignal.connect(self.startScreen)

        # QPushButton按钮事件
        self.ui.Button_pin.clicked.connect(self.stayTop)
        self.ui.Button_copy.clicked.connect(self.copyAll)
        self.ui.Button_cut.clicked.connect(self.cutAll)
        self.ui.Button_clear.clicked.connect(self.clearAll)
        self.ui.Button_monitor.clicked.connect(self.changeMonitorStatus)
        self.ui.Button_setting.clicked.connect(self.startSetting)

        self.ui.Button_pin.setToolTip("切换置顶")
        self.ui.Button_copy.setToolTip("复制")
        self.ui.Button_cut.setToolTip("剪切")
        self.ui.Button_clear.setToolTip("清空")
        self.ui.Button_monitor.setToolTip("监控剪切板")
        self.ui.Button_setting.setToolTip("设置")

        self.setWindowTitle("Power")

        # 拖拽移动
        self.m_flag = False
        self.m_Position = 0

        # 设置截图快捷键
        self.hk_start = SystemHotkey()
        self.hk_start.register(('f4',), callback=lambda x: self.send_key_event())

        self.maxWidth = 1300  # 截图的默认最大宽度
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # 窗口置顶

        self.clipboard = QGuiApplication.clipboard()
        # 开启与关闭检测剪切板功能
        self.statusFlag = False
        # 只能有一个settingWindow
        self.settingWindow = None
        self.initialization()

    def initialization(self):
        width = 1000
        height = 800
        self.setGeometry(870, -height + 2, width, height)
        # 窗口宽高
        self.h = self.height()
        self.w = self.width()
        # 图片宽度
        self.pictureWidth = None
        self.setting = QSettings("configuration.ini", QSettings.IniFormat)  # 配置文件
        self.maxWidth = int(self.setting.value("LAST_OPTION/LAST_SIZE")[:-2])

    def send_key_event(self):
        """
        设置了快捷键f4,调用截图
        """
        self.screenSignal.emit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            currentX = self.x()
            x = event.globalPosition().toPoint().x()
            y = event.globalPosition().toPoint().y()
            if currentX < x < currentX + self.w and 0 <= y <= 5:
                self.move(currentX, 0)
            else:
                self.move(currentX, -self.h - 30)

    def resizeEvent(self, event):
        if self.pictureWidth is None:
            # textEdit的宽度比窗口小24px
            self.pictureWidth = self.width() - 24
        # 因为某些原因,第一次获取的文本框宽度为80
        if self.ui.textEdit.width() > 100:
            newWidth = self.ui.textEdit.width() - 20
            html = self.ui.textEdit.toHtml()
            self.ui.textEdit.setHtml(html.replace(f"width=\"{self.pictureWidth}\"", f"width=\"{newWidth}\""))
            self.pictureWidth = newWidth
        self.h = self.height()
        self.w = self.width()

    def startScreen(self):
        """
        开始截图
        """
        self.activeMe()
        self.hideMe()
        self.cap = CaptureScreen(self.maxWidth)  # cap必须是类属性,否则方法结束后会结束生命周期
        self.cap.show()
        self.cap.setFocus()
        self.cap.signal_picAndNote.connect(self.addImageAndNote)
        self.cap.signal_close.connect(self.showMe)

    def copyAll(self):
        origin = self.ui.textEdit.toHtml().replace(f" width=\"{self.ui.textEdit.width() - 20}\"", "")
        data = QMimeData()
        data.setHtml(origin)
        self.clipboard.setMimeData(data)
        self.stopMonitor()

    def cutAll(self):
        origin = self.ui.textEdit.toHtml().replace(f" width=\"{self.ui.textEdit.width() - 20}\"", "") \
            .replace(f"font-family:'{self.ui.textEdit.font().family()}'; font-size:10pt",
                     "font-family:'GUYELUO'; font-size:13pt")
        data = QMimeData()
        data.setHtml(origin)
        self.clipboard.setMimeData(data)
        self.ui.textEdit.clear()
        self.stopMonitor()

    def clearAll(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("There are already some notes.\nAre you sure you want to clear them?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.ui.textEdit.clear()
            self.ui.textEdit.setToolTip(f"这里什么也没有")

    def exit(self):
        self.stopMonitor()
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("Make sure nothing needs to be saved before exiting.")
        msgBox.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Close:
            # 删除临时文件夹
            if os.path.exists("TempImg"):
                fileList = os.listdir("TempImg")
                for i in fileList:
                    os.remove(f"TempImg/{i}")
            self.close()

    def stayTop(self):
        """
        置顶按钮调用,切换置顶
        """
        window = win32gui.FindWindow(None, "Power")
        if self.stayOnTopFlag:
            win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER
                                  | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
        else:
            win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW
                                  | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        self.stayOnTopFlag = not self.stayOnTopFlag

    def hideMe(self):
        """
        截图时隐藏窗口
        """
        window = win32gui.FindWindow(None, "Power")
        win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)

    def showMe(self):
        """
        截图完成显示窗口
        """
        window = win32gui.FindWindow(None, "Power")
        win32gui.ShowWindow(window, win32con.SW_SHOWDEFAULT)

    def activeMe(self):
        window = win32gui.FindWindow(None, "Power")
        win32gui.SetForegroundWindow(window)

    def stopMonitor(self):
        if self.ui.Button_monitor.isChecked():
            self.ui.Button_monitor.setChecked(False)
            self.clipboard.dataChanged.disconnect(self.saveCbData)

    def saveCbData(self):
        """
        如果发现剪切板有新内容则发送到textEdit
        """
        self.ui.textEdit.append("")
        if self.clipboard.mimeData().hasImage():
            pixmap = self.clipboard.image()
            if pixmap.width() > self.maxWidth:
                pixmap = pixmap.scaledToWidth(self.maxWidth, Qt.SmoothTransformation)
            self.ui.textEdit.insertImage(pixmap, True)
        else:
            newText = self.clipboard.text().replace("。", ".") \
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

    def changeMonitorStatus(self):
        """
        打开与关闭检测剪切板功能
        """
        if self.ui.Button_monitor.isChecked():
            self.clipboard.dataChanged.connect(self.saveCbData)
        else:
            self.clipboard.dataChanged.disconnect(self.saveCbData)

    def startSetting(self):
        """
        设置子窗口
        """
        if self.settingWindow is None:
            self.settingWindow = Setting()
            self.settingWindow.signal.connect(self.reSetting)
        self.settingWindow.show()

    def reSetting(self):
        self.ui.textEdit.setStyleSheet(f"background-color:{self.setting.value('UI/MAINWINDOW_NOTE')}")
        self.maxWidth = int(self.setting.value("LAST_OPTION/LAST_SIZE")[:-2])

    @Slot(QPixmap, str)
    def addImageAndNote(self, img, note=""):
        """
        槽函数,接受截图数据和笔记
        """
        self.ui.textEdit.append("")
        self.ui.textEdit.insertImage(img, True)
        if note != "":
            self.ui.textEdit.append(note)
            cursor = self.ui.textEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.ui.textEdit.setTextCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = NoteWindow()
    mainWin.show()
    sys.exit(app.exec())
