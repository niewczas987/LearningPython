#imports
import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#add title
win.title("Exemplary GUI with label")

#add label
ttk.Label(win,text="TEST LABEL").grid(column=0, row=0)

#start GUI
win.mainloop()