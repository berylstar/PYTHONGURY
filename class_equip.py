import pygame
import random
from file_image import *
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
        self.position = position

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

        if self.rect.centery < 270:
            self.rect.centery = 270
        elif self.rect.centery > 570:
            self.rect.centery = 570

        self.position = (self.rect.centerx, self.rect.centery)
##############################################################################################
##### equip class
class Equip(pygame.sprite.Sprite):
    def __init__(self, image, index):
        super().__init__()
        self.image = image
        self.name = None

        self.msg_name = None
        self.msg_info = None
        self.msg_eff = None
        
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

    def active_skill(self, player):
        pass

##### pepper class
class e_Pepper(Equip):
    def __init__(self):
        image = pepper_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Chili Pepper"
        self.msg_name = "매운 고추"
        self.msg_info = "슬라임이 매운맛이라면 ?"
        self.msg_eff = "공격력 + 0.3"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

##### ice class
class e_Ice(Equip):
    def __init__(self):
        image = ice_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Ice"
        # self.max_row = 5
        # self.max_col = 2

        self.price = 2

##### apple class
class e_Apple(Equip):
    def __init__(self):
        image = apple_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Green Apple"
        self.max_row = 4
        self.max_col = 1

        self.price = 2

##### mandoo class
class e_Mandoo(Equip):
    def __init__(self):
        image = mandoo_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Mandoo"
        # self.max_row = 5
        # self.max_col = 2

        self.price = 5

##### ancient book class
class e_AncientBook(Equip):
    def __init__(self):
        image = a_book_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Ancient Book"
        self.max_row = 4
        self.max_col = 1

        self.price = 4

##### bone class
class e_Bone(Equip):
    def __init__(self):
        image = bone_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Bone"
        self.max_row = 4
        # self.max_col = 2

        self.price = 0
##############################################################################################
#real equip

##### straw class
class e_Straw(Equip):
    def __init__(self):
        image = straw_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Straw"
        self.msg_name = "빨대"
        self.msg_info = "포션도 빨아먹어야 제 맛"
        self.msg_eff = "포션 회복량 + 5"

        self.max_row = 3
        # self.max_col = 2

        self.price = 7

##### banana class
class e_Banana(Equip):
    def __init__(self):
        image = banana_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Banana"
        self.msg_name = "바나나"
        self.msg_info = "늦잠잤다면 밥 대신 바나나"
        self.msg_eff = "사용 : 체력 20 회복"

        self.max_row = 4
        self.max_col = 1

        self.price = 4

    def active_skill(self, player):
        player.hp = min(player.hp+20, player.max_hp)
        equip_con.equipped_group.remove(self)
        equip_con.able_equip_group.append(self)

##### sandclock class
class e_Sandclock(Equip):
    def __init__(self):
        image = sandclock_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Sand Clock"
        self.msg_name = "모래시계"
        self.msg_info = "뒤집기만 했더니 시간이 멈춰버림"
        self.msg_eff = "스킬 : 3초간 적 정지"

        self.max_row = 4
        # self.max_col = 2

        self.price = 4

    def active_skill(self, player):
        if self.cool_time == False:
            skill_con.active_sandclock[0] = True
            skill_con.active_sandclock[1] = pygame.time.get_ticks()
            self.cool_time = True

##### battery class
class e_Battery(Equip):
    def __init__(self):
        image = battery_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Battery"
        self.msg_name = "건전지"
        self.msg_info = "충전 완료 !"
        self.msg_eff = "이동 속도 + 0.1"
        # self.floor = 0

        self.max_row = 4
        # self.max_col = 2

        self.price = 7

##### dice class
class e_Dice(Equip):
    def __init__(self):
        image = dice_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Dice"
        self.msg_name = "주사위"
        self.msg_info = "운을 시험해보세요 !"
        self.msg_eff = "액티브 : 50퍼센트 확률로 체력 +10 또는 -5"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 3

    def active_skill(self, player):
        if self.cool_time == False:
            skill_con.active_dice[0] = True
            skill_con.active_dice[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            randprob = random.randrange(0,11)
            if randprob <= 5:
                player.hp = min(player.hp+10, player.max_hp)
            else:
                player.hp -= 5
##############################################################################################
##### equip controller
class EquipController():
    def __init__(self):
        self.equipped_group = []
        self.for_sale = [None, None, None]
        self.can_buy = [False, False, False]
        self.able_equip_group = [
            equip_battery,          equip_pepper,
            equip_ice,              
            equip_apple,            equip_mandoo,
            equip_ancientbook,      equip_bone,

            equip_straw,            equip_banana,           equip_sandclock,
            equip_dice,
        ]

##### active controller
class SkillController():
    def __init__(self):

        self.active_sandclock = [False, 0]
        self.active_dice = [False, 0]

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

        # sand clock - monster stop
        if self.active_dice[0] or equip_dice.cool_time:
            if now_time - self.active_dice[1] > 100:
                self.active_dice[0] = False
                equip_dice.image.set_alpha(60)
                print("set alpha")
            if now_time - self.active_dice[1] > 600:
                equip_dice.cool_time = False
                equip_dice.image.set_alpha(255)
            
##############################################################################################
# Inventory
MAX_ROW = 5
MAX_COL = 2

inven_position = [
    # [(950,180),(1010,180),(1070,180)],
    [(950,240),(1010,240),(1070,240)],
    [(950,300),(1010,300),(1070,300)],
    [(950,360),(1010,360),(1070,360)],
    [(950,420),(1010,420),(1070,420)],
    [(950,480),(1010,480),(1070,480)],
    [(950,540),(1010,540),(1070,540)]
    ]

# EQUIPS
equip_battery = e_Battery()
equip_pepper = e_Pepper()
equip_ice = e_Ice()
equip_dice = e_Dice()
equip_apple = e_Apple()
equip_mandoo = e_Mandoo()
equip_ancientbook = e_AncientBook()
equip_bone = e_Bone()
#####
equip_straw = e_Straw()
equip_banana = e_Banana()
equip_sandclock = e_Sandclock()

skill_con = SkillController()
equip_con = EquipController()