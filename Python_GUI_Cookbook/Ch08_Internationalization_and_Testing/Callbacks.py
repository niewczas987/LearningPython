#all callbacks methods migrated from GUI_Callbacks_Refactor.py
#imports
import tkinter as tk
from datetime import datetime
from time import sleep
from tkinter import messagebox as msg
from threading import Thread
import Python_GUI_Cookbook.Ch06_Threads_and_networking.Queues as bq
from tkinter import filedialog as fd
from os import path, makedirs
import pytz


#Globals
fDir = path.dirname(__file__)
netDir = fDir + '\Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)
# radiobutton globals
colors = ['blue', 'red', 'gold']

class Callbacks():
    def __init__(self,oop):
        self.oop = oop

    #TZ button callback
    def allTimeZones(self):
        self.oop.scr.delete(1.0, tk.END)
        for tr in pytz.all_timezones:
            self.oop.scr.insert(tk.INSERT, tr+'\n')

    def localTimeZone(self):
        from tzlocal import get_localzone
        self.oop.scr.delete(1.0, tk.END)
        self.oop.scr.insert(tk.INSERT,get_localzone())


    def default_file_entries(self):
        self.oop.fileEntry.delete(0, tk.END)
        self.oop.fileEntry.insert(0, fDir)
        if len(fDir) > self.oop.entry_length:
            #self.fileEntry.config(width=len(fDir)+3)
            self.oop.fileEntry.config(width=35)
            #self.fileEntry.config(state='readonly')
        self.oop.netwEntry.delete(0, tk.END)
        self.oop.netwEntry.insert(0, netDir)
        if len(netDir) > self.oop.entry_length:
            #self.netwEntry.config(width=len(netDir) + 3)
            self.oop.netwEntry.config(width=35)
            self.oop.netwEntry.config(state='readonly')
    def use_queues(self):
        while True:
            print(self.oop.gui_queue.get())

    def method_in_a_thread(self, numOfLoops=5):
        # non-threaded code with sleep that will freeze GUi
        for idx in range(numOfLoops):
            sleep(1)
            self.oop.scr.insert(tk.INSERT, str(idx) + '\n')
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
        self.oop.action.configure(text='Hello '+ self.oop.name.get()+' '+ self.oop.number.get())
        #self.create_thread()
        self.oop.a_label.configure(foreground='red')
        self.oop.a_label.configure(text='A red label')
        bq.write_to_scrol(self)



    def radCall(self):
        self.redSel = self.oop.radVar.get()
        if self.redSel == 0: self.oop.mighty2.configure(text=colors[self.redSel])
        elif self.redSel == 1: self.oop.mighty2.configure(text=colors[self.redSel])
        elif self.redSel == 2: self.oop.mighty2.configure(text=colors[self.redSel])

    def run_progressbar(self):
        self.oop.progress_bar['maximum']=100
        for i in range(101):
            sleep(0.05)
            self.oop.progress_bar['value'] = i
            self.oop.progress_bar.update()
        self.oop.progress_bar['value'] = 0

    def start_progressbar(self):
        self.oop.progress_bar.start()

    def stop_progressbar(self):
        self.oop.progress_bar.stop()

    def stop_after_progressbar(self, wait_ms=1000):
        self.oop.win.after(wait_ms, self.oop.progress_bar.stop())

    def _spin(self):
        value = self.oop.spin.get()
        #print(value)
        self.oop.scr.insert(tk.INSERT, value + '\n')

    #methods for menu
    def _quit(self):
        self.oop.win.quit()
        self.oop.win.destroy()
        exit()

    #message obx examples
    def _msgbox(self):
        # msg.showinfo('Python message info box','Created using Tkinter.\n2022')
        # msg.showwarning('Python message warning box', 'Created using Tkinter.\n2022')
        # msg.showerror('Python message error box', 'Created using Tkinter.\n2022')
        self.answer = self.oop.msg.askyesnocancel('Multiple choice box','Do you want to do this?')
        #print(self.answer)

    def get_file_name(self):
        # print('Hello from GetFile')
        self.oop.fileEntry.delete(0,tk.END)
        fDir = path.dirname(__file__)
        fName = fd.askopenfilename(parent=self.oop.win, initialdir=fDir)
        self.oop.fileEntry.insert(0,fName)
        self.oop.fileEntry.config(width=len(fName) + 3)
        self.oop.fileEntry.update()
        self.oop.win.update()

    def copy_file(self):
        import shutil
        src = self.oop.fileEntry.get()
        file = src.split('/')[-1]
        dst = self.oop.netwEntry.get() +'\\'+ file
        try:
            shutil.copy(src, dst)
            msg.showinfo('Copy file to Network', 'Success. File copied')
        except FileNotFoundError as err:
            msg.showerror('Copy file to Network', '*** Failed to copy file. \nError:'+str(err))
        except Exception as ex:
            msg.showerror('Copy file to Network', '*** Failed to copy file. \n Exception:'+str(ex))

    def insert_quote(self):
        title = self.oop.book_name.get()
        page = self.oop.page_nr.get()
        quote = self.oop.quot_scr.get(1.0,tk.END)
        #print(title)
        #print(quote)
        self.oop.sql_obj.insertBooks(title,page,quote)

    def get_books(self):
        self.oop.quot_scr.delete(1.0,tk.END)
        all_books = self.oop.sql_obj.showBooks()
        for book in all_books:
            self.oop.quot_scr.insert(tk.INSERT, book[1]+'\n')

    def get_quotes(self):
        self.oop.quot_scr.delete(1.0,tk.END)
        all_books = self.oop.sql_obj.showQuotes()
        for book in all_books:
            self.oop.quot_scr.insert(tk.INSERT, 'Book: %s\n Quote: %s'%(book[1], book[0])+'\n')

    def getDateTime(self):
        fmtStrZone = '%Y-%m-%d %H:%M:%S %Z%z'
        #get coordinated Universal time
        from pytz import timezone
        utc = datetime.now(timezone('UTC'))
        # print(utc.strftime(fmtStrZone))
        #convert utc to Los Angeles TimeZone
        la = utc.astimezone(timezone('America/Los_Angeles'))
        # print(la.strftime(fmtStrZone))
        # convert utc to New York TimeZone
        ny = utc.astimezone(timezone('America/New_York'))
        # print(ny.strftime(fmtStrZone))
        self.oop.TZ.set(ny.strftime(fmtStrZone))
        self.oop.win.update()
        return utc.strftime(fmtStrZone)