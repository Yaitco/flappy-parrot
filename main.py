from game import load, util, player
from game.window import game_window
import pyglet

main_batch = pyglet.graphics.Batch()
counter = pyglet.window.FPSDisplay(window=game_window)
game_objects = []
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
player_ship = None
event_stack_size = 0
score = 0

def init():
    global game_objects, player_ship, score, score_label
    score = 0
    score_label.text = "Score: " + str(int(score))
    pyglet.clock.schedule_interval(push_pipe, 1.5)
    player_ship = player.Player(x=game_window.width//2, y=game_window.height//2, batch=main_batch)
    game_objects.append(player_ship)
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)

def reset_level():
    global game_objects, player_ship, event_stack_size, score, score_label

    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    score = 0
    score_label.text = "Score: " + str(int(score))

    game_objects = []
    player_ship = player.Player(x=game_window.width//2, y=game_window.height//2, batch=main_batch)
    game_objects.append(player_ship)

    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1 


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
    global score
    player_dead = False

    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            # Make sure the objects haven't already been killed
            if not obj_1.is_dead and not obj_2.is_dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    for to_remove in [obj for obj in game_objects if obj.is_dead]:
        if to_remove == player_ship:
            player_dead = True
        to_remove.delete()
        game_objects.remove(to_remove)

    for obj in game_objects:
        obj.update(dt)
        if obj.is_pipe:
            score += obj.get_score()

    score_label.text = "Score: " + str(int(score))

    if player_dead:
        reset_level()
        

if __name__ == "__main__":
    init()

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()