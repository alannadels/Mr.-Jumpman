import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_surface1 = pg.image.load("Images/player_walk_1.png").convert_alpha()
        player_surface2 = pg.image.load("Images/player_walk_2.png").convert_alpha()
        self.player_jump_surface = pg.image.load("Images/jump.png").convert_alpha()
        self.player_walk = [player_surface1, player_surface2]

        self.player_index = 0
        self.image = self.player_walk[self.player_index]

        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pg.mixer.Sound("Sound/audio_jump.mp3")
        self.jump_sound.set_volume(0.05)

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -22
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump_surface
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()