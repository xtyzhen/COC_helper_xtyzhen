# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:28:52 2021

@author: XTian
"""
from threading import Thread
import pyautogui
def aasync(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def find_cocphoto(photo):
    Part=pyautogui.locateOnScreen(photo, confidence=0.95, grayscale=False)
    if Part!=None:
        print('捐兵'+str(i))
def find_coctrainphoto(photo):
    Part=pyautogui.locateOnScreen(photo, confidence=0.91, grayscale=False)
    if Part!=None:
        print('造兵'+str(i))



for i in (13,6,9,14,17,16,22,10,12,7,23,1,'c','e','h','j','l','G3','G2','G1','../oil'):
    photo='./troops/'+str(i)+'.png'
    find_cocphoto(photo)


for i in (13,6,9,14,17,16,22,10,12,7,23,1,'c','e','h','j','l','G3','G2','G1','../oil'):
    photo='./train_troops/'+str(i)+'.png'
    # find_coctrainphoto(photo)

        