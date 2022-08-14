import pygame
import os
##############################################################################################
##############################################################################################
##### equip class
class Equip(pygame.sprite.Sprite):
    def __init__(self, image, index):
        super().__init__()
        self.image = image

        self.rect_left = inven_position[index][0]
        self.rect_top = inven_position[index][1]

        self.rect = (self.rect_left,self.rect_top)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def inven_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect_left -= 60
            if event.key == pygame.K_RIGHT:
                self.rect_left += 60
            if event.key == pygame.K_UP:
                self.rect_top -= 60
            if event.key == pygame.K_DOWN:
                self.rect_top += 60
                
        if self.rect_left < 950:
            self.rect_left = 950
        elif self.rect_left > 1070:
            self.rect_left = 1070

        if self.rect_top < 120:
            self.rect_top = 120
        elif self.rect_top > 540:
            self.rect_top = 540

        self.rect = (self.rect_left,self.rect_top)

##### equip_punch class
class e_Punch(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)

##### battery class
class e_Battery(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
##############################################################################################
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

# Punch Image
punch_d_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_v_image = pygame.image.load(os.path.join(file_path, "images\\punch_v.png")).convert_alpha()
punch_f_image = pygame.image.load(os.path.join(file_path, "images\\punch_f.png")).convert_alpha()

# Equip Image
battery_image = pygame.image.load(os.path.join(file_path, "images\\battery.png")).convert_alpha()

# Others
sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()
cursor_image = pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha()

# Inventory
inven_position = [
    (950,120),(1010,120),(1070,120),
    (950,180),(1010,180),(1070,180),
    (950,240),(1010,240),(1070,240),
    (950,300),(1010,300),(1070,300),
    (950,360),(1010,360),(1070,360),
    (950,420),(1010,420),(1070,420),
    (950,480),(1010,480),(1070,480),
    (950,540),(1010,540),(1070,540),
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