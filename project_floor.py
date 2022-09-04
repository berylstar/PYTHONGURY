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
def floor_setting(pos, floor):
    number_enemies = floor//5 + 1

    if not floor % 20 == 0:
        for i in range(number_enemies):
            spawn_monster(pos, floor)
        floor_monster_setting(pos, floor)
    else:
        boss_monster = Mon_boss()
        random_away_position(pos, boss_monster)
        monster_group.add(boss_monster)

    random_field_setting()

def random_away_position(center, object):
    while True:
        rand_x = random.randint(0,9) * 60 + 370
        rand_y = random.randint(0,9) * 60 + 90

        if rand_x < center[0] - 40 or center[0] + 40 < rand_x:
            if rand_y < center[1] - 40 or center[1] + 40 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def prob_spawn_monster(floor):
    randprob = random.randrange(0,101)  # 0 ~ 100
    percent = 70 - floor

    if randprob < percent:
        return Mon_1()
    elif percent <= randprob < percent + 30:
        return Mon_2()
    elif randprob % 3 == 0:
        return Mon_ghost()
    elif randprob % 3 == 1:
        return Mon_ember()
    else:
        return Mon_skel()

def spawn_monster(pos, floor, monster_kind=None):
    if not monster_kind:
        monster = prob_spawn_monster(floor)
        random_away_position(pos, monster)
        monster_group.add(monster)
    else:
        monster = monster_kind
        random_away_position(pos, monster)
        monster_group.add(monster)

def random_monster_direction():
    if monster_group and not monster_con.dontmove:
        for monster in monster_group:
            rand = random.randrange(0,10)
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

def forward_monster_direction(target):
    if monster_group and not monster_con.dontmove:
        for monster in monster_group:
            x = target.position[0] - monster.position[0]
            y = target.position[1] - monster.position[1]
            rand = random.randrange(0,10)

            if rand < 5:
                if x < -30 :
                    monster.direction = "LEFT"
                elif x > 30:
                    monster.direction = "RIGHT"
                else:
                    monster.direction = "NONE"
            else:
                if y < -30:
                    monster.direction = "UP"
                elif y > 30:
                    monster.direction = "DOWN"
                else:
                    monster.direction = "NONE"

def random_field_setting():
    randprob = random.randrange(0,101)

    field_group.empty()

    for i in range(randprob % 4):
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

def floor_monster_setting(pos, floor):
    if 1 <= floor < 7:
        # spawn_monster(pos, floor, Mon_1())
        # spawn_monster(pos, floor, Mon_skel())
        # spawn_monster(pos, floor, Mon_skel())
        # spawn_monster(pos, floor, Mon_ember())
        # spawn_monster(pos, floor, Mon_ember())
        # spawn_monster(pos, floor, Mon_ghost())
        # spawn_monster(pos, floor, Mon_ghost())
        spawn_monster(pos, floor, Mon_slime())
    elif 7 <= floor < 12:
        spawn_monster(pos, floor, Mon_2())
    elif 12 <= floor < 15:
        spawn_monster(pos, floor, Mon_ghost())