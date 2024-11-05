import pyglet
from game import util

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

upper_pipe_image = pyglet.resource.image("green_rect_u.png")
util.center_image(upper_pipe_image)
# upper_pipe_image.anchor_x = upper_pipe_image.width / 2
# upper_pipe_image.anchor_y = 0

lower_pipe_image = pyglet.resource.image("green_rect_l.png")
util.center_image(lower_pipe_image)
# lower_pipe_image.anchor_x = lower_pipe_image.width / 2
# lower_pipe_image.anchor_y = lower_pipe_image.height

player_image = pyglet.resource.image("попуг.png")
util.center_image(player_image)

background_image = pyglet.resource.image("фон2.png")
background = pyglet.sprite.Sprite(background_image)
#player_image.anchor_x = player_image.width / 2
#player_image.anchor_y = player_image.height / 2

sound = pyglet.media.Player
jump_sound = pyglet.resource.media("звук1.wav", streaming=False)
death_sound = pyglet.resource.media("смерть.wav", streaming=False)
