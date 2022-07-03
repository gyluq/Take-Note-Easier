from PySide6.QtCore import Qt


class DragToMove:
    def setUp(self, widget, parent):
        self.widget = widget
        self.parent = parent
        self.parent.leftMouseClickFlag = False
        self.widget.mousePressEvent = lambda e: self.titleFramePress(e)
        self.widget.mouseMoveEvent = lambda e: self.titleFrameMove(e)
        self.widget.mouseReleaseEvent = lambda e: self.titleFrameRelease()

    def titleFramePress(self, event):
        if event.button() == Qt.LeftButton:
            self.parent.leftMouseClickFlag = True
            self.parent.clickPosition = event.position().toPoint()

    def titleFrameMove(self, event):
        if self.parent.leftMouseClickFlag:
            self.parent.move(event.globalPosition().toPoint() - self.parent.clickPosition)

    def titleFrameRelease(self):
        self.parent.leftMouseClickFlag = False
