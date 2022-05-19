'''
Reusing code from 'Python_GUI_Cookbook.Ch01_widgets.GUI_combobox_widget'
Program shows combo of wxPython and tkinter library.
'''

#imports
import tkinter as tk
from tkinter import ttk, scrolledtext

win = tk.Tk() #create instance
win.title("Python GUI")

a_label = ttk.Label(win, text="Enter a name") #create label
a_label.grid(column=0, row=0)

name = tk.StringVar() #adding a text to text box entry widget
name_entered = ttk.Entry(win, width=10, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(win, text='Choose a number:').grid(column=0, row=2) #adding combobox
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=10, textvariable=number)
number_chosen['values'] = (1, 2, 4, 6, 8)
number_chosen.grid(column=1, row=2)
number_chosen.current(0)

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,
wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

#button click event function
def click():
    action.configure(text='Hello '+ name.get())
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

def wxPythonApp():
    import wx
    app = wx.App()
    frame = wx.Frame(None, -1, 'wxPython GUI', size=(200,150))
    frame.SetBackgroundColour('white')
    frame.CreateStatusBar()
    menu = wx.Menu()
    menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
    menuBar = wx.MenuBar()
    menuBar.Append(menu, "File")
    frame.SetMenuBar(menuBar)
    frame.Show()
    app.MainLoop()

action = ttk.Button(win,text='Call python wx GUI!', command=wxPythonApp) #add button
action.grid(column=1, row=1)

#set focus on entry point
name_entered.focus()


if __name__ == '__main__':
    win.mainloop()