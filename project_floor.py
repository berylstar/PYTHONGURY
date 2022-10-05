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
    if not monster:
        pass
    else:
        random_away_position(pos, monster)
        monster_group.add(monster)

def random_monster(floor):
    randprob = random.randrange(1,101) # 1~100

    if 0 < floor < 20:
        if randprob < 30:
            return Mon_skel()
        elif 30 <= randprob < 60:
            return Mon_frog()
        elif randprob % 2 == 0:
            return Mon_bat()
        elif randprob % 2 == 1:
            return Mon_spider()

    elif 20 < floor < 40:
        if randprob < 30:
            return Mon_ghost()
        elif 30 <= randprob < 60:
            return Mon_werewolf()
        elif randprob % 2 == 0:
            return Mon_scarecrow()
        elif randprob % 2 == 1:
            return Mon_zombie()

    elif 40 < floor < 60:
        if randprob < 30:
            return Mon_ember()
        elif 30 <= randprob < 60:
            return Mon_golem()
        elif randprob % 2 == 0:
            return Mon_flamesnake()
        elif randprob % 2 == 1:
            return Mon_firebat()

    elif 60 < floor < 80:
        if randprob < 30:
            return Mon_magician()
        elif 30 <= randprob < 60:
            return Mon_book()
        elif randprob % 2 == 0:
            return Mon_candle()
        elif randprob % 2 == 1:
            return Mon_witch()

    else:
        return False

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
        spawn_monster(pos, Mon_zombie())
        spawn_monster(pos, Mon_zombie())
        spawn_monster(pos, Mon_zombie())
        pass
    elif floor == 40:
        spawn_monster(pos, random_boss(floor))

    if 41 <= floor < 45:
        spawn_monster(pos, Mon_ember())
    elif 45 <= floor < 50:
        spawn_monster(pos, Mon_firebat())
        spawn_monster(pos, Mon_golem())
    elif 50 <= floor < 55:
        spawn_monster(pos, Mon_flamesnake())
    elif 55 <= floor < 60:
        spawn_monster(pos, Mon_firebat())
        spawn_monster(pos, Mon_ember())
        spawn_monster(pos, Mon_golem())
        pass
    elif floor == 60:
        spawn_monster(pos, random_boss(floor))

    if 61 <= floor < 65:
        spawn_monster(pos, Mon_book())
    elif 65 <= floor < 70:
        spawn_monster(pos, Mon_witch())
    elif 70 <= floor < 75:
        spawn_monster(pos, Mon_magician())
    elif 75 <= floor < 80:
        spawn_monster(pos, Mon_candle())
        spawn_monster(pos, Mon_book())
        pass
    elif floor == 80:
        randprob = random.randrange(0,2)
        if randprob == 1:
            spawn_monster(pos, random_boss(floor))
        else:
            spawn_monster(pos, Boss_witch())
            spawn_monster(pos, Boss_book())
        

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

    elif floor == 40:
        if randprob == 1:
            return Boss_zombie()
        elif randprob == 2:
            return Boss_werewolf()
        elif randprob == 3:
            return Boss_ghost()
        elif randprob == 4:
            return Boss_scarecrow()

    elif floor == 60:
        if randprob == 1:
            return Boss_golem()
        elif randprob == 2:
            return Boss_ember()
        elif randprob == 3 or randprob == 4:
            return Boss_flamesnake()

    elif floor == 80:
        if randprob % 2 == 1 :
            return Boss_magician()
        elif randprob % 2 == 0:
            return Boss_candle()

    elif floor == 100:
        return Boss_devil()

    else:
        return False
##############################################################################################
def random_field_setting(floor):
    randprob = random.randrange(1,101)

    field_group.empty()

    if 0 < floor <= 20:
        for i in range(randprob % 3):
            web = Field(web_image, (0,0))
            random_away_position((0,0), web)
            field_group.add(web)

        if randprob <= 50:
            water = Field(water_image, (0,0))
            random_away_position((0,0), water)
            field_group.add(water)

    elif 20 < floor <= 40:
        for i in range(randprob % 4):
            web = Field(web_image, (0,0))
            random_away_position((0,0), web)
            field_group.add(web)

        if randprob <= 50:
            index = randprob % 2
            deco = Field(graveyard_deco[index], (0,0))
            random_away_position((0,0), deco)
            field_group.add(deco)

    elif 40 < floor <= 60:
        num = max(8, randprob%11)
        aa = 0 
        for i in range(num):
            lava = Field(lava_images[aa%3], (0,0))
            random_away_position((0,0), lava)
            field_group.add(lava)
            aa += 1