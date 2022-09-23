import pygame
import random

from class_character import *
from class_field import *

##############################################################################################
# 몬스터 세팅 방법
# 1. 전체 랜덤
# 2. 전체 세팅
# 3. 전체 랜덤 + 추가 세팅
##############################################################################################
def monster_setting(pos, floor):
    number_enemies = floor//5 + 1

    for i in range(number_enemies):
        spawn_monster(pos, prob_spawn_monster(floor))

    floor_monster_setting(pos, floor)

def random_away_position(center, object):
    while True:
        rand_x = random.randint(0,9) * 60 + 370
        rand_y = random.randint(0,9) * 60 + 90

        if rand_x < center[0] - 40 or center[0] + 40 < rand_x:
            if rand_y < center[1] - 40 or center[1] + 40 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def spawn_monster(pos, monster):
    random_away_position(pos, monster)
    monster_group.add(monster)

def prob_spawn_monster(floor):
    randprob = random.randrange(1,101)  # 1 ~ 100
    percent = 70 - floor

    if randprob < percent:
        return Mon_bat()
    elif percent <= randprob < percent + 30:
        return Mon_frog()
    elif randprob % 3 == 0:
        return Mon_ghost()
    elif randprob % 3 == 1:
        return Mon_ember()
    else:
        return Mon_skel()

def floor_monster_setting(pos, floor):
    if 1 <= floor < 7:
        # spawn_monster(pos, Mon_spider())
        spawn_monster(pos, Mon_frog())
        # spawn_monster(pos, Mon_bat())
        # spawn_monster(pos, Mon_bat())
        # spawn_monster(pos, Mon_skel())
        spawn_monster(pos, Mon_ghost())
        spawn_monster(pos, Mon_ghost())
        spawn_monster(pos, Mon_ghost())
        spawn_monster(pos, Mon_boss())
    elif 7 <= floor < 12:
        spawn_monster(pos, Mon_ember())
    elif 12 <= floor < 15:
        spawn_monster(pos, Mon_ghost())
    if floor % 10 == 0:
        spawn_monster(pos, Mon_boss())

##############################################################################################

def random_field_setting():
    randprob = random.randrange(1,101)

    field_group.empty()

    for i in range(randprob % 4):
        if randprob % 2 == 0:
            web = Field(web_image, (0,0))
            random_away_position((0,0), web)
            field_group.add(web)

    if randprob <= 50:
        # i = randprob % 3
        # water = Field(water_images[i], (0,0))
        water = Field(water_image, (0,0))
        random_away_position((0,0), water)
        field_group.add(water)