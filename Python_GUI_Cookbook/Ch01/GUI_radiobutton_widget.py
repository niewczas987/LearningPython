#imports
import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#add title
win.title("Exemplary GUI with label")

#button click event function
def click():
    action.configure(text='Hello '+ name.get()+' '+number.get())
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
#action.configure(state='disable') #disabing a button

#adding combobox
ttk.Label(win,text='Choose a number:').grid(column=0,row=2)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=10, textvariable = number, state='readonly')
number_chosen['values'] = (1,2,4,6,8)
number_chosen.grid(column=1, row=2)
number_chosen.current(0)

#adding checkbox
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=3)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='UnChecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=3)

#radiobutton globals
COLOR1 = 'red'
COLOR2 = 'gold'
COLOR3 = 'blue'

#radiobutton callback
def radCall():
    redSel = radVar.get()
    if redSel == 1: win.configure(background=COLOR1)
    elif redSel == 2: win.configure(background=COLOR2)
    elif redSel == 3: win.configure(background=COLOR3)

#creating radiobuttons
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1,command=radCall)
rad1.grid(column=0, row=4, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2,command=radCall)
rad2.grid(column=1, row=4, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3,command=radCall)
rad3.grid(column=2, row=4, sticky=tk.W, columnspan=3)

#set focus on entry point
name_entered.focus()

#start GUI
win.mainloop()