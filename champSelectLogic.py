import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

from gui import makeLabel, label_list

def inQueue(app, to_ban, to_pick):
    accepted = False
    banned = False
    chose = False
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
    
    
    makeLabel(app, "In Champ Select", label_list)
    print("In Champ select")
    

    #banning and picking phase

    banning_phase(app, to_ban, banned, sleep_duration)
    picking_phase(app, to_pick, to_ban, chose, sleep_duration)



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
    makeLabel(app, "Banned {to_ban} !", label_list)
    print("Banned "+ to_ban + "!")
    banned = True

def picking_phase(app, to_select, to_ban, chose, sleep_duration):
    makeLabel(app, "Banned {to_ban} !", label_list)
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

    makeLabel(app, f"Selected {to_select} And Banned {to_ban} !", label_list)
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True

