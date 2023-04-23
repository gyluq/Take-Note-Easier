适用于笔记软件mybase8.0的记笔记工具，可边看视频边记笔记
- 背景透明、可固定在桌面
- F3截图，截图时隐藏窗体
- 检测剪切板功能，支持文本和单张图片

须自行打包：
```
nuitka --windows-disable-console --standalone --show-progress --follow-imports --plugin-enable=pyside6 --output-dir=out --windows-icon-from-ico=passion.ico Main.py
```


![image](https://user-images.githubusercontent.com/57351717/233840177-1f345111-f306-49aa-880e-f9edf00f50ff.png)
