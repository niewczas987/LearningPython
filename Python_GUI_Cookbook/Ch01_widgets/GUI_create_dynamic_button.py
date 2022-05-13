#imports
import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#add title
win.title("Exemplary GUI with label")

#button click event function
def click():
    action.configure(text='I have been clicked')
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

# add label
a_label = ttk.Label(win, text="TEST LABEL")
a_label.grid(column=0, row=0)

#add button
action = ttk.Button(win,text='Click me!', command=click)
action.grid(column=0, row=1)

#start GUI
win.mainloop()