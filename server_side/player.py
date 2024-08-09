from entity import Entity, pg
from faker import Faker


f = Faker()


class Player(Entity):
    def __init__(
        self,
        pos: pg.Vector2,
        size: pg.Vector2,
        texture: pg.Surface,
        screen: pg.Surface,
        angle: float,

        default_speed: float = 10,
        default_hp: int = 100,
        nickname: str = f.name()
    ):
        super().__init__(
            pos,
            size,
            texture,
            screen,
            angle,
        )
        self.default_speed: float = default_speed
        self.nickname: str = nickname # TODO: nickname above player
        self.default_hp = default_hp
        self.hp = default_hp
    
    def set_direction(self, direction: pg.Vector2) -> None:
        # NEED FIXED CALL RATE!!!! IMPORTANT!!!!! FIXED CALL RATE (around kinda 60 or 30tps)
        # DIRECTION VECTOR   M U S T   BE NORMALIZED
        # TODO: better coeficcients
        self.speed *= 0.5 # Decreasing previous speed
        self.speed += direction * self.default_speed
        self.speed *= 0.95 # decreasing because if not decreasing then space launch
    
    def break_moving(self) -> None:
        self.set_direction(pg.Vector2(0, 0))
