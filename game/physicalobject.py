import pyglet
from game import util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs) -> None:
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # Скорость объекта
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Флаги на коллизию с трубами
        self.reacts_to_pipe = True
        self.is_pipe = False

        # Флаг на удаление объекта
        self.is_dead = False
        
        self.event_handlers = []

    def update(self, dt) -> None:
        # Обновляем положение объекта взависимости от скорости и времени
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def collides_with(self, other):
        if not self.reacts_to_pipe and other.is_pipe:
            return False
        if self.is_pipe and not other.reacts_to_pipe:
            return False

        return util.is_rect_sect(self.get_rect(), other.get_rect())

    def get_rect(self):
        return ((self.x - self.width / 2, self.y - self.height / 2), (self.x + self.width / 2, self.y + self.height / 2))
    
    def handle_collision_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.is_dead = True

