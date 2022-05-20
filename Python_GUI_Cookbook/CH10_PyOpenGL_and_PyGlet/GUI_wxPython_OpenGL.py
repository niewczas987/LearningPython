'''create a Python GUI that imports PyOpenGL modules'''

#imports
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class GUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)  #initialize super-class
        parent.SetBackgroundColour('white')   #change frame background
        menu = wx.Menu()    #create menu
        menu.Append(wx.ID_ABOUT, 'About', 'wxPython GUI') #add menu items
        menu.AppendSeparator()  #add separator
        menu.Append(wx.ID_EXIT, 'Exit', 'Exit the GUI')
        menuBar = wx.MenuBar() #create a menu bar
        menuBar.Append(menu, 'File')    #give menu a title
        parent.SetMenuBar(menuBar)    #connect menu bar to the frame
        self.textWidget = wx.TextCtrl(self, size=(280, 80), style=wx.TE_MULTILINE) #create text box
        button = wx.Button(self, label="Create OpenGL 3D Cube", pos=(60, 100)) #create button
        self.Bind(wx.EVT_BUTTON, self.buttonCallback, button)

        parent.CreateStatusBar()

    def buttonCallback(self, event):
        self.textWidget.AppendText("Enjoy 3-Dimensional Space in Python.")
        self.textWidget.AppendText("\n*** Use your mouse to spin the Cube! ***\n\n")
        frame = wx.Frame(None, -1, title='Python OpenGL', size=(300, 300), pos=(400, 20))
        CubeCanvas(frame)
        frame.Show(True)

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        #cube 3d start rotation
        self.last_X = self.x = 30
        self.last_Y = self.y = 30
        self.Bind(wx.EVT_SIZE, self.sizeCallback)
        self.Bind(wx.EVT_PAINT, self.paintCallback)
        self.Bind(wx.EVT_LEFT_DOWN, self.mouseDownCallback)
        self.Bind(wx.EVT_LEFT_UP, self.mouseUpCallback)
        self.Bind(wx.EVT_MOTION, self.mouseMotionCallback)

    def sizeCallback(self, event):
        wx.CallAfter(self.setViewport)
        event.Skip()

    def setViewport(self):
        self.size = self.GetClientSize() #get size of the client window
        self.SetCurrent(self.context)
        glViewport(0, 0, self.size.width, self.size.height)

    def paintCallback(self, event):
        wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.initGL()
            self.init = True
        self.onDraw()

    def mouseDownCallback(self, event):
        self.CaptureMouse()
        self.x, self.y, = self.last_X = self.last_Y = event.GetPosition()

    def mouseUpCallback(self, event):
        self.ReleaseMouse()

    def mouseMotionCallback(self, event):
        if event.Dragging() and event.LeftIsDown():
            self.last_X, self.last_Y = self.x, self.y
            self.x, self.y = event.GetPosition()
            self.Refresh(False)


class CubeCanvas(MyCanvasBase):
    def initGL(self):
        glMatrixMode(GL_PROJECTION)        # set viewing projection
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)

        glMatrixMode(GL_MODELVIEW)         # position viewer
        glTranslatef(0.0, 0.0, -2.0)

        glRotatef(self.y, 1.0, 0.0, 0.0)        # position object
        glRotatef(self.x, 0.0, 1.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def onDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)        # clear color and depth buffers

        glBegin(GL_QUADS)        # draw six faces of a cube
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)

        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)

        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)

        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)

        glNormal3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)

        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glEnd()

        width, height = self.size
        width = max(width, 1.0)
        height = max(height, 1.0)
        xScale = 180.0 / width
        yScale = 180.0 / height
        glRotatef((self.y - self.last_Y) * yScale, 1.0, 0.0, 0.0);
        glRotatef((self.x - self.last_X) * xScale, 0.0, 1.0, 0.0);

        self.SwapBuffers()

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(300, 230))
    GUI(frame)
    frame.Show()
    app.MainLoop()