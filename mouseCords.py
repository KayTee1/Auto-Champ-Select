import pyautogui, sys
from time import sleep
print('Press Ctrl-C to quit.')
try:
    while True:
        sleep(2)
        cords = pyautogui.locateOnScreen("imgs/test.png", confidence=0.98)
        if cords == None:
            print("NOP")
        else:
            print("yay")
            #pyautogui.moveTo(cords)

except KeyboardInterrupt:
    print('\n')