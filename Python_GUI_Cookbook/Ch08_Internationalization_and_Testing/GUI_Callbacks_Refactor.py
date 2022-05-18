#imports
import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, Spinbox, messagebox
import Python_GUI_Cookbook.Ch04_oop.GUI_Tooltip as tt
from threading import Thread
from queue import Queue
from os import path, makedirs
import Python_GUI_Cookbook.Ch06_Threads_and_networking.TCP_Server as tcp
import Python_GUI_Cookbook.Ch07_Storing_data_in_MySQL_Database.SQLite_Class as sql
from Python_GUI_Cookbook.Ch08_Internationalization_and_Testing.Language_Resources import I18N
from Python_GUI_Cookbook.Ch08_Internationalization_and_Testing.Callbacks import Callbacks

#GLOBALS
GLOBAL_CONST=42
fDir = path.dirname(__file__)
netDir = fDir + '\Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)

#radiobutton globals
colors = ['blue','red','gold']


class OOP():
    def __init__(self):
        #create instance
        self.win = tk.Tk()
        self.i18n = I18N('en')
        self.win.title(self.i18n.title)
        #callbacks methods import
        self.callBacks = Callbacks(self)
        #create widgets
        self.create_widgets()
        self.callBacks.default_file_entries()
        self.sql_obj = sql.SQLite()
        #create a queue
        self.gui_queue = Queue()
        #create msg object
        self.msg = messagebox
        # start TCP server in it's own thread
        srvT = Thread(target=tcp.start_server)
        srvT.setDaemon(True)
        srvT.start()


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
        self.tab4 = ttk.Frame(self.tabControl)
        #commented for chapter 8
        # self.tabControl.add(self.tab4, text='SQLite3')
        # self.tabControl.pack(expand=1, fill='both')

        #adding a TZ butotns
        self.allTZs = ttk.Button(self.tab1, text=self.i18n.timeZones,command=self.callBacks.allTimeZones)
        self.allTZs.grid(column=0, row=9, sticky='WE')
        self.localTZ = ttk.Button(self.tab1, text=self.i18n.localZone, command=self.callBacks.localTimeZone)
        self.localTZ.grid(column=0, row=10, sticky='WE')
        self.nyTZ = ttk.Button(self.tab1, text='NY Time', command=self.callBacks.getDateTime)
        self.nyTZ.grid(column=0, row=11, sticky='WE')
        self.TZ = tk.StringVar()
        self.lblTZ = ttk.Label(self.tab1, textvariable=self.TZ)
        self.lblTZ.grid(column=0, row=12)


        #create container for all widgets
        self.mighty = ttk.LabelFrame(self.tab1, text='Mighty Python')
        self.mighty.grid(column=0, row=0, padx=8, pady=4)
        self.mighty2 = ttk.LabelFrame(self.tab2, text='The Snake')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        # create container for SQL data
        self.sql_cont = ttk.LabelFrame(self.tab4, text='Python Database')
        self.sql_cont.grid(column=0, row=0, padx=8, pady=4)
        self.quot_cont = ttk.LabelFrame(self.tab4, text='Book quotation')
        self.quot_cont.grid(column=0, row=1, padx=8, pady=4)
        #add textboxes
        self.book_name = tk.StringVar()
        self.page_nr = tk.IntVar()
        self.book_name_entry = ttk.Entry(self.sql_cont, width=30, textvariable=self.book_name)
        self.book_name_entry.grid(column=0, row=0, sticky='W')
        self.page_nr_entry = ttk.Entry(self.sql_cont, width=10, textvariable=self.page_nr)
        self.page_nr_entry.grid(column=1, row=0, sticky='W')
        #add buttons
        self.insert_quote_btn = ttk.Button(self.sql_cont,width=15, text='Insert quote', command=self.callBacks.insert_quote)
        self.insert_quote_btn.grid(column=3, row=0)
        self.get_quotes_btn = ttk.Button(self.sql_cont,width=15, text='Get books', command=self.callBacks.get_books)
        self.get_quotes_btn.grid(column=3, row=1)
        self.modify_quote_btn = ttk.Button(self.sql_cont,width=15, text='Get quotes', command=self.callBacks.get_quotes)
        self.modify_quote_btn.grid(column=3, row=2)
        #add scrolled text widget for quotation
        self.quot_scr = scrolledtext.ScrolledText(self.quot_cont, width=40, height=20, wrap=tk.WORD)
        self.quot_scr.grid(column=0, row=0, sticky='WE', columnspan=3)

        # add label
        self.a_label = ttk.Label(self.mighty, text="Enter a name")
        self.a_label.grid(column=0, row=0)

        #adding a text to text box entry widget
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(self.mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')
        self.name_entered.delete(0, tk.END)
        self.name_entered.insert(0,'<default name>')

        #add button
        self.action = ttk.Button(self.mighty,text='Click me!', command=self.callBacks.click)
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
            self.curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, value=col, command=self.callBacks.radCall)
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
        ttk.Button(self.buttons_frame, text='Run progressbar', command=self.callBacks.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(self.buttons_frame, text='Start progressbar', command=self.callBacks.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(self.buttons_frame, text='Stop immediately', command=self.callBacks.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(self.buttons_frame, text='Stop after second', command=self.callBacks.stop_after_progressbar).grid(column=0, row=3, sticky='W')


        #adding spinbox widget
        self.spin = Spinbox(self.mighty, from_=0, to=10, width=5, bd=5, command=self.callBacks._spin)
        self.spin.grid(column=0, row=3, sticky='W')
        #second spinbox in different style
        self.spin = Spinbox(self.mighty, values=(1,2,4,10), width=5, bd=10, command=self.callBacks._spin, relief=tk.GROOVE)
        self.spin.grid(column=1, row=3, sticky='W')

        # create Manage File frame
        mngFilesFrame = ttk.LabelFrame(self.tab2, text='Manage files:')
        mngFilesFrame.grid(column=0, row=4, sticky='WE', padx=10, pady=5)
        # add button to browse files
        lb = ttk.Button(mngFilesFrame, text='Browse files', command=self.callBacks.get_file_name)
        lb.grid(column=0, row=0, sticky='W')
        # files handling
        file = tk.StringVar()
        self.entry_length = scroll_w
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entry_length, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)
        #handling network directory
        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entry_length, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)
        #create trigger button
        cb = ttk.Button(mngFilesFrame, text='Copy file to:', command=self.callBacks.copy_file)
        cb.grid(column=0, row=1, sticky=tk.E)


        #add padding in a loop
        for child in self.buttons_frame.winfo_children():
            child.grid_configure(padx=8, pady=4)

        for child in self.mighty.winfo_children():
            child.grid_configure(sticky='W')
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)





        #create menubar
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)

        #add items to menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.callBacks._quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        #creating another menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About', command=self.callBacks._msgbox)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

        self.tab3_frame = tk.Frame(self.tab3, bg='blue')
        self.tab3_frame.pack()
        for orange_color in range(2):
            self.canvas = tk.Canvas(self.tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
            self.canvas.grid(row=orange_color, column=orange_color)

        #set focus on entry point
        #self.name_entered.focus()
        self.tabControl.select(1)

        #add a tooltip
        tt.create_ToolTip(self.spin,'This is a Spin control')
        #tt.create_ToolTip(self.scr, 'This is a scroll')



#START GUI
oop = OOP()

#running methods in a thread
run_thread = Thread(target=Callbacks.method_in_a_thread)




oop.win.mainloop()