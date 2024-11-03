import pyglet
from game import physicalobject, window, const

class Pipe(physicalobject.PhysicalObject):
    
    def __init__(self, *args, **kwargs) -> None:
        super(Pipe, self).__init__(*args, **kwargs)

        self.is_pipe = True
        self.scale_x = 0.75
        self.velocity_x = -window.game_window.width * const.PIPE_SPEED
        
    def update(self, dt):
        super(Pipe, self).update(dt)
        if (self.x <= -self.width / 2):
            self.dead = True