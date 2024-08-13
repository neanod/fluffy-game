import pygame as pg
from settings import Settings
from player import Player, math
import os


class App:
    def __init__(self) -> None:
        pg.init()
        self.run: bool = True
        self.sc: pg.Surface = pg.display.set_mode(size=Settings.res)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.pressed: dict[int, bool] = dict()
        self.timedelta: float = 1 / Settings.FPS
        
        self.players: list[Player] = list()
        self.tick = 0

        self.textures: dict[str, pg.Surface] = self.load_textures()
        self.to_move = pg.Vector2()

        
    # start part (idk for what cause we have init but why not)
    # i think we will use it for kinda img loading or smth like that idk
    def start(self) -> None:
        self.players.append(
            Player(
                pos=pg.Vector2(Settings.center),
                size=pg.Vector2(32, 32),
                texture=self.textures["spaceship"],
                screen=self.sc,
                angle=1,
            )
        )

    def load_textures(self) -> dict[str, pg.Surface]:
        res = dict()
        listdir = list(map(lambda x: x.split(".", 1)[0], os.listdir("./textures/")))
        texture_name: str
        for texture_name in listdir:
            res[texture_name] = pg.image.load(f"./textures/{texture_name}.png")
        return res

        
    # render part
    def render(self) -> None:
        self.sc.fill((0, 155, 0))
        for pl in self.players:
            pl.render()
        pg.display.update()

    # post-logic part
    def post_logic(self) -> None:
        self.clock_tick()

    def clock_tick(self) -> None:
        self.timedelta = self.clock.tick(Settings.FPS)
    
    # Logic part
    def logic(self) -> None:
        self.tps_logic()
        self.fps_logic()

    def fps_logic(self) -> None:
        self.variables_logic()
        self.window_name_update()
        self.player_processing_fps()

    def tps_logic(self) -> None:
        self.player_processing_tps()
        self.keypress_processing()

    def keypress_processing(self) -> None:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.run: bool = False
                case pg.KEYDOWN:
                    self.pressed[event.key] = True
                case pg.KEYUP:
                    self.pressed[event.key] = False
        to_move = pg.Vector2()
        to_move.x += self.pressed.get(pg.K_d, 0)
        to_move.x -= self.pressed.get(pg.K_a, 0)
        to_move.y += self.pressed.get(pg.K_s, 0)
        to_move.y -= self.pressed.get(pg.K_w, 0)
        if to_move.x or to_move.y:
            to_move.normalize_ip()
        self.to_move = to_move

    def window_name_update(self) -> None:
        pg.display.set_caption(title=f"td:{self.timedelta} fps:{round(self.clock.get_fps())}") # currently not working with hyprland

    def player_processing_fps(self) -> None:
        for pl in self.players:
            pl.update()

    def player_processing_tps(self) -> None:
        if not self.tick % Settings.every_n_update:
            for pl in self.players:
                pl.set_direction(self.to_move)

    def variables_logic(self):
        self.tick += 1
                
        
    # Final part
    def play(self) -> None:
        self.start()
        while self.run:
            self.logic()
            self.render()
            self.post_logic()

