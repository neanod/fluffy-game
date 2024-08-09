import math


class Settings:
    FPS = 120
    width = 1920 // 2
    height = 1080 // 2
    res = width, height
    width_half = width // 2
    height_half = height // 2
    center = width_half, height_half

    default_player_speed = 1
    default_bullet_speed = 2 * default_player_speed

    every_n_update = math.ceil(FPS/60)
