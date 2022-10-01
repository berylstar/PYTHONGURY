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
    num = (floor % 20) //6 + 1

    for i in range(num):
        spawn_monster(pos, random_monster(floor))

    monster_floor_setting(pos, floor)

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

def random_monster(floor):
    randprob = random.randrange(1,101) # 1~100

    if 0 < floor <= 20:
        if randprob < 30:
            return Mon_skel()
        elif 30 <= randprob < 60:
            return Mon_frog()
        elif randprob % 2 == 0:
            return Mon_bat()
        elif randprob % 2 == 1:
            return Mon_spider()
    elif 20 < floor <= 40:
        if randprob < 30:
            return Mon_ghost()
        elif 30 <= randprob < 60:
            return Mon_werewolf()
        elif randprob % 2 == 0:
            return Mon_scarecrow()
        elif randprob % 2 == 1:
            # return Mon_zombie()
            return Mon_ghost()

def monster_floor_setting(pos, floor):
    if 1 <= floor < 5:
        spawn_monster(pos, Mon_frog())
    elif 5 <= floor < 10:
        spawn_monster(pos, Mon_skel())
    elif 10 <= floor < 15:
        spawn_monster(pos, Mon_spider())
    elif 15 <= floor < 20:
        spawn_monster(pos, Mon_bat())
    elif floor == 20:
        spawn_monster(pos, random_boss(floor))

    if 21 <= floor < 25:
        spawn_monster(pos, Mon_ghost())
    elif 25 <= floor < 30:
        spawn_monster(pos, Mon_scarecrow())
        spawn_monster(pos, Mon_scarecrow())
    elif 30 <= floor < 35:
        spawn_monster(pos, Mon_ghost())
        spawn_monster(pos, Mon_werewolf())
    elif 35 <= floor < 40:
        # spawn_monster(pos, Mon_zombie())
        pass
    elif floor == 40:
        spawn_monster(pos, random_boss(floor))

def random_boss(floor):
    randprob = random.randrange(1,5)
    if floor == 20:
        if randprob == 1:
            return Boss_spider()
        elif randprob == 2:
            return Boss_bat()
        elif randprob == 3:
            return Boss_frog()
        elif randprob == 4:
            return Boss_skel()
    else:
        return Mon_boss()
##############################################################################################
def random_field_setting(floor):
    randprob = random.randrange(1,101)

    field_group.empty()

    if 0 < floor <= 20:
        for i in range(randprob % 4):
            if randprob % 2 == 0:
                web = Field(web_image, (0,0))
                random_away_position((0,0), web)
                field_group.add(web)

        if randprob <= 50:
            water = Field(water_image, (0,0))
            random_away_position((0,0), water)
            field_group.add(water)

    elif 20 < floor <= 40:
        if randprob <= 50:
            index = randprob % 4
            deco = Field(graveyard_deco[index], (0,0))
            random_away_position((0,0), deco)
            field_group.add(deco)