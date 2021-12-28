import tkinter as tk
import tkinter.ttk as ttk

from TextArea import TextArea

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text_area = TextArea(self, bg='white', fg='black', undo=True)
        self.scrollbar = ttk.Scrollbar(orient='vertical', command=self.scroll_text)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.line_number = tk.Text(self, bg='grey', fg='white')
        first_500_numbers = [str(n+1) for n in range(100)]
        self.line_number.insert(1.0, '\n'.join(first_500_numbers))
        self.line_number.configure(state='disabled', width=3)
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
        self.line_number.bind("<MouseWheel>", lambda e: "break")
        self.line_number.bind("<Button-4>", lambda e: "break")
        self.line_number.bind("<Button-5>", lambda e: "break")

if __name__=='__main__':
    mw = MainWindow()
    mw.mainloop()