import wx

class GUI(wx.Frame):
    def __init__(self, parent , title, size=(200,100)):
        wx.Frame.__init__(self,parent,title=title, size=size)  #initialize super-class
        self.SetBackgroundColour('white')   #change frame background
        self.CreateStatusBar()        #create status bar
        menu = wx.Menu()    #create menu
        menu.Append(wx.ID_ABOUT, 'About', 'wxPython GUI') #add menu items
        menu.AppendSeparator()  #add separator
        menu.Append(wx.ID_EXIT, 'Exit', 'Exit the GUI')
        menuBar = wx.MenuBar() #create a menu bar
        menuBar.Append(menu, 'File')    #give menu a title
        self.SetMenuBar(menuBar)    #connect menu bar to the frame
        self.Show() #display the frame

app = wx.App()  #create an instance of wsPython application
GUI(None, 'Python GUI using wxPython', (300,150))
app.MainLoop()