import time
import adb
import operator

第一关 = (615, 314)
第二关 = (1071, 751)
第三关 = (968, 604)
第四关 = (1321, 472)
第五关 = (1764, 612)
第六关 = (1538, 233)

删除英雄 = (2159,106)
选择英雄 = (501,520)
坦克 = (493,64)
苏烈 = (737, 424)
射手 = (1569,64)
鲁班 = (1796,233)
辅助 = (1826, 64)
蔡文姬 = (370,218)

自动 = (1730, 960)
远征商店 = ((627, 970), (255, 255, 255))

挑战 = ((1620, 919), (255, 255, 255))
确认 = ((2128, 1005), (255, 255, 255))
继续1 = ((1857, 983), (255, 255, 255))
继续2 = ((1158, 1000), (255, 255, 255))
金币确认 = ((1191, 863), (255, 255, 255))


def del_hero():
    for i in range(3):
        adb.tap(删除英雄)
        time.sleep(0.5)


def select_hero():
    adb.tap(选择英雄)
    time.sleep(0.5)
    adb.tap(坦克)
    time.sleep(0.5)
    adb.tap(苏烈)
    time.sleep(0.5)
    adb.tap(射手)
    time.sleep(0.5)
    adb.tap(鲁班)
    time.sleep(0.5)
    adb.tap(坦克)
    time.sleep(0.5)
    adb.tap(辅助)
    time.sleep(0.5)
    adb.tap(蔡文姬)
    time.sleep(0.5)


def first_step():
    adb.tap(第一关)
    time.sleep(0.5)
    adb.tap(挑战[0])
    time.sleep(0.5)
    del_hero()
    select_hero()
    adb.tap(确认[0])
    time.sleep(50)
    adb.tap(确认[0])
    time.sleep(0.5)
    adb.tap(继续1[0])
    time.sleep(0.5)
    adb.tap(继续2[0])
    time.sleep(0.5)
    adb.tap(自动)


def select_level():
    adb.tap(第二关)
    adb.tap(第三关)
    adb.tap(第四关)
    adb.tap(第五关)
    adb.tap(第六关)


if __name__ == '__main__':
    first_step()
    while True:
        image = adb.crap_and_get()
        if operator.eq(image.getpixel(挑战[0]), 挑战[1]):
            adb.tap(挑战[0])
        if operator.eq(image.getpixel(确认[0]), 确认[1]):
            adb.tap(确认[0])
        if operator.eq(image.getpixel(继续1[0]), 继续1[1]):
            adb.tap(继续1[0])
        if operator.eq(image.getpixel(继续2[0]), 继续2[1]):
            adb.tap(继续2[0])
        if operator.eq(image.getpixel(金币确认[0]), 金币确认[1]):
            adb.tap(金币确认[0])
            time.sleep(0.5)
        if operator.eq(image.getpixel(远征商店[0]), 远征商店[1]):
            select_level()
        adb.tap(第一关)




