import tkinter as tk
import tkinter.ttk as ttk

from TextArea import TextArea
from Highlighter import Highlighter
from LineNumbers import LineNumbers
from FindWindow import FindWindow

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor')
        self.text_area = TextArea(self, bg='white', fg='black', undo=True)
        self.scrollbar = ttk.Scrollbar(orient='vertical', command=self.scroll_text)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.highlighter = Highlighter(self.text_area, 'languages/python.yaml')
        self.line_number = LineNumbers(self, self.text_area, bg='grey', fg='white', width=1)
        self.bind_events()
        #packing
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.line_number.pack(side=tk.LEFT, fill=tk.Y)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def scroll_text(self,*args):
        if len(args)>1:
            self.line_number.yview_moveto((args[1]))
            self.text_area.yview_moveto(args[1])
        else:
            event = args[0]
            if event.delta:
                move = -1 * (event.delta/120)
            else:
                if event.num == 5:
                    move = 1
                else:
                    move = -1
            self.line_number.yview_moveto(int(move),'units')
            self.text_area.yview_moveto(int(move),'units')

    def bind_events(self):
        self.text_area.bind('<MouseWheel>', self.scroll_text)
        self.text_area.bind('<Button-4>', self.scroll_text)
        self.text_area.bind('<Button-5>', self.scroll_text)
        self.line_number.bind('<MouseWheel>', lambda e: 'break')
        self.line_number.bind('<Button-4>', lambda e: 'break')
        self.line_number.bind('<Button-5>', lambda e: 'break')
        self.text_area.bind('<Control-f>', self.show_find_window)

    def show_find_window(self, event=None):
        FindWindow(self.text_area)

if __name__=='__main__':
    mw = MainWindow()
    mw.mainloop()