from game import load, util
from game.window import game_window
import pyglet

main_batch = pyglet.graphics.Batch()
counter = pyglet.window.FPSDisplay(window=game_window)
game_objects = []

def init():
    global game_objects
    pyglet.clock.schedule_interval(push_pipe, 1.5)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    counter.draw()

#first pipe height
pipe_mid = game_window.height // 2
def push_pipe(dt):
    global pipe_mid
    game_objects.extend(load.generate_pipe(batch=main_batch, mid=pipe_mid))
    pipe_mid = util.next_pipe_mid(pipe_mid)



def update(dt):
    for to_remove in [obj for obj in game_objects if obj.is_dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    for obj in game_objects:
        obj.update(dt)
        

if __name__ == "__main__":
    init()

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()