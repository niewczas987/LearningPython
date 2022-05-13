#imports
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')
#defining plots
axis1 = fig.add_subplot(221) #2 rows, 1 column, Top Graph
axis2 = fig.add_subplot(222)
axis3 = fig.add_subplot(223)
axis4 = fig.add_subplot(224)

x_Values = [1,2,3,4]
y_Values = [5,6,7,8]

#structure of the chart
axis1.plot(x_Values,y_Values)
axis1.set_xlabel('Horizontal label 1')
axis1.set_ylabel('Vertical label 1')
#axis1.grid #deault line style
axis1.grid(linestyle='-')

axis2.plot(x_Values,y_Values)
axis2.set_xlabel('Horizontal label 2')
axis2.set_ylabel('Vertical label 2')
#axis2.grid #deault line style
axis2.grid(linestyle='-')

axis3.plot(x_Values,y_Values)
axis3.set_xlabel('Horizontal label 3')
axis3.set_ylabel('Vertical label 3')
#axis3.grid #deault line style
axis3.grid(linestyle='-')

axis4.plot(x_Values,y_Values)
axis4.set_xlabel('Horizontal label 4')
axis4.set_ylabel('Vertical label 4')
axis4.grid #deault line style
# axis4.grid(linestyle='-')

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