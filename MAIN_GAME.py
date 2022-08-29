import pygame
import random

from class_equip import *
from class_character import *
from class_item import *
from class_field import *

from file_sound import *

from project_floor import *
##############################################################################################
def scene_title_game():
    global running, ready
        
    # msg_start = game_font.render("START", True, BLACK)
    # start_rect = msg_start.get_rect(center=(screen_width//2,500))
    # start_cursor = ((start_rect.left - 30, start_rect.top),(start_rect.left - 30,start_rect.bottom),(start_rect.left - 10,500))
    start_cursor = ((578,490), (578,510), (598,500))

    # msg_exit = game_font.render("EXIT", True, BLACK)
    # exit_rect = msg_exit.get_rect(center=(screen_width//2,550))
    # exit_cursor = ((exit_rect.left - 30, exit_rect.top),(exit_rect.left - 30,exit_rect.bottom),(exit_rect.left - 10,550))
    exit_cursor = ((587,540), (587,560), (607,550))

    cursor = start_cursor

    while ready:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ready = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cursor = start_cursor
                if event.key == pygame.K_DOWN:
                    cursor = exit_cursor
                if event.key == pygame.K_SPACE:
                    if cursor == start_cursor:
                        ready = False
                    elif cursor == exit_cursor:
                        ready = False
                        running = False

        bgm_sound.play(-1)

        screen.fill((125,125,125))
        pygame.draw.polygon(screen, GREEN, cursor)
        screen_message("SLIME PUNCH", GREEN, (screen_width//2,200), game_font_b)
        screen_message("START", BLACK, (screen_width//2,500), game_font_m)
        screen_message("EXIT", BLACK, (screen_width//2,550), game_font_m)
        pygame.display.update()

def display_game_ui():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ((340,60), (600, 600)), 1)              #MAIN GAME
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)              #INFO
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1)              #INVEN
    # screen.blit(background_zero, (340,60))
    
    screen_message(f"{floor} F", WHITE, (240,90), game_font_m)                           #FLOOR MESSAGE

    screen_message(f"HP: {int(player.hp)}", WHITE, (240,190), game_font_m)                   #HP MESSAGE

    coin_image_rect = item_images[1].get_rect(center=(215, 290))
    screen.blit(item_images[1], coin_image_rect)
    screen_message(f"       x{player.coin}", WHITE, (220,290), game_font_m)      #COIN MESSAGE

    life_image_rect = player_icon.get_rect(center=(210, 390))
    screen.blit(player_icon, life_image_rect)
    screen_message(f"      x{player.life}", WHITE, (220,390), game_font_m)      #LIFE MESSAGE

    for i in range(MAX_COL+2):                                                      #INVENTORY
        pygame.draw.line(screen, D_GRAY, (950 + 60*i, 180), (950 + 60*i, 540))
    for i in range(MAX_ROW+2):
        pygame.draw.line(screen, D_GRAY, (950, 180 + 60*i), (1130, 180 + 60*i))

    for equip in equip_con.equipped_group:
        equip.draw(screen)

    if is_inven_overlapped(equip_con.equipped_group):
        screen_message("CHECK EQUIPS !", RED, (1040,150), game_font_s)

def scene_tutorial(doing):
    global running

    idx = 0
    fin = len(tuto_images) - 1

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if idx >= fin:
                        doing = False
                    else:
                        idx += 1

        display_game_ui()

        tuto_rect = tuto_images[idx].get_rect(center=(640, 300))
        msg = "NEXT"
        if idx >= fin:
            msg = "PRESS 'SPACE BAR' TO BACK"

        screen.blit(tuto_images[idx], tuto_rect)
        screen_message(msg, WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_skeleton_shop(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    equip_for_sale(0, equip_con.for_sale[0])

                if event.key == pygame.K_2:
                    equip_for_sale(1, equip_con.for_sale[1])

                if event.key == pygame.K_3:
                    equip_for_sale(2, equip_con.for_sale[2])

                if event.key == pygame.K_0:
                    if player.coin >= 4:
                        player.coin -= 4
                        random_for_sale()

                if event.key == pygame.K_SPACE:
                    doing = False
                    if not is_inven_overlapped(equip_con.equipped_group):
                        equip_effect()

        display_game_ui()

        equip_showcase(0, equip_con.for_sale[0])
        equip_showcase(1, equip_con.for_sale[1])
        equip_showcase(2, equip_con.for_sale[2])

        shop_rect = shop_image.get_rect(center=(640, 200))

        screen.blit(shop_image, shop_rect)
        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_player_dead(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    doing = False
                    floor_zero()

        display_game_ui()
        screen_message("YOU DIE", RED, (screen_width//2, screen_height//2), game_font_b)
        screen_message("PRESS 'R' TO GO 1F", WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_game_over(doing):
    global running, ready

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doing = False
                    game_restart()
                    ready = True

        screen.fill(BLACK)
        screen_message("GAME OVER", RED, (screen_width//2, screen_height//2), game_font_b)
        screen_message(f"REACHED AT {floor} FLOOR", WHITE, (screen_width//2, screen_height//2 + 50), game_font_m)
        screen_message("PRESS 'SPACE BAR' TO MAIN", WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_equip_setting(doing):
    global running

    player.stop()
    cursor = Cursor(cursor_image[0], (980,210))
    picked_equip = None

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                running = False
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.clicking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i:
                    doing = False
                    if not is_inven_overlapped(equip_con.equipped_group):
                        equip_effect()

                if event.key == pygame.K_r:
                    remove_from_equipped_group(picked_equip)
                    cursor.clicking = False
                    cursor.image = cursor_image[0]
                    picked_equip = None

                if event.key == pygame.K_SPACE:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_image[0]
                        picked_equip = None

                    else:
                        for equip in equip_con.equipped_group:
                            if pygame.sprite.collide_mask(equip, cursor):
                                cursor.clicking = True
                                cursor.image = cursor_image[1]
                                picked_equip = equip

                if event.key == pygame.K_c:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_image[0]
                        setting_active_skill("c", picked_equip)
                        picked_equip = None
                
                if event.key == pygame.K_v:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_image[0]
                        setting_active_skill("v", picked_equip)
                        picked_equip = None

        display_game_ui()
        cursor.draw(screen)
        pygame.display.update()

def scene_treasure_box(doing):
    global running

    player.stop()
    choice = True
    if len(equip_con.able_equip_group) >= 2:
        choice_equip = [equip_con.able_equip_group[-1], equip_con.able_equip_group[-2]]

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if choice:
                    if event.key == pygame.K_1:
                        equip_con.equipped_group.append(choice_equip[0])
                        equip_con.able_equip_group.remove(choice_equip[0])
                        choice = False

                    if event.key == pygame.K_2:
                        equip_con.equipped_group.append(choice_equip[1])
                        equip_con.able_equip_group.remove(choice_equip[1])
                        choice = False

                if event.key == pygame.K_SPACE and not choice:
                    doing = False
                    if not is_inven_overlapped(equip_con.equipped_group):
                        equip_effect()

        display_game_ui()

        zero_rect = choice_equip[0].image.get_rect(center=(490,450))
        one_rect = choice_equip[1].image.get_rect(center=(790,450))
        
        if choice:
            screen_message("<1>", WHITE, (490, 350), game_font_m)
            screen.blit(choice_equip[0].image, zero_rect)
            screen_message(choice_equip[0].name, WHITE, (490,550), game_font_m)

            screen_message("OR", WHITE, (640,450), game_font_m)

            screen_message("<2>", WHITE, (790, 350), game_font_m)
            screen.blit(choice_equip[1].image, one_rect)
            screen_message(choice_equip[1].name, WHITE, (790,550), game_font_m)

            screen_message("CHOICE ONE EQUIP !", WHITE, (640,640), game_font_m)
        else:
            screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)

        shop_rect = shop_image.get_rect(center=(640, 200))
        screen.blit(shop_image, shop_rect)
        
        pygame.display.update()
##############################################################################################
def screen_message(writing, color, position, font):
    msg = font.render(writing, True, color)
    msg_rect = msg.get_rect(center=position)
    screen.blit(msg, msg_rect)

def game_restart():
    global player, saved_floor
    global item_con, equip_con, skill_con

    player = Player(player_image, player_first_position)
    make_floor_zero()
    saved_floor = None
    item_con = ItemController()
    equip_con = EquipController()
    skill_con = SkillController()

def make_floor_zero():
    global floor

    floor = 0
    monster_group.empty()
    shooting_group.empty()
    item_group.empty()
    field_group.empty()
    npc_group.add(father_slime, skeleton, ghost)
    stair.image = stair_images[0]
    stair.rect = stair.image.get_rect(center=stair_zero_floor)
    random_for_sale()
    player.rect = player.image.get_rect(center=player_first_position)
    player.hp = player.max_hp

def floor_zero():
    if floor != 0:
        make_floor_zero()

    npc_group.draw(screen)

    for punch in punch_group:
        if pygame.sprite.collide_mask(punch, father_slime):
            player.stop()
            scene_tutorial(True)

        if pygame.sprite.collide_mask(punch, skeleton):
            player.stop()
            scene_skeleton_shop(True)

def next_floor(pos):
    global floor

    floor += 1
    if floor % 10 == 0:
        player.hp += 10

    item_group.empty()

    if npc_group:
        npc_group.empty()
        stair.image = stair_images[1]

    floor_setting(pos, floor)
    
def equip_for_sale(index, equip):
    if equip_con.can_buy[index] and player.coin >= equip.price:
        equip_con.equipped_group.append(equip)
        player.coin -= equip.price
        equip_con.can_buy[index] = False
        equip_con.able_equip_group.remove(equip)

def random_for_sale():
    random.shuffle(equip_con.able_equip_group)

    total_number = min(len(equip_con.able_equip_group), len(equip_con.for_sale))

    for i in range(total_number):
        equip_con.for_sale[i] = equip_con.able_equip_group[i]
        equip_con.can_buy[i] = True

def equip_showcase(index, equip):
    sero = 350
    pygame.draw.rect(screen, WHITE, ((420 + 150*index,sero),(140,260)), 2)
    screen_message(str(index+1), WHITE, (490 + 150*index,sero+20), game_font_m)

    if equip_con.can_buy[index]:
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+40), (550 + 150*index, sero+40))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+100), (550 + 150*index, sero+100))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+160), (550 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+40), (430 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (490 + 150*index, sero+40), (490 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (550 + 150*index, sero+40), (550 + 150*index, sero+160))
        # equip_image = pygame.transform.rotozoom(equip.image, 0, 30/60)
        equip_rect = equip.image.get_rect(left=430 + 150*index, top=sero+40)
        screen.blit(equip.image, equip_rect)

        screen_message(equip.name, WHITE, (490 + 150*index, sero+185), game_font_s)

        coin_image = pygame.transform.rotozoom(item_images[1], 0, 0.5)
        coin_rect = coin_image.get_rect(center=(470 + 150*index,sero+230))
        screen.blit(coin_image, coin_rect)

        screen_message(f"x{equip.price}", WHITE, (500 + 150*index, sero+230), game_font_m)
    else:
        case_rect = sold_out_image.get_rect(center=(490 + 150*index,sero+130))
        screen.blit(sold_out_image, case_rect)

def player_move_key():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.to[0] -= player.speed
            player.direction = "LEFT"
        if event.key == pygame.K_RIGHT:
            player.to[1] += player.speed
            player.direction = "RIGHT"
        if event.key == pygame.K_UP:
            player.to[2] -= player.speed
            player.direction = "UP"
        if event.key == pygame.K_DOWN:
            player.to[3] += player.speed
            player.direction = "DOWN"
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            player.to[0] = 0
        if event.key == pygame.K_RIGHT:
            player.to[1] = 0
        if event.key == pygame.K_UP:
            player.to[2] = 0
        if event.key == pygame.K_DOWN:
            player.to[3] = 0

def random_monster_move():
    if monster_group:
        for monster in monster_group:
            if monster.direction == "LEFT":
                monster.move(-0.1, 0, fps)
            elif monster.direction == "RIGHT":
                monster.move(0.1, 0, fps)
            elif monster.direction == "UP":
                monster.move(0,-0.1, fps)
            elif monster.direction == "DOWN":
                monster.move(0,0.1, fps)

def drop_item(monster):
    randprob = random.randrange(0,101)
    # position = put_on_pixel(position)

    if monster.type == "boss":
        item_group.add(Item(box_image, monster.position, "box"))
    else:
        if randprob <= item_con.prob_portion:
            item_group.add(Item(item_images[0], monster.position, "portion"))
        elif item_con.prob_portion < randprob <= item_con.prob_portion + item_con.prob_coin:
            item_group.add(Item(item_images[1], monster.position, "coin"))

def put_on_pixel(position):
    x = position[0]
    y = position[1]

    x_ahrt = x // 60
    x_skajwl = round((x % 60) / 60)

    y_ahrt = y // 60
    y_skajwl = round((y % 60) / 60)

    fin_x = (x_ahrt + x_skajwl) * 60 + 10
    fin_y = (y_ahrt + y_skajwl) * 60 + 30

    pixel_position = (fin_x,fin_y)
    print(pixel_position)

    return pixel_position

def item_effect(item):
    if item.info == "portion":
        player.hp = min(player.hp + item_con.portion_eff, player.max_hp)
    if item.info == "coin":
        player.coin += 1
    if item.info == "box":
        scene_treasure_box(True)

def equip_effect():
    if equip_battery in equip_con.equipped_group:
        if not equip_battery.is_effected:
            player.damaged_enemy -= 0.2
            equip_battery.is_effected = True

    if equip_banana in equip_con.equipped_group:
        if not equip_banana.is_effected:
            player.max_hp += 20
            player.hp += 20
            equip_banana.is_effected = True

    if equip_pepper in equip_con.equipped_group:
        if not equip_pepper.is_effected:
            player.ap += 3            
            equip_pepper.is_effected = True

    if equip_ice in equip_con.equipped_group:
        if not equip_ice.is_effected:
            player.speed += 0.1
            equip_ice.is_effected = True

    if equip_dice in equip_con.equipped_group:
        if not equip_dice.is_effected:
            item_con.prob_coin += 5
            equip_dice.is_effected = True

    if equip_apple in equip_con.equipped_group:
        if not equip_apple.is_effected:
            big_punch_image = pygame.transform.scale(punch_d_image, (90,90))
            player.punch = big_punch_image
            equip_apple.is_effected = True

    if equip_greentea in equip_con.equipped_group:
        if not equip_greentea.is_effected:
            item_con.portion_eff += 5
            equip_greentea.is_effected = True

    if equip_mandoo in equip_con.equipped_group:
        if not equip_mandoo.is_effected:
            player.life += 1
            equip_mandoo.is_effected = True

    if equip_ancientbook in equip_con.equipped_group:
        if not equip_ancientbook.is_effected:
            player.damaged_time -= 0.5
            equip_ancientbook.is_effected = True

    if equip_bone in equip_con.equipped_group:
        if not equip_bone.is_effected:
            player.ap += 0.1
            equip_bone.is_effected = True
            
def remove_from_equipped_group(equip):
    if equip == None:
        return
    else:
        if equip == equip_battery:
            player.damaged_enemy += 0.2

        if equip == equip_banana:
            player.max_hp -= 20
            player.hp = min(player.max_hp, player.hp)

        if equip == equip_pepper:
            player.ap -= 3

        if equip == equip_ice:
            player.speed -= 0.1

        if equip == equip_dice:
            item_con.prob_coin -= 5

        if equip == equip_apple:
            player.punch = punch_d_image

        if equip == equip_greentea:
            item_con.portion_eff -= 5

        # not effect mandoo

        if equip == equip_ancientbook:
            player.damaged_time += 0.5

        if equip == equip_bone:
            player.ap += 0.1

    equip_con.equipped_group.remove(equip)
    equip_con.able_equip_group.append(equip)

def setting_active_skill(key, picked_equip):
    if key == "c":
        for equip in equip_con.equipped_group:
            equip.is_active_c = False
        picked_equip.is_active_c = True
        picked_equip.is_active_v = False
        player.equip_c = picked_equip
        if player.equip_v == player.equip_c:
            player.equip_v = None

    if key == "v":
        for equip in equip_con.equipped_group:
            equip.is_active_v = False
        picked_equip.is_active_c = False
        picked_equip.is_active_v = True
        player.equip_v = picked_equip
        if player.equip_c == player.equip_v:
            player.equip_c = None

def random_monster_shooting():
    randprob = random.randrange(0,101)

    for monster in monster_group:
        if monster.type == "boss":
            if 0 <= randprob <= 70:
                shooting_group.add(Punch(cursor_image[0], monster.position, monster.direction))
##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image_group, position):
        Character.__init__(self, image_group, position)

        self.life = 3
        self.hp = 100
        self.coin = 99

        self.equip_c = None
        self.equip_v = None

        self.ap = 10
        self.max_hp = 100
        self.speed = 0.5
        self.punch = punch_d_image
        self.damaged_enemy = 0.7
        self.damaged_time = 1

    def space_bar(self):
        punch_sound.play()
        image = self.punch

        if self.direction == "LEFT":
            position = (self.rect.centerx-40, self.rect.centery)
        elif self.direction == "RIGHT":
            image = pygame.transform.rotozoom(image, 180, 1)
            position = (self.rect.centerx+40, self.rect.centery)
        elif self.direction == "UP":
            image = pygame.transform.rotozoom(image, 270, 1)
            position = (self.rect.centerx, self.rect.centery-40)
        elif self.direction == "DOWN":
            image = pygame.transform.rotozoom(image, 90, 1)
            position = (self.rect.centerx, self.rect.centery+40)

        punch_group.add(Punch(image, position, self.direction))
    
    def skill_c(self):
        # if self.equip_c == equip_zxcv:
        #     shooting_group.add(Punch(skill_c_image, self.position, self.direction))
        if self.equip_c:
            self.equip_c.active_skill()
    
    def skill_v(self):
        if self.equip_v:
            self.equip_v.active_skill()

#### PUNCH CLASS
class Punch(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = image
        self.position = position
        self.direction = direction
        
        self.rect = image.get_rect(center=position)
        self.time = pygame.time.get_ticks()

    def get_time(self):
        return pygame.time.get_ticks() - self.time

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        if self.direction == "LEFT":
            self.rect.x -= 10
        elif self.direction == "RIGHT":
            self.rect.x += 10
        elif self.direction == "UP":
            self.rect.y -= 10
        elif self.direction == "DOWN" or "NONE":
            self.rect.y += 10

        if self.rect.left < 340 or 940 < self.rect.right or self.rect.top < 60 or 660 < self.rect.bottom:
            shooting_group.remove(self)
##############################################################################################
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("No More Slime")
clock = pygame.time.Clock()
game_font_s = pygame.font.Font("fonts\\DungGeunMo.ttf", 20)
game_font_m = pygame.font.Font("fonts\\DungGeunMo.ttf", 30)
game_font_b = pygame.font.Font("fonts\\DungGeunMo.ttf", 50)
start_ticks = pygame.time.get_ticks()
a_counter = 0
b_counter = 0

#### GAME SYSTEM
WHITE = (255,255,255)
D_GRAY = (64,64,64)
GRAY = (127,127,127)
BLACK = (0,0,0)
RED = (127,0,0)
GREEN = (0,127,0)
BLUE = (0,0,127)
floor = 0
saved_floor = None

##### PLAYER
player_first_position = (700, 360)
player = Player(player_image, player_first_position)

punch_group = pygame.sprite.Group()
shooting_group = pygame.sprite.Group()

##############################################################################################
ready = True
running = True
random_for_sale()
while running:
    fps = clock.tick(60)

    scene_title_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.space_bar()
            if event.key == pygame.K_c:
                player.skill_c()
            if event.key == pygame.K_v:
                player.skill_v()
            if event.key == pygame.K_i:
                scene_equip_setting(True)

        if not is_inven_overlapped(equip_con.equipped_group):
            player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3], fps)
    
    display_game_ui()                                                                  #UI
    screen.blit(background_zero, (340,60))                                             #BACKGROUND
    field_group.draw(screen)                                                           #FIELD

    milli_time = int((pygame.time.get_ticks() - start_ticks) / 400)
    if a_counter != milli_time:
        #for 0.4 second
        player.image_update()
        ghost.image_update()
    a_counter = milli_time

    if floor == 0:
        bgm_sound.stop()
        floor_zero()      

    elif floor > 0:
        second_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if b_counter != second_time:
            #for 1 second
            player.hp -= player.damaged_time
            random_monster_direction()
            random_monster_shooting()
        b_counter = second_time

        if not skill_con.active_sandclock[0]:
            random_monster_move()

        if player.hp <= 0:
            player.hp = 0
            player.life -= 1
            player.stop()
            pygame.time.delay(1500)
            saved_floor = floor
            if player.life <= 0:
                scene_game_over(True)
            else:
                scene_player_dead(True)

    if not monster_group:
        stair.draw(screen)                                                              #STAIR

        if pygame.sprite.collide_mask(player, stair):
            if saved_floor and floor == 0:
                floor = saved_floor - 1
            next_floor(player.position)

    for monster in monster_group:
        monster.draw(screen)                                                           #MONSTER
        if pygame.sprite.collide_mask(player, monster):
            player.hp -= player.damaged_enemy
            player.image = player_damaged_image

    for punch in punch_group:
        punch.draw(screen)                                                              #PUNCH

        if punch.get_time() > 2 * fps:
            punch_group.remove(punch)

        for monster in monster_group:
            if pygame.sprite.collide_mask(monster, punch):
                punch_group.remove(punch)
                monster.hp -= player.ap
                if monster.hp <= 0:
                    monster_group.remove(monster)
                    drop_item(monster)
                    if len(monster_group) == 0:
                        random_away_position(player.position, stair)

    for shoot in shooting_group:
        shoot.shoot()
        shoot.draw(screen)
        if pygame.sprite.collide_mask(shoot, player):
            player.hp -= 10
            shooting_group.remove(shoot)

    for item in item_group:
        item.draw(screen)                                                               #ITEM
        if pygame.sprite.collide_mask(item, player):
            if item.info == "box":
                if len(monster_group):
                    continue
            item_effect(item)
            item_group.remove(item)

    player.draw(screen)                                                                 #PLAYER
    skill_con.active_time()

    if running: 
        pygame.display.update()

pygame.quit()