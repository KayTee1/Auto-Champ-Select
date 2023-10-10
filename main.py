import pyautogui
from time import sleep
import tkinter as tk
from tkinter import messagebox, ttk

class AutoChampGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto-Champ-Select")
        self.root.geometry("400x400")
        title_label = ttk.Label(master = self.root, text = "Automatic Champ Select", font = "calibri 24 bold")
        title_label.pack()

        inputTxt = tk.Text(self.root,
				height = 5,
				width = 20)
        inputTxt.pack()
        acceptButton = tk.Button(self.root,
						text = "Print",
						command = printInput)
        acceptButton.pack()


    def run(self):
        self.root.mainloop()



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

    while findImage("imgs/ban_search.png") is None and banned == False:
        print(findImage("imgs/ban_search.png"))
        sleep(sleep_duration)

    ban_cords = findImage("imgs/ban_search.png")
    click("imgs/ban_search.png")
    sleep(sleep_duration)

    pyautogui.write(to_ban, interval=0.25)
    sleep(sleep_duration)

    ban_champion_x = ban_cords[0]-500
    ban_champion_y = ban_cords[1]+100

    pyautogui.click(ban_champion_x, ban_champion_y)
    sleep(sleep_duration)

    click("imgs/ban_button.png")
    sleep(sleep_duration)

    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(to_select, to_ban, chose, sleep_duration):

    print("Waiting for pick turn")
    #used sort_by_fav button, because the search button didnt work >:
    while findImage("imgs/sort_by_fav.png") is None and chose == False:
        sleep(sleep_duration)

    sort_by_fav_btn = findImage("imgs/sort_by_fav.png")

    #not using findImage or click funtion because it doesnt recognize the search-field like it does in the banning phase
    search_bar_x = sort_by_fav_btn[0]+300
    search_bar_y = sort_by_fav_btn[1]+35

    pyautogui.click(search_bar_x, search_bar_y)
    sleep(sleep_duration)

    pyautogui.write(to_select, interval=0.25)
    sleep(sleep_duration)

    champion_picking_x = sort_by_fav_btn[0]-340
    champion_picking_y = sort_by_fav_btn[1]+95

    pyautogui.click(champion_picking_x, champion_picking_y)
    sleep(sleep_duration)
    click("imgs/lock_button.png")

    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True

def main():
    app = AutoChampGUI()
    app.run()


def oldMain():

    accepted = False
    banned = False
    chose = False
    sleep_duration = 0.5

    to_ban = input("what champion to ban?: ")
    to_select= input("what champion to play?: ")
    print("In Queue")

    #searching for accept button
    while findImage("imgs/accepted.png") is None and accepted == False:
        sleep(sleep_duration)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered
            click("imgs/accept.png") or click("imgs/hovered_accept.png")
        except:
            print("cant find accept")
    accepted = True
    print("In Champ select")

    #banning and picking phase

    banning_phase(to_ban, banned, sleep_duration)
    picking_phase(to_select, to_ban, chose, sleep_duration)
if __name__ == "__main__":
    main()
