from time import perf_counter as T
import pyautogui
# NOTICE that in pyautogui: region=(left, top, width, height)
pyautogui.screenshot('pyautogui_region_screenshot.png', region=(300, 500, 300, 200))
sT = T()
img = pyautogui.locateOnScreen('pyautogui_region_screenshot.png', region=(300, 500, 300, 200))
eT = T()
print(f'img = pyautogui.locateOnScreen took: {eT-sT:9.5f} seconds')
print(img)