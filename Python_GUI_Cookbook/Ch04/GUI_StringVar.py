import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()

strData.set('test')

varData = strData.get()

print(varData)