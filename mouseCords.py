import pyautogui, sys
from time import sleep

#option 0 = just return the cords
#option 1 = click it
def findImage(image, option):
    sleep(1)
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(option == 0):
        #cords = pixel coordinates for specific images
        if(cords != None):
           return cords
    else:
        pyautogui.click(cords)
        if(cords != None):
            return cords
    

print('Press Ctrl-C to quit.')
try:
    while True:
        sleep(2)
        cords = findImage("imgs/test.png", 0)
        if cords == None:
            print("NOP")
        else:
            print("yay")
            #pyautogui.moveTo(cords)

except KeyboardInterrupt:
    print('\n')