import tkinter as tk
win = tk.Tk()
text = tk.Text(win, fg="black", bg="white")
text.bind('<Control-o>', lambda e, t=text: t.insert(1.0, 'aaa'))
text.pack()

'''
When an event occurs in Tkinter, it will propagate from the instance level down to the class
level. This means that any bindings which occur on the Text widget class itself, not
specifically our instance, will also happen. This is why we get the additional blank line—the
behavior has been bound to the Text widget at a class level.
'''
def on_control_o(event=None):
    t.insert(1.0, 'aaa')
    return "break"
t = tk.Text(win, fg="black", bg="white")
t.bind('<Control-o>', on_control_o)
t.pack()
win.mainloop()