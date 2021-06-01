import time
import adb
import operator

挑战1 = ((1129, 746), (255, 255, 255))
# 挑战1 = ((1124, 752), (255, 255, 255))
# 挑战1 = ((1735, 753), (255, 255, 255))
挑战2 = ((1414, 443), (251, 243, 221))
确认 = ((2128, 1005), (255, 255, 255))
继续1 = ((1857, 983), (255, 255, 255))
继续2 = ((1158, 1000), (255, 255, 255))


if __name__ == "__main__":
    count = 0
    while True:
        image = adb.crap_and_get()
        if operator.eq(image.getpixel(挑战1[0]), 挑战1[1]):
            adb.tap(挑战1[0])
        if operator.eq(image.getpixel(挑战2[0]), 挑战2[1]):
            adb.tap(挑战2[0])
        if operator.eq(image.getpixel(确认[0]), 确认[1]):
            adb.tap(确认[0])
            time.sleep(30)
            count += 1
        if operator.eq(image.getpixel(继续1[0]), 继续1[1]):
            adb.tap(继续1[0])
        if operator.eq(image.getpixel(继续2[0]), 继续2[1]):
            adb.tap(继续2[0])
        adb.tap(挑战2[0])
        if count >= 10:
            break