import tkinter as tk
import tkinter.messagebox as msgbox
# print(tk.TkVersion) #check your Tkinter version

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world')
        self.label_text = tk.StringVar()
        self.label_text.set('My name is:')
        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)
        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self,text='Say Hello', command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))
        goodbye_button = tk.Button(self,text='Say Goodbye', command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        message = 'Hello there '+self.name_entry.get()
        msgbox.showwarning('Hello',message)
    def say_goodbye(self):
        if msgbox.askyesno('Close window?','Would you like to close the window?'):
            self.label_text.set('Window will close in 2 sec')
            msgbox.showerror('Goodbye','ELO '+self.name_entry.get())
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo('Not closing','Window will stay open.')
if __name__ == '__main__':
    window = Window()
    window.mainloop()