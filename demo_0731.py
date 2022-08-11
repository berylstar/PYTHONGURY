import pygame
import os
import random
##############################################################################################
def scene_title_game():
    global ready, running

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
                # pygame.quit()
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
                        # pygame.quit()

        screen.fill((125,125,125))                              #BACKGROUND
        pygame.draw.polygon(screen, GREEN, cursor)              #CURSOR
        screen.blit(msg_title, title_rect)                      #TITLE
        screen.blit(msg_start, start_rect)                      #GAME START
        screen.blit(msg_exit, exit_rect)                        #EXIT

        pygame.display.update()

def display_game_ui(option):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ((340,60), (600, 600)), 1)      #MAIN GAME
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)      #INFO
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1)      #INVEN

    if option == "main":
        msg_floor = game_font.render(f"{floor} F", True, WHITE)
        floor_rect = msg_floor.get_rect(center=(240,90))
        screen.blit(msg_floor, floor_rect)                                #FLOOR MESSAGE

        msg_hp = game_font.render(f"HP : {player.hp}", True, WHITE)
        hp_rect = msg_hp.get_rect(center=(240,190))
        screen.blit(msg_hp, hp_rect)                                      #HP MESSAGE

    elif option == "tutorial":
        tuto_image = pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
        tuto_rect = tuto_image.get_rect(center=(640, 300))
        screen.blit(tuto_image, tuto_rect)

        msg_back = game_font.render("PRESS SPACE BAR TO BACK", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)

    elif option == "shop":
        shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()
        shop_rect = shop_image.get_rect(center=(640, 300))
        screen.blit(shop_image, shop_rect)

        msg_back = game_font.render("PRESS SPACE BAR TO BACK", True, WHITE)
        exit_rect = msg_back.get_rect(center=(640, 640))
        screen.blit(msg_back, exit_rect)

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

        screen.fill(BLACK)
        display_game_ui("tutorial")
        pygame.display.update()


def scene_skeleton_shop(shopping):
    global running

    while shopping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                shopping = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shopping = False

        screen.fill(BLACK)
        display_game_ui("shop")
        pygame.display.update()

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


def next_floor(pos):
    global floor

    floor += 1
    if floor % 10 == 0:
        player.hp += 10

    stair.image = stair_images[1]
    
    random_position(pos, enemy, 50)
    random_position(enemy.position, stair, 100)  
    
    enemy.is_died = False

def random_position(position, object, distance):
    while True:
        rand_x = random.randint(370, 910)
        rand_y = random.randint(150, 570)

        if rand_x < position[0] - distance or position[0] + distance < rand_x:
            if rand_y < position[1] - distance or position[1] + distance < rand_y:
                object.position = (rand_x, rand_y)
                object.rect = object.image.get_rect(center=object.position)
                break 

def drop_item(percentage):

    if percentage <= 20:
        item_group.add(Item(portion_image, enemy.position))
        # item_group.draw(screen)

def get_percentage():
    return random.randrange(0,101)
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

        self.hp = 100

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
        # if pygame.sprite.collide_mask(self, father_slime):
        #     to_x = 0
        #     to_y = 0

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

##### ENEMY CLASS
class Enemy(Character):
    def __init__(self, image, position):
        Character.__init__(self, image, position)
        self.is_died = False

    def die(self):
        self.is_died = True
        drop_item(get_percentage())

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
            r_image = pygame.transform.rotozoom(punch_image, 180, 1)
            self.rect = (player.rect.x+60, player.rect.y)
        elif self.direction == "UP":
            r_image = pygame.transform.rotozoom(punch_image, 270, 1)
            self.rect = (player.rect.x, player.rect.y-60)
        elif self.direction == "DOWN":
            r_image = pygame.transform.rotozoom(punch_image, 90, 1)
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
second_tick = 0

####GAME SYSTEM
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,125,0)
floor = 0

#####PLAYER
player_image = pygame.image.load(os.path.join(file_path, "images\\slime.png")).convert_alpha()
player = Player(player_image, (700, 360))
player_speed = 0.5

punch_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_group = pygame.sprite.Group()

#####STAIR
stair_images = [
    pygame.image.load(os.path.join(file_path, "images\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]
stair = Stair(stair_images[0], (640, 90))

#####ENEMY
enemy_image = pygame.image.load(os.path.join(file_path, "images\\enemy.png")).convert_alpha()
enemy = Enemy(enemy_image, (0,0))
enemy_group = pygame.sprite.Group()

######NPC
father_slime_image = pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()
father_slime = Character(father_slime_image, (540, 360))

skeleton_image = pygame.image.load(os.path.join(file_path, "images\\skeleton.png")).convert_alpha()
skeleton = Character(skeleton_image, (840, 600))

npc_group = pygame.sprite.Group()
npc_group.add(father_slime, skeleton)

#####PORTION
portion_image = pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha()
item_group = pygame.sprite.Group()

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

    display_game_ui("main")                                                         #UI

    if floor == 0:
        npc_group.draw(screen)                                                      #NPC
        enemy.is_died = True

        for punch in punch_group:
            if pygame.sprite.collide_mask(punch, father_slime):
                player.stop()
                scene_tutorial(True)

            if pygame.sprite.collide_mask(punch, skeleton):
                player.stop()
                scene_skeleton_shop(True)            

    elif floor > 0:
        elapsed_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if second_tick != elapsed_time:
            player.hp -= 1
        second_tick = elapsed_time

        if player.hp <= 0:
            msg_gameover = game_font.render("GAME OVER", True, WHITE)
            msg_gameover_rect = msg_gameover.get_rect(center=(screen_width//2, screen_height//2))
            screen.blit(msg_gameover, msg_gameover_rect)
            pygame.display.update()
            running = False

    if not enemy.is_died:        
        enemy.draw(screen)                                                          #ENEMY
        if pygame.sprite.collide_mask(player, enemy):
            player.hp -= 1
    else:
        stair.draw(screen)                                                          #STAIR
        
        if pygame.sprite.collide_mask(player, stair):
            item_group.empty()
            next_floor(player.position)

    for punch in punch_group:
        punch.draw(screen)                                                          #PUNCH
        if pygame.sprite.collide_mask(punch, enemy):
            enemy.die()

        if punch.get_time() > 10:
            punch_group.remove(punch)

    for item in item_group:
        item.draw(screen)                                                           #ITEM
        if pygame.sprite.collide_mask(item, player):
            player.hp += 5
            item_group.remove(item)

    player.draw(screen)                                                             #PLAYER

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()