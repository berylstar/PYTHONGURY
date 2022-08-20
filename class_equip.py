import pygame
from file_image import *
from class_character import monster_group
##############################################################################################
def is_inven_overlapped(equip_group):
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
        self.clicking = False

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
        self.name = None
        
        self.row = index[0]
        self.col = index[1]
        self.max_row = MAX_ROW
        self.max_col = MAX_COL
        self.rect_left = inven_position[self.row][self.col][0]
        self.rect_top = inven_position[self.row][self.col][1]
        self.rect = (self.rect_left,self.rect_top)

        self.is_effected = False
        self.is_active_c = False
        self.is_active_v = False
        self.cool_time = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        if self.is_active_c:
            screen.blit(skill_c_image, self.rect)
        elif self.is_active_v:
            screen.blit(skill_v_image, self.rect)

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

    def get_index(self):
        return (self.row, self.col)

    def active_skill(self):
        pass

##### battery class
class e_Battery(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Battery"
        self.max_row = 4
        # self.max_col = 2

        self.price = 7

##### banana class
class e_Banana(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Banana"
        self.max_row = 4
        self.max_col = 1

        self.price = 4

##### pepper class
class e_Pepper(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Chili Pepper"
        # self.max_row = 5
        self.max_col = 1

        self.price = 3

##### ice class
class e_Ice(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Ice"
        # self.max_row = 5
        # self.max_col = 2

        self.price = 2

##### dice class
class e_Dice(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Dice"
        # self.max_row = 5
        # self.max_col = 2

        self.price = 3

##### sandclock class
class e_Sandclock(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Sand Clock"
        self.max_row = 4
        # self.max_col = 2

        self.price = 4

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_sandclock[0] = True
            skill_con.active_sandclock[1] = pygame.time.get_ticks()
            self.cool_time = True

##### apple class
class e_Apple(Equip):
    def __init__(self, image, index):
        Equip.__init__(self, image, index)
        self.name = "Green Apple"
        self.max_row = 4
        self.max_col = 1

        self.price = 2
##############################################################################################
##### equip controller
class EquipController():
    def __init__(self):
        self.equipped_group = []
        self.for_sale = [None, None, None]
        self.can_buy = [True, True, True]
        self.able_equip_group = [
            equip_banana,
            equip_battery,
            equip_pepper,
            equip_ice,
            equip_dice,
            equip_sandclock,
            equip_apple,
        ]

##### active controller
class SkillController():
    def __init__(self):
        self.active_sandclock = [False, 0]

    def active_time(self):
        now_time = pygame.time.get_ticks()

        # sand clock - monster stop
        if self.active_sandclock[0] or equip_sandclock.cool_time:
            if now_time - self.active_sandclock[1] > 3000:
                self.active_sandclock[0] = False
                equip_sandclock.image.set_alpha(60)
            if now_time - self.active_sandclock[1] > 30000:
                equip_sandclock.cool_time = False
                equip_sandclock.image.set_alpha(255)
            
##############################################################################################
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

# EQUIPS
equip_banana = e_Banana(banana_image, (0,0))
equip_battery = e_Battery(battery_image, (0,0))
equip_pepper = e_Pepper(pepper_image, (0,0))
equip_ice = e_Ice(ice_image, (0,0))
equip_dice = e_Dice(dice_image, (0,0))
equip_sandclock = e_Sandclock(sandclock_image, (0,0))
equip_apple = e_Apple(apple_iamge, (0,0))

skill_con = SkillController()
equip_con = EquipController()