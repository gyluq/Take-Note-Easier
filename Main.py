import sys

import keyboard
import win32con
import win32gui
from PySide6.QtCore import Slot, Qt, Signal, QSettings, QByteArray, QBuffer
from PySide6.QtGui import QCursor, QPixmap, QGuiApplication
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from system_hotkey import SystemHotkey

from Screenshot import CaptureScreen
from VideoNote import Ui_Form
import img_rc


class yes(QWidget, Ui_Form):
    cap = None
    keyboardSignal = Signal()
    pic_num = 0  # 图片数量
    note_num = 0  # 笔记数量
    stayOnTopFlag = False

    def __init__(self):
        super(yes, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.keyboardSignal.connect(self.startScreen)

        # QPushButton按钮事件
        self.ui.pushButton.clicked.connect(self.copyAll)
        self.ui.pushButton1.clicked.connect(self.clearAll)
        self.ui.pushButton2.clicked.connect(self.cutAll)
        self.ui.pushButton3.clicked.connect(self.exit)
        self.ui.pushButton4.clicked.connect(self.sendNote)
        self.ui.pushButton5.clicked.connect(self.stayTop)
        self.ui.pushButton6.clicked.connect(self.changeMonitorStatus)
        self.ui.pushButton.setToolTip("复制")
        self.ui.pushButton1.setToolTip("清空")
        self.ui.pushButton2.setToolTip("剪切")
        self.ui.pushButton3.setToolTip("退出")
        self.ui.pushButton4.setToolTip("添加笔记")
        self.ui.pushButton5.setToolTip("切换置顶")

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
        self.setting = QSettings("configuration.ini", QSettings.IniFormat)  # 配置文件
        self.loadConfigurationFile()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # 窗口置顶

        self.clipboard = QGuiApplication.clipboard()
        self.statusFlag = False
        self.ui.textEdit2.textChanged.connect(lambda: self.ui.textEdit2.setToolTip(self.ui.textEdit2.toPlainText()))

    def loadConfigurationFile(self):
        """
        加载配置文件
        """
        # 界面背景
        bg = self.setting.value("UI/mainWindow_bg_color")
        self.ui.label_BG.setStyleSheet(f"background-color:{bg}")
        # 初始化comboBox
        sizeList = self.setting.value("OPTION/allSize")
        self.ui.comboBox.addItems(sizeList)
        self.ui.comboBox.currentTextChanged.connect(self.changeSize)
        self.ui.comboBox.setCurrentText(self.setting.value("OPTION/lastSelectedSize"))

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
        self.hideMe()
        self.cap = CaptureScreen(self.maxWidth)  # cap必须是类属性,否则方法结束后会结束生命周期
        self.cap.show()
        self.cap.setFocus()
        self.cap.signal_size.connect(self.lastImageSize)
        self.cap.signal_picAndNote.connect(self.appendImageAndNote)
        self.cap.signal_close.connect(self.showMe)

    def copyAll(self):
        self.resetStatus()
        self.ui.textEdit1.setFocus()
        self.ui.textEdit1.selectAll()
        keyboard.press_and_release("ctrl+c")
        keyboard.press_and_release("right")

    def cutAll(self):
        self.resetStatus()
        self.ui.textEdit1.setFocus()
        self.ui.textEdit1.selectAll()
        keyboard.press_and_release("ctrl+x")
        self.pic_num = 0
        self.note_num = 0
        self.ui.textEdit1.setToolTip(f"这里什么也没有")

    def clearAll(self):
        self.ui.label.setText(" ")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("There are already some notes.\nAre you sure you want to clear them?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.ui.textEdit1.clear()
            self.pic_num = 0
            self.note_num = 0
            self.ui.textEdit1.setToolTip(f"这里什么也没有")

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
            self.setting.setValue("OPTION/lastSelectedSize", currentSize)
            self.close()

    def sendNote(self):
        self.resetStatus()
        if self.ui.textEdit2.toPlainText() != "":
            self.ui.textEdit1.append(self.ui.textEdit2.toPlainText())
            self.ui.textEdit2.clear()
            self.note_num += 1
            self.ui.textEdit1.setToolTip(f"{self.pic_num}张图,{self.note_num}条笔记")

    def stayTop(self):
        """
        置顶按钮调用,切换置顶
        """
        window = win32gui.FindWindow(None, "Power")
        self.ui.label.setStyleSheet("color:green;font-weight:bold")
        if self.stayOnTopFlag:
            win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER
                                  | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
            self.ui.pushButton5.setStyleSheet("background-image:url(:/icons/icons/pin_active.png);")
            self.ui.label.setText("已置顶")
        else:
            win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW
                                  | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            self.ui.pushButton5.setStyleSheet("background-image:url(:/icons/icons/pin_default.png);")
            self.ui.label.setText("未置顶")
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

    def resetStatus(self):
        self.ui.label.setText(" ")
        if self.statusFlag:
            self.changeMonitorStatus()
            self.ui.pushButton6.setChecked(False)

    def saveCbData(self):
        """
        如果发现剪切板有新内容则发送到textEdit2
        """
        self.ui.textEdit1.append("")
        if self.clipboard.mimeData().hasImage():
            pixmap = self.clipboard.pixmap()
            imgStr = self.imgToBase64(pixmap)
            self.ui.textEdit1.append(imgStr)
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
            self.ui.textEdit1.append(newText)

    def changeMonitorStatus(self):
        """
        打开与关闭检测剪切板功能
        """
        if self.statusFlag:
            self.clipboard.dataChanged.disconnect(self.saveCbData)
        else:
            self.clipboard.dataChanged.connect(self.saveCbData)
        self.statusFlag = ~ self.statusFlag

    def imgToBase64(self, img):
        """
        图片转base64
        :param img: QPixmap or QImage
        :return: str
        """
        data = QByteArray()
        buf = QBuffer(data)
        img.save(buf, "PNG")
        imgData = str(data.toBase64(), encoding="utf-8")
        return f"<img src=\"data:image/png;base64,{imgData}\" alt=\"**图片**\"/>"

    def changeSize(self, rbt):
        """
        控制截图的最大宽度
        """
        if rbt == "无限制":
            self.maxWidth = 9999
            return
        self.maxWidth = int(rbt[:-2])

    @Slot(QPixmap, str)
    def appendImageAndNote(self, img, note=""):
        """
        槽函数,接受截图数据和笔记
        """
        if self.note_num or self.pic_num:
            self.ui.textEdit1.append("")
        self.ui.textEdit1.append(self.imgToBase64(img))
        self.pic_num += 1
        if note != "":
            self.ui.textEdit1.append(note)
            self.note_num += 1
        self.ui.textEdit1.setToolTip(f"{self.pic_num}张图,{self.note_num}条笔记")

    @Slot(int, int)
    def lastImageSize(self, width, height):
        """
        槽函数,检测图片大小,提醒用户是否截图成功
        """
        if width < 50 and height < 50:
            self.ui.label.setPixmap(QPixmap(":/icons/icons/important.png"))
        else:
            self.ui.label.setPixmap(QPixmap(":/icons/icons/ok.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = yes()
    mainWin.move(500, 27)
    mainWin.show()
    sys.exit(app.exec())
