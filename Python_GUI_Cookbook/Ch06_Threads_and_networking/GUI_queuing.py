#imports
import queue
import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
import Python_GUI_Cookbook.Ch04_oop.GUI_Tooltip as tt
from threading import Thread
from queue import Queue
import Python_GUI_Cookbook.Ch06_Threads_and_networking.Queues as bq


#GLOBALS
GLOBAL_CONST=42
#radiobutton globals
colors = ['blue','red','gold']


class OOP():
    def __init__(self):
        #create instance
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.create_widgets()
        #create a queue
        self.gui_queue = Queue()

    def use_queues(self):
        while True:
            print(self.gui_queue.get())

    def method_in_a_thread(self, numOfLoops=5):
        print('Hi!')
        # non-threaded code with sleep that will freeze GUi
        for idx in range(numOfLoops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
            print('methodInThread:', self.run_thread.is_alive())

    #working with threads
    def create_thread(self, args):
        self.run_thread = Thread(target=self.method_in_a_thread, args=[args])
        self.run_thread.setDaemon(True)
        self.run_thread.start()
        # print(self.run_thread)
        # print('createThread:', self.run_thread.is_alive())
        #start queue in it's own thread
        write_thread = Thread(target=self.use_queues, daemon=True)
        write_thread.start()

    #callback methods
    def click(self):
        self.action.configure(text='Hello '+ self.name.get()+' '+ self.number.get())
        #self.create_thread()
        self.a_label.configure(foreground='red')
        self.a_label.configure(text='A red label')
        bq.write_to_scrol(self)



    def radCall(self):
        self.redSel = self.radVar.get()
        if self.redSel == 0: self.mighty2.configure(text=colors[self.redSel])
        elif self.redSel == 1: self.mighty2.configure(text=colors[self.redSel])
        elif self.redSel == 2: self.mighty2.configure(text=colors[self.redSel])

    def run_progressbar(self):
        self.progress_bar['maximum']=100
        for i in range(101):
            sleep(0.05)
            self.progress_bar['value'] = i
            self.progress_bar.update()
        self.progress_bar['value'] = 0

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def stop_after_progressbar(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop())

    def _spin(self):
        value = self.spin.get()
        #print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    #methods for menu
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    #message obx examples
    def _msgbox(self):
        # msg.showinfo('Python message info box','Created using Tkinter.\n2022')
        # msg.showwarning('Python message warning box', 'Created using Tkinter.\n2022')
        # msg.showerror('Python message error box', 'Created using Tkinter.\n2022')
        self.answer = self.msg.askyesnocancel('Multiple choice box','DO you want to do this?')
        #print(self.answer)


    def create_widgets(self):
        #create tabs
        self.tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Tab1')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Tab2')
        self.tabControl.pack(expand=1, fill='both')
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Tab3')
        self.tabControl.pack(expand=1, fill='both')

        #create container for all widgets
        self.mighty = ttk.LabelFrame(self.tab1, text='Mighty Python')
        self.mighty.grid(column=0, row=0, padx=8, pady=4)
        self.mighty2 = ttk.LabelFrame(self.tab2, text='The Snake')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        # add label
        self.a_label = ttk.Label(self.mighty, text="Enter a name")
        self.a_label.grid(column=0, row=0)

        #adding a text to text box entry widget
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(self.mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')

        #add button
        self.action = ttk.Button(self.mighty,text='Click me!', command=self.click)
        self.action.grid(column=1, row=1)
        #action.configure(state='disable') #disabling a button

        #adding combobox
        ttk.Label(self.mighty,text='Choose a number:').grid(column=0,row=2)
        self.number = tk.StringVar()
        self.number_chosen = ttk.Combobox(self.mighty, width=14, textvariable=self.number, state='readonly')
        self.number_chosen['values'] = (1,2,4,6,8)
        self.number_chosen.grid(column=1, row=2)
        self.number_chosen.current(0)

        #adding checkbox
        self.chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.mighty2, text='Disabled', variable=self.chVarDis, state='disabled')
        self.check1.select()
        self.check1.grid(column=0, row=3)

        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.mighty2, text='UnChecked', variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=3)

        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.mighty2, text='Enabled', variable=self.chVarEn)
        self.check3.select()
        self.check3.grid(column=2, row=3)

        #creating radiobuttons
        self.radVar = tk.IntVar()
        self.radVar.set(99)

        #create radiobuttons in a loop
        for col in range(3):
            self.curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            self.curRad.grid(column=col, row=4, sticky=tk.W)

        #scrollbar widget
        scroll_w = 40
        scroll_h = 10
        self.scr = scrolledtext.ScrolledText(self.mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=5, sticky='WE', columnspan=3)

        #add progressbar
        self.progress_bar = ttk.Progressbar(self.tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        #adding button frame
        self.buttons_frame = ttk.LabelFrame(self.mighty2, text='Labels in the frame')
        self.buttons_frame.grid(column=0, row=7, padx=20, pady=40) #frame can be put in any column

        #place labels into the container
        ttk.Button(self.buttons_frame, text='Run progressbar', command=self.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(self.buttons_frame, text='Start progressbar', command=self.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(self.buttons_frame, text='Stop immediately', command=self.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(self.buttons_frame, text='Stop after second', command=self.stop_after_progressbar).grid(column=0, row=3, sticky='W')


        #adding spinbox widget
        self.spin = Spinbox(self.mighty, from_=0, to=10, width=5, bd=5, command=self._spin)
        self.spin.grid(column=0, row=3, sticky='W')
        #second spinbox in different style
        self.spin = Spinbox(self.mighty, values=(1,2,4,10), width=5, bd=10, command=self._spin, relief=tk.GROOVE)
        self.spin.grid(column=1, row=3, sticky='W')




        #add padding in a loop
        for child in self.buttons_frame.winfo_children():
            child.grid_configure(padx=8, pady=4)

        for child in self.mighty.winfo_children():
            child.grid_configure(sticky='W')





        #create menubar
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)

        #add items to menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self._quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        #creating another menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About', command=self._msgbox)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

        self.tab3_frame = tk.Frame(self.tab3, bg='blue')
        self.tab3_frame.pack()
        for orange_color in range(2):
            self.canvas = tk.Canvas(self.tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
            self.canvas.grid(row=orange_color, column=orange_color)

        #set focus on entry point
        self.name_entered.focus()

        #add a tooltip
        tt.create_ToolTip(self.spin,'This is a Spin control')
        #tt.create_ToolTip(self.scr, 'This is a scroll')



#START GUI
oop = OOP()

#running methods in a thread
run_thread = Thread(target=oop.method_in_a_thread)

oop.win.mainloop()