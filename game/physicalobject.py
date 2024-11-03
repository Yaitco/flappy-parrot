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

    def update(self, dt) -> None:
        # Обновляем положение объекта взависимости от скорости и времени
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def collides_with(self, other):
        if not self.reacts_to_pipe and other.is_pipe:
            return False
        if self.is_pipe and not other.reacts_to_pipe:
            return False
        
        collision_distance = self.image.width * 0.5 * self.scale \
                             + other.image.width * 0.5 * other.scale
        
        actual_distance = util.distance(self.position, other.position)

        return (actual_distance <= collision_distance)
    
    def handle_collision_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.dead = True

