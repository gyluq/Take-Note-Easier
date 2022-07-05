import base64
import os
import time
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QTextEdit


class TextEdit(QTextEdit):
    insertImgSuccessSignel = Signal()

    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.pop = None

    def canInsertFromMimeData(self, source):
        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def createMimeDataFromSelection(self):
        cursor = self.textCursor()
        if len(cursor.selectedText()) == 1:
            cursor.setPosition(cursor.selectionEnd())
            fmt = cursor.charFormat()
            if fmt.isImageFormat():
                url = QtCore.QUrl(fmt.property(fmt.ImageName))
                print(url)
                image = self.document().resource(QtGui.QTextDocument.ImageResource, url)
                mime = QtCore.QMimeData()
                mime.setImageData(image)
                return mime
        return super().createMimeDataFromSelection()

    def insertImage(self, image, flag=False, picWidth=None):
        if image.isNull():
            return False

        # 图片保存到TempImg文件夹
        if not os.path.exists("TempImg"):
            os.mkdir("TempImg")
        fileName = f"{int(time.time() * 1000 // 1)}.png"
        success = image.save(f"TempImg/{fileName}")

        # 检测剪切板得到的图片插入末尾
        cursor = self.textCursor()
        if flag:
            cursor.movePosition(QTextCursor.End)
            self.setTextCursor(cursor)

        if picWidth is None:
            picWidth = self.width() - 20
        width = image.width()
        if success:
            print("实际:", self.width())
            filePath = os.path.join(os.getcwd(), 'TempImg', fileName)
            with open(filePath, 'rb') as file:
                imageData = str(base64.b64encode(file.read()), encoding="utf-8")
            if width > picWidth:
                HTMLBin = f"<img src=\"data:image/png;base64,{imageData}\" width='{picWidth}'/>"
            else:
                HTMLBin = f"<img src=\"data:image/png;base64,{imageData}\"/>"
            self.textCursor().insertHtml(HTMLBin)
            self.textCursor().insertHtml("<br/>")
            cursor.movePosition(QTextCursor.End)
            self.setTextCursor(cursor)
            self.insertImgSuccessSignel.emit()
            return True
        return False

    def insertFromMimeData(self, source):
        if source.hasImage() and self.insertImage(source.imageData()):
            return
        elif source.hasUrls():
            for url in source.urls():
                if not url.isLocalFile():
                    continue
                path = url.toLocalFile()
                info = QtCore.QFileInfo(path)
                if not info.suffix().lower() in ['jpg', 'png', 'bmp', 'gif', 'jpeg']:
                    continue
                elif self.insertImage(QtGui.QImage(path)):
                    return
        # 自写,使复制的文本不带格式
        mime = QtCore.QMimeData()
        mime.setText(source.text())
        super().insertFromMimeData(mime)
