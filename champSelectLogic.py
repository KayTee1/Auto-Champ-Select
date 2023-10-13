import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

from gui import makeLabel
from labelList import labels

#CRASHING!!
def inQueue(app, to_ban, to_pick):
    accepted = False
    sleep_duration = 0.5
    """
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
    pyautogui.moveTo(findImage("imgs/test.png"))
    #google search for working find "pyautogui confidence"
    
    
    makeLabel(app, "In Champ Select", labels)
    print("In Champ select")
    

    #banning and picking phase

    banning_phase(app, to_ban, sleep_duration)
    picking_phase(app, to_pick, to_ban, sleep_duration)


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
    
    

def banning_phase(app, to_ban, banned, sleep_duration):
    banned = False
    makeLabel(app, f"Waiting for Banning phase", labels)

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
    makeLabel(app, "Banned {to_ban} !", labels)
    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(app, to_select, to_ban, sleep_duration):
    picked = False
    makeLabel(app, "Waiting for Picking phase!", labels)
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

    makeLabel(app, f"Selected {to_select} And Banned {to_ban} !", labels)
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
   

