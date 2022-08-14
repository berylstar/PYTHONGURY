import pygame
import os
##############################################################################################
def check_inven():
    for i in range(7):
        for j in range(2):
            if inven_check[i][j] >2:
                return False
            else:
                return True
##############################################################################################
class Cursor(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image = image
        self.poisiton = position

        self.rect = image.get_rect(center=position)
        self.is_picking = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, event):
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
##############################################################################################
##### equip class
class Equip(pygame.sprite.Sprite):
    def __init__(self, image, index):
        super().__init__()
        self.image = image
        
        self.row = index[0]
        self.col = index[1]

        self.max_row = 7
        self.max_col = 2

        self.rect_left = inven_position[self.row][self.col][0]
        self.rect_top = inven_position[self.row][self.col][1]
        self.rect = (self.rect_left,self.rect_top)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # def inven_move(self, event):
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             self.rect_left -= 60
    #         if event.key == pygame.K_RIGHT:
    #             self.rect_left += 60
    #         if event.key == pygame.K_UP:
    #             self.rect_top -= 60
    #         if event.key == pygame.K_DOWN:
    #             self.rect_top += 60
                
    #     if self.rect_left < 950:
    #         self.rect_left = 950
    #     elif self.rect_left > 1070:
    #         self.rect_left = 1070

    #     if self.rect_top < 120:
    #         self.rect_top = 120
    #     elif self.rect_top > 540:
    #         self.rect_top = 540

    #     self.rect = (self.rect_left,self.rect_top)

    def inven_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.col -= 1
            if event.key == pygame.K_RIGHT:
                self.col += 1
            if event.key == pygame.K_UP:
                self.row -= 1
            if event.key == pygame.K_DOWN:
                self.row += 1
                
        if self.col < 0:
            self.col = 0
        elif self.col > self.max_col:
            self.col = self.max_col
        
        if self.row < 0:
            self.row = 0
        elif self.row > self.max_row:
            self.row = self.max_row

        self.rect_left = inven_position[self.row][self.col][0]
        self.rect_top = inven_position[self.row][self.col][1]

        self.rect = (self.rect_left,self.rect_top)

        # inven_check[self.row][self.col] = 1

##### equip_punch class
class e_Punch(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        # self.max_row = 7
        # self.max_col = 2

##### battery class
class e_Battery(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.max_row = 6
        # self.max_col = 2

##### banana class
class e_Banana(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.max_row = 6
        self.max_col = 1
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
banana_image = pygame.image.load(os.path.join(file_path, "images\\banana.png")).convert_alpha()

# Others
sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()
cursor_image = pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha()

# Inventory
inven_position = [
    [(950,120),(1010,120),(1070,120)],
    [(950,180),(1010,180),(1070,180)],
    [(950,240),(1010,240),(1070,240)],
    [(950,300),(1010,300),(1070,300)],
    [(950,360),(1010,360),(1070,360)],
    [(950,420),(1010,420),(1070,420)],
    [(950,480),(1010,480),(1070,480)],
    [(950,540),(1010,540),(1070,540)]
    ]

inven_check = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]