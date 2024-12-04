import pyglet
from game import util
from game.window import game_window

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

upper_pipe_image = pyglet.resource.image("green_rect_u.png")
util.center_image(upper_pipe_image)

lower_pipe_image = pyglet.resource.image("green_rect_l.png")
util.center_image(lower_pipe_image)

player_image = pyglet.resource.image("parrot-1/frame_0.png")
util.center_image(player_image)

background_image = pyglet.resource.image("фон2.png")
util.center_image(background_image)
background = pyglet.sprite.Sprite(background_image, x=game_window.width//2, y=game_window.height//2)
background.scale_x = game_window.width / background.width * 1
background.scale_y = game_window.height / background.height * 1.2

sound = pyglet.media.Player
jump_sound = pyglet.resource.media("звук1.wav", streaming=False)
point_sound = pyglet.resource.media("get_point.wav", streaming=False)
death_sound = pyglet.resource.media("смерть.wav", streaming=False)

frames = []
for i in (0, 1, 2, 1, 0):
    img = pyglet.resource.image(f"base-parrot/frame_{i}.png")
    # util.center_image(img)
    img.anchor_x = 0.4 * img.width
    img.anchor_y = 0.5 * img.height
    frames.append(img)

player_animation = pyglet.image.Animation.from_image_sequence(frames, duration=0.1)
player_animation
