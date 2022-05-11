#imports
import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox

#tooltip
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self,tip_text):
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox('insert') #get a size of widget
        x = x + self.widget.winfo_rootx() + 25 #configure where to display tooltip window
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget) #create new tooltip window
        tw.wm_overrideredirect(True)    #remove window decoration
        tw.wm_geometry('+%d+%d' % (x,y))
        label = tk.Label(tw, text=tip_text, justify=tk.LEFT, background='#ffffe0', relief=tk.SOLID, borderwidth=1, font=('tahoma','8','normal'))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

def create_ToolTip(widget,text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



#create instance
win = tk.Tk()
win.title("Python GUI")
#adding icon
win.iconbitmap('icon.ico')

#create tabs
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab2')
tabControl.pack(expand=1, fill='both')

#create container for all widgets
mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)
mighty2 = ttk.LabelFrame(tab2, text='The Snake')
mighty2.grid(column=0, row=0, padx=8, pady=4)

#button click event function
def click():
    action.configure(text='Hello '+ name.get()+' '+number.get())
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

# add label
a_label = ttk.Label(mighty, text="Enter a name")
a_label.grid(column=0, row=0)

#adding a text to text box entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=10, textvariable=name)
name_entered.grid(column=0, row=1)

#add button
action = ttk.Button(mighty,text='Click me!', command=click)
action.grid(column=1, row=1)
#action.configure(state='disable') #disabling a button

#adding combobox
ttk.Label(mighty,text='Choose a number:').grid(column=0,row=2)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=10, textvariable = number, state='readonly')
number_chosen['values'] = (1,2,4,6,8)
number_chosen.grid(column=1, row=2)
number_chosen.current(0)

#adding checkbox
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=3)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text='UnChecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=3)

#radiobutton globals
colors = ['blue','red','gold']

#radiobutton callback
def radCall():
    redSel = radVar.get()
    if redSel == 0: mighty2.configure(text=colors[redSel])
    elif redSel == 1: mighty2.configure(text=colors[redSel])
    elif redSel == 2: mighty2.configure(text=colors[redSel])

#creating radiobuttons
radVar = tk.IntVar()
radVar.set(99)

#create radiobuttons in a loop
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=4, sticky=tk.W)

#scrollbar widget
scroll_w = 30
scroll_h = 5
scr = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)

#add progressbar
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)

#update progressbar method
def run_progressbar():
    progress_bar['maximum']=100
    for i in range(101):
        sleep(0.05)
        progress_bar['value'] = i
        progress_bar.update()
    progress_bar['value'] = 0

#progress bar events handling
def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def stop_after_progressbar(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop())

#adding button frame
buttons_frame = ttk.LabelFrame(mighty2, text='Labels in the frame')
buttons_frame.grid(column=0, row=7, padx=20, pady=40) #frame can be put in any column

#place labels into the container
ttk.Button(buttons_frame, text='Run progressbar', command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text='Start progressbar', command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text='Stop immediately', command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text='Stop after second', command=stop_after_progressbar).grid(column=0, row=3, sticky='W')



#spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

#adding spinbox widget
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=5, command=_spin)
spin.grid(column=0, row=3)
#second spinbox in different style
spin = Spinbox(mighty, values=(1,2,4,10), width=5, bd=10, command=_spin, relief=tk.GROOVE)
spin.grid(column=1, row=3)




#add padding in a loop
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in mighty.winfo_children():
    child.grid_configure(sticky='W')



#methods for menu
def _quit():
    win.quit()
    win.destroy()
    exit()

#message obx examples
def _msgbox():
    # msg.showinfo('Python message info box','Created using Tkinter.\n2022')
    # msg.showwarning('Python message warning box', 'Created using Tkinter.\n2022')
    # msg.showerror('Python message error box', 'Created using Tkinter.\n2022')
    answer = msg.askyesnocancel('Multiple choice box','DO you want to do this?')
    print(answer)

#create menubar
menu_bar = Menu(win)
win.config(menu=menu_bar)

#add items to menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

#creating another menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=_msgbox)
menu_bar.add_cascade(label='Help', menu=help_menu)




#set focus on entry point
name_entered.focus()

#add a tooltip
create_ToolTip(spin,'This is a sSpin control')
create_ToolTip(scr, 'This is a scroll')



#start GUI
win.mainloop()