import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

from champSelectLogic import inQueue


def makeInputFields(app, entry_vars, label_list):
    input_frame_ban = tk.Frame(app)
    entry_ban = ttk.Entry(input_frame_ban, textvariable=entry_vars[0])
    entry_pick = ttk.Entry(input_frame_ban, textvariable=entry_vars[1])
    button = ttk.Button(input_frame_ban, text='Confirm',
                        command=lambda:inQueue(app, "da", "za", label_list))
                        #command=lambda: processInputs(app, entry_vars))
    entry_ban.pack(side='left', padx=10)
    entry_pick.pack(side='left', padx=10)
    button.pack(side='left')
    input_frame_ban.pack(pady=10)


def makeLabel(app, string, label_list):
    label = ttk.Label(app, text=string, font="calibri 18")
    label.pack()
    label_list.append(label)


def processInputs(app, entry_vars, label_list):
    #clearing out previous labels
    for label in label_list:
        label.destroy()
    label_list.clear()

    to_ban = entry_vars[0].get()
    to_pick = entry_vars[1].get()
    print("Champ To Ban:", to_ban)
    print("Champ To Pick:", to_pick)

    if to_pick != "" and to_ban != "":
        makeLabel(app, "In Queue", label_list)
        sleep(1)

        inQueue(app, to_ban, to_pick)
    else:
        makeLabel(app, "Invalid Input!", label_list)


def main():
    label_list = []

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

    makeInputFields(app, [to_ban, to_pick], label_list)

    app.mainloop()
    print("baibai")


if __name__ == "__main__":
    main()