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

    def image_update(self):
        g_len = len(self.image_group) - 1

        self.i_i += 1

        if self.i_i == g_len:
            self.i_i = 0

        self.image = self.image_group[self.i_i]
            
        # if self.i_i == g_len:
        #     flag = True
        # elif self.i_i == 0:
        #     flag = False

        # print(self.i_i)
        # self.image = self.image_group[self.i_i]

        # if not flag:
        #     self.i_i += 1
        # else:
        #     self.i_i -= 1

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

        # if self.rect.centerx < 340 + (self.rect.width // 2):
        #     self.rect.centerx = 340 + (self.rect.width // 2)
        # elif self.rect.centerx > 940 - (self.rect.width // 2):
        #     self.rect.centerx = 940 - (self.rect.width // 2)

        self.rect.centerx = max(self.rect.centerx, 340 + (self.rect.width // 2))
        self.rect.centerx = min(self.rect.centerx, 940 - (self.rect.width // 2))

        # if self.rect.centery < 60 + (self.rect.height // 2):
        #     self.rect.centery = 60 + (self.rect.height // 2)
        # elif self.rect.centery > 660 - (self.rect.height // 2):
        #     self.rect.centery = 660 - (self.rect.height // 2)
        self.rect.centery = max(self.rect.centery, 60 + (self.rect.height // 2))
        self.rect.centery = min(self.rect.centery, 660 - (self.rect.height // 2))

        self.position = (self.rect.centerx, self.rect.centery)

    def stop(self):
        self.to = [0,0,0,0]

##### MONSTER CLASS
class Monster(Character):
    def __init__(self, image_group, position, type, hp):
        Character.__init__(self, image_group, position)
        self.is_died = False
        self.type = type    # normal, boss
        self.hp = hp

    def die(self, drop_item):
        self.is_died = True
        drop_item(self)
        monster_group.remove(self)

##############################################################################################

##### about monster
monster_group = pygame.sprite.Group()

MON_0_HP = 10
MON_1_HP = 25

###### about npc
father_slime = Character(father_slime_image, (540, 360))
skeleton = Character(skeleton_image, (840, 600))
ghost = Character(ghost_images, (800, 150))

npc_group = pygame.sprite.Group()
npc_group.add(father_slime, skeleton, ghost)