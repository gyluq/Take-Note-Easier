from system_hotkey import SystemHotkey
from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtCore import QObject, Signal


# 这里之所以继承QObject是因为要使用自定义信号(PySide6要求)
class c_demo(QWidget, QObject):
    # 定义一个热键信号
    sig_keyhot = Signal(str)

    def __init__(self, From):
        # 1. 简单的绘制一个窗口
        super().__init__(From)
        From.resize(100, 150)
        # 2. 设置我们的自定义热键响应函数
        self.sig_keyhot.connect(self.MKey_pressEvent)
        # 3. 初始化两个热键
        self.hk_start, self.hk_stop = SystemHotkey(), SystemHotkey()
        # 4. 绑定快捷键和对应的信号发送函数
        self.hk_start.register(('control', '1'), callback=lambda x: self.send_key_event("start"))
        self.hk_stop.register(('control', '2'), callback=lambda x: self.send_key_event("stop"))

    # 热键处理函数
    def MKey_pressEvent(self, i_str):
        print(f"按下的按键是{i_str}")
    # # 热键处理函数
    # def MKey_pressEvent(self, i_str):
    #     print(f"按下的按键是{i_str}")

    # 热键信号发送函数(将外部信号，转化成qt信号)
    def send_key_event(self, i_str):
        self.sig_keyhot.emit(i_str)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Dialog_main = QDialog()
    ui = c_demo(Dialog_main)
    Dialog_main.show()
    sys.exit(app.exec())
