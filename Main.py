import sys
import win32con
import win32gui

from PySide6.QtCore import Slot, Qt, Signal, QSettings, QMimeData
from PySide6.QtGui import QCursor, QPixmap, QGuiApplication
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from system_hotkey import SystemHotkey
from Screenshot import CaptureScreen
from ScreenshotNote.UI.VideoNote import Ui_Form


class yes(QWidget, Ui_Form):
    cap = None
    keyboardSignal = Signal()
    stayOnTopFlag = False

    def __init__(self):
        super(yes, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.keyboardSignal.connect(self.startScreen)

        # QPushButton按钮事件
        self.ui.Button_copy.clicked.connect(self.copyAll)
        self.ui.Button_cut.clicked.connect(self.cutAll)
        self.ui.Button_clear.clicked.connect(self.clearAll)
        self.ui.Button_shrink.clicked.connect(self.shrink)
        self.ui.Button_monitor.clicked.connect(self.changeMonitorStatus)
        self.ui.Button_setting.clicked.connect(self.settings)
        self.ui.Button_close.clicked.connect(self.exit)
        self.ui.Button_pin.clicked.connect(self.stayTop)

        self.ui.Button_copy.setToolTip("复制")
        self.ui.Button_cut.setToolTip("剪切")
        self.ui.Button_clear.setToolTip("清空")
        self.ui.Button_monitor.setToolTip("监控剪切板")
        self.ui.Button_shrink.setToolTip("收缩/展开")
        self.ui.Button_setting.setToolTip("设置")
        self.ui.Button_close.setToolTip("退出")
        self.ui.Button_pin.setToolTip("切换置顶")

        # 无边框,背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 拖拽移动
        self.m_flag = False
        self.m_Position = 0

        # 设置截图快捷键
        self.hk_start = SystemHotkey()
        self.hk_start.register(('f4',), callback=lambda x: self.send_key_event())

        self.maxWidth = 1300  # 截图的默认最大宽度
        self.loadConfigurationFile()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # 窗口置顶

        self.clipboard = QGuiApplication.clipboard()
        self.statusFlag = False  # 开启与关闭检测剪切板功能

    def loadConfigurationFile(self):
        """
        加载配置文件
        """
        self.setting = QSettings("configuration.ini", QSettings.IniFormat)  # 配置文件
        self.ui.comboBox.addItems(self.setting.value("OPTION/COMBOBOX_ITEM"))
        self.ui.comboBox.currentTextChanged.connect(self.changeSize)
        self.ui.comboBox.setCurrentText(self.setting.value("LAST_OPTION/LAST_SIZE"))
        self.ui.frame_2.setStyleSheet(f"background-color:{self.setting.value('UI/MAINWINDOW_BAR')}")
        self.ui.textEdit.setStyleSheet(f"background-color:{self.setting.value('UI/MAINWINDOW_NOTE')}")

        flag = self.setting.value('LAST_OPTION/FOLD_FLAG')
        if flag == "1":
            self.ui.Button_shrink.setChecked(True)
            self.shrink()
        else:
            self.ui.Button_shrink.setChecked(False)

    def send_key_event(self):
        """
        设置了快捷键f4,调用截图
        """
        self.keyboardSignal.emit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPosition().toPoint() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if self.m_flag:
            self.move(QMouseEvent.globalPosition().toPoint() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

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
        origin = self.ui.textEdit.toHtml()
        data = QMimeData()
        data.setHtml(origin)
        self.clipboard.setMimeData(data)
        self.resetStatus()

    def cutAll(self):
        origin = self.ui.textEdit.toHtml().replace(" width=\"280\"", "")\
            .replace("font-family:'Microsoft YaHei UI'; font-size:10pt;", "font-family:'GUYELUO'; font-size:13pt;")
        data = QMimeData()
        data.setHtml(origin)
        self.clipboard.setMimeData(data)
        self.ui.textEdit.clear()
        self.resetStatus()

    def clearAll(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("There are already some notes.\nAre you sure you want to clear them?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.ui.textEdit.clear()
            self.ui.textEdit.setToolTip(f"这里什么也没有")

    def shrink(self):
        if self.ui.Button_shrink.isChecked():
            self.ui.textEdit.setMaximumHeight(35)
            self.ui.textEdit.setMinimumHeight(35)
        else:
            self.ui.textEdit.setMaximumHeight(200)
            self.ui.textEdit.setMaximumHeight(200)

    def exit(self):
        self.resetStatus()
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("Make sure nothing needs to be saved before exiting.")
        msgBox.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Close:
            currentSize = self.ui.comboBox.currentText()
            self.setting.setValue("LAST_OPTION/LAST_SIZE", currentSize)
            if self.ui.Button_shrink.isChecked():
                self.setting.setValue("LAST_OPTION/FOLD_FLAG", 1)
            else:
                self.setting.setValue("LAST_OPTION/FOLD_FLAG", 0)
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
            self.ui.Button_pin.setStyleSheet("background-image:url(:/new/icons/pin_default.png);")
        else:
            win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW
                                  | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            self.ui.Button_pin.setStyleSheet("background-image:url(:/new/icons/pin_active.png);")
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

    def resetStatus(self):
        if self.statusFlag:
            self.changeMonitorStatus()
            self.ui.Button_monitor.setChecked(False)

    def saveCbData(self):
        """
        如果发现剪切板有新内容则发送到textEdit
        """
        self.ui.textEdit.append("")
        if self.clipboard.mimeData().hasImage():
            pixmap = self.clipboard.image()
            if pixmap.width() > self.maxWidth:
                pixmap = pixmap.scaledToWidth(self.maxWidth, Qt.SmoothTransformation)
            self.ui.textEdit.insertImage(pixmap)
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

    def changeMonitorStatus(self):
        """
        打开与关闭检测剪切板功能
        """
        if self.statusFlag:
            self.clipboard.dataChanged.disconnect(self.saveCbData)
            self.ui.Button_monitor.setStyleSheet("background-color:#ffffff")
        else:
            self.clipboard.dataChanged.connect(self.saveCbData)
            self.ui.Button_monitor.setStyleSheet(
                f"background-color:{self.setting.value('UI/MAINWINDOW_MONITOR_BUTTON')}")
        self.statusFlag = ~ self.statusFlag

    def settings(self):
        pass

    def changeSize(self, rbt):
        """
        控制截图的最大宽度
        """
        if rbt == "无限制":
            self.maxWidth = 9999
            return
        self.maxWidth = int(rbt[:-2])

    @Slot(QPixmap, str)
    def addImageAndNote(self, img, note=""):
        """
        槽函数,接受截图数据和笔记
        """
        self.ui.textEdit.append("")  # 空行
        # 控制截图尺寸
        if img.size().width() > self.maxWidth:
            img = img.scaledToWidth(self.maxWidth, Qt.SmoothTransformation)
        self.ui.textEdit.insertImage(img)
        if note != "":
            self.ui.textEdit.append(note)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = yes()
    mainWin.move(500, 27)
    mainWin.show()
    sys.exit(app.exec())
