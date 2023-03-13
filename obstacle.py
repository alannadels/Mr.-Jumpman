import pygame as pg
from random import randint, choice


class Obstacle(pg.sprite.Sprite):
    def __init__(self, obstacle_type):
        super().__init__()
        if obstacle_type == "fly":
            fly_surface1 = pg.image.load("Images/fly.png").convert_alpha()
            fly_surface2 = pg.image.load("Images/Fly2.png").convert_alpha()
            self.frames = [fly_surface1, fly_surface2]

            self.y_pos = 210
        else:
            snail_surface1 = pg.image.load("Images/snail.png").convert_alpha()
            snail_surface2 = pg.image.load("Images/snail2.png").convert_alpha()
            self.frames = [snail_surface1, snail_surface2]

            self.y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.remove()

    def remove(self):
        if self.rect.x <= -100:
            self.kill()

