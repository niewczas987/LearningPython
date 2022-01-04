import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from chatWindow import ChatWindow

class FriendsList(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #window configuration
        self.title('Tk Chat')
        self.geometry('700x500')
        #widget decaration
        self.canvas = tk.Canvas(self, bg='white')
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar_frame = ttk.Frame(self.canvas)
        self.scrollbar_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.menu = tk.Menu(self, bg='lightgrey', fg='black', tearoff=0)
        self.friends_menu = tk.Menu(self.menu, bg='lightgrey', fg='black', tearoff=0)
        self.friends_menu.add_command(label='Add friend', command=self.add_friend)
        self.menu.add_cascade(label='Friends', menu=self.friends_menu)
        self.configure(menu=self.menu)
        #pack widgets
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self.friends_area = self.canvas.create_window((0,0), window=self.scrollbar_frame, anchor='nw')
        # trigger functions
        self.bind_events()
        self.load_friends()

    def bind_events(self):
        # self.bind('<Configure>', self.on_frame_resized)
        self.canvas.bind('<Configure>', self.friends_width)

    def on_frame_resized(self):
        # self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        pass

    def load_friends(self):
        friend_frame = ttk.Frame(self.scrollbar_frame)
        '''
        #picture resize - if needed
        picture = Image.open('images/avatar.png')
        resized_picture = picture.resize((100,100), Image.ANTIALIAS)
        profile_photo = ImageTk.PhotoImage(resized_picture)
        '''
        profile_photo = tk.PhotoImage(file='images/avatar.png')
        profile_photo_label = ttk.Label(friend_frame, image=profile_photo)
        profile_photo_label.image = profile_photo
        friend_name = ttk.Label(friend_frame, text='Jan Kowalski', anchor=tk.W)
        message_button = ttk.Button(friend_frame, text='Chat', command=self.open_chat_window)
        #pack widgets
        profile_photo_label.pack(side=tk.LEFT)
        friend_name.pack(side=tk.LEFT)
        message_button.pack(side=tk.RIGHT)
        friend_frame.pack(fill=tk.X, expand=1)

    def open_chat_window(self):
        cw = ChatWindow(self, 'Jan Kowalski', 'images/avatar.png')

    def friends_width(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.friends_area, width=canvas_width)

    def add_friend(self):
        self.load_friends()

if __name__=='__main__':
    fw = FriendsList()
    fw.mainloop()