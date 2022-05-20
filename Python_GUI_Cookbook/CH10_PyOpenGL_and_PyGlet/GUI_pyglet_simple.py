'''
PyGlet example
'''
import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Pyglet GUI Example', font_size=44, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
label.color = (100, 255, 100, 255) #hange color of the label

@window.event
def on_draw(): #predefined event names
    window.clear()
    label.draw()

pyglet.app.run()
