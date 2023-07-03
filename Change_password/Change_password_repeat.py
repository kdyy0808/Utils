import pyautogui
import keyboard
import time

print("Hello")
count = 111

while 1:
    position = pyautogui.position()
    pyautogui.click(x=1100, y=574)
    time.sleep(0.2)
    pyautogui.scroll(-10000)
    time.sleep(3.0)
    pyautogui.click(x=806, y=574)
    time.sleep(2.0)

    pyautogui.click(x=856,y=459)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.2)
    pyautogui.typewrite(str(count), interval=0.1)

    pyautogui.click(x=856,y=645)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    pyautogui.typewrite(str(count), interval=0.1)

    
    time.sleep(1.0)

    pyautogui.click(x=982, y=737)
    time.sleep(1.0)
    pyautogui.click(x=1151, y=641)


    time.sleep(7.0)
    count=count+1
    print(count)
    if count>140:
        break



'''
while 1:
    position = pyautogui.position()
    if keyboard.is_pressed('enter'):
        print(position)
        time.sleep(0.2)

'''


'''
    
    Point(x=755, y=645)
    if keyboard.is_pressed('enter'):
        print(position)
        time.sleep(0.2)




Point(x=856, y=459)
Point(x=860, y=645)

Point(x=982, y=737)

Point(x=1151, y=641)

Point(x=694, y=1002)

*/

'''
