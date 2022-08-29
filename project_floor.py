import pygame
import random

from class_character import *
from class_field import *

##############################################################################################
def floor_setting(pos, floor):
    number_enemies = floor//5 + 1

    for i in range(number_enemies):
        monster = prob_spawn_monster(90 - floor)
        random_away_position(pos, monster)
        monster_group.add(monster)

    if floor % 10 == 0:
        boss_monster = Monster(monster_boss_image, (0,0), "boss", 100)
        random_away_position(pos, boss_monster)
        monster_group.add(boss_monster)

    random_field_setting()

def random_away_position(center, object):
    while True:
        rand_x = random.randint(0,9) * 60 + 370
        rand_y = random.randint(0,9) * 60 + 90

        if rand_x < center[0] - 30 or center[0] + 30 < rand_x:
            if rand_y < center[1] - 30 or center[1] + 30 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def prob_spawn_monster(percent):
    randprob = random.randrange(0,101)  # 0 ~ 100

    if randprob <= percent:
        return Monster(monster_1_image, (0,0), "normal", MON_0_HP)
    else:
        return Monster(monster_2_image, (0,0), "normal", MON_1_HP)

def random_monster_direction():
    if monster_group:
        for monster in monster_group:
            rand = random.randrange(0,11)
            if rand <= 1:
                monster.direction = "LEFT"
            elif 1 < rand and rand <= 3:
                monster.direction = "RIGHT"
            elif 3 < rand and rand <= 5:
                monster.direction = "UP"
            elif 5 < rand and rand <= 7:
                monster.direction = "DOWN"
            else:
                monster.direction = "NONE"

            if monster.rect.centerx <= 340 + (monster.rect.width // 2):
                monster.direction = "RIGHT"
            elif monster.rect.centerx >= 940 - (monster.rect.width // 2):
                monster.direction = "LEFT"

            if monster.rect.centery <= 60 + (monster.rect.height // 2):
                monster.direction = "DOWN"
            elif monster.rect.centery >= 660 - (monster.rect.height // 2):
                monster.direction = "UP"

def random_field_setting():
    randprob = random.randrange(0,101)

    field_group.empty()

    if randprob % 2 == 0:
        web = Field(web_image, (0,0))
        random_away_position((0,0), web)
        field_group.add(web)

    if randprob <= 50:
        # i = randprob % 3
        # water = Field(water_images[i], (0,0))
        water = Field(water_images[0], (0,0))
        random_away_position((0,0), water)
        field_group.add(water)