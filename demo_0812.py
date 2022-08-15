import pygame
import os
import random

from class_equip import *
from class_character import *
from class_item import *
##############################################################################################
def scene_title_game():
    global running, ready
        
    msg_start = game_font.render("START", True, BLACK)
    start_rect = msg_start.get_rect(center=(screen_width//2,500))
    start_cursor = ((start_rect.left - 30, start_rect.top),(start_rect.left - 30,start_rect.bottom),(start_rect.left - 10,500))

    msg_exit = game_font.render("EXIT", True, BLACK)
    exit_rect = msg_exit.get_rect(center=(screen_width//2,550))
    exit_cursor = ((exit_rect.left - 30, exit_rect.top),(exit_rect.left - 30,exit_rect.bottom),(exit_rect.left - 10,550))

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

        screen.fill((125,125,125))                              #BACKGROUND
        pygame.draw.polygon(screen, GREEN, cursor)              #CURSOR
        screen_message("SLIME PUNCH", GREEN, (screen_width//2,200))
        screen_message("START", BLACK, (screen_width//2,500))
        screen_message("EXIT", BLACK, (screen_width//2,550))

        pygame.display.update()

def display_game_ui():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ((340,60), (600, 600)), 1)      #MAIN GAME
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)      #INFO
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1)      #INVEN
              
    screen_message(f"{floor} F", WHITE, (240,90))                   #FLOOR MESSAGE
    screen_message(f"HP : {player.hp}", WHITE, (240,190))           #HP MESSAGE

    coin_image_rect = item_images[1].get_rect(center=(215, 290))
    screen.blit(item_images[1], coin_image_rect)
    screen_message(f"              X {player.coin}", WHITE, (220,290))      #COIN MESSAGE

    life_image_rect = player_image.get_rect(center=(210, 390))
    screen.blit(player_image, life_image_rect)
    screen_message(f"              X {player.life}", WHITE, (220,390))      #LIFE MESSAGE

    for i in range(4):
        pygame.draw.line(screen, GRAY, (950 + 60*i, 180), (950 + 60*i, 540))
    for i in range(7):
        pygame.draw.line(screen, GRAY, (950, 180 + 60*i), (1130, 180 + 60*i))

    for equip in equip_group:
        equip.draw(screen)

    if inven_is_overlap(equip_group):
        screen_message("ARRANGE EQUIP !", RED, (1040,150))

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
    global running, shop_is_buy

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if not shop_is_buy[0] and player.coin >= 3:
                        equip_group[0] = e_Punch(punch_v_image, (0,0))
                        player.coin -= 3
                        shop_is_buy[0] = True
                if event.key == pygame.K_2:
                    if not shop_is_buy[1] and player.coin >= 6:
                        equip_group.append(e_Banana(banana_image, (0,0)))
                        player.coin -= 6
                        shop_is_buy[1] = True
                if event.key == pygame.K_3:
                    if not shop_is_buy[2] and player.coin >= 3:
                        equip_group.append(e_Battery(battery_image, (0,0)))
                        player.coin -= 3
                        shop_is_buy[2] = True
                if event.key == pygame.K_SPACE:
                    doing = False

        display_game_ui()

        equip_showcase(0, punch_v_image, 3)
        equip_showcase(1, banana_image, 6)
        equip_showcase(2, battery_image, 3)

        check_equip()

        screen.blit(shop_image, shop_rect)
        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640))
        pygame.display.update()

def equip_showcase(index, image, price):
    pygame.draw.rect(screen, WHITE, ((450 + 150*index,350),(80,120)), 1)

    if not shop_is_buy[index]:
        equip_image = pygame.transform.scale(image, (60,60))
        equip_rect = equip_image.get_rect(center=(490+ 150*index, 390))
        screen.blit(equip_image, equip_rect)

        coin_image = pygame.transform.rotozoom(item_images[1], 0, 0.5)
        coin_rect = coin_image.get_rect(center=(470+ 150*index,440))
        screen.blit(coin_image, coin_rect)

        screen_message(f"  x {price}", WHITE, (500+ 150*index, 440))
    else:
        case_rect = sold_out_image.get_rect(center=(490+ 150*index,410))
        screen.blit(sold_out_image, case_rect)

def scene_player_dead(doing):
    global running

    player.stop()

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
        screen_message("PRESS 'R' TO REPLAY", WHITE, (640,640))
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
                if event.key == pygame.K_ESCAPE:
                    running = False
                    doing = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    doing = False
                    game_restart()
                    ready = True

        screen.fill(BLACK)
        screen_message("GAME OVER", RED, (screen_width//2, screen_height//2))
        screen_message("PRESS 'ESC' TO QUIT", WHITE, (640,590))
        screen_message("PRESS 'SPACE BAR' TO MAIN", WHITE, (640,640))
        pygame.display.update()

def scene_arrange_equip(doing):
    global running

    cursor = Cursor(cursor_image, (980,210))
    picked_equip = None

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.is_picking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i:
                    doing = False
                    print(inven_is_overlap(equip_group))

                if event.key == pygame.K_SPACE:
                    if cursor.is_picking:
                        cursor.is_picking = False
                        picked_equip = None

                    else:
                        for equip in equip_group:
                            if pygame.sprite.collide_mask(equip, cursor):
                                cursor.is_picking = True
                                picked_equip = equip

        display_game_ui()
        cursor.draw(screen)
        if inven_is_overlap(equip_group):
            screen_message("ARRANGE EQUIP !", RED, (1040,150))
        pygame.display.update()

##############################################################################################
def screen_message(writing, color, position):
    msg = game_font.render(writing, True, color)
    msg_rect = msg.get_rect(center=position)
    screen.blit(msg, msg_rect)

def game_restart():
    global floor, player, shop_is_buy, equip_group

    player = Player(player_image, player_first_position)
    floor_zero()
    floor = 0
    shop_is_buy = [False, False, False]
    equip_group = [e_Punch(punch_d_image, (0,0))]

def floor_zero():
    global floor

    if floor != 0:
        floor = 0
        monster_group.empty()
        item_group.empty()
        stair.image = stair_images[0]
        stair.rect = stair.image.get_rect(center=stair_zero_floor)

        player.rect = player.image.get_rect(center=player_first_position)
        player.hp = 100

    npc_group.draw(screen)                                                      #NPC

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

    stair.image = stair_images[1]

    number_enemies = floor//5 + 1

    for i in range(number_enemies):
        monster = prob_spawn_monster(90 - floor)
        random_position(pos, monster)
        monster_group.add(monster)

def player_move_key():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.to[0] -= player_speed
            player.direction = "LEFT"
        if event.key == pygame.K_RIGHT:
            player.to[1] += player_speed
            player.direction = "RIGHT"
        if event.key == pygame.K_UP:
            player.to[2] -= player_speed
            player.direction = "UP"
        if event.key == pygame.K_DOWN:
            player.to[3] += player_speed
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

def random_position(center, object):
    while True:
        rand_x = random.randint(370, 910)
        rand_y = random.randint(150, 570)

        if rand_x < center[0] - 60 or center[0] + 60 < rand_x:
            if rand_y < center[1] - 60 or center[1] + 60 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def prob_spawn_monster(percent):
    randprob = random.randrange(0,101)

    if randprob <= percent:
        return Monster(monster_images[0], (0,0), MON_0_HP)
    else:
        return Monster(monster_images[1], (0,0), MON_1_HP)

def monster_random_direction():
    if monster_group:
        for monster in monster_group:
            rand = random.randrange(0,11)
            if rand <= 1:
                monster.direction = "LEFT"
            elif 1 < rand and rand <= 3:
                monster.direction = "RIGHT"
            elif 3 < rand and rand <= 5:
                monster.direction = "UP"
            elif 5 < rand and rand <= 7:
                monster.direction = "DOWN"
            else:
                monster.direction = "NONE"

            if monster.rect.centerx < 410:
                monster.direction = "RIGHT"
            elif monster.rect.centerx > 870:
                monster.direction = "LEFT"

            if monster.rect.centery < 130:
                monster.direction = "DOWN"
            elif monster.rect.centery > 590:
                monster.direction = "UP"

def monster_random_move():
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

    if randprob <= PROB_PORTION:
        item_group.add(Item(item_images[0], position, "portion"))
    elif PROB_PORTION < randprob <= PROB_PORTION + PROB_COIN:
        item_group.add(Item(item_images[1], position, "coin"))

def item_effect(item):
    if item.info == "portion":
        player.hp = min(player.hp + 5, 100)
    if item.info == "coin":
        player.coin += 1

def check_equip():

    # 장비 장착
    if equip_group[0].image == punch_v_image:
        player.punch = punch_v_image
        player.damage = 15

    elif equip_group[0].image == punch_f_image:
        player.punch = punch_f_image
        player.damage = 17
        
    # 장비 해제
    else:
        player.punch = punch_d_image
        player.damage = 10

##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image, position):
        Character.__init__(self, image, position)

        self.life = 3
        self.hp = 100
        self.coin = 100
        self.punch = punch_d_image
        self.equip_c = None
        self.equip_v = None
        self.damage = 10    

    def space_bar(self):
        image = self.punch

        if self.direction == "LEFT":
            position = (self.rect.centerx-60, self.rect.centery)
        elif self.direction == "RIGHT":
            image = pygame.transform.rotozoom(image, 180, 1)
            position = (self.rect.centerx+60, self.rect.centery)
        elif self.direction == "UP":
            image = pygame.transform.rotozoom(image, 270, 1)
            position = (self.rect.centerx, self.rect.centery-60)
        elif self.direction == "DOWN":
            image = pygame.transform.rotozoom(image, 90, 1)
            position = (self.rect.centerx, self.rect.centery+60)

        punch_group.add(Punch(image, position, self.direction))
    
    def skill_c(self):
        print(self.equip_c)
    
    def skill_v(self):
        print(self.equip_v)

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

##### STIAR CLASS
class Stair(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
##############################################################################################
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("No More Slime")
file_path = os.path.dirname(__file__)
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 30)
start_ticks = pygame.time.get_ticks()
second_counter = 0

#### GAME SYSTEM
WHITE = (255,255,255)
GRAY = (64,64,64)
BLACK = (0,0,0)
RED = (127,0,0)
GREEN = (0,127,0)
BLUE = (0,0,127)
floor = 0

##### PLAYER
player_image = pygame.image.load(os.path.join(file_path, "images\\slime.png")).convert_alpha()
player_first_position = (700, 360)
player = Player(player_image, player_first_position)
player_speed = 0.5

punch_group = pygame.sprite.Group()

##### STAIR
stair_images = [
    pygame.image.load(os.path.join(file_path, "images\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]
stair_zero_floor = (640, 90)
stair = Stair(stair_images[0], stair_zero_floor)

###### NPC

father_slime = Character(father_slime_image, (540, 360))
skeleton = Character(skeleton_image, (840, 600))

npc_group = pygame.sprite.Group()
npc_group.add(father_slime, skeleton)

##### ITEM
item_group = pygame.sprite.Group()

##### INVENTORY
    
equip_group = [e_Punch(punch_d_image, (0,0))] # index 0 : punch
len_1 = 0
len_2 = 0
shop_is_buy = [False, False, False]

##### ETC
tuto_image = pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
tuto_rect = tuto_image.get_rect(center=(640, 300))
shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()
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
                player.stop()
                scene_arrange_equip(True)

        if not inven_is_overlap(equip_group):
            player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3], fps)

    display_game_ui()                                                         #UI

    if floor == 0:
        floor_zero()      

    elif floor > 0:
        elapsed_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if second_counter != elapsed_time:
            #for 1 second
            player.hp -= 1
            monster_random_direction()
        second_counter = elapsed_time

        if player.hp <= 0:
            player.life -= 1
            if player.life <= 0:
                scene_game_over(True)
            else:
                scene_player_dead(True)

        monster_random_move()

    if not monster_group:
        stair.draw(screen)                                                          #STAIR

        if pygame.sprite.collide_mask(player, stair):
            next_floor(player.position) 

    for monster in monster_group:
        if not monster.is_died:        
            monster.draw(screen)                                                      #MONSTER
            if pygame.sprite.collide_mask(player, monster):
                player.hp -= 1

        for punch in punch_group:
            if pygame.sprite.collide_mask(monster, punch):
                punch.draw(screen)
                punch_group.remove(punch)
                monster.hp -= player.damage
                if monster.hp <= 0:
                    monster.die(drop_item, monster_group)
                random_position(player.position, stair)

    for punch in punch_group:
        punch.draw(screen)                                                          #PUNCH

        if punch.get_time() > 10:
            punch_group.remove(punch)   

    for item in item_group:
        item.draw(screen)                                                           #ITEM
        if pygame.sprite.collide_mask(item, player):
            item_effect(item)
            item_group.remove(item)

    len_1 = len(equip_group)
    if len_1 != len_2:
        check_equip()
    len_2 = len(equip_group)

    player.draw(screen)                                                             #PLAYER

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()