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
        if width > 287:
            HTMLBin = f"<p style=\" margin-top:3px; margin-bottom:0px; margin-left:0px; margin-right:0px;" \
                      f" -qt-block-indent:0; text-indent:0px;\">" \
                      f"<img src=\"data:image/png;base64,{imgData}\" width='287'/></p>"
        else:
            HTMLBin = f"<p style=\" margin-top:3px; margin-bottom:0px; margin-left:0px; margin-right:0px;" \
                      f" -qt-block-indent:0; text-indent:0px;\">" \
                      f"<img src=\"data:image/png;base64,{imgData}\"/></p>"
        self.textCursor().insertHtml(HTMLBin)
        # self.textCursor().insertHtml("<p><span style=\" font-size:6pt;\">.</span></p>")
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

