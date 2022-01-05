import tkinter as tk
import tkinter.ttk as ttk
from emojiSelect import EmojiSelect

class ChatWindow(tk.Toplevel):
    def __init__(self, master, friend_name, friend_username, friend_avatar, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        #configure window
        self.title(friend_name)
        self.geometry('540x640')
        self.minsize(540, 640)
        self.right_frame = tk.Frame(self)
        self.left_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self.left_frame)
        #create widgets
        #left frame
        self.message_area = tk.Text(self.left_frame, bg='white', fg='black', wrap=tk.WORD, width=30)
        self.scrollbar = ttk.Scrollbar(self.left_frame, orient='vertical', command=self.message_area.yview)
        self.message_area.configure(yscrollcommand=self.scrollbar.set)
        #bottom frame
        self.text_area = tk.Text(self.bottom_frame, bg='white', fg='black', height=3, width=30)
        self.send_button = ttk.Button(self.bottom_frame, text='Send', command=self.send_message, style='send.TButton')
        self.text_area.emojis = []
        self.emoji_image = tk.PhotoImage(file='emoji/mikulka-smile-cool.png')
        self.emoji_button = tk.Button(self.bottom_frame, image=self.emoji_image, command=self.emoji_chooser)
        #right frame
        self.profile_picture = tk.PhotoImage(file='images/avatar.png')
        self.friend_profile_picture = tk.PhotoImage(file=friend_avatar)
        self.profile_picture_area = tk.Label(self.right_frame, image=self.profile_picture, relief=tk.RIDGE)
        self.friend_profile_picture_area = tk.Label(self.right_frame, image=self.friend_profile_picture, relief=tk.RIDGE)
        #pack widgets
        #left frame
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.LEFT,fill=tk.Y)
        self.message_area.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.message_area.configure(state='disabled')
        #right frame
        self.right_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.profile_picture_area.pack(side=tk.BOTTOM)
        self.friend_profile_picture_area.pack(side=tk.TOP)
        #bottom frame
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.emoji_button.pack(side=tk.LEFT, pady=5)
        self.text_area.pack(side=tk.LEFT, fill=tk.X, expand=1, pady=5)
        self.send_button.pack(side=tk.RIGHT, pady=5)
        #trigger functions & variables
        self.friend_username = friend_username
        self.configure_styles()
        self.bind_events()
        self.load_history()

    def configure_styles(self):
        style = ttk.Style()
        style.configure('send.TButton', background='#dddddd', foreground="black", padding=16)

    def bind_events(self):
        self.bind('<Return>', self.send_message)
        self.text_area.bind('<Return>', self.send_message)

    def load_history(self):
        history = self.master.requester.prepare_conversation(self.master.username, self.friend_username)
        if len(history['history']):
            for message in history['histoyr']:
                self.receive_message(message['author'], message['message'])
    def send_message(self):
        message = self.text_area.get(1.0, tk.END)
        if message.strip() or len(self.text_area.emojis):
            self.master.requester.send_message(self.master.username, self.friend_username, message,)
            message = 'Me:' + message
            self.message_area.configure(state='normal')
            self.message_area.insert(tk.END, message)
            # self.message_area.configure(state='disabled')
            if len(self.text_area.emojis):
                last_line_no = self.message_area.index(tk.END)
                last_line_no = str(last_line_no).split('.')[0]
                last_line_no = str(int(last_line_no)-2) #to accomodate new line character
            for index, file in self.text_area.emojis:
                global emoji_image
                emoji_image = file
                char_index = str(index).split('.')[0]
                char_index = str(int(char_index)+4) # because of 'Me :' prefix
                emoji_index = last_line_no+'.'+char_index
                self.message_area.image_create(emoji_index, image=emoji_image)
            self.text_area.emojis = []
            self.message_area.configure(state='disabled')
            self.text_area.delete(1.0, tk.END)
        return 'break'

    def receive_message(self, author, message):
        self.message_area.configure(state='normal')
        if author == self.master.username:
            author = 'Me'
        message_with_author = author + ': ' + message
        self.message_area.insert(tk.END, message_with_author)
        self.message_area.configure(state='disabled')

    def add_emoji(self, emoji):
        emoji_index = self.text_area.index(self.text_area.image_create(tk.END, image=emoji))
        self.text_area.emojis.append((emoji_index, emoji))

    def emoji_chooser(self, event=None):
        EmojiSelect(self)

if __name__=='__main__':
    w = tk.Tk()
    c = ChatWindow(w, 'friend', 'images/avatar.png')
    c.protocol('WM_DELETE_WINDOW', w.destroy)
    w.mainloop()