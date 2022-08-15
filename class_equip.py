import pygame
import os
##############################################################################################
def inven_is_overlap(equip_group):
    flag = False
    for equip_1 in equip_group:
        for equip_2 in equip_group:
            if equip_1 != equip_2:
                if pygame.sprite.collide_mask(equip_1, equip_2):
                    flag = True
                else:
                    pass
    return flag
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

        if self.rect.centery < 210:
            self.rect.centery = 210
        elif self.rect.centery > 510:
            self.rect.centery = 510

        self.position = (self.rect.centerx, self.rect.centery)
##############################################################################################
##### equip class
class Equip(pygame.sprite.Sprite):
    def __init__(self, image, index):
        super().__init__()
        self.image = image
        
        self.row = index[0]
        self.col = index[1]

        self.max_row = 5
        self.max_col = 2

        self.rect_left = inven_position[self.row][self.col][0]
        self.rect_top = inven_position[self.row][self.col][1]
        self.rect = (self.rect_left,self.rect_top)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

##### equip_punch class
class e_Punch(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        # self.max_row = 5
        # self.max_col = 2

##### battery class
class e_Battery(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.max_row = 4
        # self.max_col = 2

##### banana class
class e_Banana(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.max_row = 4
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
MAX_ROW = 5
MAX_COL = 2
inven_position = [
    [(950,180),(1010,180),(1070,180)],
    [(950,240),(1010,240),(1070,240)],
    [(950,300),(1010,300),(1070,300)],
    [(950,360),(1010,360),(1070,360)],
    [(950,420),(1010,420),(1070,420)],
    [(950,480),(1010,480),(1070,480)]
    ]