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
                pygame.quit()
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
                        pygame.quit()

        screen.fill((125,125,125))
        bgm_sound.play(-1)
        pygame.draw.polygon(screen, GREEN, cursor)
        screen_message("SLIME PUNCH", GREEN, (screen_width//2,200))
        screen_message("START", BLACK, (screen_width//2,500))
        screen_message("EXIT", BLACK, (screen_width//2,550))

        pygame.display.update()

def display_game_ui():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ((340,60), (600, 600)), 1)              #MAIN GAME
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)              #INFO
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1)              #INVEN
    screen.blit(background_zero, (340,60))
              
    screen_message(f"{floor} F", WHITE, (240,90))                           #FLOOR MESSAGE

    screen_message(f"HP: {int(player.hp)}", WHITE, (240,190))                   #HP MESSAGE

    coin_image_rect = item_images[1].get_rect(center=(215, 290))
    screen.blit(item_images[1], coin_image_rect)
    screen_message(f"       x{player.coin}", WHITE, (220,290))      #COIN MESSAGE

    life_image_rect = player_icon.get_rect(center=(210, 390))
    screen.blit(player_icon, life_image_rect)
    screen_message(f"      x{player.life}", WHITE, (220,390))      #LIFE MESSAGE

    for i in range(MAX_COL+2):                                                      #INVENTORY
        pygame.draw.line(screen, GRAY, (950 + 60*i, 180), (950 + 60*i, 540))
    for i in range(MAX_ROW+2):
        pygame.draw.line(screen, GRAY, (950, 180 + 60*i), (1130, 180 + 60*i))

    for equip in equip_con.equipped_group:
        equip.draw(screen)

    if is_inven_overlapped(equip_con.equipped_group):
        screen_message("CHECK EQUIPS !", RED, (1040,150))

def scene_tutorial(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doing = False

        display_game_ui()

        screen.blit(tuto_image, tuto_rect)
        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640))

        pygame.display.update()

def scene_skeleton_shop(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    equip_for_sale(0, equip_con.for_sale[0])

                if event.key == pygame.K_2:
                    equip_for_sale(1, equip_con.for_sale[1])

                if event.key == pygame.K_3:
                    equip_for_sale(2, equip_con.for_sale[2])

                if event.key == pygame.K_SPACE:
                    doing = False
                    if not is_inven_overlapped(equip_con.equipped_group):
                        equip_effect()

        display_game_ui()

        equip_showcase(0, equip_con.for_sale[0])
        equip_showcase(1, equip_con.for_sale[1])
        equip_showcase(2, equip_con.for_sale[2])

        screen.blit(shop_image, shop_rect)
        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640))
        pygame.display.update()

def scene_player_dead(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    doing = False
                    floor_zero()

        display_game_ui()
        screen_message("YOU DIE", RED, (screen_width//2, screen_height//2))
        screen_message("PRESS 'R' TO GO 1F", WHITE, (640,640))
        pygame.display.update()

def scene_game_over(doing):
    global running, ready, floor

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doing = False
                    game_restart()
                    ready = True

        screen.fill(BLACK)
        screen_message("GAME OVER", RED, (screen_width//2, screen_height//2))
        screen_message(f"RECORD : {floor}", WHITE, (screen_width//2, screen_height//2 + 50))
        screen_message("PRESS 'SPACE BAR' TO MAIN", WHITE, (640,640))
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
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.clicking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i:
                    doing = False
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

##############################################################################################
def screen_message(writing, color, position):
    msg = game_font.render(writing, True, color)
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
    item_group.empty()
    npc_group.add(father_slime, skeleton)
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

    if len(equip_con.able_equip_group) == 0:
        equip_con.for_sale = [None, None, None]
        equip_con.can_buy = [False, False, False] 

    elif len(equip_con.able_equip_group) == 1:
        equip_con.for_sale = [equip_con.able_equip_group[0], None, None]
        equip_con.can_buy = [True, False, False]

    elif len(equip_con.able_equip_group) == 2:
        equip_con.for_sale = [equip_con.able_equip_group[0], equip_con.able_equip_group[1], None]
        equip_con.can_buy = [True, True, False]

    else:
        equip_con.for_sale = [equip_con.able_equip_group[0], equip_con.able_equip_group[1], equip_con.able_equip_group[2]]
        equip_con.can_buy = [True, True, True]

def equip_showcase(index, equip):
    pygame.draw.rect(screen, WHITE, ((450 + 150*index,350),(80,120)), 1)

    if equip_con.can_buy[index]:
        equip_image = pygame.transform.scale(equip.image, (60,60))
        equip_rect = equip_image.get_rect(center=(490+ 150*index, 390))
        screen.blit(equip_image, equip_rect)

        coin_image = pygame.transform.rotozoom(item_images[1], 0, 0.5)
        coin_rect = coin_image.get_rect(center=(470+ 150*index,440))
        screen.blit(coin_image, coin_rect)

        screen_message(f"x{equip.price}", WHITE, (500+ 150*index, 440))
    else:
        case_rect = sold_out_image.get_rect(center=(490+ 150*index,410))
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

def drop_item(position):
    randprob = random.randrange(0,101)

    if randprob <= item_con.prob_portion:
        item_group.add(Item(item_images[0], position, "portion"))
    elif item_con.prob_portion < randprob <= item_con.prob_portion + item_con.prob_coin:
        item_group.add(Item(item_images[1], position, "coin"))

def item_effect(item):
    if item.info == "portion":
        player.hp = min(player.hp + 5, player.max_hp)
    if item.info == "coin":
        player.coin += 1

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
        image = self.punch
        punch_sound.play()

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
        # if player.direction == "LEFT":
        #     self.rect = (player.rect.x-60, player.rect.y)
        # elif player.direction == "RIGHT":
        #     self.rect = (player.rect.x+60, player.rect.y)
        # elif player.direction == "UP":
        #     self.rect = (player.rect.x, player.rect.y-60)
        # elif player.direction == "DOWN":
        #     self.rect = (player.rect.x, player.rect.y+60)

        screen.blit(self.image, self.rect)
##############################################################################################
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("No More Slime")
clock = pygame.time.Clock()
game_font = pygame.font.Font("fonts\\DungGeunMo.ttf", 30)
start_ticks = pygame.time.get_ticks()
a_counter = 0
b_counter = 0

#### GAME SYSTEM
WHITE = (255,255,255)
GRAY = (64,64,64)
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

##### INVENTORY
random_for_sale()

##### ETC
tuto_rect = tuto_image.get_rect(center=(640, 300))
shop_rect = shop_image.get_rect(center=(640, 200))

##############################################################################################
ready = True
running = True
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

    milli_time = int((pygame.time.get_ticks() - start_ticks) / 400)
    if a_counter != milli_time:
        #for 0.4 second
        player.image_update()
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
        b_counter = second_time

        if not skill_con.active_sandclock[0]:
            random_monster_move()

        if player.hp <= 0:
            player.hp = 0
            player.life -= 1
            player.stop()
            saved_floor = floor
            if player.life <= 0:
                scene_game_over(True)
            else:
                scene_player_dead(True)

    if not monster_group:
        stair.draw(screen)                                                            #STAIR

        if pygame.sprite.collide_mask(player, stair):
            if saved_floor and floor == 0:
                floor = saved_floor - 1
            next_floor(player.position) 

    for monster in monster_group:
        if not monster.is_died:        
            monster.draw(screen)                                                      #MONSTER
            if pygame.sprite.collide_mask(player, monster):
                player.hp -= player.damaged_enemy

        # for punch in punch_group:
        #     if pygame.sprite.collide_mask(monster, punch):
        #         # punch.draw(screen)
        #         punch_group.remove(punch)
        #         monster.hp -= player.ap
        #         if monster.hp <= 0:
        #             monster.die(drop_item, monster_group)
        #             random_away_position(player.position, stair)

    for punch in punch_group:
        punch.draw(screen)                                                              #PUNCH

        if punch.get_time() > 2 * fps:
            punch_group.remove(punch)

        for monster in monster_group:
            if pygame.sprite.collide_mask(monster, punch):
                punch_group.remove(punch)
                monster.hp -= player.ap
                if monster.hp <= 0:
                    monster.die(drop_item, monster_group)
                    random_away_position(player.position, stair)

    for item in item_group:
        item.draw(screen)                                                               #ITEM
        if pygame.sprite.collide_mask(item, player):
            item_effect(item)
            item_group.remove(item)

    # for field in field_group:
    #     field.draw(screen)
    #     if pygame.sprite.collide_mask(field, player):
    #         field_effect(field)
    #     if field.is_collision and not pygame.sprite.collide_mask(field, player):
    #         field_uneffect(field)

    player.draw(screen)                                                                 #PLAYER
    # check_player_collision()
    skill_con.active_time()

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()