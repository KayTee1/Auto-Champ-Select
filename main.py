import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

label_list = []
def inQueue(app, to_ban, to_pick):
    accepted = False
    banned = False
    chose = False
    sleep_duration = 0.5

    #searching for accept button
    while findImage("imgs/accept.png") is None and accepted == False:
        sleep(sleep_duration)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered
            click("imgs/accept.png") or click("imgs/hovered_accept.png")
            accepted = True
        except:
            makeLabel(app, "Cant find Accept Button")
            print("cant find accept")
    """
    sleep(1)
    findImage("imgs/accept.png")
    click("imgs/accept.png")
    """
    
    makeLabel(app, "In Champ Select")
    print("In Champ select")
    

    #banning and picking phase

    banning_phase(app, to_ban, banned, sleep_duration)
    picking_phase(app, to_pick, to_ban, chose, sleep_duration)


def makeInputFields(app, entry_vars):
    input_frame_ban = tk.Frame(app)
    entry_ban = ttk.Entry(input_frame_ban, textvariable=entry_vars[0])
    entry_pick = ttk.Entry(input_frame_ban, textvariable=entry_vars[1])
    button = ttk.Button(input_frame_ban, text='Confirm',
                        command=lambda:inQueue(app, "da", "za"))
                        #command=lambda: processInputs(app, entry_vars))
    entry_ban.pack(side='left', padx=10)
    entry_pick.pack(side='left', padx=10)
    button.pack(side='left')
    input_frame_ban.pack(pady=10)


def makeLabel(app, string):
    label = ttk.Label(app, text=string, font="calibri 18")
    label.pack()
    label_list.append(label)


def processInputs(app, entry_vars):
    #clearing out previous labels
    for label in label_list:
        label.destroy()
    label_list.clear()

    to_ban = entry_vars[0].get()
    to_pick = entry_vars[1].get()
    print("Champ To Ban:", to_ban)
    print("Champ To Pick:", to_pick)

    if to_pick != "" and to_ban != "":
        makeLabel(app, "In Queue")
        sleep(1)

        inQueue(app, to_ban, to_pick)
    else:
        makeLabel(app, "Invalid Input!")



def findImage(image):
    #cords = pixel coordinates for specific images
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(cords is not None):
        return cords

def click(img):
    sleep(2)
    if(findImage(img) is not None):
        pyautogui.click(findImage(img))

def banning_phase(app, to_ban, banned, sleep_duration):

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
    makeLabel(app, "Banned {to_ban} !")
    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(app, to_select, to_ban, chose, sleep_duration):
    makeLabel(app, "Banned {to_ban} !")
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

    makeLabel(app, f"Selected {to_select} And Banned {to_ban} !")
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True

def main():
    app = tk.Tk()
    app.title("Auto-Champ-Select")
    app.geometry('400x300')

    title_label = ttk.Label(
        app, text="Automatic Champ Select", font="calibri 24 bold")
    title_label.pack()

    to_ban = tk.StringVar()
    to_pick = tk.StringVar()

    input_label = ttk.Label(
        app, text="Champ To Ban and Champ To Pick:", font="calibri 18")
    input_label.pack()

    makeInputFields(app, [to_ban, to_pick])

    app.mainloop()
    print("baibai")


if __name__ == "__main__":
    main()
