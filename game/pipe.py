import pyglet
from enum import StrEnum
from game import physicalobject, window, const, resources

class PipeStatus(StrEnum):
    NOT_PASSED = "NOT_PASSED"
    PASSED = "PASSED"
    SCORED = "SCORED"

class Pipe(physicalobject.PhysicalObject):

    def __init__(self, *args, is_upper=True, **kwargs) -> None:
        super(Pipe, self).__init__(*args, **kwargs)

        self.is_pipe = True
        self.scale_x = 0.75
        self.is_upper = is_upper 
        self.status = PipeStatus.NOT_PASSED
        self.velocity_x = -window.game_window.width * const.PIPE_SPEED
        
    def update(self, dt):
        super(Pipe, self).update(dt)
        if self.status == PipeStatus.NOT_PASSED and self.x <= window.game_window.width / 2:
            self.status = PipeStatus.PASSED
        if (self.x <= -self.width / 2):
            self.is_dead = True

    def get_score(self):
        if self.status == PipeStatus.PASSED:
            self.status = PipeStatus.SCORED
            if self.is_upper:
                resources.point_sound.play()
            return 0.5
        return 0