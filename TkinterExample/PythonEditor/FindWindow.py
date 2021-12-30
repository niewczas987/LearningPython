import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

class FindWindow(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #configure window
        self.geometry('400x100')
        self.resizable(0,0)
        self.attributes('-toolwindow', True) #removes minimize,maximize buttons
        self.title('Find and replace')
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        #configuring widgets
        self.text_to_find = tk.StringVar()
        self.text_to_replace_with = tk.StringVar()
        self.find_match_index = None
        self.find_search_starting_index = 1.0
        #top frame
        top_frame = tk.Frame(self)
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(0, weight=5)
        find_entry_label = tk.Label(top_frame, text='Find: ').grid(column=0, row=0, sticky=tk.E)
        self.find_entry = ttk.Entry(top_frame, textvar=self.text_to_find, width=30).grid(column=1, row=0, sticky=tk.W)
        #bottom_frame
        middle_frame = tk.Frame(self)
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(0, weight=5)
        replace_entry_label = tk.Label(middle_frame, text='Replace: ').grid(column=0, row=0, sticky=tk.E)
        self.replace_entry = ttk.Entry(middle_frame, textvar=self.text_to_replace_with, width=30).grid(column=1, row=0, sticky=tk.W)
        #button frame
        button_frame = tk.Frame(self)
        button_frame.columnconfigure(0, weight=1)
        self.find_button = ttk.Button(button_frame, text='Find', command=self.on_find).grid(column=0, row=1, sticky=tk.W)
        self.replace_button = ttk.Button(button_frame, text='Replace', command=self.on_replace).grid(column=0, row=2, sticky=tk.W)
        self.cancel_button = ttk.Button(button_frame, text='Cancel', command=self.on_cancel).grid(column=0, row=3, sticky=tk.W)
        #put things on the screen
        top_frame.grid(column=0, row=0, sticky='nsew', pady=15, padx=10)
        middle_frame.grid(column=0, row=1, sticky='nsew', pady=5, padx=10)
        button_frame.grid(column=1, row=0, rowspan=2, sticky='nsew', pady=10, padx=10)

    def on_find(self):
        self.master.find(self.text_to_find.get())

    def on_replace(self):
        self.master.replace_text(self.text_to_find.get(), self.text_to_replace_with.get())

    def on_cancel(self):
        self.master.cancel_find()
        self.destroy()


if __name__=='__main__':
    mw = tk.Tk()
    fw = FindWindow(mw)
    mw.mainloop()
