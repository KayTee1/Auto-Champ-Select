import pyautogui
from time import sleep

def findImage(image):
    #cords = pixel coordinates for specific images
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(cords is not None):
        return cords

def click(img):
    sleep(2)
    if(findImage(img) is not None):
        pyautogui.click(findImage(img))

def banning_phase(to_ban, banned, sleep_duration):

    while findImage("ban_search.png") is None and banned == False:
        print(findImage("ban_search.png"))
        sleep(sleep_duration)

    ban_cords = findImage("ban_search.png")
    click("ban_search.png")
    sleep(sleep_duration)

    pyautogui.write(to_ban, interval=0.25)
    sleep(sleep_duration)

    ban_champion_x = ban_cords[0]-500
    ban_champion_y = ban_cords[1]-75

    pyautogui.click(ban_champion_x, ban_champion_y)
    sleep(sleep_duration)

    click("ban_button.png")
    sleep(sleep_duration)

    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(to_select, to_ban, chose, sleep_duration):

    print("Waiting for pick turn")
    #used sort_by_fav button, because the search button didnt work >:
    while findImage("sort_by_fav.png") is None and chose == False:
        sleep(sleep_duration)

    normal_search_cords = findImage("sort_by_fav.png")

    search_cords_x = normal_search_cords[0]+300
    search_cords_y = normal_search_cords[1]+35

    pyautogui.click(search_cords_x, search_cords_y)

    sleep(sleep_duration)
    pyautogui.write(to_select,interval=0.25)
    sleep(sleep_duration)

    pyautogui.click(normal_search_cords[0]-340,normal_search_cords[1]+95)
    sleep(sleep_duration)
    click("lock_button.png")

    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True

def main():
    accepted = False
    banned = False
    chose = False
    sleep_duration = 0.5

    to_ban = input("what champion to ban?: ")
    to_select= input("what champion to play?: ")
    print("In Queue")

    #searching for accept button
    while findImage("accepted.png") is None and accepted == False:
        sleep(sleep_duration)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered
            click("accept.png") or click("hovered_accept.png")
        except:
            print("cant find accept")
    accepted = True
    print("In Champ select")

    #banning and picking phase
    banning_phase(to_ban, banned, sleep_duration)
    picking_phase(to_select, to_ban, chose, sleep_duration)


if __name__ == "__main__":
    main()