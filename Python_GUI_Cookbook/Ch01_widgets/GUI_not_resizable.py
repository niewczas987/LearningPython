#imports
import tkinter as tk

#create instance
win = tk.Tk()

#add title
win.title("Non-resizable GUI")

#disable resizing
win.resizable(False,False)

#start GUI
win.mainloop()