import pygame
import os

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

##### PLAYER
player_icon = pygame.image.load(os.path.join(file_path, "design\\c_main2.png")).convert_alpha()

player_images =[
    pygame.image.load(os.path.join(file_path, "design\\c_main0.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\c_main1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\c_main2.png")).convert_alpha(),
    # pygame.image.load(os.path.join(file_path, "design\\c_main1.png")).convert_alpha(),
]
player_damaged_image = pygame.image.load(os.path.join(file_path, "design\\c_main_red.png")).convert_alpha()


##### MONSTER
monster_1_images = [pygame.image.load(os.path.join(file_path, "images\\monster_1.png")).convert_alpha()]
monster_2_images = [pygame.image.load(os.path.join(file_path, "images\\monster_2.png")).convert_alpha()]
monster_boss_images = [pygame.image.load(os.path.join(file_path, "images\\monster_boss.png")).convert_alpha()]


##### NPC
father_slime_images = [pygame.image.load(os.path.join(file_path, "images\\father_slime.png")).convert_alpha()]
skeleton_images = [pygame.image.load(os.path.join(file_path, "design\\gwan1.png")).convert_alpha()]
ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\ghost_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\ghost_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\ghost_2.png")).convert_alpha(),
    # pygame.image.load(os.path.join(file_path, "design\\ghost_1.png")).convert_alpha()
]
shooter_images = [pygame.image.load(os.path.join(file_path, "images\\slime.png")).convert_alpha()]
runner_images = [pygame.image.load(os.path.join(file_path, "design\\skeleton.png")).convert_alpha()]


##### FIELD
stair_images = [
    pygame.image.load(os.path.join(file_path, "design\\stair_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\stair_1.png")).convert_alpha()
]
web_image = pygame.image.load(os.path.join(file_path, "design\\web.png")).convert_alpha()
water_images = [
    pygame.image.load(os.path.join(file_path, "design\\water_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\water_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "design\\water_2.png")).convert_alpha()
]


##### ETC
background_zero = pygame.image.load(os.path.join(file_path, "design\\0F.png"))


##### ITEM
portion_image = pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha()
coin_image = pygame.image.load(os.path.join(file_path, "images\\coin_2.png")).convert_alpha()
box_image = pygame.image.load(os.path.join(file_path, "images\\box.png")).convert_alpha()


# Punch Image
punch_d_image = pygame.image.load(os.path.join(file_path, "design\\punch.png")).convert_alpha()


# Equip Image
battery_image = pygame.image.load(os.path.join(file_path, "design\\equips\\battery.png")).convert_alpha()
banana_image = pygame.image.load(os.path.join(file_path, "images\\e_banana.png")).convert_alpha()
pepper_image = pygame.image.load(os.path.join(file_path, "design\\equips\\pepper.png")).convert_alpha()
ice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\ice_m.png")).convert_alpha()
dice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\dice.png")).convert_alpha()
sandclock_image = pygame.image.load(os.path.join(file_path, "images\\e_sandclock.png")).convert_alpha()
apple_image = pygame.image.load(os.path.join(file_path, "images\\e_apple.png")).convert_alpha()
greentea_image = pygame.image.load(os.path.join(file_path, "images\\e_greentea.png")).convert_alpha()
mandoo_image = pygame.image.load(os.path.join(file_path, "images\\e_mandoo.png")).convert_alpha()
a_book_image = pygame.image.load(os.path.join(file_path, "images\\e_a_book.png")).convert_alpha()
bone_image = pygame.image.load(os.path.join(file_path, "images\\e_bone.png")).convert_alpha()


# Others
story_images = [
    
]

tuto_images = [
    pygame.image.load(os.path.join(file_path, "images\\xx.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\tuto.png")).convert_alpha()
]

shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png")).convert_alpha()

sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()
cursor_images = [
    pygame.image.load(os.path.join(file_path, "images\\cursor.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\cursor_is_picking.png")).convert_alpha()
]
skill_c_image = pygame.image.load(os.path.join(file_path, "images\\skill_c.png")).convert_alpha()
skill_v_image = pygame.image.load(os.path.join(file_path, "images\\skill_v.png")).convert_alpha()