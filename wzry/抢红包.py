import operator
import adb
import time

红包 = (1300, 97)
点击点 = (1198,151)
关闭 = (1245,797)
红包颜色 = (184, 71, 56)
count = 0

def main():
    image = adb.crap_and_get()
    if operator.eq(image.getpixel(红包), 红包颜色):
        adb.tap(点击点)
        time.sleep(0.5)
        adb.tap(关闭)



if __name__ == '__main__':
    while 1:
        main()
        time.sleep(0.2)
