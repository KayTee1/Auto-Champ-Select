import pyautogui
from time import sleep
global accepted
global banned
global chose
accepted = False
banned = False
chose = False

def findimage(image):
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(cords is not None):
        return cords

def click(img):
    sleep(2)
    if(findimage(img) is not None):
        pyautogui.click(findimage(img))

def main():
    to_ban = input("what champion to ban?: ")
    to_select= input("what champion to play?: ")
    global accepted,banned,chose
    print("In Queue")

    #searching for accept button
    while findimage("accepted.png") is None and accepted == False:
        sleep(0.1)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered
            click("accept.png") or click("hovered_accept.png")
        except:
            print("cant find accept")
    accepted = True
    print("Game Started!")

    #banning
    while findimage("ban_search.png") is None and banned == False:
        print(findimage("ban_search.png"))
        sleep(0.1)

    #ban_cords = pixel coordinates for specific image
    ban_cords = findimage("ban_search.png")
    click("ban_search.png")
    sleep(0.3)

    pyautogui.write(to_ban,interval=0.25)
    sleep(0.5)

    ban_champion_x = ban_cords[0]-500
    ban_champion_y = ban_cords[1]-75

    pyautogui.click(ban_champion_x, ban_champion_y)
    sleep(0.5)

    click("ban_button.png")
    sleep(0.5)

    print("Banned "+ to_ban + "!")
    banned = True
    #

    #picking
    print("Waiting for pick turn")
    #used sort_by_fav button, because the search button didnt work >:
    while findimage("sort_by_fav.png") is None and chose == False:
        sleep(0.5)

    normal_search_cords = findimage("sort_by_fav.png")

    search_cords_x = normal_search_cords[0]+300
    search_cords_y = normal_search_cords[1]+35

    pyautogui.click(search_cords_x, search_cords_y)

    sleep(0.5)
    pyautogui.write(to_select,interval=0.25)
    sleep(1)

    pyautogui.click(normal_search_cords[0]-340,normal_search_cords[1]+95)
    sleep(1)
    click("lock_button.png")

    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True

if __name__ == "__main__":
    main()