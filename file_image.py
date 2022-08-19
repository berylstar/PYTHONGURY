import pygame
import os

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

##### PLAYER
player_icon = pygame.image.load(os.path.join(file_path, "design\\c_main0.png")).convert_alpha()

player_image =[
    pygame.image.load(os.path.join(file_path, "design\\c_main0.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\c_main1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\c_main2.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\c_main1.png")).convert_alpha(),
]


##### MONSTER
monster_1_image = [pygame.image.load(os.path.join(file_path, "images\\monster_1.png")).convert_alpha()]
monster_2_image = [pygame.image.load(os.path.join(file_path, "images\\monster_2.png")).convert_alpha()]


##### NPC
father_slime_image = [pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()]
skeleton_image = [pygame.image.load(os.path.join(file_path, "design\\gwan1.png")).convert_alpha()]


##### FIELD
stair_images = [
    pygame.image.load(os.path.join(file_path, "design\\stair.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\stair_2.png")).convert_alpha()
]
web_image = pygame.image.load(os.path.join(file_path, "design\\web.png")).convert_alpha()


##### ETC
background_zero = pygame.image.load(os.path.join(file_path, "design\\0F.png"))
tuto_image = pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()


##### ITEM
item_images = [
    pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\coin.png")).convert_alpha()
]


# Punch Image
punch_d_image = pygame.image.load(os.path.join(file_path, "design\\punch.png")).convert_alpha()


# Equip Image
battery_image = pygame.image.load(os.path.join(file_path, "images\\e_battery.png")).convert_alpha()
banana_image = pygame.image.load(os.path.join(file_path, "images\\e_banana.png")).convert_alpha()
pepper_image = pygame.image.load(os.path.join(file_path, "images\\e_pepper.png")).convert_alpha()
ice_image = pygame.image.load(os.path.join(file_path, "images\\e_ice.png")).convert_alpha()
dice_image = pygame.image.load(os.path.join(file_path, "images\\e_dice.png")).convert_alpha()
sandclock_image = pygame.image.load(os.path.join(file_path, "images\\e_sandclock.png")).convert_alpha()
apple_iamge = pygame.image.load(os.path.join(file_path, "images\\e_apple.png")).convert_alpha()


# Others
sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()
cursor_image = [
    pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\cursor_is_picking.png")).convert_alpha()
]
skill_c_image = pygame.image.load(os.path.join(file_path, "images\\skill_c.png")).convert_alpha()
skill_v_image = pygame.image.load(os.path.join(file_path, "images\\skill_v.png")).convert_alpha()