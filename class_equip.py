import pygame
import random
from file_image import *
from class_field import field_group, mand
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

        self.msg_name = None        # 12글자
        self.msg_info = None
        self.msg_eff = None
        self.grade = 0              # 0:normal / 1:rare / 2: unique

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
        self.target = None
        self.active = False

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

    def active_skill(self):
        pass

##############################################################################################
##### pepper class
class e_Pepper(Equip):
    def __init__(self):
        image = pepper_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Chili Pepper"
        self.msg_name = "매운 고추"
        self.msg_info = "슬라임이 매운맛이라면?"
        self.msg_eff = "공격력 +3"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

##### ice class
class e_Ice(Equip):
    def __init__(self):
        image = ice_images[0]
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Ice"
        self.msg_name = "얼음"
        self.msg_info = "녹기 전에 빨리"
        self.msg_eff = "이동속도 +0.1, 녹으면서 점점 감소"

        self.floor = 0
        self.charge_times = 0

        # self.max_row = 5
        # self.max_col = 2

        self.price = 2

    def draw(self, screen):
        if self.charge_times == 0:
            screen.blit(self.image, self.rect)
        if self.charge_times == 1:
            screen.blit(ice_images[1], self.rect)
        
        if self.is_active_c:
            screen.blit(skill_c_image, self.rect)
        elif self.is_active_v:
            screen.blit(skill_v_image, self.rect)

##### straw class
class e_Straw(Equip):
    def __init__(self):
        image = straw_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Straw"
        self.msg_name = "빨대"
        self.msg_info = "포션도 빨아먹어야 제 맛"
        self.msg_eff = "포션 회복량 +5"

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
        self.msg_info = "밥 대신 바나나 하나정도"
        self.msg_eff = "사용 : HP +20"
        self.grade = 1
        self.active = True

        self.max_row = 4
        self.max_col = 1

        self.price = 4

    def active_skill(self):
        self.target.hp = min(self.target.hp+20, self.target.max_hp)
        equip_con.equipped_group.remove(self)
        equip_con.able_equip_group.append(self)

##### sandclock class
class e_TrafficLight(Equip):
    def __init__(self):
        image = trafficlight_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Traffic Light"
        self.msg_name = "신호등"
        self.msg_info = "빨간 불 = 멈춤"
        self.msg_eff = "스킬 : 3초간 적 정지"
        self.grade = 1
        self.active = True

        self.max_row = 3
        # self.max_col = 2

        self.price = 4

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_sandclock[0] = True
            skill_con.active_sandclock[1] = pygame.time.get_ticks()
            self.cool_time = True

##### battery class
class e_Battery(Equip):
    def __init__(self):
        image = battery_image       # image = battery_images[self.charge_times]
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Battery"
        self.msg_name = "건전지"
        self.msg_info = "충전 중"
        self.msg_eff = "충전마다 이동속도 +0.05 (/0.15)"
        self.grade = 1

        self.floor = 0
        self.charge_times = 0

        self.max_row = 4
        # self.max_col = 2

        self.price = 7

##### dice class
class e_Dice(Equip):
    def __init__(self):
        image = dice_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Lucky Dice"
        self.msg_name = "행운의 주사위"
        self.msg_info = "운을 시험해보세요 !"
        self.msg_eff = "스킬 : 50퍼센트 확률로 HP +10 또는 -10"
        self.grade = 1
        self.active = True

        # self.max_row = 5
        # self.max_col = 2

        self.price = 3

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_dice[0] = True
            skill_con.active_dice[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            randprob = random.randrange(1,11)
            if randprob <= 5:
                self.target.hp = min(self.target.hp+10, self.target.max_hp)
            else:
                self.target.hp -= 10

##### thunder class
class e_Thunder(Equip):
    def __init__(self):
        image = thunder_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Thunder"
        self.msg_name = "천둥번개"
        self.msg_info = "마른 하늘에 날벼락"
        self.msg_eff = "스킬 : 전체 적에게 5 데미지"
        self.grade = 1
        self.active = True

        self.max_row = 3
        self.max_col = 1

        self.price = 7

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_thunder[0] = True
            skill_con.active_thunder[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            for monster in self.target:
                monster.hp -= 30

##### gloves class
class e_BoxingGlove(Equip):
    def __init__(self):
        image = gloves_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = " Boxer Glove"
        self.msg_name = "복싱 글러브"
        self.msg_info = "싸울 준비 완료 !"
        self.msg_eff = "펀치 크기 증가"
        self.grade = 2
        
        self.max_row = 3
        self.max_col = 1

        self.price = 10

##### wax class
class e_Wax(Equip):
    def __init__(self):
        image = wax_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Hair Wax"
        self.msg_name = "헤어 왁스"
        self.msg_info = "슬라임도 왁스 바를 줄 압니다"
        self.msg_eff = "공격력 +2"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 3

##### turtle shell class
class e_TurtleShell(Equip):
    def __init__(self):
        image = turtleshell_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Turtle Shell"
        self.msg_name = "거북이 등껍질"
        self.msg_info = "시간이.. 느리게.."
        self.msg_eff = "시간 데미지 감소"
        self.grade = 1

        self.max_row = 4
        self.max_col = 1

        self.price = 6

##### helmet class
class e_Helmet(Equip):
    def __init__(self):
        image = helmet_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Helemt"
        self.msg_name = "하이바"
        self.msg_info = "머리를 안전하게 !"
        self.msg_eff = "적 충돌 데미지 감소"

        self.max_row = 4
        self.max_col = 1

        self.price = 6

##### heartstone class
class e_Heartstone(Equip):
    def __init__(self):
        image = heartstone_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Heart Stone"
        self.msg_name = "하트 모양 원석"
        self.msg_info = "하트스톤"
        self.msg_eff = "최대 체력 +20"
        self.grade = 1

        self.max_row = 4
        self.max_col = 1

        self.price = 6

##### brokenstone class
class e_Brokenstone(Equip):
    def __init__(self):
        image = brokenstone_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Broken Stone"
        self.msg_name = "부서진 원석"
        self.msg_info = "하트스톤이 반 갈라짐"
        self.msg_eff = "최대 체력 +10"

        self.max_row = 4
        # self.max_col = 2

        self.price = 6

##### crescentmoon class
class e_Crescent(Equip):
    def __init__(self):
        image = crescentmoon_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Crescent Moon"
        self.msg_name = "초승달"
        self.msg_info = "달에게 소원을 빌어보자"
        self.msg_eff = "낮은 확률로 부활"

        self.revival = False

        self.max_row = 4
        self.max_col = 1

        self.price = 6

    def prob_revival(self):
        randprob = random.randrange(1,101)
        if randprob <= 3:
            self.revival = True
        else:
            self.revival = False

##### brokenstone class
class e_Mushroom(Equip):
    def __init__(self):
        image = mushroom_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Bonus Mushroom"
        self.msg_name = "보너스 버섯"
        self.msg_info = "어디서 본 듯 한 버섯"
        self.msg_eff = "목숨이 0 되면 부활"
        self.grade = 2

        # self.max_row = 4
        # self.max_col = 2

        self.price = 6

##### binoculars class
class e_Binoculars(Equip):
    def __init__(self):
        image = binoculars_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Binoculars"
        self.msg_name = "쌍안경"
        self.msg_info = "두 눈 크게 뜨고 찾아보자"
        self.msg_eff = "아이템 드롭률 +3%"

        # self.max_row = 5
        self.max_col = 0

        self.price = 6

##### pizza class
class e_Pizza(Equip):
    def __init__(self):
        image = pizza_image
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Hot Pizza"
        self.msg_name = "뜨거운 피자"
        self.msg_info = "치즈가 끈적거려요"
        self.msg_eff = "투사체 속도 감소"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

##### smokebomb class
class e_Smokebomb(Equip):
    def __init__(self):
        image = None
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Smoke Bomb"
        self.msg_name = "연막탄"
        self.msg_info = "연기 속에 가려진"
        self.msg_eff = "스킬 : 일정시간 무적"
        self.grade = 1
        self.active = True

        self.save = [0, 0]

        # self.max_row = 5
        # self.max_col = 1

        self.price = 3

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_smokebomb[0] = True
            skill_con.active_smokebomb[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            self.save = [self.target.dp, self.target.damaged_time]
            self.target.dp = 100
            self.target.damaged_time = 0

##### keys class
class e_Keys(Equip):
    def __init__(self):
        image = None
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Keys"
        self.msg_name = "열쇠 꾸러미"
        self.msg_info = "이 중 하나는 맞겠지"
        self.msg_eff = "사용 : 계단 열기"
        self.grade = 1
        self.active = True

        # self.max_row = 4
        # self.max_col = 1

        self.price = 4

    def active_skill(self):
        if not self.target % 20 == 0 :
            field_group.add(mand)   #keys field
            equip_con.equipped_group.remove(self)
            equip_con.able_equip_group.append(self)

##### rope class
class e_Rope(Equip):
    def __init__(self):
        image = None
        index = (0,0)
        Equip.__init__(self, image, index)
        self.name = "Rope"
        self.msg_name = "비상 탈출 로프"
        self.msg_info = "지상으로 !"
        self.msg_eff = "사용 : 0층으로"
        self.grade = 1
        self.active = True

        # self.max_row = 4
        # self.max_col = 1

        self.price = 4

    def active_skill(self):
        
        field_group.add(mand)   #rope field
        skill_con.active_rope = True
        equip_con.equipped_group.remove(self)
        equip_con.able_equip_group.append(self)
##############################################################################################
##### equip controller
class EquipController():
    def __init__(self):
        self.equipped_group = []
        self.for_sale = [None, None, None]
        self.can_buy = [False, False, False]
        self.able_equip_group = [
            equip_pepper,           equip_straw,            equip_banana,               equip_sandclock,            equip_ice,
            equip_dice,             equip_battery,          equip_thunder,              equip_wax,
            equip_heartstone,       equip_brokenstone,      equip_crescentmoon,         equip_mushroom,
            equip_pizza,            equip_helmet,           equip_gloves,               equip_turtleshell,
            equip_binoculars
            #, , , , , , , , smokebomb, keys, rope
        ]
        # self.perc_normal = 80
        self.normal_equips = [
            equip_ice,              equip_pepper,           equip_straw,                equip_wax,
            equip_helmet,           equip_brokenstone,      equip_binoculars,           equip_pizza,
            equip_crescentmoon,     
        ]

        self.perc_rare = 15
        self.rare_equips = [
            equip_dice,             equip_battery,          equip_sandclock,            equip_banana,
            equip_turtleshell,      equip_heartstone,       equip_thunder,
        ]

        self.perc_unique = 5
        self.unique_equips = [
            equip_gloves,           equip_mushroom, 
        ]
        print("RESET EQUIP_CON")

##### active controller
class SkillController():
    def __init__(self):

        self.active_sandclock = [False, 0]
        self.active_dice = [False, 0]
        self.active_thunder = [False, 0]
        self.active_smokebomb = [False, 0]
        self.active_rope = False

    def active_time(self):                          # 시연시간, 쿨타임 밸런스 조절 필요
        now_time = pygame.time.get_ticks()

        # sand clock - monster stop
        if self.active_sandclock[0] or equip_sandclock.cool_time:
            if now_time - self.active_sandclock[1] > 3000:
                self.active_sandclock[0] = False
                equip_sandclock.image.set_alpha(60)
            if now_time - self.active_sandclock[1] > 30000:
                equip_sandclock.cool_time = False
                equip_sandclock.image.set_alpha(255)

        # dice - random effect
        if self.active_dice[0] or equip_dice.cool_time:
            if now_time - self.active_dice[1] > 100:
                self.active_dice[0] = False
                equip_dice.image.set_alpha(60)
            if now_time - self.active_dice[1] > 1000:
                equip_dice.cool_time = False
                equip_dice.image.set_alpha(255)

        # thunder - monster damage
        if self.active_thunder[0] or equip_thunder.cool_time:
            if now_time - self.active_thunder[1] > 100:
                self.active_thunder[0] = False
                equip_thunder.image.set_alpha(60)
            if now_time - self.active_thunder[1] > 600:
                equip_thunder.cool_time = False
                equip_thunder.image.set_alpha(255)

        # smokebomb - player no damage
        if self.active_smokebomb[0] or equip_smokebomb.cool_time:
            if now_time - self.active_smokebomb[1] > 3000:
                if self.active_smokebomb[0]:
                    equip_smokebomb.target.dp = equip_smokebomb.save[0]
                    equip_smokebomb.target.damaged_time = equip_smokebomb.save[1]
                self.active_smokebomb[0] = False
                equip_smokebomb.image.set_alpha(60)
                
            if now_time - self.active_smokebomb[1] > 30000:
                equip_smokebomb.cool_time = False
                equip_smokebomb.image.set_alpha(255)
                
            
##############################################################################################
# Inventory
MAX_ROW = 5
MAX_COL = 2

inven_position = [
    [(950,240),(1010,240),(1070,240)],
    [(950,300),(1010,300),(1070,300)],
    [(950,360),(1010,360),(1070,360)],
    [(950,420),(1010,420),(1070,420)],
    [(950,480),(1010,480),(1070,480)],
    [(950,540),(1010,540),(1070,540)]
    ]

# EQUIPS
equip_ice = e_Ice()
equip_dice = e_Dice()
equip_pepper = e_Pepper()
equip_battery = e_Battery()
equip_straw = e_Straw()
equip_gloves = e_BoxingGlove()
equip_sandclock = e_TrafficLight()
equip_banana = e_Banana()
equip_wax = e_Wax()
equip_turtleshell = e_TurtleShell()
equip_helmet = e_Helmet()
equip_heartstone = e_Heartstone()
equip_brokenstone = e_Brokenstone()
equip_binoculars = e_Binoculars()
equip_pizza = e_Pizza()
equip_mushroom = e_Mushroom()
equip_thunder = e_Thunder()
# poisonapple
equip_crescentmoon = e_Crescent()
equip_smokebomb = e_Smokebomb()
equip_keys = e_Keys()
equip_rope = e_Rope()


skill_con = SkillController()
equip_con = EquipController()

def equip_reset():
    global equip_ice, equip_dice, equip_pepper, equip_battery, equip_straw, equip_gloves, equip_sandclock, equip_banana
    global equip_wax, equip_turtleshell, equip_helmet, equip_heartstone, equip_brokenstone, equip_binoculars
    global equip_pizza, equip_mushroom, equip_thunder,                  equip_crescentmoon, equip_smokebomb
    global equip_keys, equip_rope

    equip_ice = e_Ice()
    equip_dice = e_Dice()
    equip_pepper = e_Pepper()
    equip_battery = e_Battery()
    equip_straw = e_Straw()
    equip_gloves = e_BoxingGlove()
    equip_sandclock = e_TrafficLight()
    equip_banana = e_Banana()
    equip_wax = e_Wax()
    equip_turtleshell = e_TurtleShell()
    equip_helmet = e_Helmet()
    equip_heartstone = e_Heartstone()
    equip_brokenstone = e_Brokenstone()
    equip_binoculars = e_Binoculars()
    equip_pizza = e_Pizza()
    equip_mushroom = e_Mushroom()
    equip_thunder = e_Thunder()
    # poisonapple
    equip_crescentmoon = e_Crescent()
    equip_smokebomb = e_Smokebomb()
    equip_keys = e_Keys()
    equip_rope = e_Rope()