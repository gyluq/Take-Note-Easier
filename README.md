# 笔记工具
适用于笔记软件mybase8.0的记笔记工具，可边看视频边记笔记
- 背景透明、可固定在桌面
- F3截图，截图时隐藏窗体
- 检测剪切板功能，支持文本和单张图片(图片会转换为base64格式)

# 环境
| 环境      | 版本 |
| :---        |    :----:   |
| Python      | 3.9.13       |
| pywin32   | 306        |
| system-hotkey   | 1.0.3        |
| Nuitka   | 1.1        |
| pyside6   | 6.5       |

# 打包
使用nuitka打包：
```
nuitka --windows-disable-console --standalone --show-progress --follow-imports --plugin-enable=pyside6 --output-dir=out --windows-icon-from-ico=passion.ico Main.py
```
完成后须将configuration.ini文件放到out/Main.dist目录下

# 工具界面
![image](https://user-images.githubusercontent.com/57351717/233840177-1f345111-f306-49aa-880e-f9edf00f50ff.png)
# 截图界面
![image](https://user-images.githubusercontent.com/57351717/233842828-18b4c7cc-fe2a-49c4-a45d-d7b70b9fca17.png)
