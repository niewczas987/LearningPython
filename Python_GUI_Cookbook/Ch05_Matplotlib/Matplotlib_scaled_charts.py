#imports
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')
#defining plots
axis = fig.add_subplot(111) #2 rows, 1 column, Top Graph

x_Values = [1,2,3,4]
y_Values0 = [5,6,7,8]
y_Values1 = [5.5,6.5,50,4.5]
y_Values2 = [5.1,6.1,7,8.1]
y_all = [y_Values0, y_Values1, y_Values2]

#flatten list o list retireving minimal value
minY = min([y for yValues in y_all for y in yValues])
upperLimitY=20
maxY = max([y for yValues in y_all for y in yValues if y < upperLimitY])
#structure of the chart - IMPORTANT: Commas are mandatory
t1, = axis.plot(x_Values,y_Values0)
t2, = axis.plot(x_Values,y_Values1)
t3, = axis.plot(x_Values,y_Values2)

#grid setting
axis.grid()
axis.set_ylim(minY,maxY) #limiting display onm axis
axis.set_xlim(min(x_Values),max(x_Values))
#set up legend
fig.legend((t1,t2,t3),('First line','Second line','Third line'), 'lower right')

def destroy_window():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', destroy_window)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()