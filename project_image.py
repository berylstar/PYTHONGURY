import pygame
import os

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

##### PLAYER
player_image = pygame.image.load(os.path.join(file_path, "images\\slime.png")).convert_alpha()
# player_image = pygame.image.load(os.path.join(file_path, "design\\c_main0.png")).convert_alpha()

##### STAIR
stair_images = [
    pygame.image.load(os.path.join(file_path, "images\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]

##### ETC
background_zero = pygame.image.load(os.path.join(file_path, "design\\0F.png"))
tuto_image = pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()

##### MONSTER
monster_images = [
    pygame.image.load(os.path.join(file_path, "images\\monster_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\monster_2.png")).convert_alpha()
]
monster_group = pygame.sprite.Group()

##### NPC
father_slime_image = pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()
skeleton_image = pygame.image.load(os.path.join(file_path, "images\\skeleton.png")).convert_alpha()

##### ITEM
item_images = [
    pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\coin.png")).convert_alpha()
]

# Punch Image
punch_d_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_v_image = pygame.image.load(os.path.join(file_path, "images\\punch_v.png")).convert_alpha()
punch_f_image = pygame.image.load(os.path.join(file_path, "images\\punch_f.png")).convert_alpha()

# Equip Image
battery_image = pygame.image.load(os.path.join(file_path, "images\\e_battery.png")).convert_alpha()
banana_image = pygame.image.load(os.path.join(file_path, "images\\e_banana.png")).convert_alpha()

# Others
sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()
cursor_image = [
    pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\cursor_is_picking.png")).convert_alpha()
]
skill_c_image = pygame.image.load(os.path.join(file_path, "images\\skill_c.png")).convert_alpha()
skill_v_image = pygame.image.load(os.path.join(file_path, "images\\skill_v.png")).convert_alpha()
