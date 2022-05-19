import wx

class GUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent) #init super-class
        parent.CreateStatusBar()    #create status bar
        menu = wx.Menu()# Add Menu Items to the Menu
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT,"Exit"," Exit the GUI")
        menuBar = wx.MenuBar()        # Create the MenuBar
        menuBar.Append(menu,"File")        # Give the Menu a Title
        parent.SetMenuBar(menuBar) #attach menu bar to frame
        button = wx.Button(self, label='Print', pos=(0,60)) #create print button
        self.Bind(wx.EVT_BUTTON, self.print_button, button)
        self.textBox = wx.TextCtrl(self, size=(280,50), style=wx.TE_MULTILINE)

    def print_button(self, event):
        '''callback method for print button'''
        self.textBox.AppendText('Print Btn has been clicked.')


if __name__=='__main__':
    app = wx.App()  #create an instance of wsPython application
    frame = wx.Frame(None, size=(300,180))
    GUI(frame)
    frame.Show()
    app.MainLoop()