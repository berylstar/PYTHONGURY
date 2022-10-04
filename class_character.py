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

    def damaged(self, screen):
        if not self.is_die:
            surface = self.image.copy()
            w, h = surface.get_size()
            r, g, b, _ = (120,0,0,0)
            for x in range(w):
                for y in range(h):
                    a = surface.get_at((x, y))[3]
                    surface.set_at((x, y), pygame.Color(r, g, b, a))
            screen.blit(surface, self.rect)

def images_bigger(images, xg):
    list = []
    for img in images:
        img = pygame.transform.rotozoom(img, 0, xg)
        list.append(img)
    return list

##### MONSTER CLASS
# "normal" / "shooter" / "alpha" / "runner" / "toward" / "boss"

                                        # 1 ~ 20 : lower part of tower
class Mon_spider(Character):
    def __init__(self):
        image_group = mon_spider_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = spider_die
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
        self.die_images = bat_die
        self.type = ["runner"]

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
        self.die_images = skel_die
        self.type = []

        self.hp = 21
        self.ap = 1
        self.speed = 0.12

# BOSS
class Boss_spider(Character):
    def __init__(self):
        image_group = images_bigger(mon_spider_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_spider"]

        self.hp = 120
        self.ap = 2
        self.speed = 0.1

class Boss_bat(Character):
    def __init__(self):
        image_group = images_bigger(mon_bat_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_bat", "runner"]

        self.hp = 80
        self.ap = 1
        self.speed = 0.2
        self.is_dashed = False
        self.dashes = 0

class Boss_frog(Character):
    def __init__(self):
        image_group = images_bigger(mon_frog_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_frog"]

        self.hp = 200
        self.ap = 1
        self.speed = 0.15
        self.cycle = 2

class Mon_frog_m(Character):
    def __init__(self):
        image_group = mon_frog_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = frog_die
        self.type = []

        self.hp = 3
        self.ap = 0.5
        self.speed = 0.2

class Boss_skel(Character):
    def __init__(self):
        image_group = images_bigger(mon_skel_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_skel"]

        self.hp = 160
        self.ap = 1.5
        self.speed = 0.2
        self.bullet = skel_atk_images
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "bone"

                                        # 21 ~ 40 : graveyard
class Mon_zombie(Character):
    def __init__(self):
        image_group = mon_zombie_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = zombie_die
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
        self.die_images = ghost_die
        self.type = ["alpha"]

        self.hp = 20
        self.ap = 1.5
        self.speed = 0.2

class Mon_scarecrow(Character):
    def __init__(self):
        image_group = mon_scarecrow_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = scarecrow_die
        self.type = ["shooter"]

        self.hp = 18
        self.ap = 1.5
        self.speed = 0.2
        self.bullet = crow_atk_image
        self.b_speed = 15
        self.b_damage = 5
        self.b_type = "crow"

# BOSS
class Boss_zombie(Character):
    def __init__(self):
        image_group = images_bigger(mon_zombie_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_zombie"]

        self.hp = 100
        self.ap = 2
        self.speed = 0.2

class Boss_werewolf(Character):
    def __init__(self):
        image_group = images_bigger(mon_werewolf_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "runner", "toward"]

        self.hp = 180
        self.ap = 2.5
        self.speed = 0.15
        self.is_dashed = False
        self.dashes = 0

class Boss_ghost(Character):
    def __init__(self):
        image_group = images_bigger(mon_ghost_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_ghost", "alpha"]

        self.hp = 230
        self.ap = 1.5
        self.speed = 0.25

class Boss_scarecrow(Character):
    def __init__(self):
        image_group = images_bigger(mon_scarecrow_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_scarecrow"]

        self.hp = 200
        self.ap = 1.5
        self.speed = 0.1
        self.bullet = crow_atk_image
        self.b_speed = 16
        self.b_damage = 4
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
        self.die_images = ember_die
        self.type = ["shooter"]

        self.hp = 25
        self.ap = 1.7
        self.speed = 0.2
        self.bullet = fire_atk_image
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "ember"

class Mon_flamesnake(Character):
    def __init__(self):
        image_group = mon_flamesnake_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = flamesnake_die
        self.type = ["shooter_four"]

        self.hp = 32
        self.ap = 2
        self.speed = 0
        self.bullet = fire_atk_image
        self.b_speed = 15
        self.b_damage = 10
        self.b_type = "ember"

class Mon_firebat(Character):
    def __init__(self):
        image_group = mon_firebat_images
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.die_images = firebat_die
        self.type = ["runner", "toward"]

        self.hp = 18
        self.ap = 1.3
        self.speed = 0.2
        self.is_dashed = False
        self.dashes = 0

# BOSS
class Boss_golem(Character):
    def __init__(self):
        image_group = images_bigger(mon_golem_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "toward"]

        self.hp = 400
        self.ap = 2
        self.speed = 0.08

class Boss_ember(Character):
    def __init__(self):
        image_group = images_bigger(mon_ember_images, 2)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_ember", "shooter"]

        self.hp = 220
        self.ap = 1.7
        self.speed = 0.17
        self.bullet = fire_atk_image
        self.b_speed = 18
        self.b_damage = 10
        self.b_type = "ember"
        self.cycle = 0

class Boss_flamesnake(Character):
    def __init__(self):
        image_group = images_bigger(mon_flamesnake_images, 1.5)
        position = (0,0)
        Character.__init__(self, image_group, position)
        self.type = ["boss", "boss_flamesnake", "shooter_four"]

        self.hp = 250
        self.ap = 3
        self.speed = 0
        self.bullet = fire_atk_image
        self.b_speed = 18
        self.b_damage = 10
        self.b_type = "ember"
        self.cycle = 0

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
        self.boss_scene = False

        self.dontmove = False
        self.dont_alpha = False
        self.dont_dash = False

        self.b_speed = 0

        self.is_blind = False

        self.boss_zombie = 0
##############################################################################################

##### about monster
monster_group = pygame.sprite.Group()
monster_con = MonsterController()

###### about npc
npc_kingslime = Character(father_slime_images, (540, 360))
npc_kingslime.direction = "RIGHT"
npc_coffin = Character(coffin_images, (840, 600))

npc_group = pygame.sprite.Group()
npc_group.add(npc_kingslime, npc_coffin)