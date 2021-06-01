import os
import operator
from PIL import Image


#获取手机的截屏
def cap_screen():
    os.system("adb shell screencap -p /sdcard/01.png")
    os.system("adb pull /sdcard/01.png")

def click(p):
    os.system('adb shell input tap {} {}'.format(p[0], p[1]))

cap_screen()



