import pygame
import random
from file_image import *
from file_sound import *
from class_field import field_group, key_field, portal
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
            sound_con.play_sound(sound_wasd)
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
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.name = None

        self.msg_name = None
        self.msg_info = None
        self.msg_eff = None
        self.msg_eff_2 = None
        self.grade = 0              # 0:normal / 1:rare / 2: unique

        self.row = 0
        self.col = 0     #(0,0)으로 초기화 해도 문제없나 ?
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

    def reset(self):
        self.row = 0
        self.col = 0
        self.rect_left = inven_position[self.row][self.col][0]
        self.rect_top = inven_position[self.row][self.col][1]
        self.rect = (self.rect_left,self.rect_top)

        self.is_effected = False
        self.is_active_c = False
        self.is_active_v = False
        self.cool_time = False

##############################################################################################
#                                                                           #### mushroom
class E_Mushroom(Equip):
    def __init__(self):
        image = mushroom_image
        Equip.__init__(self, image)
        self.msg_name = "보너스 버섯"
        self.msg_info = "어디서 본 듯 한 버섯 ?"
        self.msg_eff = "목숨이 0 되면 부활"
        self.grade = 2

        # self.max_row = 4
        # self.max_col = 2

        self.price = 6

#                                                                           #### crescentmoon
class E_CrescentMoon(Equip):
    def __init__(self):
        image = crescentmoon_image
        Equip.__init__(self, image)
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

#                                                                           #### banana
class E_Banana(Equip):
    def __init__(self):
        image = banana_image
        Equip.__init__(self, image)
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
        equip_con.rare_equips.append(self)

#                                                                           #### wax
class E_Wax(Equip):
    def __init__(self):
        image = wax_image
        Equip.__init__(self, image)
        self.msg_name = "헤어 왁스"
        self.msg_info = "슬라임도 왁스 바른다네요"
        self.msg_eff = "공격력 +2"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 3

#                                                                           #### pepper
class E_Pepper(Equip):
    def __init__(self):
        image = pepper_image
        Equip.__init__(self, image)
        self.msg_name = "빨간 고추"
        self.msg_info = "슬라임이 매운맛이라면?"
        self.msg_eff = "공격력 +3"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

#                                                                           #### heartstone
class E_HeartStone(Equip):
    def __init__(self):
        image = heartstone_image
        Equip.__init__(self, image)
        self.msg_name = "마음의 돌"
        self.msg_info = "하트스톤"
        self.msg_eff = "최대 체력 +20"
        self.grade = 1

        self.max_row = 4
        self.max_col = 1

        self.price = 6

#                                                                           #### halfstone 
class E_HalfStone(Equip):
    def __init__(self):
        image = halfstone_image
        Equip.__init__(self, image)
        self.msg_name = "반 돌"
        self.msg_info = "나머지 반쪽은 어디에"
        self.msg_eff = "최대 체력 +10"

        self.max_row = 4
        # self.max_col = 2

        self.price = 6

#                                                                           #### poison apple 
class E_PoisonApple(Equip):
    def __init__(self):
        image = poisonapple_image
        Equip.__init__(self, image)
        self.msg_name = "독사과"
        self.msg_info = "먹어도 되는 걸까..?"
        self.msg_eff = "체력 +10, 최대 체력 +10"
        self.msg_eff_2 = "시간 데미지와 충돌 데미지 증가"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 6

#                                                                           #### ice
class E_Ice(Equip):
    def __init__(self):
        image = ice_images[0]
        Equip.__init__(self, image)
        self.msg_name = "얼음"
        self.msg_info = "녹기 전에 빨리 움직이세요"
        self.msg_eff = "이동속도 +0.1"
        self.msg_eff_2 = "녹으면서 점점 감소"

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

#                                                                           #### battery
class E_Battery(Equip):
    def __init__(self):
        image = battery_image
        Equip.__init__(self, image)
        self.msg_name = "건전지"
        self.msg_info = "충전 중-!"
        self.msg_eff = "충전마다 이동속도 +0.05"
        self.msg_eff_2 = "최대 3번"
        self.grade = 1

        self.floor = 0
        self.charge_times = 0

        self.max_row = 4
        # self.max_col = 2

        self.price = 7

    # def draw(self, screen):
    #     if self.charge_times == 0:
    #         screen.blit(self.image, self.rect)
    #     elif self.charge_times == 1:
    #         screen.blit(battery_images[1], self.rect)
    #     elif self.charge_times == 2:
    #         screen.blit(battery_images[2], self.rect)
        
    #     if self.is_active_c:
    #         screen.blit(skill_c_image, self.rect)
    #     elif self.is_active_v:
    #         screen.blit(skill_v_image, self.rect)

#                                                                           #### roller skate
class E_RollerSkate(Equip):
    def __init__(self):
        image = rollerskate_image
        Equip.__init__(self, image)
        self.msg_name = "롤러스케이트"
        self.msg_info = "신나게 달려보자"
        self.msg_eff = "이동속도 + 0.1"

        self.max_row = 4
        self.max_col = 1

        self.price = 7

#                                                                           #### boxer glove
class E_BoxerGlove(Equip):
    def __init__(self):
        image = gloves_image
        Equip.__init__(self, image)
        self.msg_name = "복싱 글러브"
        self.msg_info = "싸울 준비 완료 !"
        self.msg_eff = "펀치 크기 증가"
        self.grade = 2
        
        self.max_row = 3
        self.max_col = 1

        self.price = 10

#                                                                           #### helmet
class E_Helmet(Equip):
    def __init__(self):
        image = helmet_image
        Equip.__init__(self, image)
        self.msg_name = "헬멧"
        self.msg_info = "머리를 안전하게 !"
        self.msg_eff = "적 충돌 데미지 감소"

        self.max_row = 4
        self.max_col = 1

        self.price = 6

#                                                                           #### turtle shell
class E_TurtleShell(Equip):
    def __init__(self):
        image = turtleshell_image
        Equip.__init__(self, image)
        self.msg_name = "거북이 등껍질"
        self.msg_info = "시간이.. 느리게.."
        self.msg_eff = "시간 데미지 감소"

        self.max_row = 4
        self.max_col = 1

        self.price = 6

#                                                                           #### pizza
class E_Pizza(Equip):
    def __init__(self):
        image = pizza_image
        Equip.__init__(self, image)
        self.msg_name = "치즈 피자"
        self.msg_info = "치즈가 끈적거려요"
        self.msg_eff = "적 투사체 속도 감소"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

#                                                                           #### glasses
class E_3DGlasses(Equip):
    def __init__(self):
        image = sdglasses_image
        Equip.__init__(self, image)
        self.msg_name = "3D 안경"
        self.msg_info = "2D로 보는거 보단 낫겠죠"
        self.msg_eff = "적 투명화 감지"

        # self.max_row = 5
        self.max_col = 1

        self.price = 3

#                                                                           #### talisman
class E_Talisman(Equip):
    def __init__(self):
        image = talisman_image
        Equip.__init__(self, image)
        self.msg_name = "부적"
        self.msg_info = "강시 이마에 붙어있던 거"
        self.msg_eff = "적 대시 금지"

        self.max_row = 4
        # self.max_col = 2

        self.price = 3

#                                                                           #### ticket
class E_Ticket(Equip):
    def __init__(self):
        image = ticket_image
        Equip.__init__(self, image)
        self.msg_name = "황금 티켓"
        self.msg_info = "상점 우수 고객"
        self.msg_eff = "상점 레어도 증가"
        self.grade = 1

        # self.max_row = 5
        self.max_col = 0

        self.price = 3

#                                                                           #### straw
class E_Straw(Equip):
    def __init__(self):
        image = straw_image
        Equip.__init__(self, image)
        self.msg_name = "빨대"
        self.msg_info = "포션도 빨아먹어야 제 맛"
        self.msg_eff = "포션 회복량 +5"
        self.grade = 1

        self.max_row = 3
        # self.max_col = 2

        self.price = 7

#                                                                           #### machine
class E_Machine(Equip):
    def __init__(self):
        image = machine_image
        Equip.__init__(self, image)
        self.msg_name = "오래된 기계"
        self.msg_info = "옛날 포션은 기계에서 만들어졌습니다.."
        self.msg_eff = "포션 드롭률 +3%"

        # self.max_row = 5
        self.max_col = 1

        self.price = 7

#                                                                           #### piggy bank
class E_PiggyBank(Equip):
    def __init__(self):
        image = piggybank_image
        Equip.__init__(self, image)
        self.msg_name = "돼지 저금통"
        self.msg_info = "----"
        self.msg_eff = "레드 코인 등장"
        self.grade = 1

        # self.max_row = 5
        self.max_col = 1

        self.price = 7

#                                                                           #### metal detector
class E_MetalDetector(Equip):
    def __init__(self):
        image = metaldetector_image
        Equip.__init__(self, image)
        self.msg_name = "금속 탐지기"
        self.msg_info = "삐비비비비빅"
        self.msg_eff = "코인 드롭률 +3%"

        self.max_row = 4
        # self.max_col = 2

        self.price = 7

#                                                                           #### binoculars 
class E_Binoculars(Equip):
    def __init__(self):
        image = binoculars_image
        Equip.__init__(self, image)
        self.msg_name = "쌍안경"
        self.msg_info = "멀리 있는 아이템까지"
        self.msg_eff = "아이템 드롭률 +3%"

        # self.max_row = 5
        self.max_col = 0

        self.price = 6

#                                                                           #### traffic light
class E_TrafficLight(Equip):
    def __init__(self):
        image = trafficlight_image
        Equip.__init__(self, image)
        self.msg_name = "신호등"
        self.msg_info = "빨간 불에는 멈춰"
        self.msg_eff = "스킬 : 3초간 적 정지"
        self.grade = 1
        self.active = True

        self.max_row = 3
        # self.max_col = 2

        self.price = 4

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_trafficlight[0] = True
            skill_con.active_trafficlight[1] = pygame.time.get_ticks()
            self.cool_time = True

#                                                                           #### thunder
class E_Thunder(Equip):
    def __init__(self):
        image = thunder_image
        Equip.__init__(self, image)
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
                monster.hp -= 5

#                                                                           #### dice
class E_Dice(Equip):
    def __init__(self):
        image = dice_image
        Equip.__init__(self, image)
        self.msg_name = "행운의 주사위"
        self.msg_info = "운을 시험해보세요 !"
        self.msg_eff = "스킬 : 50퍼센트 확률로"
        self.msg_eff_2 = "HP +10 또는 -10"
        self.grade = 1
        self.active = True

        self.max_row = 4
        self.max_col = 1

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

#                                                                           #### magic cloak
class E_MagicCloak(Equip):
    def __init__(self):
        image = magiccloak_image
        Equip.__init__(self, image)
        self.msg_name = "마법 망토"
        self.msg_info = "마법학교에서 가져왔다네요"
        self.msg_eff = "스킬 : 일정시간 무적"
        self.grade = 1
        self.active = True

        self.save = [0, 0]

        self.max_row = 4
        self.max_col = 1

        self.price = 3

    def active_skill(self):
        if self.cool_time == False:
            skill_con.active_magiccloak[0] = True
            skill_con.active_magiccloak[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            self.save = self.target.dp
            self.target.dp = 100
            e_magiccloak.target.alpha(60)

#                                                                           #### golden key
class E_GoldenKey(Equip):
    def __init__(self):
        image = goldenkey_image
        Equip.__init__(self, image)
        self.msg_name = "황금 열쇠"
        self.msg_info = "어딘가에는 맞겠지"
        self.msg_eff = "사용 : 계단 열기"
        self.grade = 2
        self.active = True

        self.max_row = 3
        # self.max_col = 2

        self.price = 4

    def active_skill(self):
        if not self.target % 20 == 0 :
            field_group.add(key_field)   #keys field
            equip_con.equipped_group.remove(self)
            equip_con.unique_equips.append(self)

#                                                                           #### rope
class E_EscapeRope(Equip):
    def __init__(self):
        image = dummy
        Equip.__init__(self, image)
        self.msg_name = "탈출 로프"
        self.msg_info = "지상으로 !"
        self.msg_eff = "사용 : 0층으로"
        self.grade = 1
        self.active = True

        # self.max_row = 4
        # self.max_col = 1

        self.price = 4

    def active_skill(self):
        
        field_group.add(portal)
        skill_con.active_escaperope = True
        equip_con.equipped_group.remove(self)
        equip_con.rare_equips.append(self)

#                                                                           #### for treasure box 
class E_Potion(Equip):
    def __init__(self):
        image = potion_image
        Equip.__init__(self, image)
        self.msg_name = "대용량 포션"
        self.msg_info = "마시고 기운내세요"
        self.msg_eff = "HP + 50"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 0
##############################################################################################
##### equip controller
class EquipController():
    def __init__(self):
        self.equipped_group = []
        self.for_sale = [None, None, None]
        self.can_buy = [False, False, False]
        
        self.normal_equips = [
            e_crescentmoon, e_wax, e_pepper, e_halfstone, e_poisonapple, e_ice, e_rollerskate, e_helmet, e_turtleshell,
            e_pizza, e_3dglasses, e_talisman, e_machine, e_metaldetector, e_binoculars
        ]

        self.perc_rare = 10
        self.rare_equips = [
            e_banana, e_heartstone, e_battery, e_ticket, e_straw, e_piggybank,
            e_trafficlight, e_thunder, e_dice, e_magiccloak, e_escaperope
        ]

        self.perc_unique = 2
        self.unique_equips = [
            e_mushroom, e_boxerglove, e_goldenkey
        ]

    def equip_grade(self, equip):
        if equip.grade == 0:
            return ("NORMAL", (255,255,255))
        elif equip.grade == 1:
            return ("RARE", (255,255,0))
        elif equip.grade == 2:
            return ("UNIQUE", (255,0,255))

    def equip_on(self, equip):
        if equip.grade == 0:
            self.normal_equips.remove(equip)
        elif equip.grade == 1:
            self.rare_equips.remove(equip)
        elif equip.grade == 2:
            self.unique_equips.remove(equip)

    def equip_off(self, equip):
        if equip.grade == 0:
            self.normal_equips.append(equip)
        elif equip.grade == 1:
            self.rare_equips.append(equip)
        elif equip.grade == 2:
            self.unique_equips.append(equip)

##### active controller
class SkillController():
    def __init__(self):

        self.active_trafficlight = [False, 0]
        self.active_dice = [False, 0]
        self.active_thunder = [False, 0]
        self.active_magiccloak = [False, 0]
        self.active_escaperope = False

    def active_time(self):                          # 시연시간, 쿨타임 밸런스 조절 필요
        now_time = pygame.time.get_ticks()

        # traffic light - monster stop
        if self.active_trafficlight[0] or e_trafficlight.cool_time:
            if now_time - self.active_trafficlight[1] > 3000:
                self.active_trafficlight[0] = False
                e_trafficlight.image.set_alpha(60)
            if now_time - self.active_trafficlight[1] > 30000:
                e_trafficlight.cool_time = False
                e_trafficlight.image.set_alpha(255)

        # dice - random effect
        if self.active_dice[0] or e_dice.cool_time:
            if now_time - self.active_dice[1] > 100:
                self.active_dice[0] = False
                e_dice.image.set_alpha(60)
            if now_time - self.active_dice[1] > 1000:
                e_dice.cool_time = False
                e_dice.image.set_alpha(255)

        # thunder - monster damage
        if self.active_thunder[0] or e_thunder.cool_time:
            if now_time - self.active_thunder[1] > 100:
                self.active_thunder[0] = False
                e_thunder.image.set_alpha(60)
            if now_time - self.active_thunder[1] > 600:
                e_thunder.cool_time = False
                e_thunder.image.set_alpha(255)

        # magiccloak - player no damage
        if self.active_magiccloak[0] or e_magiccloak.cool_time:
            
            if now_time - self.active_magiccloak[1] > 3000:
                if self.active_magiccloak[0]:
                    e_magiccloak.target.dp = e_magiccloak.save
                    
                self.active_magiccloak[0] = False
                e_magiccloak.image.set_alpha(60)
                e_magiccloak.target.alpha(255)
                
            if now_time - self.active_magiccloak[1] > 30000:
                e_magiccloak.cool_time = False
                e_magiccloak.image.set_alpha(255)
                
            
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
e_mushroom = E_Mushroom()
e_crescentmoon = E_CrescentMoon()
e_banana = E_Banana()
e_wax = E_Wax()
e_pepper = E_Pepper()
e_heartstone = E_HeartStone()
e_halfstone = E_HalfStone()
e_poisonapple = E_PoisonApple()
e_ice = E_Ice()
e_battery = E_Battery()
e_rollerskate = E_RollerSkate()
e_boxerglove = E_BoxerGlove()
e_helmet = E_Helmet()
e_turtleshell = E_TurtleShell()
e_pizza = E_Pizza()
e_3dglasses = E_3DGlasses()
e_talisman = E_Talisman()
e_ticket = E_Ticket()
e_straw = E_Straw()
e_machine = E_Machine()
e_piggybank = E_PiggyBank()
e_metaldetector = E_MetalDetector()
e_binoculars = E_Binoculars()
e_trafficlight = E_TrafficLight()
e_thunder = E_Thunder()
e_dice = E_Dice()
e_magiccloak = E_MagicCloak()
e_goldenkey = E_GoldenKey()
e_escaperope = E_EscapeRope()       # NONE

e_potion = E_Potion()



skill_con = SkillController()
equip_con = EquipController()

def equip_reset():
    pass