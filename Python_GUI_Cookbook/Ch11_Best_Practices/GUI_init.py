import tkinter as tk
from tkinter import ttk
import __init__
from Python_GUI_Cookbook.Ch11_Best_Practices.Folder1.Folder2.Folder3.MessageBox import clickMe


win = tk.Tk()

win.title("Python GUI")

lFrame = ttk.LabelFrame(win, text="Python GUI Programming Cookbook")
lFrame.grid(column=0, row=0, sticky='WE', padx=10, pady=10)
# def clickMe():
#     from tkinter import messagebox
#     messagebox.showinfo('Message Box', 'Hi from same Level.')
button = ttk.Button(lFrame, text="Click Me ", command=clickMe)
button.grid(column=1, row=0, sticky=tk.S)

win.mainloop()