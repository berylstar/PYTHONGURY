import pygame
import os
import random
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
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    equip_group.append("punch_v")
                    print("GET PUNCH_V")
                if event.key == pygame.K_SPACE:
                    doing = False

        display_game_ui()
        shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()
        shop_rect = shop_image.get_rect(center=(640, 300))
        screen.blit(shop_image, shop_rect)

        msg_back = game_font.render("PRESS 'SPACE BAR' TO BACK", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)
        pygame.display.update()

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

def game_restart():
    global floor, player

    player = Player(player_image, player_first_position)
    floor_zero()
    floor = 0
    equip_group.clear()

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

def floor_zero():
    global floor

    if floor != 0:
        floor = 0
        monster_group.empty()
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
     
def random_position(center, object):
    while True:
        rand_x = random.randint(370, 910)
        rand_y = random.randint(150, 570)

        if rand_x < center[0] - 60 or center[0] + 60 < rand_x:
            if rand_y < center[1] - 60 or center[1] + 60 < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def drop_item(position):
    randprob = random.randrange(0,101)

    if randprob <= PROB_PORTION:
        item_group.add(Item(item_images[0], position, "portion"))
    elif PROB_PORTION < randprob <= PROB_PORTION + PROB_COIN:
        item_group.add(Item(item_images[1], position, "coin"))

def prob_spawn_monster(percent):
    randprob = random.randrange(0,101)

    if randprob <= percent:
        return Monster(monster_images[0], (0,0), MON_1_HP)
    else:
        return Monster(monster_images[1], (0,0), MON_2_HP)

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
                monster.move(-0.1, 0)
            elif monster.direction == "RIGHT":
                monster.move(0.1, 0)
            elif monster.direction == "UP":
                monster.move(0,-0.1)
            elif monster.direction == "DOWN":
                monster.move(0,0.1)
            else:
                pass

def check_equip():
    global punch_image

    # 장비 장착
    for equip in equip_group:
        if equip == "punch_v":
            punch_image = pygame.image.load(os.path.join(file_path, "images\\punch_v.png")).convert_alpha()
            player.damage = 15

    # 장비 해제
    if "punch_v" not in equip_group:
        punch_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
        player.damage = 10
##############################################################################################
##### CHARACTER CLASS
class Character(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)
        self.direction = "LEFT"
        self.to = [0, 0, 0, 0]  #LEFT, RIGHT, UP, DOWN
        self.flip = False
        self.r_image = pygame.transform.flip(image, True, False)

    def draw(self, screen):
        if self.direction == "LEFT":
            self.flip = False
        elif self.direction == "RIGHT":
            self.flip = True

        if not self.flip:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.r_image, self.rect)

    def move(self, to_x, to_y):
        self.rect.x += to_x * fps
        self.rect.y += to_y * fps

        if self.rect.centerx < 370:
            self.rect.centerx = 370
        elif self.rect.centerx > 910:
            self.rect.centerx = 910

        if self.rect.centery < 90:
            self.rect.centery = 90
        elif self.rect.centery > 630:
            self.rect.centery = 630

        self.position = (self.rect.centerx, self.rect.centery)

    def stop(self):
        self.to = [0,0,0,0]

##### PLAYER CLASS
class Player(Character):
    def __init__(self, image, position):
        Character.__init__(self, image, position)

        self.life = 3
        self.hp = 100
        self.coin = 0
        self.weapon = "punch"
        self.damage = 10

    # def attack(self):
    #     if self.weapon == "punch":
    #         punch_attack()

    def attack(self):
        global punch_group
        
        if self.direction == "LEFT":
            punch_group.add(Punch(punch_image, (self.rect.centerx-60, self.rect.centery), self.direction))
        elif self.direction == "RIGHT":
            r_image = pygame.transform.rotozoom(punch_image, 180, 1)
            punch_group.add(Punch(r_image, (self.rect.centerx+60, self.rect.centery), self.direction))
        elif self.direction == "UP":
            r_image = pygame.transform.rotozoom(punch_image, 270, 1)
            punch_group.add(Punch(r_image, (self.rect.centerx, self.rect.centery-60), self.direction))
        elif self.direction == "DOWN":
            r_image = pygame.transform.rotozoom(punch_image, 90, 1)
            punch_group.add(Punch(r_image, (self.rect.centerx, self.rect.centery+60), self.direction))

##### MONSTER CLASS
class Monster(Character):
    def __init__(self, image, position, hp):
        Character.__init__(self, image, position)
        self.is_died = False
        self.hp = hp

    def die(self):
        self.is_died = True
        drop_item(self.position)
        monster_group.remove(self)

##### PUNCH CLASS
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

        if self.direction == "LEFT":
            self.rect = (player.rect.x-60, player.rect.y)
        elif self.direction == "RIGHT":
            self.rect = (player.rect.x+60, player.rect.y)
        elif self.direction == "UP":
            self.rect = (player.rect.x, player.rect.y-60)
        elif self.direction == "DOWN":
            self.rect = (player.rect.x, player.rect.y+60)

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

##### ITEM CLASS
class Item(pygame.sprite.Sprite):
    def __init__(self, image, position, info):
        super().__init__()
        self.image = image
        self.position = position
        self.info = info

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

####GAME SYSTEM
WHITE = (255,255,255)
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

punch_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_group = pygame.sprite.Group()

#####STAIR
stair_images = [
    pygame.image.load(os.path.join(file_path, "images\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]
stair_zero_floor = (640, 90)
stair = Stair(stair_images[0], stair_zero_floor)

#####MONSTER
monster_images = [
    pygame.image.load(os.path.join(file_path, "images\\monster_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\monster_2.png")).convert_alpha()
]
monster_group = pygame.sprite.Group()
MON_1_HP = 10
MON_2_HP = 25

######NPC
father_slime_image = pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()
father_slime = Character(father_slime_image, (540, 360))

skeleton_image = pygame.image.load(os.path.join(file_path, "images\\skeleton.png")).convert_alpha()
skeleton = Character(skeleton_image, (840, 600))

npc_group = pygame.sprite.Group()
npc_group.add(father_slime, skeleton)

#####ITEM
item_images = [
    pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\coin.png")).convert_alpha()
]
item_group = pygame.sprite.Group()
PROB_PORTION = 10
PROB_COIN = 10

equip_group = []
len_1 = 0
len_2 = 0
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
                player.attack()

        player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3])

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
                print(monster.hp, player.damage)
                if monster.hp <= 0:
                    monster.die()
                random_position(player.position, stair)

    for punch in punch_group:
        punch.draw(screen)                                                          #PUNCH

        if punch.get_time() > 10:
            punch_group.remove(punch)

    if not monster_group:
        stair.draw(screen)                                                          #STAIR

        if pygame.sprite.collide_mask(player, stair):
            next_floor(player.position)    

    for item in item_group:
        item.draw(screen)                                                           #ITEM
        if pygame.sprite.collide_mask(item, player):
            if item.info == "portion":
                player.hp += 5
            if item.info == "coin":
                player.coin += 1
            item_group.remove(item)

    len_1 = len(equip_group)
    if len_1 != len_2:
        check_equip()
    len_2 = len(equip_group)

    player.draw(screen)                                                             #PLAYER

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()