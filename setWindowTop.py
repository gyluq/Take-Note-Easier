import win32api
import win32con
import win32gui
import win32process

'''
没有用到
'''


class setWindowTopOrNot:
    hwnd_list = {}

    def __init__(self):
        self.hwnd_list = self.get_hwnd()
        print(self.get_hwnd())

    def get_hwnd_dict(self, hwnd, hwnd_title):  # 获取所有窗口的名称
        if (win32gui.IsWindow(hwnd)
                and win32gui.IsWindowEnabled(hwnd)
                and win32gui.IsWindowVisible(hwnd)
                and win32gui.GetWindowText(hwnd)):
            hwnd_title[f"{hwnd}"] = win32gui.GetWindowText(hwnd)

    def get_hwnd(self):  # 获取所有窗口的句柄与名称
        hwnd_title = {}
        win32gui.EnumWindows(self.get_hwnd_dict, hwnd_title)
        return hwnd_title

    '''
    windowName:需要置顶窗口的名称
    flag:True则置顶,False取消置顶
    '''

    def setWindowTop(self, windowName, flag):
        for i, j in self.hwnd_list.items():
            if windowName in j:
                dwForeID = win32process.GetWindowThreadProcessId(i)
                dwCurId = win32api.GetCurrentThreadId()
                win32process.AttachThreadInput(dwForeID[0], dwCurId, 1)
                if flag:
                    win32gui.SetWindowPos(i, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                else:
                    win32gui.SetWindowPos(i, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                break


if __name__ == "__main__":
    a = setWindowTopOrNot()
    a.setWindowTop("Chrome", False)
