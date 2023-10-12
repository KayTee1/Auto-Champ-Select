import tkinter as tk
from tkinter import ttk


def makeInputFields(entry_vars):
    input_frame_ban = tk.Frame(app)
    entry_ban = ttk.Entry(input_frame_ban, textvariable=entry_vars[0])
    entry_pick = ttk.Entry(input_frame_ban, textvariable=entry_vars[1])
    button = ttk.Button(input_frame_ban, text='Confirm',
                        command=lambda: processInputs(entry_vars))
    entry_ban.pack(side='left', padx=10)
    entry_pick.pack(side='left', padx=10)
    button.pack(side='left')
    input_frame_ban.pack(pady=10)


def makeLabel(string):
    champToBanLabel = ttk.Label(app, text=string, font="calibri 18")
    champToBanLabel.pack()


def processInputs(entry_vars):
    champ_to_ban_text = entry_vars[0].get()
    champ_to_pick_text = entry_vars[1].get()
    print("Champ To Ban:", champ_to_ban_text)
    print("Champ To Pick:", champ_to_pick_text)


app = tk.Tk()
app.title("TextBox Input")
app.geometry('400x400')

title_label = ttk.Label(
    app, text="Automatic Champ Select", font="calibri 24 bold")
title_label.pack()

champ_to_ban_var = tk.StringVar()
champ_to_pick_var = tk.StringVar()

makeLabel("Champ To Ban and Champ To Pick:")
makeInputFields([champ_to_ban_var, champ_to_pick_var])

app.mainloop()


"""def inChampSelect(app, to_ban, to_pick):
    accepted = False
    banned = False
    chose = False
    sleep_duration = 0.5

    #searching for accept button
    while findImage("imgs/accepted.png") is None and accepted == False:
        sleep(sleep_duration)
        try:
            #hovered accept: when someone dodges, the mouse is still on the accept button
            #the accept button glows when its hovered
            click("imgs/accept.png") or click("imgs/hovered_accept.png")
        except:
            makeInputFields()
            print("cant find accept")
    accepted = True
    makeLabel(app, "In Champ Select")
    print("In Champ select")

    #banning and picking phase

    banning_phase(app, to_ban, banned, sleep_duration)
    picking_phase(app, to_pick, to_ban, chose, sleep_duration)

   """