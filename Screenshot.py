import sys

import keyboard
from PySide6 import QtCore
from PySide6.QtCore import Qt, qAbs, QRect, Signal, QSize
from PySide6.QtGui import QPen, QPainter, QColor, QGuiApplication, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QGroupBox, QHBoxLayout
import img_rc


class CaptureScreen(QMainWindow):
    # 初始化变量
    _speak = Signal(str)
    _size = Signal(int, int)
    beginPosition = None
    endPosition = None
    fullScreenImage = None
    captureImage = None
    isMousePressLeft = None
    painter = QPainter()
    text = None

    def __init__(self, maxWidth):
        super().__init__()
        self.initWindow()  # 初始化窗口
        self.captureFullScreen()  # 获取全屏
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.maxWidth = maxWidth

        # 实时笔记窗口
        self.textedit = QTextEdit(self)
        self.textedit.setPlaceholderText("记些什么...")
        self.textedit.setStyleSheet(
            "background-color:rgba(255,255,255, 50);border-radius:4px;font-size:13px;margin:0;padding:0;color:white;")
        self.textedit.hide()
        # 确认按钮
        self.okButton = QPushButton(QIcon(":/icons/icons/yes3.png"), "", self)
        self.okButton.setIconSize(QSize(20, 20))
        self.okButton.setStyleSheet(
            "background-repeat:none;background-position:center;background-color:rgba(255,255,255, 50);"
            "border:#FFFFFF;border-radius:4px;margin:0;padding:0;")
        self.okButton.setCursor(Qt.PointingHandCursor)
        self.okButton.setMaximumWidth(30)
        self.okButton.setMinimumWidth(30)
        self.okButton.setMaximumHeight(30)
        self.okButton.setMinimumHeight(30)
        self.okButton.hide()
        self.okButton.clicked.connect(self.saveNote)

        # 鼠标移动才更新edit和button的位置
        self.drawFlag = False

    def initWindow(self):
        self.setMouseTracking(True)  # 鼠标追踪
        self.setCursor(Qt.CrossCursor)  # 设置光标
        self.setWindowFlag(Qt.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowFullScreen)  # 窗口全屏

    def captureFullScreen(self):
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(0)

    def saveNote(self):
        self.sendImage()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.beginPosition = event.position()
            self.isMousePressLeft = True
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if self.isMousePressLeft is True:
            self.textedit.hide()
            self.okButton.hide()
            self.endPosition = event.position()
            self.drawFlag = True
            self.update()

    def mouseReleaseEvent(self, event):
        self.endPosition = event.position()
        if event.button() == Qt.LeftButton:
            self.isMousePressLeft = False
            if self.captureImage is not None and self.drawFlag:
                # 右下角的坐标
                bottomRight_x = min(self.beginPosition.x(), self.endPosition.x())
                bottomRight_y = max(self.beginPosition.y(), self.endPosition.y())

                # 设置文本框的尺寸
                selectWidth = abs(self.beginPosition.x() - self.endPosition.x())
                if selectWidth < 300:
                    self.textedit.setMinimumWidth(300)
                    self.textedit.setMaximumWidth(300)
                else:
                    self.textedit.setMinimumWidth(selectWidth - self.okButton.width() - 2)
                    self.textedit.setMaximumWidth(selectWidth - self.okButton.width() - 2)
                self.textedit.setMinimumHeight(30)
                self.textedit.setMaximumHeight(30)

                # 移动位置
                self.textedit.move(bottomRight_x, bottomRight_y + 5)
                self.okButton.move(bottomRight_x + self.textedit.width() + 2, bottomRight_y + 5)

                self.textedit.setFocus()
                self.drawFlag = False
                self.textedit.show()
                self.okButton.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    '''
    绘制全屏截图作为背景
    '''

    def paintBackgroundImage(self):
        self.painter.drawPixmap(0, 0, self.fullScreenImage)

    '''
    绘图事件
    '''

    def paintEvent(self, event):
        self.painter.begin(self)  # 开始重绘
        self.paintBackgroundImage()
        penColor = QColor(30, 144, 245)  # 画笔颜色
        self.painter.setPen(QPen(penColor, 2, Qt.SolidLine, Qt.RoundCap))  # 设置画笔,蓝色,1px大小,实线,圆形笔帽
        if self.isMousePressLeft is True:
            pickRect = self.getRectangle(self.beginPosition, self.endPosition)  # 获得要截图的矩形框
            self.captureImage = self.fullScreenImage.copy(pickRect)  # 捕获截图矩形框内的图片
            self.painter.drawRect(pickRect)  # 画矩形边框
        self.painter.end()  # 结束重绘

    '''
    获取框选区域的截图
    '''

    def getRectangle(self, beginPoint, endPoint):
        pickRectWidth = int(qAbs(beginPoint.x() - endPoint.x()))
        pickRectHeight = int(qAbs(beginPoint.y() - endPoint.y()))
        pickRectTop = beginPoint.x() if beginPoint.x() < endPoint.x() else endPoint.x()
        pickRectLeft = beginPoint.y() if beginPoint.y() < endPoint.y() else endPoint.y()
        pickRect = QRect(pickRectTop, pickRectLeft, pickRectWidth, pickRectHeight)
        # 避免高度宽度为0时候报错
        if pickRectWidth == 0:
            pickRect.setWidth(2)
        if pickRectHeight == 0:
            pickRect.setHeight(2)

        return pickRect

    '''
    发送截图的base64数据
    '''

    def sendImage(self):
        # 发送截图尺寸到信号signal2中
        width = self.captureImage.size().width()
        height = self.captureImage.size().height()
        self.signal2.emit(width, height)

        # 控制截图尺寸
        if width > self.maxWidth:
            self.captureImage = self.captureImage.scaledToWidth(self.maxWidth, Qt.SmoothTransformation)
        elif height > 700:
            self.captureImage = self.captureImage.scaled(QSize(int(width * 700 / height), 700), Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation)

        # 转为base64
        data = QtCore.QByteArray()
        buf = QtCore.QBuffer(data)
        self.captureImage.save(buf, "PNG")
        str1 = data.toBase64()
        imageBase64 = str(str1, encoding="utf-8")

        # 发送图片数据到信号signal中
        self.signal.emit(imageBase64)

    @property
    def signal(self):
        return self._speak

    @property
    def signal2(self):
        return self._size


if __name__ == "__main__":
    keyboard.wait(hotkey='f4')  # 按F4开始截图
    app = QApplication(sys.argv)
    windows = CaptureScreen()
    windows.show()
    sys.exit(app.exec())
