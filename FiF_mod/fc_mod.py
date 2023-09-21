# from PIL import ImageGrab
# from functools import partial
# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random



width, height = pgi.size()
print('해상도 :', width, height)
print("시작은 F3")
print("F2: mini_mod 시작")


def skey():
    pyd.keyDown("s")
    time.sleep(0.05)
    pyd.keyUp("s")
    
    #
def imgclick(files):
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile, end=" ")
        print("이미지 버튼 클릭")
        x, y = imgfile
        x = x- random.randint(1, 20) + random.randint(1, 20)
        y = y- random.randint(1, 18) + random.randint(1, 20)
        pgi.click(x, y)
        
def skeypress(files):
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile, end=" ")
        print("스킵")
        print(files)
        x, y = imgfile
        x = x- random.randint(1, 20) + random.randint(1, 20)
        y = y- random.randint(1, 18) + random.randint(1, 20)
        pgi.click(x, y)
        pyd.keyDown("s")
        time.sleep(0.08)
        pyd.keyUp("s")

        
def esckeypress(files):
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile, end=" ")
        print("ESC 누름")
        x, y = imgfile
        x = x- random.randint(1, 20) + random.randint(1, 20)
        y = y- random.randint(1, 18) + random.randint(1, 20)
        pgi.click(x, y)
        pyd.keyDown("esc")
        time.sleep(0.08)
        pyd.keyUp("esc")
        
end_flag = False
mini_flag = False
while not end_flag:
    if keyboard.is_pressed('F2'):
        mini_flag = True
        
    if keyboard.is_pressed('F3'):
        if mini_flag == True:
            print("mini mode")
        print('작업시작')
        
        
        while True:
            if keyboard.is_pressed('F4'):
                end_flag = True
                print('중지')
                break
            
            else:
                if mini_flag == True:
                    # skeypress('fhds.png')
                    imgclick('mini_fhd2.png')
                    imgclick('mini_fhd3.png')
                    imgclick('mini_fhd4.png')
                    imgclick('mini_fhd5.png')
                    imgclick('mini_fhd6.png')
                    # imgclick('fhd7.png')
                    esckeypress('mini_esc.png')
                    skeypress('mini_sskip.png')
                    skeypress('mini_ssskip.png')
                    
                    # skeypress('23.png')
                    # skeypress('fhdskip2.png')
                    
                elif width == 2500:
                    skeypress('ss.png')
                    imgclick('s2.png')
                    imgclick('s3.png')
                    imgclick('s4.png')
                    imgclick('s5.png')
                    imgclick('s6.png')
                    imgclick('s7.png')
                    esckeypress('sesc.png')
                    skeypress('sskip.png')
                else:
                    # skeypress('fhds.png')
                    # imgclick('fhd2.png')
                    # imgclick('fhd3.png')
                    # imgclick('fhd4.png')
                    # imgclick('fhd5.png')
                    # imgclick('fhd6.png')
                    # imgclick('fhd7.png')
                    # esckeypress('fhdesc.png')
                    # skeypress('sskip.png')
                    # skeypress('23.png')
                    # skeypress('fhdskip2.png')
                    
                    #skeypress('fhds.png')
                    imgclick('fhd2.png')
                    imgclick('fhd3_fc.png')
                    imgclick('fhd4_fc.png')
                    imgclick('fhd5_fc.png')
                    imgclick('fhd6_fc.png')
                    imgclick('fhd7_fc.png')
                    esckeypress('fhdesc.png')
                    esckeypress('fhdesc_fc.png')
                    skeypress('sskip.png')
                    skeypress('23.png')
                    skeypress('fhdskip2_fc.png')
                    skeypress('fhdskip3_fc.png')
                    
                    
                    
print("종료")
                    