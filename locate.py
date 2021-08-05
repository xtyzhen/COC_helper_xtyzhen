# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:40:03 2021

@author: XTian
"""
from threading import Thread
import pyautogui
import win32api,win32con
import time
import random
import sys
import keyboard
import requests



findt=[]
what={'1':'野蛮人','2':'弓箭手','3':'胖子','4':'哥布林','5':'炸弹人','6':'气球','7':'法师','8':'天使','9':'龙','10':'皮卡','11':'龙宝宝','12':'矿工','13':'电龙','14':'雪怪','15':'苍蝇','16':'野猪','17':'武神','18':'石头人','19':'女巫','20':'天狗','21':'投石手','22':'冰人','23':'英雄猎手','a':'雷电','b':'治疗','c':'狂暴','d':'弹跳','e':'冰冻','f':'复制','g':'隐身法术','h':'毒药','i':'地震','j':'疾速','k':'骷髅','l':'蝙蝠','G1':'攻城车','G2':'飞艇','G3':'大气球','G4':'训练营'}
def mistaken():
    time.sleep(1)
    try:
        print('*****循环跳过，本页无内容*****')
        #此处可添加异常服务通知
        print('——————————正常运行——————————')
    except:
        mistaken()

def aasync(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper

@aasync
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

@aasync
def findtroops(i,x):
    photo='./troops/'+str(i)+'.png'
    Part = pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=True,region=(x,0,763,1080))         # <class 'pyscreeze.Box'>
    if Part==None:
        #print('未识别到图片'+str(i)+what[str(i)])
        return 0
    Center=pyautogui.center(Part)
    rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
    if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
        #print('没有库存，不捐赠')
        return 0
    else:
        findt.append(i)

def autotrain(troops):
    time.sleep(1)
    Part=pyautogui.locateOnScreen('./others/close.png', confidence=0.8, grayscale=False)
    Center=pyautogui.center(Part)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并关闭聊天界面
    time.sleep(1)
    Part=pyautogui.locateOnScreen('./others/train.png', confidence=0.8, grayscale=False)
    Center=pyautogui.center(Part)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开训练界面
    time.sleep(1)
    last=None
    for t in troops:
        print('需要训练'+what[str(t)]+str(troops[t])+'个')
        if type(t)==int and type(t)!=type(last):
            print(str(t)+'开始训练军队'+what[str(t)]+str(troops[t])+'个')
            Part=pyautogui.locateOnScreen('./others/train_troops.png', confidence=0.8, grayscale=False)
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开造兵    
            time.sleep(0.5)
        else:
            if type(t)==str and t>='a' and (type(last)==type(None) or type(last)==int or (last<'a')): #type(t)==str
                print(str(t)+'开始配置法术'+what[str(t)]+str(troops[t])+'个')
                Part=pyautogui.locateOnScreen('./others/spells.png', confidence=0.8, grayscale=False)
                Center=pyautogui.center(Part)
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开造兵    
                time.sleep(0.5)
            else:
                if type(t)==str and t<'a' and (type(last)==type(None) or type(last)==int or last>='a'):
                    Part=pyautogui.locateOnScreen('./others/machine.png', confidence=0.8, grayscale=False)
                    print(str(t)+'开始建造攻城器械'+what[str(t)]+str(troops[t])+'个')
                    Center=pyautogui.center(Part)
                    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开造兵    
                    time.sleep(0.5)
        photo='./train_troops/'+str(t)+'.png'
        if pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=True)==None and type(t)==int:
            if t>=14:
                slip_position=pyautogui.center(pyautogui.locateOnScreen('./train_troops/1.png', confidence=0.8, grayscale=True))
                pyautogui.mouseDown(slip_position.x+random.randint(10,100),slip_position.y+random.randint(-10,95))
                pyautogui.dragRel(-153+random.randint(0,8), 10+random.randint(-8,8), button='left', duration=0.20)
                #pyautogui.mouseUp()
                time.sleep(1)
            else:
                slip_position=pyautogui.center(pyautogui.locateOnScreen('./train_troops/14.png', confidence=0.8, grayscale=True))
                pyautogui.mouseDown(slip_position.x+random.randint(10,100),slip_position.y+random.randint(-10,95))
                pyautogui.dragRel(188+random.randint(0,8), 10+random.randint(-8,8), button='left', duration=0.20)
                #pyautogui.mouseUp()
                time.sleep(1)
        Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=True)
        Center=pyautogui.center(Part)
        while troops[t]>0:
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
            troops[t]=troops[t]-1
            time.sleep(0.1)
        last=t
    # if troops[t]==0:
    #     del troops[t]
        # if troops=={}:
        #     break
    Part=pyautogui.locateOnScreen('./others/open.png', confidence=0.8, grayscale=False)
    Center=pyautogui.center(Part)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
    time.sleep(0.5)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
    return troops

    # return troops


# Part.png需事先准备好，并与代码放在同一目录下，confidence为精度（数值为0到1）
def give_troops(i,troops):
    print(i)
    number=0
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    
    while Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            #print('没有库存，不捐赠')
            #print('捐出'+str(i)+what[str(i)]+str(number)+'个')
            break
        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        if i in troops:
            troops[i]=troops[i]+1
            number=number+1
        else:
            troops[i]=1
            number=number+1
        time.sleep(0.6)
        Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    print('捐出'+str(i)+what[str(i)]+str(number)+'个')
    return troops

def give_G(i,troops):
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.9, grayscale=False)
    if Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        #rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        #if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            #print('没有库存，不捐赠')
        print('捐出'+str(i)+what[str(i)])
        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        if i in troops:
            troops[i]=troops[i]+1
        else:
            troops[i]=1
    return troops

def give_spells(i,troops):
    number=0
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    while Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            
            #print('没有库存，不捐赠')
            break
        #print('捐出'+str(i)+what[str(i)])
        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        if i in troops:
            troops[i]=troops[i]+1
            number=number+1
        else:
            troops[i]=1
            number=number+1
        time.sleep(0.7)
        Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    print('捐出'+str(i)+what[str(i)]+str(number)+'个')
    return troops

def yyz():
    Part=pyautogui.locateOnScreen('./others/yyz.png', confidence=0.98, grayscale=False)
    if Part!=None:
        Center=pyautogui.center(Part)
        print('友谊战请求')
        time.sleep(random.randint(1, 3)+random.random())
        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/yyz_start.png', confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            time.sleep(random.randint(1, 3)+random.random())
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
            time.sleep(0.5)
            Part=pyautogui.locateOnScreen('./others/yyz_start2.png', confidence=0.95, grayscale=False)
            if Part!=None:
                Center=pyautogui.center(Part)
                time.sleep(random.randint(1, 3)+random.random())
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))

def main():
        troops={}
        Part=pyautogui.locateOnScreen('./others/reload.png', confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('休息15分钟')
            time.sleep(900)
            Part=pyautogui.locateOnScreen('./others/reload.png', confidence=0.95, grayscale=False)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/tryagain.png', confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print('掉线重连')
            time.sleep(random.randint(1, 3)+random.random())
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/tryagain2.png', confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print('未操作重连')
            time.sleep(random.randint(1, 3)+random.random())
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        yyz()
        Part=pyautogui.locateOnScreen('./others/oil.png', confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/gold.png', confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/water.png', confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/open.png', confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))

        Part_help=pyautogui.locateAllOnScreen('./others/help.png', confidence=0.95, grayscale=False)
        #print(Part_help)
        for all_help in Part_help:
            #print(all_help)
            Center=pyautogui.center(all_help)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开增援    
            time.sleep(1)

            for i in (13,6,19,9,14,17,18,16,22,10,20,21,11,12,7,23,5,19,21,8,3,2,1,'a','c','e','h','j','G3','G2','G1','G4'):#账号1 可定义无图像要求情况下的捐兵顺序
            #for i in (13,6,10,22,'a','b','c','e',17,16,14,9,12,5,20,3,19,21,8,7,1,15,2,'j','h','G1'):#账号2
                findtroops(i,Center.x)
            time.sleep(1.5)
            for i in findt:
                if type(i)==int:
                    print('捐兵'+str(i)+what[str(i)])
                    troops=give_troops(i,troops) #1-23
                else:
                    if type(i)==str and i<='a':
                        troops=give_G(i,troops) 
                    else:
                        troops=give_spells(i,troops)
                if pyautogui.locateOnScreen('./others/closegive.png', confidence=0.8, grayscale=False)==None:
                    break
            del findt[:]
            Part=pyautogui.locateOnScreen('./others/closegive.png', confidence=0.8, grayscale=False)
            if Part!=None:
                Center=pyautogui.center(Part)
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并关闭增援界面
                time.sleep(0.5)
        if troops!={}:
            # try:
            for i in troops:
                print('还需要训练'+str(i)+what[str(i)]+str(troops[i])+'个')
            troops=autotrain(troops) 
            #     print('训练结束')
            # except:
            #     print('训练出错')
            #     for i in troops:
            #         print('还需要训练'+str(i)+what[str(i)]+str(troops[i])+'个')

while(1):
    if keyboard.is_pressed('s') == True:
        sys.exit()
    
    try:
        main()
        time.sleep(0.5)
    except:
        mistaken()