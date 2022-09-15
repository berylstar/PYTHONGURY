import pygame
from file_image import *
##############################################################################################
##### CHARACTER CLASS
class Character(pygame.sprite.Sprite):
    def __init__(self, image_group, position):
        super().__init__()
        self.image_group = image_group
        self.position = position

        self.i_i = 0
        self.image = image_group[self.i_i]
        self.rect = self.image.get_rect(center=position)

        self.direction = "LEFT"
        self.to = [0, 0, 0, 0]  #LEFT, RIGHT, UP, DOWN
        self.flip = False

        self.is_die = False
        self.die_images = monster_die_images

    def change_image_group(self, new_images):
        self.i_i = 0
        self.image_group = new_images

    def image_update(self):
        g_len = len(self.image_group)

        self.image = self.image_group[self.i_i]

        self.i_i += 1
        if self.i_i == g_len:
            self.i_i = 0

    def draw(self, screen):
        if self.direction == "LEFT":
            self.flip = False
        elif self.direction == "RIGHT":
            self.flip = True

        if not self.flip:
            screen.blit(self.image, self.rect)
        else:
            r_image = pygame.transform.flip(self.image, True, False)
            screen.blit(r_image, self.rect)

    def move(self, to_x, to_y, fps):
        self.rect.x += to_x * fps
        self.rect.y += to_y * fps

        self.rect.centerx = max(self.rect.centerx, 340 + (self.rect.width // 2))
        self.rect.centerx = min(self.rect.centerx, 940 - (self.rect.width // 2))

        self.rect.centery = max(self.rect.centery, 60 + (self.rect.height // 2))
        self.rect.centery = min(self.rect.centery, 660 - (self.rect.height // 2))

        self.position = (self.rect.centerx, self.rect.centery)

    def stop(self):
        self.to = [0,0,0,0]

##### MONSTER CLASS
# "normal" / "shooter" / "alpha" / "runner" / "toward" / "boss"
                                                        #후에 클래스에 이미지그룹, 죽음이미지그룹 넣는 클래스로 변경

# 1 ~ 20 : lower part of tower
class Mon_skel(Character):
    def __init__(self):
        image_group = mon_skel_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "normal"

        self.hp = 10
        self.speed = 0.1

class Mon_spider(Character):
    def __init__(self):
        image_group = monster_1_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "normal"

        self.hp = 10
        self.speed = 0.1

class Mon_bat(Character):
    def __init__(self):
        image_group = monster_2_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "normal"

        self.hp = 10
        self.speed = 0.1

class Mon_frog(Character):
    def __init__(self):
        image_group = monster_3_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "normal"

        self.hp = 25
        self.speed = 0.1


# 21 ~ 40 : grass land


# 41 ~ 60 : graveyard
class Mon_ghost(Character):
    def __init__(self):
        image_group = mon_ghost_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "alpha"

        self.hp = 15
        self.speed = 0.1


# 61 ~ 80 : fire land
class Mon_ember(Character):
    def __init__(self):
        image_group = mon_ember_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "shooter"

        self.hp = 10
        self.speed = 0.05

# 81 ~ 100 : king castle


class Mon_skell(Character):
    def __init__(self):
        image_group = mon_skel_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "runner"
        self.curr_dir = None        # runner는 self.curr_dir=None 필요

        self.hp = 10
        self.speed = 0.1

class Mon_boss(Character):
    def __init__(self):
        image_group = monster_boss_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = "boss"

        self.hp = 100
        self.speed = 0.1

##############################################################################################
class MonsterController():
    def __init__(self):
        self.dontmove = False

        self.shooting_speed = 10
        self.shooting_damage = 5
##############################################################################################

##### about monster
monster_group = pygame.sprite.Group()
monster_con = MonsterController()

###### about npc
npc_kingslime = Character(father_slime_images, (540, 360))
npc_coffin = Character(coffin_images, (840, 600))
npc_ghost = Character(ghost_images, (800, 150))

npc_group = pygame.sprite.Group()
npc_group.add(npc_kingslime, npc_coffin, npc_ghost)

##### about monster