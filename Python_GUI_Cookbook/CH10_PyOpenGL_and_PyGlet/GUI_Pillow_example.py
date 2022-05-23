'''
GUI that shuffles slides within a window frame
'''
import os
from tkinter import Tk, PhotoImage, Label
from itertools import cycle
from os import listdir


class SlideShow(Tk):
    #inherit GUI framework extending tkinter
    def __init__(self, meShowTimeBetweenSlides=1500):
        Tk.__init__(self) #init tkinter super-class
        self.showTime = meShowTimeBetweenSlides
        listOfSlides = [slide for slide in listdir(os.curdir) if slide.endswith('gif')]
        self.iterableCycle = cycle((PhotoImage(file=slide), slide) for slide in listOfSlides) #cycle slides to show on the tkinter Label
        self.slidesLabel = Label(self) #tkinter label to display images
        self.slidesLabel.pack()        #create the Frame widget

    def slidesCallback(self):
        currentInstance, nameOfSlide = next(self.iterableCycle)         #get next slide from iterable cycle
        self.slidesLabel.config(image=currentInstance)         #assign next slide to Label widget
        self.title(nameOfSlide)         #update Window title with current slide
        self.after(self.showTime, self.slidesCallback)         #recursively repeat the Show

if __name__=='__main__':
    win = SlideShow()
    win.after(0, win.slidesCallback())
    win.mainloop()