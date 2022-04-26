from PySide6.QtCore import Qt, QRect, Signal, QSize, QByteArray, QBuffer, QPointF
from PySide6.QtGui import QPen, QPainter, QColor, QGuiApplication, QIcon
from PySide6.QtWidgets import QMainWindow, QTextEdit, QPushButton
import img_rc


class CaptureScreen(QMainWindow):
    signal_picAndNote = Signal(str, str)  # 发送截图和笔记
    signal_size = Signal(int, int)  # 发送截图尺寸
    signal_close = Signal()  # 发送截图尺寸

    clickPosition = None  # 点击位置
    releasePosition = None  # 释放位置
    TLPosition = None  # 截图左上角位置
    BRPosition = None  # 截图右下角位置

    # 用于整体移动
    TLPosition_copy = None
    BRPosition_copy = None

    fullScreenImage = None  # 全屏截图
    captureImage = None  # 捕捉的截图
    painter = QPainter()  # 刷子

    leftMousePressFlag = None
    drawFlag = False  # 鼠标移动才更新edit和button的位置
    totalMoveFlag = False
    borderMoveFlag = {"left": 0, "right": 0, "bottom": 0, "top": 0, "top-left": 0,
                      "top-right": 0, "bottom-left": 0, "bottom-right": 0}

    def __init__(self, maxWidth):
        super().__init__()
        self.initWindow()
        self.captureFullScreen()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.maxWidth = maxWidth

        # 实时笔记窗口
        backgroundColor = "255, 208, 115, 60"
        self.textedit = QTextEdit(self)
        self.textedit.setPlaceholderText("记些什么...")
        self.textedit.setStyleSheet(
            f"background-color:rgba({backgroundColor});border-radius:4px;font-size:13px;margin:0;padding:0;color:white;")
        self.textedit.hide()
        # 确认按钮
        self.okButton = QPushButton(QIcon(":/icons/icons/yes3.png"), "", self)
        self.okButton.setIconSize(QSize(20, 20))
        self.okButton.setStyleSheet(
            f"background-repeat:none;background-position:center;background-color:rgba({backgroundColor});"
            "border:#FFFFFF;border-radius:4px;margin:0;padding:0;")
        self.okButton.setCursor(Qt.PointingHandCursor)
        self.okButton.setMaximumWidth(30)
        self.okButton.setMinimumWidth(30)
        self.okButton.setMaximumHeight(30)
        self.okButton.setMinimumHeight(30)
        self.okButton.hide()
        self.okButton.clicked.connect(self.saveNote)

        # 保存由点位置转换得到的边位置
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

    def initWindow(self):
        self.setMouseTracking(True)
        self.setCursor(Qt.CrossCursor)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowFullScreen)

    def captureFullScreen(self):
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(0)

    def saveNote(self):
        self.sendImageAndNote()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 实时记录点击位置
            self.clickPosition = event.position()
            self.leftMousePressFlag = True

            # 判断进行的操作
            if self.captureImage is not None:
                self.refreshBorderLocation()
                self.TLPosition_copy = self.TLPosition
                self.BRPosition_copy = self.BRPosition
                # 整体移动
                if self.left + 9 < event.x() < self.right - 9 and self.top + 9 < event.y() < self.bottom - 9:
                    self.totalMoveFlag = True
                    return
                # 拖动边框调整尺寸
                else:
                    # 左右
                    if self.left - 9 < event.x() < self.left + 9 and self.top + 9 < event.y() < self.bottom - 9:
                        self.borderMoveFlag["left"] = 1
                        return
                    if self.right - 9 < event.x() < self.right + 9 and self.top + 9 < event.y() < self.bottom - 9:
                        self.borderMoveFlag["right"] = 1
                        return
                    # 上下
                    if self.top - 9 < event.y() < self.top + 9 and self.left + 9 < event.x() < self.right - 9:
                        self.borderMoveFlag["top"] = 1
                        return
                    if self.bottom - 9 < event.y() < self.bottom + 9 and self.left + 9 < event.x() < self.right - 9:
                        self.borderMoveFlag["bottom"] = 1
                        return
                    # 顶点(1,4)
                    if self.top - 9 < event.y() < self.top + 9 and self.left - 9 < event.x() < self.left + 9:
                        self.borderMoveFlag["top-left"] = 1
                        return
                    if self.bottom - 9 < event.y() < self.bottom + 9 and self.right - 9 < event.x() < self.right + 9:
                        self.borderMoveFlag["bottom-right"] = 1
                        return
                    # 顶点(2,3)
                    if self.top - 9 < event.y() < self.top + 9 and self.right - 9 < event.x() < self.right + 9:
                        self.borderMoveFlag["top-right"] = 1
                        return
                    if self.bottom - 9 < event.y() < self.bottom + 9 and self.left - 9 < event.x() < self.left + 9:
                        self.borderMoveFlag["bottom-left"] = 1
                        return
            # 截图操作
            self.TLPosition = event.position()
        elif event.button() == Qt.RightButton:
            self.signal_close.emit()
            self.close()

    def mouseMoveEvent(self, event):
        # 按下鼠标开始截图
        if self.leftMousePressFlag is True:
            # 移动时隐藏文本框和按钮
            self.textedit.hide()
            self.okButton.hide()
            # 防止单纯的点击事件重置截图
            self.drawFlag = True

            # 整体移动
            if self.totalMoveFlag:
                self.TLPosition = QPointF(self.TLPosition_copy.x() + event.x() - self.clickPosition.x(),
                                          self.TLPosition_copy.y() + event.y() - self.clickPosition.y())
                self.BRPosition = QPointF(self.BRPosition_copy.x() + event.x() - self.clickPosition.x(),
                                          self.BRPosition_copy.y() + event.y() - self.clickPosition.y())
                # 边界范围
                if self.TLPosition.x() <= 0:
                    self.TLPosition.setX(1)
                    self.BRPosition.setX(abs(self.BRPosition_copy.x() - self.TLPosition_copy.x()))
                if self.TLPosition.y() <= 0:
                    self.TLPosition.setY(1)
                    self.BRPosition.setY(abs(self.BRPosition_copy.y() - self.TLPosition_copy.y()))
                if self.BRPosition.x() >= 1919:
                    self.BRPosition.setX(1919)
                    self.TLPosition.setX(1919 - abs(self.BRPosition_copy.x() - self.TLPosition_copy.x()))
                if self.BRPosition.y() >= 1079:
                    self.BRPosition.setY(1079)
                    self.TLPosition.setY(1079 - abs(self.BRPosition_copy.y() - self.TLPosition_copy.y()))
                self.update()
                return
            else:
                if self.borderMoveFlag["left"]:
                    if self.BRPosition.x() < self.TLPosition.x():
                        self.BRPosition.setX(event.x())
                    else:
                        self.TLPosition.setX(event.x())
                    self.update()
                    return
                if self.borderMoveFlag["right"]:
                    if self.BRPosition.x() > self.TLPosition.x():
                        self.BRPosition.setX(event.x())
                    else:
                        self.TLPosition.setX(event.x())
                    self.update()
                    return
                if self.borderMoveFlag["top"]:
                    if self.BRPosition.y() < self.TLPosition.y():
                        self.BRPosition.setY(event.y())
                    else:
                        self.TLPosition.setY(event.y())
                    self.update()
                    return
                if self.borderMoveFlag["bottom"]:
                    if self.BRPosition.y() > self.TLPosition.y():
                        self.BRPosition.setY(event.y())
                    else:
                        self.TLPosition.setY(event.y())
                    self.update()
                    return
                if self.borderMoveFlag["top-left"]:
                    if self.BRPosition.x() < self.TLPosition.x():
                        self.BRPosition.setX(event.x())
                        self.BRPosition.setY(event.y())
                    else:
                        self.TLPosition.setY(event.y())
                        self.TLPosition.setX(event.x())
                    self.update()
                    return
                if self.borderMoveFlag["top-right"]:
                    if self.BRPosition.x() < self.TLPosition.x():
                        self.BRPosition.setY(event.y())
                        self.TLPosition.setX(event.x())
                    else:
                        self.TLPosition.setY(event.y())
                        self.BRPosition.setX(event.x())
                    self.update()
                    return
                if self.borderMoveFlag["bottom-right"]:
                    if self.BRPosition.x() > self.TLPosition.x():
                        self.BRPosition.setY(event.y())
                        self.BRPosition.setX(event.x())
                    else:
                        self.TLPosition.setY(event.y())
                        self.TLPosition.setX(event.x())
                    self.update()
                    return
                if self.borderMoveFlag["bottom-left"]:
                    if self.BRPosition.x() < self.TLPosition.x():
                        self.BRPosition.setX(event.x())
                        self.TLPosition.setY(event.y())
                    else:
                        self.BRPosition.setY(event.y())
                        self.TLPosition.setX(event.x())
                    self.update()
                    return
            self.BRPosition = event.position()
            self.update()
        # 设置各区域光标样式
        elif self.captureImage is not None:
            self.refreshBorderLocation()
            # 左右
            if self.left - 9 < event.x() < self.left + 9 and self.top + 9 < event.y() < self.bottom - 9:
                self.setCursor(Qt.SizeHorCursor)
            elif self.right - 9 < event.x() < self.right + 9 and self.top + 9 < event.y() < self.bottom - 9:
                self.setCursor(Qt.SizeHorCursor)
            # 上下
            elif self.top - 9 < event.y() < self.top + 9 and self.left + 9 < event.x() < self.right - 9:
                self.setCursor(Qt.SizeVerCursor)
            elif self.bottom - 9 < event.y() < self.bottom + 9 and self.left + 9 < event.x() < self.right - 9:
                self.setCursor(Qt.SizeVerCursor)
            # 顶点(1,4)
            elif self.top - 9 < event.y() < self.top + 9 and self.left - 9 < event.x() < self.left + 9 or \
                    self.bottom - 9 < event.y() < self.bottom + 9 and self.right - 9 < event.x() < self.right + 9:
                self.setCursor(Qt.SizeFDiagCursor)
            # 顶点(2,3)
            elif self.top - 9 < event.y() < self.top + 9 and self.right - 9 < event.x() < self.right + 9 or \
                    self.bottom - 9 < event.y() < self.bottom + 9 and self.left - 9 < event.x() < self.left + 9:
                self.setCursor(Qt.SizeBDiagCursor)
            # 中心
            elif self.left + 9 < event.x() < self.right - 9 and self.top + 9 < event.y() < self.bottom - 9:
                self.setCursor(Qt.SizeAllCursor)
            # 其他位置
            else:
                self.setCursor(Qt.ArrowCursor)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftMousePressFlag = False
            self.releasePosition = event.position()
            if self.captureImage is not None and self.drawFlag:
                # 重新截图时才清空textedit
                if not self.totalMoveFlag and 1 not in self.borderMoveFlag.values():
                    self.textedit.clear()
                # 左下角的坐标
                bottomRight_x = min(self.TLPosition.x(), self.BRPosition.x())
                bottomRight_y = max(self.TLPosition.y(), self.BRPosition.y())

                # 设置文本框的尺寸
                selectWidth = abs(self.TLPosition.x() - self.BRPosition.x())
                if selectWidth < 300:  # 最小不得小于300px
                    self.textedit.setMinimumWidth(300)
                    self.textedit.setMaximumWidth(300)
                else:
                    self.textedit.setMinimumWidth(selectWidth - self.okButton.width() - 10)
                    self.textedit.setMaximumWidth(selectWidth - self.okButton.width() - 10)
                self.textedit.setMinimumHeight(30)
                self.textedit.setMaximumHeight(30)

                # 移动笔记框和按钮位置
                if bottomRight_y < 1030:
                    self.textedit.move(bottomRight_x + 3, bottomRight_y + 5)
                    self.okButton.move(bottomRight_x + self.textedit.width() + 5, bottomRight_y + 5)
                else:
                    self.textedit.move(bottomRight_x + 3, bottomRight_y - 35)
                    self.okButton.move(bottomRight_x + self.textedit.width() + 5, bottomRight_y - 35)
                # 笔记框获得焦点
                self.textedit.setFocus()
                self.drawFlag = False
                self.textedit.show()
                self.okButton.show()
            self.totalMoveFlag = False
            self.refreshFlags()  # 重置边框移动flag

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def paintBackgroundImage(self):
        """
        绘制全屏截图作为背景
        """
        shadowColor = QColor(171, 190, 234, 50)
        # 绘制全屏截图
        self.painter.drawPixmap(0, 0, self.fullScreenImage)
        # 绘制遮罩层
        self.painter.fillRect(self.fullScreenImage.rect(), shadowColor)

    def paintEvent(self, event):
        self.painter.begin(self)  # 开始重绘
        self.paintBackgroundImage()
        # 因未知原因,拖动释放鼠标时会产生update事件,调用paintEvent方法.此时leftMousePressFlag变为False,仅仅绘制了背景,没有绘制矩形框
        # 因此需要添加另一个条件self.captureImage is not None
        if self.leftMousePressFlag is True or self.captureImage is not None:
            # 获得要截图的矩形框
            pickRect = self.getRectangle()
            # 捕获截图矩形框内的图片
            self.captureImage = self.fullScreenImage.copy(pickRect)
            # 填充截取的区域
            self.painter.drawPixmap(pickRect.topLeft(), self.captureImage)
            # 绘制顶点
            penColor = QColor(255, 159, 0)  # 画笔颜色
            self.painter.fillRect(QRect(self.left - 3, self.top - 3, 6, 6), penColor)
            self.painter.fillRect(QRect(self.left - 3, self.bottom - 3, 6, 6), penColor)
            self.painter.fillRect(QRect(self.right - 3, self.top - 3, 6, 6), penColor)
            self.painter.fillRect(QRect(self.right - 3, self.bottom - 3, 6, 6), penColor)
            # 画矩形边框
            self.painter.setPen(QPen(QColor(255, 202, 115), 2, Qt.SolidLine, Qt.RoundCap))
            self.painter.drawRect(pickRect)
        # 结束重绘
        self.painter.end()

    def getRectangle(self):
        """
        获取框选区域的截图
        """
        self.refreshBorderLocation()
        pickRectWidth = self.right - self.left
        pickRectHeight = self.bottom - self.top
        pickRect = QRect(self.left, self.top, pickRectWidth, pickRectHeight)
        # 避免高度宽度为0时候报错
        if pickRectWidth == 0:
            pickRect.setWidth(2)
        if pickRectHeight == 0:
            pickRect.setHeight(2)
        return pickRect

    def refreshBorderLocation(self):
        """
        刷新边界位置
        """
        self.left = min(self.TLPosition.x(), self.BRPosition.x())
        self.right = max(self.TLPosition.x(), self.BRPosition.x())
        self.top = min(self.TLPosition.y(), self.BRPosition.y())
        self.bottom = max(self.TLPosition.y(), self.BRPosition.y())

    def refreshFlags(self):
        self.borderMoveFlag = {"left": 0, "right": 0, "bottom": 0, "top": 0, "top-left": 0,
                               "top-right": 0, "bottom-left": 0, "bottom-right": 0}

    def sendImageAndNote(self):
        """
        发送截图的base64数据
        """
        # 发送截图尺寸到信号signal2中
        width = self.captureImage.size().width()
        height = self.captureImage.size().height()
        self.signal_size.emit(width, height)
        # 控制截图尺寸
        if width > self.maxWidth:
            self.captureImage = self.captureImage.scaledToWidth(self.maxWidth, Qt.SmoothTransformation)
        # 转为base64
        data = QByteArray()
        buf = QBuffer(data)
        self.captureImage.save(buf, "PNG")
        str1 = data.toBase64()
        imageBase64 = str(str1, encoding="utf-8")
        # 发送图片数据到信号signal中
        self.signal_picAndNote.emit(imageBase64, self.textedit.toPlainText())
        self.signal_close.emit()
