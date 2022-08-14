import pygame
import os
##############################################################################################
##############################################################################################
##### EQUIP CLASS
class Equip(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position
        
        self.rect = image.get_rect(center=position)
        self.time = pygame.time.get_ticks()
        # self.is_picked = False

    # def put_in(self):
    #     inven_check[0] = 1

    def get_time(self):
        return pygame.time.get_ticks() - self.time

    def draw(self, screen, object):
        if object.direction == "LEFT":
            self.rect = (object.rect.x-60, object.rect.y)
        elif object.direction == "RIGHT":
            self.rect = (object.rect.x+60, object.rect.y)
        elif object.direction == "UP":
            self.rect = (object.rect.x, object.rect.y-60)
        elif object.direction == "DOWN":
            self.rect = (object.rect.x, object.rect.y+60)

        screen.blit(self.image, self.rect)

    def inven_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.centerx -= 60
            if event.key == pygame.K_RIGHT:
                self.rect.centerx += 60
            if event.key == pygame.K_UP:
                self.rect.centery -= 60
            if event.key == pygame.K_DOWN:
                self.rect.centery += 60
                
        if self.rect.centerx < 980:
            self.rect.centerx = 980
        elif self.rect.centerx > 1100:
            self.rect.centerx = 1100

        if self.rect.centery < 150:
            self.rect.centery = 150
        elif self.rect.centery > 570:
            self.rect.centery = 570

        self.position = (self.rect.centerx, self.rect.centery)

##### PUNCH CLASS
class Punch(Equip):
    def __init__(self, image, position, direction):
        Equip.__init__(self, image, position)
        self.direction = direction

##### PORTION CLASS
class Whatisthis(Equip):
    def __init__(self, image, position):
        Equip.__init__(self,image,position)
##############################################################################################
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

punch_d_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_v_image = pygame.image.load(os.path.join(file_path, "images\\punch_v.png")).convert_alpha()
punch_f_image = pygame.image.load(os.path.join(file_path, "images\\punch_f.png")).convert_alpha()

wit_image = pygame.image.load(os.path.join(file_path, "images\\equip_1.png")).convert_alpha()

sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()


inven_position = [
    (980,150),(1040,150),(1100,150),
    (980,210),(1040,210),(1100,210),
    (980,270),(1040,270),(1100,270),
    (980,330),(1040,330),(1100,330),
    (980,390),(1040,390),(1100,390),
    (980,450),(1040,450),(1100,450),
    (980,510),(1040,510),(1100,510),
    (980,570),(1040,570),(1100,570),
    ]

inven_check = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
]