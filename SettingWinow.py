from PySide6.QtCore import (QSettings, Signal, Qt)
from PySide6.QtWidgets import (QWidget, QApplication, QColorDialog)

from UI.ui_setting import Ui_Form


class Setting(QWidget):
    signal = Signal()

    def __init__(self):
        super(Setting, self).__init__(None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initialization()

    def initialization(self):
        # 配置文件
        self.setting = QSettings("configuration.ini", QSettings.IniFormat)
        # 初始化comboBox
        self.ui.comboBox.addItems(self.setting.value("OPTION/COMBOBOX_ITEM"))
        self.ui.comboBox.setCurrentText(self.setting.value("LAST_OPTION/LAST_SIZE"))
        # 读取配置文件
        mainwindow_bar = self.setting.value("UI/MAINWINDOW_BAR")
        mainwindow_note = self.setting.value("UI/MAINWINDOW_NOTE")
        screen_mask = self.setting.value("UI/SCREEN_MASK")
        screen_vertex = self.setting.value("UI/SCREEN_VERTEX")
        screen_border = self.setting.value("UI/SCREEN_BORDER")
        self.ui.Color_mainwindow.setText(mainwindow_bar)
        self.ui.Color_textedit.setText(mainwindow_note)
        self.ui.Color_mask.setText(screen_mask)
        self.ui.Color_border.setText(screen_border)
        self.ui.Color_dot.setText(screen_vertex)
        # 绑定按钮点击事件
        self.ui.Color_mainwindow.clicked.connect(lambda x: self.changeColor(self.ui.Color_mainwindow))
        self.ui.Color_textedit.clicked.connect(lambda x: self.changeColor(self.ui.Color_textedit))
        self.ui.Color_mask.clicked.connect(lambda x: self.changeColor(self.ui.Color_mask))
        self.ui.Color_border.clicked.connect(lambda x: self.changeColor(self.ui.Color_border))
        self.ui.Color_dot.clicked.connect(lambda x: self.changeColor(self.ui.Color_dot))
        self.ui.Button_apply.clicked.connect(self.apply)

    def changeColor(self, widget):
        col = QColorDialog(self)
        color = col.getColor()
        if color.isValid():
            widget.setStyleSheet(f'background-color:{color.name()}')
            widget.setText(color.name())

    def apply(self):
        # 应用设置，写回配置文件
        self.setting.setValue("UI/MAINWINDOW_BAR", self.ui.Color_mainwindow.text())
        self.setting.setValue("UI/MAINWINDOW_NOTE", self.ui.Color_textedit.text())
        self.setting.setValue("UI/SCREEN_MASK", self.ui.Color_mask.text())
        self.setting.setValue("UI/SCREEN_BORDER", self.ui.Color_border.text())
        self.setting.setValue("UI/SCREEN_VERTEX", self.ui.Color_dot.text())

        currentSize = self.ui.comboBox.currentText()
        self.setting.setValue("LAST_OPTION/LAST_SIZE", currentSize)
        self.signal.emit()


if __name__ == '__main__':
    app = QApplication()
    a = Setting()
    app.exec()
