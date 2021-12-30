import tkinter as tk

win = tk.Tk()
win.geometry('400x300')

lab = tk.Label(win, text='Demo app')

menu = tk.Menu()
menu.add_command(label=' Change label text', command=lambda : lab.configure(text='Menu Item Clicked'))
menu.add_command(label=' Change window size', command=lambda : win.geometry('600x600'))

cascade = tk.Menu(win)
cascade.add_command(label='Change Label color', command=lambda : lab.configure(fg='blue4'))
cascade.add_command(label='Change Label highlight', command=lambda : lab.configure(bg='yellow'))

menu.add_cascade(label='Label colours', menu=cascade)
win.configure(menu=menu)
context_menu = tk.Menu(win)
context_menu.add_command(label='close', command=win.destroy)
def on_right_click(event):
    x = win.winfo_x() + event.x
    y = win.winfo_y() + event.y
    context_menu.post(x, y)
win.bind('<Button-3>', on_right_click)
lab.pack(padx=50, pady=50)
win.mainloop()