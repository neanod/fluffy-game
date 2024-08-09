from entity import Entity, pg, math
from faker import Faker
from settings import Settings


f = Faker()


class Player(Entity):
    def __init__(
        self,
        pos: pg.Vector2,
        size: pg.Vector2,
        texture: pg.Surface,
        screen: pg.Surface,
        angle: float = 0,

        default_speed: float = Settings.default_player_speed,
        default_hp: int = 100,
        nickname: str = f.name()
    ):
        super().__init__(
            pos=pos,
            size=size,
            texture=texture,
            screen=screen,
            angle=angle,
        )
        self.default_speed: float = default_speed
        self.nickname: str = nickname # TODO: nickname above player
        self.default_hp = default_hp
        self.hp = default_hp
        self.is_shooting: bool = False
        self.shoting_delay: int = 0
    
    def set_direction(self, direction: pg.Vector2) -> None:
        # NEED FIXED CALL RATE!!!! IMPORTANT!!!!! FIXED CALL RATE (around kinda 60 or 30tps)
        # DIRECTION VECTOR   M U S T   BE abs() <= 1
        # TODO: better coeficcients Upd: ideal founded
        self.speed *= 0.9 # Decreasing previous speed
        self.speed += direction * self.default_speed
        self.speed *= 0.95 # decreasing because if not decreasing then space launch
        if self.speed.x or self.speed.y:
            ang = math.atan2(*self.speed) + math.pi
            self.set_angle(ang)
    
    def break_moving(self) -> None:
        self.set_direction(pg.Vector2(0, 0))
