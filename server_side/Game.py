import pygame as pg
from settings import Settings


class App:
    def __init__(self) -> None:
        pg.init()
        self.run: bool = True
        self.sc: pg.Surface = pg.display.set_mode(size=Settings.res)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.pressed: dict[int, bool] = dict()
        self.timedelta: float = 1 / Settings.FPS
        
        self.players: list = list()
        
    # start part (idk for what cause we have init but why not)
    # i think we will use it for kinda img loading or smth like that idk
    def start(self) -> None:
        pass
        
    # render part
    def render(self) -> None:
        self.sc.fill((0, 255, 0))
        pg.display.update()

    # post-logic part
    def post_logic(self) -> None:
        self.clock_tick()

    def clock_tick(self) -> None:
        self.timedelta = self.clock.tick(Settings.FPS)
    
    # Logic part
    def logic(self) -> None:
        self.keypress_processing()
        self.window_name_update()

    def keypress_processing(self) -> None:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.run: bool = False
                case pg.KEYDOWN:
                    self.pressed[event.key] = True
                    print(self.pressed)
                case pg.KEYUP:
                    self.pressed[event.key] = False
                    print(self.pressed)

    def window_name_update(self) -> None:
        pg.display.set_caption(title=f"td:{self.timedelta} fps:{self.clock.get_fps()}") # currently not working with hyprland
        
    # Final part
    def play(self) -> None:
        self.start()
        while self.run:
            self.logic()
            self.render()
            self.post_logic()

