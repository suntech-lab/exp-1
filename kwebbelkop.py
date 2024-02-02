import pyautogui
import subprocess
import time
import random
import sys

def write():
    subprocess.run(["start", "chrome.exe"], shell = True)
    pyautogui.hotkey('winleft', 'up')
    time.sleep(2)
    pyautogui.typewrite("discord.com")
    pyautogui.press('enter')
    pyautogui.mouseDown(1200, 870)
    while pyautogui.pixel(1200, 870) != (49, 51, 56):
        time.sleep(0.001)
    else:
        pyautogui.moveTo(1250, 870, 0.001)
        pyautogui.doubleClick()
    pyautogui.mouseDown(400, 570)
    time.sleep(5)
    time.sleep(0.1)
    while pyautogui.pixel(400, 570) != (53, 55, 60):
        time.sleep(0.001)
    else:
        pyautogui.moveTo(390, 570, 0.001)
        pyautogui.leftClick()
    time.sleep(2)
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    

def track():
    print('press ctrl-c to quit')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'x: ' + str(x).rjust(4) + ' y: ' + str(y).rjust(4)
            print(positionStr, end = '')
            print('\b' * len(positionStr), end = '', flush = True)
    except KeyboardInterrupt:
        print('\n')

def rgbtrack():
    print('press ctrl-c to quit')
    try:
        while True:
            x, y = pyautogui.position()
            r, g, b = pyautogui.pixel(x, y)
            positionRGB = str(r).rjust(4) + str(g).rjust(4) + str(b).rjust(4)
            print(positionRGB, end = '')
            print('\b' * len(positionRGB), end = '', flush = True)
    except KeyboardInterrupt:
        print('\n')



dict = [
    {'pyautogui': 1, 'desc': 'write a discord message', 'func': write},
    {'pyautogui': 2, 'desc': 'track the pixel', 'func': track},
    {'pyautogui': 3, 'desc': 'track the rgb value of the pixel the cursor is on', 'func': rgbtrack},
    {'pyautogui': 4, 'desc': 'press a key every once in a while', 'func': keymacro},
    {'pyautogui': 5, 'desc': 'do a click every once in a while', 'func': clickmacro}
]

def start():
    for i in dict:
        print(f"enter {i['pyautogui']} to {i['desc']}")

    user_prompt = input("\nhere:")

    for i in dict:
        if user_prompt == str(i['pyautogui']):
            i['func']()
            break
    else:
        print('unacceptable input')

start()
