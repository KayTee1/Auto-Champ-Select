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
    accept_coords = findImage("imgs/accept.png")
    if accept_coords is not None:
        print("Accept button found at:", accept_coords)
        click("imgs/accept.png")
        break  # Exit the loop once the accept button is found
    else:
        print("Accept button not found. Retrying...")
        sleep(1)
