'''
PyGlet 3D example
'''
# imports
import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

# global variables
WINDOW = 400
INCREMENT = 5


class Window(pyglet.window.Window):
    xRotation = yRotation = 30  # cube 3d start rotation

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

    def on_draw(self):
        self.clear() #clear current GL Window
        glPushMatrix()

pyglet.app.run()
