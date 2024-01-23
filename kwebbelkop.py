'''
def crash():
    try:
        crash()
    except:
        crash()
    crash()

crash()

print('juujikakunkyugo')

dict = [
    {'number': 1, 'display': 'one'},
    {'number': 2, 'display': 'two'},
    {'number': 3, 'display': 'three'}
]

for i in dict:
    print(f"enter {i['number']} to print {i['display']}")

user_prompt = input("\nhere:")

for i in dict:
    if user_prompt == str(i['number']):
        print(i['display'])
    else:
        print('unacceptable input')
        break
'''

import pyautogui
import subprocess
import time

def write():
    subprocess.run(["start", "chrome.exe"], shell = True)
    time.sleep(2)
    pyautogui.typewrite("discord.com")
    pyautogui.press('enter')
    pyautogui.mouseDown(1200, 870)
    while pyautogui.pixel(1200, 870) != (49, 51, 56):
        time.sleep(0.001)
    else:
        pyautogui.doubleClick()
    pyautogui.mouseDown(400, 570)
    time.sleep(5)
    print(pyautogui.pixel(400,570))
    time.sleep(0.1)
    while pyautogui.pixel(400, 570) != (43, 45, 49):
        time.sleep(0.001)
    else:
        pyautogui.doubleClick
    time.sleep(2)
    pyautogui.typewrite('this message was written automatically by python.')
    pyautogui.press('enter')

write()

