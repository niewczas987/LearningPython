#imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
colors = ['blue','red','gold']

#radiobutton callback
def radCall():
    redSel = radVar.get()
    if redSel == 0: win.configure(background=colors[redSel])
    elif redSel == 1: win.configure(background=colors[redSel])
    elif redSel == 2: win.configure(background=colors[redSel])

#creating radiobuttons
radVar = tk.IntVar()
radVar.set(99)

#create radiobuttons in a loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=4, sticky=tk.W)

#scrollbar widget
scroll_w = 30
scroll_h = 5
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

#adding labelframe
buttons_frame = ttk.LabelFrame(win, text='Labels in the frame')
buttons_frame.grid(column=0, row=7, padx=20, pady=40) #frame can be put in any column

#place labels into the container
ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label2').grid(column=1, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text='Label3').grid(column=2, row=2, sticky=tk.W)

#set focus on entry point
name_entered.focus()

#start GUI
win.mainloop()