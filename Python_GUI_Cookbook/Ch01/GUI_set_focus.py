#imports
import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#add title
win.title("Exemplary GUI with label")

#button click event function
def click():
    action.configure(text='Hello '+ name.get())
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

# add label
a_label = ttk.Label(win, text="Enter a name")
a_label.grid(column=0, row=0)

#adding a text to text box entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=10, textvariable=name)
name_entered.grid(column=0, row=1)

#add button
action = ttk.Button(win,text='Click me!', command=click)
action.grid(column=1, row=1)
action.configure(state='disable') #disabing a button

#set focus on entry point
name_entered.focus()

#start GUI
win.mainloop()