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
            screen.blit(skill_c_image, (self.rect[0]+15, self.rect[1]+15))
        elif self.is_active_v:
            screen.blit(skill_v_image, (self.rect[0]+15, self.rect[1]+15))

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
        self.msg_name = "1UP"
        self.msg_info = "어디서 본 듯한 버섯입니다..."
        self.msg_eff = "목숨이 0 되면 life +1"
        self.grade = 2

        # self.max_row = 4
        # self.max_col = 2

        self.price = 15

#                                                                           #### crescentmoon
class E_CrescentMoon(Equip):
    def __init__(self):
        image = crescentmoon_image
        Equip.__init__(self, image)
        self.msg_name = "초승달"
        self.msg_info = "달에게 소원을 빌어보자 !"
        self.msg_eff = "낮은 확률로 즉시 부활"

        self.revival = False

        self.max_row = 4
        self.max_col = 1

        self.price = 7

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
        self.msg_info = "맛있으면 바나나, 바나나는 길어"
        self.msg_eff = "사용 : HP +25"
        self.active = True

        self.max_row = 4
        self.max_col = 1

        self.price = 5

    def active_skill(self):
        if self in equip_con.equipped_group:
            self.target.hp = min(self.target.hp+25, self.target.max_hp)
            equip_con.equipped_group.remove(self)
            equip_con.normal_equips.append(self)

#                                                                           #### banana
class E_Mandoo(Equip):
    def __init__(self):
        image = mandoo_image
        Equip.__init__(self, image)
        self.msg_name = "만두"
        self.msg_info = "일단 한번 잡솨봐"
        self.msg_eff = "사용 : HP +10"
        self.active = True

        # self.max_row = 5
        # self.max_col = 2

        self.price = 0

    def active_skill(self):
        if self in equip_con.equipped_group:
            self.target.hp = min(self.target.hp+10, self.target.max_hp)
            equip_con.equipped_group.remove(self)
            equip_con.normal_equips.append(self)

#                                                                           #### wax
class E_Wax(Equip):
    def __init__(self):
        image = wax_image
        Equip.__init__(self, image)
        self.msg_name = "헤어 왁스"
        self.msg_info = "던전에서도 멋을 챙기자 !"
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
        self.msg_info = "맵지만 작지 않습니다."
        self.msg_eff = "공격력 +4"

        # self.max_row = 5
        self.max_col = 1

        self.price = 5

#                                                                           #### heartstone
class E_HeartStone(Equip):
    def __init__(self):
        image = heartstone_image
        Equip.__init__(self, image)
        self.msg_name = "마음의 돌"
        self.msg_info = "하트스톤"
        self.msg_eff = "최대 체력 +50"
        self.grade = 2

        self.max_row = 4
        self.max_col = 1

        self.price = 13

#                                                                           #### halfstone 
class E_HalfStone(Equip):
    def __init__(self):
        image = halfstone_image
        Equip.__init__(self, image)
        self.msg_name = "미움의 돌"
        self.msg_info = "하프스톤"
        self.msg_eff = "최대 체력 +20"

        self.max_row = 4
        # self.max_col = 2

        self.price = 6

#                                                                           #### poison apple 
class E_PoisonApple(Equip):
    def __init__(self):
        image = poisonapple_image
        Equip.__init__(self, image)
        self.msg_name = "독사과"
        self.msg_info = "마녀의 애장품"
        self.msg_eff = "체력 +10, 최대 체력 +10"
        self.msg_eff_2 = "시간 데미지와 충돌 데미지 증가"

        # self.max_row = 5
        # self.max_col = 2

        self.price = 0

#                                                                           #### ice
class E_Ice(Equip):
    def __init__(self):
        image = ice_images[0]
        Equip.__init__(self, image)
        self.msg_name = "얼음"
        self.msg_info = "배탈 조심"
        self.msg_eff = "이동속도 +0.1"
        self.msg_eff_2 = "녹으면서 점점 감소"

        self.floor = 0
        self.charge_times = 0

        # self.max_row = 5
        # self.max_col = 2

        self.price = 4

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
        self.msg_eff_2 = "최대 3번 충전"
        self.grade = 1

        self.floor = 0
        self.charge_times = 0

        self.max_row = 4
        # self.max_col = 2

        self.price = 8

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
        self.msg_name = "인라인 스케이트"
        self.msg_info = "거꾸로 해도 인라인"
        self.msg_eff = "이동속도 + 0.1"

        self.max_row = 4
        self.max_col = 1

        self.price = 5

#                                                                           #### boxer glove
class E_BoxerGlove(Equip):
    def __init__(self):
        image = gloves_image
        Equip.__init__(self, image)
        self.msg_name = "복싱 글러브"
        self.msg_info = "무려 18온스입니다."
        self.msg_eff = "펀치 크기 증가"
        self.grade = 2
        
        self.max_row = 3
        self.max_col = 1

        self.price = 18

#                                                                           #### helmet
class E_Helmet(Equip):
    def __init__(self):
        image = helmet_image
        Equip.__init__(self, image)
        self.msg_name = "하이바"
        self.msg_info = "모자랄게 없는 헬멧입니다."
        self.msg_eff = "방어력 +0.3"

        self.max_row = 4
        self.max_col = 1

        self.price = 8

#                                                                           #### turtle shell
class E_TurtleShell(Equip):
    def __init__(self):
        image = turtleshell_image
        Equip.__init__(self, image)
        self.msg_name = "거북이 등껍질"
        self.msg_info = "생각한 것처럼 던질수는 없습니다."
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
        self.msg_info = "나는 3D로 본다."
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
        self.msg_info = "강시 이마에 붙여주세요."
        self.msg_eff = "적 대시 금지"
        self.grade = 1

        self.max_row = 4
        # self.max_col = 2

        self.price = 6

#                                                                           #### ticket
class E_Ticket(Equip):
    def __init__(self):
        image = ticket_image
        Equip.__init__(self, image)
        self.msg_name = "황금 티켓"
        self.msg_info = "상점 VIP 고객"
        self.msg_eff = "상점 레어도 증가"
        self.grade = 1

        # self.max_row = 5
        self.max_col = 0

        self.price = 7

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

        self.price = 6

#                                                                           #### machine
class E_Machine(Equip):
    def __init__(self):
        image = machine_image
        Equip.__init__(self, image)
        self.msg_name = "ESP-8266"
        self.msg_info = "포션 자동화 기술의 부산물"
        self.msg_eff = "포션 드롭률 +5%"

        # self.max_row = 5
        self.max_col = 1

        self.price = 5

#                                                                           #### piggy bank
class E_PiggyBank(Equip):
    def __init__(self):
        image = piggybank_image
        Equip.__init__(self, image)
        self.msg_name = "돼지 저금통"
        self.msg_info = "티끌 모아 태산"
        self.msg_eff = "레드 코인 등장"
        self.grade = 1

        # self.max_row = 5
        self.max_col = 1

        self.price = 9

#                                                                           #### metal detector
class E_MetalDetector(Equip):
    def __init__(self):
        image = metaldetector_image
        Equip.__init__(self, image)
        self.msg_name = "금속 탐지기"
        self.msg_info = "삐비비비비비빅"
        self.msg_eff = "코인 드롭률 +5%"

        self.max_row = 4
        # self.max_col = 2

        self.price = 5

#                                                                           #### binoculars 
class E_Binoculars(Equip):
    def __init__(self):
        image = binoculars_image
        Equip.__init__(self, image)
        self.msg_name = "쌍안경"
        self.msg_info = "보일락 말락"
        self.msg_eff = "아이템 드롭률 +3%"
        self.grade = 1

        # self.max_row = 5
        self.max_col = 0

        self.price = 7

#                                                                           #### traffic light
class E_TrafficLight(Equip):
    def __init__(self):
        image = trafficlight_image
        Equip.__init__(self, image)
        self.msg_name = "신호등"
        self.msg_info = "붉은색 푸른색 그 사이 3초 그 짧은 시간"
        self.msg_eff = "스킬 : 3초간 모두 정지"
        self.grade = 1
        self.active = True

        self.max_row = 3
        # self.max_col = 2

        self.price = 10

    def active_skill(self):
        if self.cool_time == False and self in equip_con.equipped_group:
            skill_con.active_trafficlight[0] = True
            skill_con.active_trafficlight[1] = pygame.time.get_ticks()
            self.cool_time = True

#                                                                           #### thunder
class E_Thunder(Equip):
    def __init__(self):
        image = thunder_image
        Equip.__init__(self, image)
        self.msg_name = "벼락"
        self.msg_info = "마른 하늘에 날벼락"
        self.msg_eff = "스킬 : 전체 적에게 10 데미지"
        self.grade = 1
        self.active = True

        self.max_row = 3
        self.max_col = 1

        self.price = 10

    def active_skill(self):
        if self.cool_time == False and self in equip_con.equipped_group:
            skill_con.active_thunder[0] = True
            skill_con.active_thunder[1] = pygame.time.get_ticks()
            self.cool_time = True
            
            for monster in self.target:
                monster.hp -= 10

#                                                                           #### dice
class E_Dice(Equip):
    def __init__(self):
        image = dice_image
        Equip.__init__(self, image)
        self.msg_name = "사기 주사위"
        self.msg_info = "♚♚주☆사☆위♚♚굴릴시$$HP☜☜100%증정※"
        self.msg_eff = "스킬 : 50퍼센트 확률로"
        self.msg_eff_2 = "HP +10 또는 -10"
        self.grade = 1
        self.active = True

        self.max_row = 4
        self.max_col = 1

        self.price = 5

    def active_skill(self):
        if self.cool_time == False and self in equip_con.equipped_group:
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
        self.msg_name = "투명 망토"
        self.msg_info = "마법사의 비밀 컬렉션 2호"
        self.msg_eff = "스킬 : 1초간 무적"
        self.grade = 2
        self.active = True

        self.save = [0, 0]

        self.max_row = 4
        self.max_col = 1

        self.price = 10

    def active_skill(self):
        if self.cool_time == False and self in equip_con.equipped_group:
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
        self.msg_info = "어디로든 키"
        self.msg_eff = "사용 : 다음층으로 가는"
        self.msg_eff_2 = "계단 열기"
        self.grade = 1
        self.active = True

        self.max_row = 3
        # self.max_col = 2

        self.price = 5

    def active_skill(self):
        if not self.target % 20 == 0 and self in equip_con.equipped_group:
            field_group.add(key_field)   #keys field
            equip_con.equipped_group.remove(self)
            equip_con.rare_equips.append(self)

#                                                                           #### rope
class E_EscapeRope(Equip):
    def __init__(self):
        image = rope_image
        Equip.__init__(self, image)
        self.msg_name = "오누이의 동앗줄"
        self.msg_info = "떡 하나 주면 안잡아먹지 !"
        self.msg_eff = "사용 : 0층으로"
        self.grade = 2
        self.active = True

        self.max_row = 4
        self.max_col = 0

        self.price = 10

    def active_skill(self):
        if self in equip_con.equipped_group:
            field_group.add(portal)
            skill_con.active_escaperope = True
            equip_con.equipped_group.remove(self)
            equip_con.unique_equips.append(self)

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

class E_Coins(Equip):
    def __init__(self):
        image = coins_image
        Equip.__init__(self, image)
        self.msg_name = "돈 뭉치"
        self.msg_info = "이것만 있으면 나도 부자"
        self.msg_eff = "COIN + 15"

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
            e_crescentmoon, e_banana, e_mandoo, e_wax, e_pepper, e_halfstone, e_poisonapple, e_ice, e_rollerskate, e_helmet, e_turtleshell,
            e_pizza, e_3dglasses, e_machine, e_metaldetector,
        ]

        self.perc_rare = 10
        self.rare_equips = [
            e_battery, e_talisman, e_ticket, e_straw, e_piggybank, e_binoculars,
            e_trafficlight, e_thunder, e_dice, e_goldenkey,
        ]

        self.perc_unique = 2
        self.unique_equips = [
            e_mushroom, e_heartstone, e_boxerglove, e_magiccloak, #e_escaperope,
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
            if now_time - self.active_trafficlight[1] > 100000:
                e_trafficlight.cool_time = False
                e_trafficlight.image.set_alpha(255)

        # dice - random effect
        if self.active_dice[0] or e_dice.cool_time:
            if now_time - self.active_dice[1] > 100:
                self.active_dice[0] = False
                e_dice.image.set_alpha(60)
            if now_time - self.active_dice[1] > 5000:
                e_dice.cool_time = False
                e_dice.image.set_alpha(255)

        # thunder - monster damage
        if self.active_thunder[0] or e_thunder.cool_time:
            if now_time - self.active_thunder[1] > 100:
                self.active_thunder[0] = False
                e_thunder.image.set_alpha(60)
            if now_time - self.active_thunder[1] > 50000:
                e_thunder.cool_time = False
                e_thunder.image.set_alpha(255)

        # magiccloak - player no damage
        if self.active_magiccloak[0] or e_magiccloak.cool_time:
            
            if now_time - self.active_magiccloak[1] > 1000:
                if self.active_magiccloak[0]:
                    e_magiccloak.target.dp = e_magiccloak.save
                    
                self.active_magiccloak[0] = False
                e_magiccloak.image.set_alpha(60)
                e_magiccloak.target.alpha(255)
                
            if now_time - self.active_magiccloak[1] > 10000:
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
e_mandoo = E_Mandoo()
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
e_coins = E_Coins()



skill_con = SkillController()
equip_con = EquipController()

def equip_reset():
    pass