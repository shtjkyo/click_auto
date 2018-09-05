from pymouse import PyMouse
import time
import webbrowser
from pykeyboard import PyKeyboard

url = "http://xx.xx.xx.xx" #打开设备网址
webbrowser.open_new_tab(url)
m = PyMouse()
k = PyKeyboard()
m.move(73, 423)
time.sleep(10)
m.click(73, 423)
time.sleep(2)
m.move(670, 268)
m.click(670, 268)
time.sleep(5)
m.move(430, 21)
m.click(430, 21)

