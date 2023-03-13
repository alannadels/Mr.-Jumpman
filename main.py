import pygame
import pygame as pg
from sys import exit
from random import randint, choice
from player import Player
from obstacle import Obstacle

FONT_TYPE = "Font/Pixeltype.ttf"
FONT_SIZE = 50
TEXT_COLOR = (64, 64, 64)
TEXT_BOX_COLOR = "#c0e8ec"
TITLE_SCREEN_COLOR = (94, 129, 162)
TITLE_SCREEN_TEXT_COLOR = (111, 196, 169)
GAME_ACTIVE = False
START_TIME = 0
SCORE = 0


def display_score():
    current_time = int(pg.time.get_ticks() / 1000) - START_TIME
    score_surface = main_font.render(f"Score:  {current_time}", False, TEXT_COLOR)
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def collision_sprite():
    if pg.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


pg.init()

# Screen
screen = pg.display.set_mode((800, 400))
pg.display.set_caption("Mr. JumpMan")

# Clock
clock = pg.time.Clock()

# Groups
player = pg.sprite.GroupSingle()
# noinspection PyTypeChecker
player.add(Player())
obstacle_group = pg.sprite.Group()

# Font
main_font = pg.font.Font(FONT_TYPE, FONT_SIZE)

# Surfaces
sky_surface = pg.image.load("Images/sky.png").convert()
ground_surface = pg.image.load("Images/ground.png").convert()

# Title Screen
title_screen_player = pg.image.load("Images/player_stand.png").convert_alpha()
# title_screen_player_scaled = pg.transform.rotozoom(title_screen_player, 0, 2)
title_screen_player_scaled = pg.transform.scale2x(title_screen_player)
game_name = main_font.render("Mr. JumpMan", False, TITLE_SCREEN_TEXT_COLOR)
game_message = main_font.render("Press 'space' to run", False, TITLE_SCREEN_TEXT_COLOR)

# Rectangles
title_screen_player_rect = title_screen_player_scaled.get_rect(center=(400, 200))
game_name_rect = game_name.get_rect(center=(400, 70))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Obstacles
obstacle_rect_list = []

# Music
background_music = pg.mixer.Sound("Sound/music.wav")
background_music.set_volume(0.05)
background_music.play(loops=-1)

# Game
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if GAME_ACTIVE:
            if event.type == obstacle_timer:
                # noinspection PyTypeChecker
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail"])))
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                GAME_ACTIVE = True
                START_TIME = int(pg.time.get_ticks() / 1000)

    if GAME_ACTIVE:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        SCORE = display_score()

        # Calling player class
        player.draw(screen)
        player.update()

        # Calling obstacle class
        obstacle_group.draw(screen)
        obstacle_group.update()

        # collision
        GAME_ACTIVE = collision_sprite()

    else:
        screen.fill(TITLE_SCREEN_COLOR)
        screen.blit(title_screen_player_scaled, title_screen_player_rect)
        screen.blit(game_name, game_name_rect)

        score_message = main_font.render(f"Your Score:  {SCORE}", False, TITLE_SCREEN_TEXT_COLOR)
        score_message_rect = score_message.get_rect(center=(400, 330))

        if SCORE == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pg.display.update()
    clock.tick(60)
