import pyglet

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

upper_pipe_image = pyglet.resource.image("green_rect_u.png")
upper_pipe_image.anchor_x = upper_pipe_image.width / 2
upper_pipe_image.anchor_y = 0
lower_pipe_image = pyglet.resource.image("green_rect_l.png")
lower_pipe_image.anchor_x = lower_pipe_image.width / 2
lower_pipe_image.anchor_y = lower_pipe_image.height

