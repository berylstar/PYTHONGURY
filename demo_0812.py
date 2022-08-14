import pygame
import os
import random

from class_equip import *
from class_monster import *
from class_item import *
##############################################################################################
def scene_title_game():
    global running, ready

    msg_title = game_font.render("SLIME PUNCH", True, GREEN)
    title_rect = msg_title.get_rect(center=(screen_width//2,200))
        
    msg_start = game_font.render("GAME START", True, BLACK)
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
        screen.blit(msg_title, title_rect)                      #TITLE
        screen.blit(msg_start, start_rect)                      #GAME START
        screen.blit(msg_exit, exit_rect)                        #EXIT

        pygame.display.update()

def display_game_ui():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ((340,60), (600, 600)), 1)      #MAIN GAME
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)      #INFO
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1)      #INVEN
    # pygame.draw.rect(screen, GREEN, ((410, 130),(460, 460)), 1)    # monster moving zone

    msg_floor = game_font.render(f"{floor} F", True, WHITE)
    floor_rect = msg_floor.get_rect(center=(240,90))
    screen.blit(msg_floor, floor_rect)                                #FLOOR MESSAGE

    msg_hp = game_font.render(f"HP : {player.hp}", True, WHITE)
    hp_rect = msg_hp.get_rect(center=(240,190))
    screen.blit(msg_hp, hp_rect)                                      #HP MESSAGE

    msg_coin = game_font.render(f"              X {player.coin}", True, WHITE)
    coin_rect = msg_coin.get_rect(center=(220,290))
    coin_image_rect = item_images[1].get_rect(center=(215, 290))
    screen.blit(item_images[1], coin_image_rect)
    screen.blit(msg_coin, coin_rect)                                  #COIN MESSAGE

    msg_life = game_font.render(f"              X {player.life}", True, WHITE)
    life_rect = msg_life.get_rect(center=(220,390))
    life_image_rect = player_image.get_rect(center=(210, 390))
    screen.blit(player_image, life_image_rect)
    screen.blit(msg_life, life_rect)                                  #COIN MESSAGE

    for i in range(4):
        pygame.draw.line(screen, GRAY, (950 + 60*i, 120), (950 + 60*i, 600))
    for i in range(10):
        pygame.draw.line(screen, GRAY, (950, 120 + 60*i), (1130, 120 + 60*i))

    for equip in equip_group:
    #     idx = equip_group.index(equip) + 1
    #     equip.rect = equip.image.get_rect(center=(1040, 160*idx))
        screen.blit(equip.image, equip.rect)

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

        tuto_image = pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
        tuto_rect = tuto_image.get_rect(center=(640, 300))
        screen.blit(tuto_image, tuto_rect)

        msg_back = game_font.render("PRESS 'SPACE BAR' TO BACK", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)

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
                        equip_group[0] = Punch(punch_v_image, inven_position[0], "UP")
                        player.coin -= 3
                        shop_is_buy[0] = True
                if event.key == pygame.K_2:
                    if not shop_is_buy[1] and player.coin >= 6:
                        equip_group[0] = Punch(punch_f_image, inven_position[0], "UP")
                        player.coin -= 6
                        shop_is_buy[1] = True
                if event.key == pygame.K_3:
                    if not shop_is_buy[2] and player.coin >= 3:
                        equip_group.append(Whatisthis(wit_image, inven_position[0]))
                        player.coin -= 3
                        shop_is_buy[2] = True
                if event.key == pygame.K_SPACE:
                    doing = False

        display_game_ui()

        equip_showcase(0, punch_v_image, 3)
        equip_showcase(1, punch_f_image, 6)
        equip_showcase(2, wit_image, 3)

        check_equip()

        shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()
        shop_rect = shop_image.get_rect(center=(640, 200))
        screen.blit(shop_image, shop_rect)

        msg_back = game_font.render("PRESS 'SPACE BAR' TO BACK", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)
        pygame.display.update()

def equip_showcase(index, image, price):
    pygame.draw.rect(screen, WHITE, ((450 + 150*index,350),(80,120)), 1)
    if not shop_is_buy[index]:
        equip_rect = image.get_rect(center=(490+ 150*index, 390))
        screen.blit(image, equip_rect)

        coin_image = pygame.transform.rotozoom(item_images[1], 0, 0.5)
        coin_rect = coin_image.get_rect(center=(470+ 150*index,440))
        screen.blit(coin_image, coin_rect)

        msg_price = game_font.render("  x {0}".format(price), True, WHITE)
        price_rect = msg_price.get_rect(center=(500+ 150*index, 440))
        screen.blit(msg_price, price_rect)
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
        msg_gameover = game_font.render("YOU DIE", True, RED)
        msg_gameover_rect = msg_gameover.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(msg_gameover, msg_gameover_rect)

        msg_back = game_font.render("PRESS 'R' TO REPLAY", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)
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
        msg_gameover = game_font.render("GAME OVER", True, RED)
        msg_gameover_rect = msg_gameover.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(msg_gameover, msg_gameover_rect)

        msg_quit = game_font.render("PRESS 'ESC' TO QUIT", True, WHITE)
        quit_rect = msg_quit.get_rect(center=(640, 590))
        screen.blit(msg_quit, quit_rect)

        msg_back = game_font.render("PRESS 'SPACE BAR' TO MAIN", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)
        pygame.display.update()

def scene_arrange_equip(doing):
    global running

    cursor = Cursor(cursor_image, inven_position[0])
    picked_equip = None
    is_arranged = True

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

                if event.key == pygame.K_SPACE:
                    if cursor.is_picking:
                        cursor.is_picking = False
                        picked_equip = None

                    else:
                        for equip in equip_group:
                            if pygame.sprite.collide_mask(equip, cursor):
                                cursor.is_picking = True
                                picked_equip = equip

        # for equip_1 in equip_group:
        #     for equip_2 in equip_group:
        #         if pygame.sprite.collide_mask(equip_1, equip_2):
        #             is_arranged = False
        #             if not is_arranged:
        #                 print(is_arranged)
        #         else:
        #             is_arranged = True    
        #             print(is_arranged)      

        display_game_ui()
        cursor.draw(screen)
        pygame.display.update()

##############################################################################################
def game_restart():
    global floor, player, shop_is_buy, equip_group

    player = Player(player_image, player_first_position)
    floor_zero()
    floor = 0
    shop_is_buy = [False, False, False]
    equip_group = [Punch(punch_d_image, (-50,-50), "UP")]

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
        player.punch = "punch_v"
        player.damage = 15

    elif equip_group[0].image == punch_f_image:
        player.punch = "punch_f"
        player.damage = 17
        
    # 장비 해제
    else:
        player.punch = "punch_d"
        player.damage = 10

##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image, position):
        Character.__init__(self, image, position)

        self.life = 3
        self.hp = 100
        self.coin = 100
        self.punch = "punch_d"
        self.equip = "None"
        self.damage = 10

    def space_bar(self):
        if self.punch == "punch_d":
            self.attack(Punch, punch_group, punch_d_image)
        elif self.punch == "punch_v":
            self.attack(Punch, punch_group, punch_v_image)
        elif self.punch == "punch_f":
            self.attack(Punch, punch_group, punch_f_image)

    def attack(self, equip, group, image):
        if self.direction == "LEFT":
            group.add(equip(image, (self.rect.centerx-60, self.rect.centery), self.direction))
        elif self.direction == "RIGHT":
            r_image = pygame.transform.rotozoom(image, 180, 1)
            group.add(equip(r_image, (self.rect.centerx+60, self.rect.centery), self.direction))
        elif self.direction == "UP":
            r_image = pygame.transform.rotozoom(image, 270, 1)
            group.add(equip(r_image, (self.rect.centerx, self.rect.centery-60), self.direction))
        elif self.direction == "DOWN":
            r_image = pygame.transform.rotozoom(image, 90, 1)
            group.add(equip(r_image, (self.rect.centerx, self.rect.centery+60), self.direction))
    
    def skill(self):
        print(self.equip)

##### STIAR CLASS
class Stair(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

####GAME SYSTEM
WHITE = (255,255,255)
GRAY = (64,64,64)
BLACK = (0,0,0)
RED = (127,0,0)
GREEN = (0,127,0)
BLUE = (0,0,127)
floor = 0

#####PLAYER
player_image = pygame.image.load(os.path.join(file_path, "images\\slime.png")).convert_alpha()
player_first_position = (700, 360)
player = Player(player_image, player_first_position)
player_speed = 0.5

punch_group = pygame.sprite.Group()

#####STAIR
stair_images = [
    pygame.image.load(os.path.join(file_path, "images\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]
stair_zero_floor = (640, 90)
stair = Stair(stair_images[0], stair_zero_floor)

######NPC
father_slime_image = pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()
father_slime = Character(father_slime_image, (540, 360))

skeleton_image = pygame.image.load(os.path.join(file_path, "images\\skeleton.png")).convert_alpha()
skeleton = Character(skeleton_image, (840, 600))

npc_group = pygame.sprite.Group()
npc_group.add(father_slime, skeleton)

#####ITEM
item_group = pygame.sprite.Group()

##### INVENTORY
cursor_image = pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha()
    
equip_group = [Punch(punch_d_image, inven_position[0], "UP")] # index 0 : punch
len_1 = 0
len_2 = 0
shop_is_buy = [False, False, False]
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
                player.skill()
            if event.key == pygame.K_i:
                player.stop()
                scene_arrange_equip(True)

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
                punch.draw(screen, player)
                punch_group.remove(punch)
                monster.hp -= player.damage
                if monster.hp <= 0:
                    monster.die(drop_item, monster_group)
                random_position(player.position, stair)

    for punch in punch_group:
        punch.draw(screen, player)                                                          #PUNCH

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