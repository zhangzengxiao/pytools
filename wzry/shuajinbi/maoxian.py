import win32con
import win32gui
import win32api
import time


current_gold = 0
gold_every_week = 4900
gold_every_time = 56

万象天工 = (1344, 769)
冒险玩法 = (238, 325)
挑战 = (934, 670)
下一步 = (1400, 890)
闯关 = (1445, 833)
点击继续 = (872, 518)
再次挑战 = (1510, 911)

def mouse_click(pos):
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def show_wzry():
    wzry = win32gui.FindWindow("TXGuiFoundation", "腾讯手游助手【极速傲引擎】")
    win32gui.SetForegroundWindow(wzry)

def get_gold():
    time.sleep(1)
    mouse_click(万象天工)
    time.sleep(1)
    mouse_click(冒险玩法)
    time.sleep(1)
    mouse_click(挑战)
    time.sleep(1)
    mouse_click(下一步)

    i = 1
    #循环刷
    while(i * gold_every_time < (gold_every_week - current_gold)):
        #点击闯关
        time.sleep(1)
        mouse_click(闯关)
        #等待刷完点击继续
        time.sleep(160)
        mouse_click(点击继续)
        #点击再次挑战
        time.sleep(2)
        mouse_click(再次挑战)
        print(i*gold_every_time)
        i +=1


if __name__ == '__main__':
    show_wzry()
    get_gold()