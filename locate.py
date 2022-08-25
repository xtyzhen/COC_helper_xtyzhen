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

check_sleep=random.randint(60, 920)
troops={}
findt=[]
what={0:'超级巨人',1:'野蛮人',2:'弓箭手',3:'胖子',4:'哥布林',5:'炸弹人',6:'气球',7:'法师',8:'天使',9:'龙',10:'皮卡',11:'龙宝宝',12:'矿工',13:'电龙',14:'雪怪',15:'苍蝇',16:'野猪',17:'武神',18:'石头人',19:'女巫',20:'天狗',21:'投石手',22:'冰人',23:'英雄猎手',24:'蓝胖','a':'雷电','b':'治疗','c':'狂暴','d':'弹跳','e':'冰冻','f':'复制','g':'隐身法术','h':'毒药','i':'地震','j':'疾速','k':'骷髅','l':'蝙蝠','G1':'攻城车','G2':'飞艇','G3':'大气球','G4':'训练营','G5':'滚木车','G6':'投石车'}
donate={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'G1':0,'G2':0,'G3':0,'G4':0,'G5':0,'G6':0}

start_time=time.time()
def anti_detected():
    global start_time
    global check_sleep
    if ((int(time.strftime("%H", time.localtime())))>=23 and int(time.strftime("%M", time.localtime()))>35) or (int(int(time.strftime("%H", time.localtime())))<=6 and int(time.strftime("%M", time.localtime()))<15):#此处修改夜间休息时间段
        Part=pyautogui.locateOnScreen('./others/close_coc.png', confidence=0.8, grayscale=True)
        if Part!=None:
            click(Part.left+126,Part.top+14)
            time.sleep(24000)#此处修改夜间休息时间长度
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("夜间休息")
        Part=pyautogui.locateOnScreen('./others/icon.png', confidence=0.8, grayscale=True)
        if Part!=None:
            click(Part.left+45,Part.top+45)
        return
    if (time.time()-start_time)>random.randint(520, 920):
        Part=pyautogui.locateOnScreen('./others/close_coc.png', confidence=0.8, grayscale=True)
        if Part!=None:
            click(Part.left+126,Part.top+14)
            sleep_time=check_sleep
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("工作间隙休息"+str(sleep_time/60))
            time.sleep(sleep_time)
            check_sleep=random.randint(60, 920)
        Part=pyautogui.locateOnScreen('./others/icon.png', confidence=0.8, grayscale=True)
        if Part!=None:
            click(Part.left+45,Part.top+45)
        start_time=time.time()
def mistaken():
    time.sleep(1)
    try:
        print('*****循环跳过，本页无内容*****')
        print('可以加入报警通知程序')
        print('——————————开始正常运行——————————')
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
def findtroops(i,im):
    photo='./troops/'+str(i)+'.png'
    Part = pyautogui.locate(photo,im,confidence=0.8)      # <class 'pyscreeze.Box'>
    if Part==None:
        #print('未识别到图片'+str(i)+what[i])
        return 0
    Center=pyautogui.center(Part)
    rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
    if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
        #print('没有库存，不捐赠')
        return 0
    else:
        findt.append(i)

def autotrain():
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
    for t in what:
        if t in troops:
            print('需要训练'+what[t]+str(troops[t])+'个')
            donate[t]+=troops[t]
            if type(t)==int and type(t)!=type(last):
                print(str(t)+'开始训练军队'+what[t]+str(troops[t])+'个')
                Part=pyautogui.locateOnScreen('./others/train_troops.png', confidence=0.8, grayscale=False)
                Center=pyautogui.center(Part)
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开造兵    
                time.sleep(0.5)
            else:
                if type(t)==str and t>='a' and (type(last)==type(None) or type(last)==int or (last<'a')): #type(t)==str
                    print(str(t)+'开始配置法术'+what[t]+str(troops[t])+'个')
                    Part=pyautogui.locateOnScreen('./others/spells.png', confidence=0.8, grayscale=False)
                    Center=pyautogui.center(Part)
                    click(Center.x+random.randint(-10,5),Center.y+random.randint(-5,5))#识别并打开造兵    
                    time.sleep(0.5)
                else:
                    if type(t)==str and t<'a' and (type(last)==type(None) or type(last)==int or last>='a'):
                        Part=pyautogui.locateOnScreen('./others/machine.png', confidence=0.8, grayscale=False)
                        print(str(t)+'开始建造攻城器械'+what[t]+str(troops[t])+'个')
                        Center=pyautogui.center(Part)
                        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并打开造兵    
                        time.sleep(0.5)
            photo='./train_troops/'+str(t)+'.png'
            if pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=True)==None and type(t)==int:
                if t>=13:
                    slip_position=pyautogui.center(pyautogui.locateOnScreen('./train_troops/13.png', confidence=0.8, grayscale=True))
                    pyautogui.mouseDown(slip_position.x+random.randint(10,100),slip_position.y+random.randint(-10,95))
                    pyautogui.dragRel(-200+random.randint(0,8), 10+random.randint(-8,8), button='left', duration=0.20)
                    #pyautogui.mouseUp()
                    time.sleep(1)
                else:
                    slip_position=pyautogui.center(pyautogui.locateOnScreen('./train_troops/13.png', confidence=0.8, grayscale=True))
                    pyautogui.mouseDown(slip_position.x+random.randint(10,100),slip_position.y+random.randint(-10,95))
                    pyautogui.dragRel(230+random.randint(0,8), 10+random.randint(-8,8), button='left', duration=0.20)
                    #pyautogui.mouseUp()
                    time.sleep(1)
            if t=="G6":
                    slip_position=pyautogui.center(pyautogui.locateOnScreen('./train_troops/G2.png', confidence=0.8, grayscale=True))
                    pyautogui.mouseDown(slip_position.x+random.randint(10,100),slip_position.y+random.randint(-10,95))
                    pyautogui.dragRel(-100+random.randint(0,8), 10+random.randint(-8,8), button='left', duration=0.20)
                    #pyautogui.mouseUp()
                    time.sleep(1)
            Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=True)
            Center=pyautogui.center(Part)
            while troops[t]>0:
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
                troops[t]=troops[t]-1
                time.sleep(0.1)
            del troops[t]
            last=t
            if troops=={}:
                break
    Part=pyautogui.locateOnScreen('./others/open.png', confidence=0.8, grayscale=False)
    Center=pyautogui.center(Part)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
    time.sleep(0.5)
    click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
    return 0

    # return troops


# Part.png需事先准备好，并与代码放在同一目录下，confidence为精度（数值为0到1）
def give_troops(i):
    print(i)
    number=0
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    
    while Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            #print('没有库存，不捐赠')
            #print('捐出'+str(i)+what[i]+str(number)+'个')
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
    print('捐出'+str(i)+what[i]+str(number)+'个')
    return 0

def give_G(i):
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.9, grayscale=False)
    if Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        #rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        #if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            #print('没有库存，不捐赠')
        print('捐出'+str(i)+what[i])
        click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        if i in troops:
            troops[i]=troops[i]+1
        else:
            troops[i]=1
    return 0

def give_spells(i):
    number=0
    photo='./troops/'+str(i)+'.png'
    Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    while Part!=None:       # <class 'pyscreeze.Box'> 
        Center=pyautogui.center(Part)
        rgb=pyautogui.screenshot().getpixel((int(Center.x+random.randint(-10,10)),int(Center.y+random.randint(-10,10))))
        if rgb[0]==rgb[1] and rgb[1]==rgb[2]:
            
            #print('没有库存，不捐赠')
            break
        #print('捐出'+str(i)+what[i])
        click(Center.x+random.randint(-5,7),Center.y+random.randint(-7,5))
        if i in troops:
            troops[i]=troops[i]+1
            number=number+1
        else:
            troops[i]=1
            number=number+1
        time.sleep(0.7)
        Part=pyautogui.locateOnScreen(photo, confidence=0.8, grayscale=False)
    print('捐出'+str(i)+what[i]+str(number)+'个')
    return 0

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
        im=pyautogui.screenshot()
        Part = pyautogui.locate('./others/reload.png',im, confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('休息15分钟')
            time.sleep(900)
            Part = pyautogui.locate('./others/reload.png',im, confidence=0.95, grayscale=False)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part=pyautogui.locateOnScreen('./others/tryagain.png', confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print('掉线重连')
            time.sleep(random.randint(1, 3)+random.random())
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part = pyautogui.locate('./others/tryagain2.png',im, confidence=0.95, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            print('未操作重连')
            time.sleep(random.randint(1, 3)+random.random())
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        yyz()
        Part = pyautogui.locate('./others/oil.png',im, confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part = pyautogui.locate('./others/gold.png',im, confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part = pyautogui.locate('./others/water.png',im, confidence=0.8, grayscale=False)
        if Part!=None:
            Center=pyautogui.center(Part)
            click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
        Part = pyautogui.locate('./others/open.png',im, confidence=0.8, grayscale=False)
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
            im=pyautogui.screenshot()
            for i in (13,6,0,19,9,14,17,18,16,22,10,20,21,4,11,12,7,23,5,19,21,8,3,2,1,24,'a','b','c','d','e','f','g','h','j','G3','G2','G1','G4','G5','G6'):#账号1
            #for i in (13,6,10,22,'a','b','c','e',17,16,14,9,12,5,20,3,19,21,8,7,1,15,2,'j','h','G1'):#账号2
                findtroops(i,im)
            time.sleep(1.5)
            for i in findt:
                if type(i)==int:
                    print('捐兵'+str(i)+what[i])
                    give_troops(i) #1-23
                else:
                    if type(i)==str and i<='a':
                        give_G(i) 
                    else:
                        give_spells(i)
                if pyautogui.locateOnScreen('./others/closegive.png', confidence=0.8, grayscale=False)==None:
                    break
            del findt[:]
            Part=pyautogui.locateOnScreen('./others/closegive.png', confidence=0.8, grayscale=False)
            pyautogui.locate
            if Part!=None:
                Center=pyautogui.center(Part)
                click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))#识别并关闭增援界面
                time.sleep(0.5)
        if troops!={}:
            # try:
            for i in troops:
                print('还需要训练'+str(i)+what[i]+str(troops[i])+'个')
            autotrain() 
            #     print('训练结束')
            # except:
            #     print('训练出错')
            #     for i in troops:
            #         print('还需要训练'+str(i)+what[i]+str(troops[i])+'个')

while(1):
    if keyboard.is_pressed('s') == True:
        for t in donate:
            if donate[t]:
                print("{0:{3}<4}{1:{3}^5}{2:<1}个".format('共捐赠', what[t], donate[t], chr(12288)))
        sys.exit()
    #main()
    try:
        main()
        time.sleep(0.5)
        anti_detected()
        
    except:
        mistaken()
        
        
    # give_troops(1) #1-23
    # give_G(2)      #1-3
    # give_spells('a') #a-l

# for i in range(23,0,-1):
#     if i==4 or i==5 :
#         continue
#     photo='./troops/'+str(i)+'.png'
#     Part = pyautogui.locateOnScreen(photo, confidence=0.92, grayscale=False)         # <class 'pyscreeze.Box'>
#     if Part==None:
#         print('未识别到图片'+str(i))
#         continue
#     Center=pyautogui.center(Part)
#     print('识别到图片'+str(i))
#     click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
#     if i in c:
#         c[i]=c[i]+1
#     else:
#         c[i]=1
#     time.sleep(0.1)
    
# for i in range(1,4):
#     photo='./troops/G'+str(i)+'.png'
#     Part = pyautogui.locateOnScreen(photo, confidence=0.90, grayscale=False)         # <class 'pyscreeze.Box'>
#     if Part==None:
#         print('未识别到图片'+str(i))
#         continue
#     Center=pyautogui.center(Part)
#     print('识别到图片'+str(i))
#     click(Center.x+random.randint(-10,10),Center.y+random.randint(-10,10))
#     if i in c:
#         c['G'+str(i)]=c['G'+str(i)]+1
#     else:
#         c['G'+str(i)]=1
#     break

