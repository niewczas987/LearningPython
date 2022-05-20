from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# initial position and size
x = GLfloat(0.0).value
y = GLfloat(0.0).value
rect_size = GLfloat(25.0).value

# number of pixels to move each step
xstep = GLfloat(1.0).value
ystep = GLfloat(1.0).value

# initialize bouncing window
windowWidth = GLfloat(133).value       # 800/600 = 1.33
windowHeight = GLfloat(100).value

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)  # clear window with color defined in SetupRC
    glColor3f(1.0, 0.0, 0.0)
    glRectf(x, y, x + rect_size, y - rect_size)  # draw filled rectangle - animation call
    glFlush()  # flush/execute openGL drawing commands
    glutSwapBuffers() #flush and swap double buffers


def TimerFunction(value):
    global x, xstep, y, ystep

    # reverse direction left/right
    if ((x > windowWidth - rect_size) or (x < -windowWidth)):
        xstep = -xstep

    # reverse direction top/bottom
    if ((y > windowHeight) or (y < -windowHeight + rect_size)):
        ystep = -ystep

    # move the red square
    x += xstep
    y += ystep

    # check the bounds of the clipping area
    if (x > (windowWidth - rect_size + xstep)):
        x = windowWidth - rect_size - 1
    elif (x < -(windowWidth + xstep)):
        x = -windowWidth - 1

    if (y > (windowHeight + ystep)):
        y = windowHeight - 1
    elif (y < -(windowHeight - rect_size + ystep)):
        y = -windowHeight + rect_size - 1

    # redraw the scene
    glutPostRedisplay()
    glutTimerFunc(33, TimerFunction, 1)  # recursive call


def SetupRC():  # rendering context
    glClearColor(0.0, 0.0, 1.0, 1.0)  # blue color

def ChangeSize(w, h):                   # callback when window size changes
    if h == 0: h =1                     # prevent divide by zero
    glViewport(0, 0, w, h)              # set Viewport to Window dimensions
    glMatrixMode(GL_PROJECTION)         # define the viewing volume
    glLoadIdentity()                    # reset coordinate system
    aspectRatio = GLfloat(w).value / GLfloat(h).value   # establish clipping volume
                                                        # GLfloat becomes ctypes.c_float
                                                        # Use the value attribute before dividing
    if w <= h: glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)
    else:      glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)    # single buffer; RGBA color mode
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'Bouncing square')                     # Python 3: bytes instead of string for Title
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    glutTimerFunc(33, TimerFunction, 1)
    SetupRC()
    glutMainLoop()


if __name__ == '__main__':
    main()
