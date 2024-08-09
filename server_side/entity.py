import pygame as pg
import math


class Entity:
    def __init__(
        self,
        pos: pg.Vector2,
        size: pg.Vector2,
        texture: pg.Surface,
        screen: pg.Surface,
        angle: float,
    ):
        self.pos: pg.Vector2 = pos
        self.size: pg.Vector2 = size
        self.sc: pg.Surface = screen
        self.angle: float = angle # radians
        self.texture = texture
        
        self.speed: pg.Vector2 = pg.Vector2(0, 0)
        temp: tuple[pg.Surface, pg.Vector2] = self.update_current_texture()
        self.current_texture: pg.Surface = temp[0]
        self.current_draw_offset: pg.Vector2 = temp[1]
    
    def update(self) -> None:
        self.pos += self.speed

    def set_angle(self, new_angle: float) -> None:
        self.angle = new_angle
        self.update_current_texture()
    
    def update_current_texture(self) -> tuple[pg.Surface, pg.Vector2]:
        return pg.transform.rotate(pg.transform.smoothscale(self.texture, self.size), math.degrees(self.angle)), pg.Vector2(self.current_texture.get_rect().size) / 2

    def render(self) -> None:
        self.sc.blit(
            source=self.current_texture,
            dest=self.pos - self.current_draw_offset
        )

