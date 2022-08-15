import pygame
import os
##############################################################################################
##### CHARACTER CLASS
class Character(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)
        self.direction = "LEFT"
        self.to = [0, 0, 0, 0]  #LEFT, RIGHT, UP, DOWN
        self.flip = False

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

        if self.rect.centerx < 370:
            self.rect.centerx = 370
        elif self.rect.centerx > 910:
            self.rect.centerx = 910

        if self.rect.centery < 90:
            self.rect.centery = 90
        elif self.rect.centery > 630:
            self.rect.centery = 630

        self.position = (self.rect.centerx, self.rect.centery)

    def stop(self):
        self.to = [0,0,0,0]

##### MONSTER CLASS
class Monster(Character):
    def __init__(self, image, position, hp):
        Character.__init__(self, image, position)
        self.is_died = False
        self.hp = hp

    def die(self, drop_item, monster_group):
        self.is_died = True
        drop_item(self.position)
        monster_group.remove(self)

##############################################################################################
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

##### MONSTER
monster_images = [
    pygame.image.load(os.path.join(file_path, "images\\monster_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\monster_2.png")).convert_alpha()
]
monster_group = pygame.sprite.Group()
MON_0_HP = 10
MON_1_HP = 25

##### NPC
father_slime_image = pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()
skeleton_image = pygame.image.load(os.path.join(file_path, "images\\skeleton.png")).convert_alpha()