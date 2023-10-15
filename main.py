import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

label_list = []
sleep_duration = 1


#for testing purposes will use "imgs/test.png" instead of the real use case
#will comment the supposed image

#CRASHING!!
def inQueue(app, to_ban, to_pick):
    accepted = False
    sleep_duration = 0.5
    
    print("here")

    #searching for accept button
    ##imgs/accept.png
    while findImage("imgs/test.png", 0) is None and accepted == False:
        sleep(sleep_duration)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered

            ##imgs/accept.png imgs/hovered_accept.png
            findImage("imgs/test.png", 1) or findImage("imgs/test.png", 1)
            accepted = True
        except:
            makeLabel(app, "Cant find Accept Button")
            print("cant find accept")

    
    makeLabel(app, "In Champ Select")
    print("In Champ select")
    

    #banning and picking phase

    banning_phase(app, to_ban)
    picking_phase(app, to_pick, to_ban)


#option 0 = just return the cords
#option 1 = click it
def findImage(image, option):
    sleep(1)
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(option == 0):
        #cords = pixel coordinates for specific images    
        return cords
    else:
        pyautogui.click(cords)
        return cords
    
    

def banning_phase(app, to_ban):
    banned = False
    makeLabel(app, f"Waiting for Banning phase")

    while banned == False:
        cords = findImage("imgs/ban_search.png", 1)
        sleep(sleep_duration)
        if(cords != None): 
            banned = True

    
    pyautogui.write(to_ban, interval=0.25)
    sleep(sleep_duration)

    #cords for the actual icon after typing to_ban in the search bar 
    ban_cords = findImage("imgs/ban_search.png")
    ban_champion_x = ban_cords[0]-500
    ban_champion_y = ban_cords[1]+100

    pyautogui.click(ban_champion_x, ban_champion_y)
    sleep(sleep_duration)

    findImage("imgs/ban_button.png", 1)
    sleep(sleep_duration)
    makeLabel(app, "Banned {to_ban} !")
    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(app, to_select, to_ban):
    picked = False
    makeLabel(app, "Waiting for Picking phase!")
    print("Waiting for pick turn")

    #used sort_by_fav button, because the search button didnt work >:
    while picked == False:
        sleep(sleep_duration)
        sort_by_fav_btn = findImage("imgs/sort_by_fav.png", 0)
        if(sort_by_fav_btn != None):
            picked = True
            
    #not using findImage or click funtion because it doesnt recognize the search-field like it does in the banning phase
    search_bar_x = sort_by_fav_btn[0]+300
    search_bar_y = sort_by_fav_btn[1]+35

    findImage([search_bar_x, search_bar_y], 1)
    sleep(sleep_duration)

    pyautogui.write(to_select, interval=0.25)
    sleep(sleep_duration)

    champion_picking_x = sort_by_fav_btn[0]-340
    champion_picking_y = sort_by_fav_btn[1]+95

    findImage([champion_picking_x, champion_picking_y], 1)
    sleep(sleep_duration)
    findImage("imgs/lock_button.png", 1)

    makeLabel(app, f"Selected {to_select} And Banned {to_ban} !")
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
   


def makeInputFields(app, entry_vars):
    input_frame_ban = tk.Frame(app)
    entry_ban = ttk.Entry(input_frame_ban, textvariable=entry_vars[0])
    entry_pick = ttk.Entry(input_frame_ban, textvariable=entry_vars[1])
    button = ttk.Button(input_frame_ban, text='Confirm',
                        command=lambda: processInputs(app, entry_vars))
    entry_ban.pack(side='left', padx=10)
    entry_pick.pack(side='left', padx=10)
    button.pack(side='left')
    input_frame_ban.pack(pady=10)


def makeLabel(app, string):
    #clearing out previous labels
    #for label in label_list:
        #label.destroy()
    #label_list.clear()

    sleep(sleep_duration)

    label = ttk.Label(app, text=string, font="calibri 18")
    label.pack()
    label_list.append(label)


def processInputs(app, entry_vars):
    
    to_ban = entry_vars[0].get()
    to_pick = entry_vars[1].get()
    print("Champ To Ban:", to_ban)
    print("Champ To Pick:", to_pick)
    makeLabel(app, "WHAT")
    makeLabel(app, "WHAT")
    makeLabel(app, "WHAT")
    makeLabel(app, "WHAT")
    if to_pick != "" and to_ban != "":
        makeLabel(app, "In Queue")
        sleep(1)
        inQueue(app, to_ban, to_pick)
    else:
        makeLabel(app, "Invalid Input!")


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