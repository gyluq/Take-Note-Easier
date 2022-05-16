from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QTextEdit


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)

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

    def insertImage(self, image):
        if image.isNull():
            return False
        width = image.width()
        ba = QtCore.QByteArray()
        buffer = QtCore.QBuffer(ba)
        image.save(buffer, 'PNG', quality=95)
        imgData = str(ba.toBase64(), encoding="utf-8")
        if width > 280:
            HTMLBin = f"<img src=\"data:image/png;base64,{imgData}\" width='280'/>\n"
        else:
            HTMLBin = f"<img src=\"data:image/png;base64,{imgData}\"/>\n"
        self.textCursor().insertHtml(HTMLBin)
        self.setTextCursor(self.textCursor())
        return True

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
        super().insertFromMimeData(source)

