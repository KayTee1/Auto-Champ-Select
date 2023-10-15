import pyautogui
from time import sleep

#option 0 = just return the cords
#option 1 = click it
def findImage(image, option):
    sleep(1)
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    print(cords)
    if(option == 1):
        #cords = pixel coordinates for specific images 
        if(cords != None):
            pyautogui.click(cords)
        
    return cords


while True:
    accept_cords = findImage("imgs/test.png", 1)
    
    if accept_cords is not None:
        print("YA")
    
    sleep(1)
    print("finding...")
