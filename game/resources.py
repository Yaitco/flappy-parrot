import pyglet
from game import util
from game.window import game_window

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

upper_pipe_image = pyglet.resource.image("green_rect_u.png")
util.center_image(upper_pipe_image)

lower_pipe_image = pyglet.resource.image("green_rect_l.png")
util.center_image(lower_pipe_image)

player_image = pyglet.resource.image("попуг.png")
util.center_image(player_image)

background_image = pyglet.resource.image("фон2.png")
background = pyglet.sprite.Sprite(background_image)
background.x = 0
background.y = 0
background.scale_x = game_window.width / background.width
background.scale_y = game_window.height / background.height

sound = pyglet.media.Player
jump_sound = pyglet.resource.media("звук1.wav", streaming=False)
death_sound = pyglet.resource.media("смерть.wav", streaming=False)
