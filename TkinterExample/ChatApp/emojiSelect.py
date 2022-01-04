import os
import tkinter as tk
import tkinter.ttk as ttk

class EmojiSelect(tk.Toplevel):
    smilies_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'emoji/'))
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.transient = master
        self.position_window()
        self.title('Choose emoji')
        self.attributes('-toolwindow', True)
        emojis = [file for file in os.listdir(self.smilies_dir) if file.endswith('.png')]
        self.emoji_images = []
        for face in emojis:
            full_path = os.path.join(self.smilies_dir, face)
            image = tk.PhotoImage(file=full_path)
            self.emoji_images.append(image)
        for index, file in enumerate(self.emoji_images):
            row, col = divmod(index,3)
            button = ttk.Button(self, image=file, command=lambda s=file: self.insert_emoji(s))
            button.grid(row=row, column=col, sticky='nsew')
        for i in range(3):
            tk.Grid.columnconfigure(self, i, weight=1)
            tk.Grid.rowconfigure(self, i, weight=1)


    def position_window(self):
        master_pos_x = self.master.winfo_x()
        master_pos_y = self.master.winfo_y()
        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()
        my_width = 100
        my_height = 100
        pos_x = (master_pos_x + (master_width//2) - (my_width//2))
        pos_y = (master_pos_y + (master_height//2) - (my_height//2))
        geometry = f"{my_width}x{my_height}+{pos_x}+{pos_y}"
        self.geometry(geometry)

    def insert_emoji(self, smilie_face):
        self.master.add_emoji(smilie_face)
        self.destroy()

if __name__ == '__main__':
    w = tk.Tk()
    s = EmojiSelect(w)
    w.mainloop()