'''
Connected them further by making one GUI launch another, and, via a simple
multiprocessing Python queue mechanism, we were able to make them communicate with
each other, writing data from a shared queue into both GUIs.
'''

#imports
import tkinter as tk
from tkinter import ttk, scrolledtext
from threading import Thread
from queue import Queue



sharedQueue = Queue() #setup queue
dataInQueue = False

def putDataIntoQueue(data):
    global dataInQueue
    dataInQueue = True
    sharedQueue.put(data)

def readDataFromQueue():
    global dataInQueue
    dataInQueue = False
    return sharedQueue.get()

#set up tkinter app
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

#set up wxPython app
import wx
class GUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        parent.SetBackgroundColour('white')
        parent.CreateStatusBar()
        menu = wx.Menu()
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "File")
        parent.SetMenuBar(menuBar)
        button = wx.Button(self, label="Print", pos=(0,60))
        self.Bind(wx.EVT_BUTTON, self.writeToSharedQueue, button)
        self.textBox = wx.TextCtrl(self, size=(280, 50), style=wx.TE_MULTILINE)

    def writeToSharedQueue(self, event):
        self.textBox.AppendText("The Print Button has been clicked!\n")
        putDataIntoQueue('Hi from wxPython via Shared Queue.\n')
        if dataInQueue:
            data = readDataFromQueue()
            self.textBox.AppendText(data)
            scr.insert('0.0', data) # insert data into tkinter GUI

def wxPythonApp():
    app = wx.App()
    frame = wx.Frame(None, -1, 'wxPython GUI', size=(200,150))

    GUI(frame)
    frame.Show()
    #app.MainLoop() - needs to be deleted for program to work properly
    runT = Thread(target=app.MainLoop)
    runT.setDaemon(True)
    runT.start()
    print(runT)
    print('createThread():', runT.is_alive())

action = ttk.Button(win,text='Call python wx GUI!', command=wxPythonApp) #add button
action.grid(column=1, row=1)

#set focus on entry point
name_entered.focus()


if __name__ == '__main__':
    win.mainloop()