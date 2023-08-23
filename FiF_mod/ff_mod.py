import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random

width, height = pgi.size()
print('해상도 :', width, height)
print("시작은 F3")

def skey():
    pyd.keyDown("s")
    time.sleep(0.05)
    pyd.keyUp("s")
    
    
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
while not end_flag:
    if keyboard.is_pressed('F3'):
        print('작업시작')
        
        
        while True:
            if keyboard.is_pressed('F4'):
                end_flag = True
                print('중지')
                break
            
            else:
                if width == 2500:
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
                    skeypress('fhds.png')
                    imgclick('fhd2.png')
                    imgclick('fhd3.png')
                    imgclick('fhd4.png')
                    imgclick('fhd5.png')
                    imgclick('fhd6.png')
                    imgclick('fhd7.png')
                    esckeypress('fhdesc.png')
                    skeypress('sskip.png')
                    skeypress('23.png')
                    skeypress('fhdskip2.png')
                    
print("종료")
                    