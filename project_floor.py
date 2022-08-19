import pygame
import random

from class_character import *

##############################################################################################
def floor_setting(pos, floor):
    number_enemies = floor//5 + 1

    for i in range(number_enemies):
        monster = prob_spawn_monster(90 - floor)
        random_away_position(pos, monster)
        monster_group.add(monster)

def random_away_position(center, object):
    while True:
        rand_x = random.randint(370, 910)
        rand_y = random.randint(150, 570)

        if rand_x < center[0] - 60 or center[0] + 60 < rand_x:
            if rand_y < center[1] - 60 or center[1] + 60 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def prob_spawn_monster(percent):
    randprob = random.randrange(0,101)  # 0 ~ 100

    if randprob <= percent:
        return Monster(monster_1_image, (0,0), MON_0_HP)
    else:
        return Monster(monster_2_image, (0,0), MON_1_HP)

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

            if monster.rect.centerx < 410:
                monster.direction = "RIGHT"
            elif monster.rect.centerx > 870:
                monster.direction = "LEFT"

            if monster.rect.centery < 130:
                monster.direction = "DOWN"
            elif monster.rect.centery > 590:
                monster.direction = "UP"