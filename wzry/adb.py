from PIL import Image
import os


def crap_screen():
    os.system("adb shell screencap -p /sdcard/01.png")
    os.system("adb pull /sdcard/01.png ./112.png")

def tap(p):
    os.system("adb shell input tap {} {}".format(p[0], p[1]))

def get_image():
    image = Image.open("./112.png")
    return image.convert("RGB")

def crap_and_get():
    crap_screen()
    image = get_image()
    return image

