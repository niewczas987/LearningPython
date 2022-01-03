import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import families

class FontChooser(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.master = master
        # self.transient(self.master)
        self.geometry('300x250')
        self.resizable(0,0)
        self.attributes('-toolwindow', True)
        self.title('Choose font and size')
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=2)
        self.configure(bg=self.master.background)
        #configuring widgets
        self.font_list = tk.Listbox(self, exportselection=False)
        self.available_fonts = sorted(families())
        #get_fonts into widget
        for family in self.available_fonts:
            self.font_list.insert(tk.END, family)
        current_selection_index = self.available_fonts.index(self.master.font_family)
        if current_selection_index:
            self.font_list.select_set(current_selection_index)
            self.font_list.see(current_selection_index)
        #get font sizes into widget
        current_size_value = tk.StringVar(value=self.master.font_size)
        self.size_input = tk.Spinbox(self, from_=5, to=99, textvariable=current_size_value)
        #buttons
        self.save_button = ttk.Button(self, text='Save', command=self.save)
        self.cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        #pack widgets
        self.font_list.grid(column=0, row=0, sticky='nsew', pady=15, padx=10)
        self.size_input.grid(column=1, row=0, sticky='nsew', pady=15, padx=10)
        self.save_button.grid(column=0, row=1, columnspan=1)
        self.cancel_button.grid(column=1, row=1)

    def save(self):
        font_family = self.font_list.get(self.font_list.curselection()[0])
        font_size = self.size_input.get()
        yaml_file_contents = f'family: {font_family}\n' + f'size: {font_size}'
        with open('schemes/font.yaml','w') as file:
            file.write(yaml_file_contents)
        self.master.update_font()
        self.destroy()

if __name__=='__main__':
    from TextEditor import MainWindow
    mw = MainWindow()
    fw = FontChooser(mw)
    mw.mainloop()