from pygame import Vector2
from entity import Entity, pg, math
from settings import Settings


class Bullet(Entity):
    # should be only updated/rendered
    def __init__(
        self, 
        pos: pg.Vector2,
        size: pg.Vector2,
        texture: pg.Surface,
        screen: pg.Surface,
        angle: float,
        speed: float = Settings.default_bullet_speed,
    ):
        super().__init__(pos, size, texture, screen, angle)
        self.speed = pg.Vector2( # TODO: minuses
            math.sin(angle) * speed,
            math.cos(angle) * speed,
        )
        
