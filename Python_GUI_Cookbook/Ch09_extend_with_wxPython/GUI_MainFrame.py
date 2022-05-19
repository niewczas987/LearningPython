'''imports'''
import wx

'''GLOBALS'''
BACKGROUNDCOLOR = (240,240,240,255)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()

    def exitGUI(self):
        self.Destroy()

    def createWidgets(self):
        self.CreateStatusBar()
        # self.createMenu()
        self.createNotebook()

    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, 'Widgets')
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        boxSizer = wx.BoxSizer()  #layout setting
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)

class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFileFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()

    def createWidgetsFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, 'Widgets Frame', size=(285, -1))
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL) #setting up vertical static box

    def createManageFileFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, 'Manage Files', size=(285, -1))
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)  # setting up vertical static box

    def addWidgets(self):
        # self.addCheckBoxes()
        # self.addRadioButtons()
        self.addStaticBoxWithLabels()

    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)  #add button browse file
        boxSizerH.Add(wx.Button(self.panel, label='Browse to:'))
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(174,-1), value='Z:'))
        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)  # add button copy file
        boxSizerH1.Add(wx.Button(self.panel, label='Copy file to:'))
        boxSizerH1.Add(wx.TextCtrl(self.panel, size=(174, -1), value='Z:/Backup'))
        boxSizerV = wx.BoxSizer(wx.VERTICAL) #arrange box sizers vertically
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)
        self.statBoxSizerMgrV.Add(boxSizerV) #add local box sizer to global


    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV, 1, wx.ALL)
        boxSizerV.Add(self.statBoxSizerMgrV, 1, wx.ALL)
        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)



    def addStaticBoxWithLabels(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        staticBox = wx.StaticBox(self.panel, -1, 'Labels within frames.')
        staticBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        staticText1 = wx.StaticText(self.panel, -1, 'Choose a number')  #add static labels
        boxSizerV.Add(staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText(self.panel, -1, 'Label 2')
        boxSizerV.Add(staticText2, 0, wx.ALL)
        staticBoxSizerV.Add(boxSizerV, 0, wx.ALL)
        boxSizerH.Add(staticBoxSizerV)
        boxSizerH.Add(wx.TextCtrl(self.panel))
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL) #add local box sizer to main frame

if __name__ == '__main__':
    app = wx.App()
    MainFrame(None, size=(350,450))
    app.MainLoop()

