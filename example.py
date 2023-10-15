import pyautogui
from time import sleep

def click(img):
    sleep(2)
    image_coords = findImage(img)
    if image_coords is not None:
        pyautogui.click(image_coords)
    else:
        print(f"Image '{img}' not found")

def findImage(image):
    # Try to locate the image on the screen
    try:
        cords = pyautogui.locateOnScreen(image, confidence=0.98)
        return cords
    except Exception as e:
        print(f"An error occurred while searching for '{image}': {e}")

while True:
    accept_cords = findImage("imgs/test.png")
    if accept_cords is not None:
        print("test found at:", accept_cords)
        sleep(1)
    else:
        print("test not found. Retrying...")
        sleep(1)
