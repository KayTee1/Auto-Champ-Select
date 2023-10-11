import tkinter as tk
from tkinter import ttk

def makeInputField(entry_var):
    input_frame = tk.Frame(app)
    entry = ttk.Entry(input_frame, textvariable=entry_var)
    button = ttk.Button(input_frame, text='Confirm', command=lambda: getEntryInput(entry_var))
    entry.pack(side='left', padx=10)
    button.pack(side='left')
    input_frame.pack(pady=10)

def makeLabel(string):
    champToBanLabel = ttk.Label(app, text=string, font="calibri 18")
    champToBanLabel.pack()

def getEntryInput(entry_var):
    input_text = entry_var.get()
    print("Input:", input_text)

app = tk.Tk()
app.title("TextBox Input")
app.geometry('400x400')

title_label = ttk.Label(app, text="Automatic Champ Select", font="calibri 24 bold")
title_label.pack()

champ_to_ban = tk.StringVar()
champ_to_pick = tk.StringVar()

makeLabel("Champ To Ban:")
makeInputField(champ_to_ban)

makeLabel("Champ To Pick:")
makeInputField(champ_to_pick)



app.mainloop()
