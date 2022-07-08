import base64
import os
import re
import time

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtGui import QTextCursor, QColor, QTextFormat
from PySide6.QtWidgets import QTextEdit


class TextEdit(QTextEdit):
    insertImgSuccessSignel = Signal()

    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.pop = None
        self.cursorPositionChanged.connect(self.highlight_current_line)

    @Slot()
    def highlight_current_line(self):
        extra_selections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor("#2F2F40")
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)

    def canInsertFromMimeData(self, source):
        """
        添加支持的资源类型
        :param source:
        :return:
        """
        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def createMimeDataFromSelection(self):
        """
        将选中的一张图片包装为mimeData
        :return:
        """
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
        """
        插入图片
        :param image: 图片
        :param flag: 图片是否由检测剪切板功能自动获取,用来判断是否将光标置于末尾
        :param picWidth: 图片显示宽度
        :return: boolean
        """
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
        """
        粘贴或调用特定函数时调用
        :param source: 图片或文本
        """
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

    def keyPressEvent(self, event):
        """
        增强换行和删除键的功能
        :param event: 按钮事件
        """
        # 保留前一行开头空格数
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # 获取当前行文本
            cursors = self.textCursor()
            cursors.select(QTextCursor.BlockUnderCursor)
            s = cursors.selectedText()
            # 匹配开头空字符
            re_space = re.compile(r'^\s+')
            match = re_space.search(s)
            # 有匹配项
            if match:
                additionSpace = match.group(0)
                cursors.movePosition(QTextCursor.EndOfLine)
                super(TextEdit, self).keyPressEvent(event)
                # 8233为段分隔符,另外ord()获取字符的ASCLL码
                if additionSpace[0] == chr(8233):
                    additionSpace = additionSpace[1:]
                cursors.insertText(additionSpace)
            else:
                # 出现异常表示开头不是空字符,直接换行
                super(TextEdit, self).keyPressEvent(event)
        # 整行都是空字符则删除整行
        elif event.key() == Qt.Key_Backspace:
            cursors = self.textCursor()
            cursors.select(QTextCursor.LineUnderCursor)
            s = cursors.selectedText()
            # 匹配全空字符
            space = re.compile(r'^\s+$')
            match = space.search(s)
            if match:
                cursors.select(QTextCursor.LineUnderCursor)
                cursors.removeSelectedText()
            else:
                super(TextEdit, self).keyPressEvent(event)
        # 增强Home键
        elif event.key() == Qt.Key_Home:
            cursors = self.textCursor()
            cursors.select(QTextCursor.LineUnderCursor)
            s = cursors.selectedText()
            # 匹配开头空格字符
            space = re.compile(r'^\s+')
            match = space.search(s)
            if match:
                cursors.movePosition(QTextCursor.StartOfBlock)
                cursors.movePosition(QTextCursor.NextCharacter, n=len(match.group(0)))
                self.setTextCursor(cursors)
            else:
                super(TextEdit, self).keyPressEvent(event)
        # Ctrl+D复制当前行
        elif event.key() == Qt.Key_D and event.modifiers() == Qt.ControlModifier:
            cursors = self.textCursor()
            cursors.select(QTextCursor.BlockUnderCursor)
            s = cursors.selectedText()
            if s != "":
                cursors.movePosition(QTextCursor.EndOfBlock)
                if s[0] == chr(8233):
                    s = s[1:]
                cursors.insertText(f"\n{s}")
        # Ctrl+Y删除当前行
        elif event.key() == Qt.Key_Y and event.modifiers() == Qt.ControlModifier:
            cursors = self.textCursor()
            cursors.select(QTextCursor.BlockUnderCursor)
            cursors.removeSelectedText()
        # Alt+Q格式选择的文本
        elif event.key() == Qt.Key_Q and event.modifiers() == Qt.AltModifier:
            cursors = self.textCursor()
            s = cursors.selectedText()
            if s != "":
                cursors.removeSelectedText()
                s = s.replace("   ", " ").replace("  ", " ").replace("  ", " ")
                cursors.insertText(s)
        else:
            super(TextEdit, self).keyPressEvent(event)
