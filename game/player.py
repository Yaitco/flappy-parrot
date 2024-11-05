from game import physicalobject, resources
from game.window import game_window
from pyglet.window import key

class Player(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs) -> None:
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)
        
        self.scale = 0.25

        self.jump_speed = 300.
        self.gravity_speed = 450.

        self.reacts_to_pipe = True

        self.key_handler = key.KeyStateHandler()

        self.event_handlers = [self, self.key_handler]

    def update(self, dt) -> None:
        super(Player, self).update(dt)
        self.velocity_y -= self.gravity_speed * dt
        if not(0 <= self.y <= game_window.height):
            self.is_dead = True

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case key.SPACE:
                self.jump()

    def jump(self):
        self.velocity_y = self.jump_speed
        resources.jump_sound.play()
