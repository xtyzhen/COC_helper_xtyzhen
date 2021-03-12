# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:15:55 2021

@author: XTian
"""
import random
import pyautogui
for i in range(1,24):
    
    photo='./troops/'+str(i)+'.png'
    alllocation=pyautogui.locateAllOnScreen(photo, confidence=0.9, grayscale=False)
    for t in alllocation:
        print('found')
        print(t)
        Center=pyautogui.center(t)
        rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            print('没有库存，不捐赠')
        else:
            print('Yes!!')

# import time
# import win32api,win32con
# def slip():
#     win32api.keybd_event(65,0,0,0)     # enter
#     time.sleep(0.1)
#     win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
#     time.sleep(0.5)

# time.sleep(2)
# slip()
# slip()
# slip()
# slip()
