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
        self.image_update()

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

    def alpha(self, val):
        for img in self.image_group:
            img.set_alpha(val)

##### MONSTER CLASS
# "normal" / "shooter" / "alpha" / "runner" / "toward" / "boss"
                                                        #후에 클래스에 이미지그룹, 죽음이미지그룹 넣는 클래스로 변경

                                        # 1 ~ 20 : lower part of tower
class Mon_spider(Character):
    def __init__(self):
        image_group = mon_spider_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["shooter"]

        self.hp = 12
        self.ap = 1
        self.speed = 0.15
        self.bullet = spider_atk_image
        self.b_speed = 8
        self.b_damage = 0
        self.b_type = "web"

class Mon_frog(Character):
    def __init__(self):
        image_group = mon_frog_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = frog_die
        self.type = []

        self.hp = 12
        self.ap = 1
        self.speed = 0.2

class Mon_bat(Character):
    def __init__(self):
        image_group = mon_bat_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["runner", "toward"]

        self.hp = 8
        self.ap = 0.5
        self.speed = 0.2
        self.is_dashed = False
        self.dashes = 0

class Mon_skel(Character):
    def __init__(self):
        image_group = mon_skel_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = []

        self.hp = 21
        self.ap = 1
        self.speed = 0.12

                                        # 21 ~ 40 : graveyard
class Mon_zombie(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = []

        self.hp = 18
        self.ap = 2
        self.speed = 0.23

class Mon_werewolf(Character):
    def __init__(self):
        image_group = mon_werewolf_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = werewolf_die
        self.type = ["toward"]

        self.hp = 30
        self.ap = 2.5
        self.speed = 0.15

class Mon_ghost(Character):
    def __init__(self):
        image_group = mon_ghost_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["alpha"]

        self.hp = 20
        self.ap = 1.5
        self.speed = 0.2

class Mon_scarecrow(Character):
    def __init__(self):
        image_group = mon_scarecrow_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["shooter"]

        self.hp = 18
        self.ap = 1.5
        self.speed = 0.2
        self.bullet = crow_atk_image
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "crow"


                                        # 41 ~ 60 : lava land
class Mon_golem(Character):
    def __init__(self):
        image_group = mon_golem_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = golem_die
        self.type = []

        self.hp = 50
        self.ap = 2.5
        self.speed = 0.1

class Mon_ember(Character):
    def __init__(self):
        image_group = mon_ember_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["shooter"]

        self.hp = 25
        self.ap = 1.7
        self.speed = 0.2
        self.bullet = ember_atk_image
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "ember"

class Mon_firesnake(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["shooter"]

        self.hp = 32
        self.ap = 2
        self.speed = 0
        self.bullet = ember_atk_image
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "ember"

class Mon_firebat(Character):
    def __init__(self):
        image_group = mon_firebat_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["runner", "toward"]

        self.hp = 18
        self.ap = 1.3
        self.speed = 0.2
        self.is_dashed = False
        self.dashes = 0


                                        # 61 ~ 80 : magical library
class Mon_witch(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["runner"]

        self.hp = 21
        self.ap = 1.5
        self.speed = 0.22
        self.is_dashed = False
        self.dashes = 0

class Mon_book(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = None
        self.type = ["toward"]

        self.hp = 18
        self.ap = 1.3
        self.speed = 0.2

class Mon_magician(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["shooter"]

        self.hp = 21
        self.ap = 0.7
        self.speed = 0.1
        self.bullet = None
        self.b_speed = 10
        self.b_damage = 15
        self.b_type = "magic"

class Mon_candle(Character):
    def __init__(self):
        image_group = None
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = None
        self.type = []

        self.hp = 60
        self.ap = 2
        self.speed = 0.3

                                        # 81 ~ 100 : king castle


# BOSS
class Mon_boss(Character):
    def __init__(self):
        image_group = monster_boss_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_spawner", "runner"]

        self.hp = 100
        self.ap = 2
        self.speed = 0.1
        # self.bullet = ember_attack_image
        # self.b_speed = 10
        # self.b_damage = 10
        # self.b_type = "NONE"
        self.is_dashed = False
        self.dashes = 0

class Mon_mini(Character):
    def __init__(self):
        image_group = monster_2_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["mini"]

        self.hp = 1
        self.ap = 0.2
        self.speed = 0.2

##############################################################################################
class MonsterController():
    def __init__(self):
        self.mon_count = 0

        self.dontmove = False
        self.dont_alpha = False
        self.dont_dash = False

        self.b_speed = 0

        self.is_blind = False
##############################################################################################

##### about monster
monster_group = pygame.sprite.Group()
monster_con = MonsterController()

###### about npc
npc_kingslime = Character(father_slime_images, (540, 360))
npc_kingslime.direction = "RIGHT"
npc_coffin = Character(coffin_images, (840, 600))
# npc_ghost = Character(ghost_images, (800, 150))

npc_group = pygame.sprite.Group()
npc_group.add(npc_kingslime, npc_coffin)