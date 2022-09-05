import pygame
import os

# screen_width = 1280
# screen_height = 720
# screen = pygame.display.set_mode((screen_width, screen_height))

file_path = os.path.dirname(__file__)

##### PLAYER
player_icon = pygame.image.load(os.path.join(file_path, "design\\c_main2.png"))

player_images =[
    pygame.image.load(os.path.join(file_path, "design\\c_main0.png")),
    pygame.image.load(os.path.join(file_path, "design\\c_main1.png")),
    pygame.image.load(os.path.join(file_path, "design\\c_main2.png")),
    pygame.image.load(os.path.join(file_path, "design\\c_main1.png")),
]
player_damaged_image = pygame.image.load(os.path.join(file_path, "design\\c_main_red.png"))


##### MONSTER
monster_1_images = [pygame.image.load(os.path.join(file_path, "images\\monster_1.png"))]
monster_2_images = [pygame.image.load(os.path.join(file_path, "images\\monster_2.png"))]
monster_boss_images = [pygame.image.load(os.path.join(file_path, "images\\monster_boss.png"))]

mon_skel_images = [pygame.image.load(os.path.join(file_path, "design\\monster\\skel.png")),]
mon_ember_images = [pygame.image.load(os.path.join(file_path, "design\\monster\\ember.png")),]
ember_attack_image = pygame.image.load(os.path.join(file_path, "design\\monster\\ember_attack.png"))
runner_images = [pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))]
mon_ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]
mon_slime_images = [pygame.image.load(os.path.join(file_path, "images\\slime.png")),]

##### NPC
father_slime_images = [pygame.image.load(os.path.join(file_path, "images\\father_slime.png"))]
coffin_images = [
    pygame.image.load(os.path.join(file_path, "design\\coffin_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\coffin_1.png"))
]
ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]


##### FIELD
stair_images = [
    pygame.image.load(os.path.join(file_path, "design\\stair_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\stair_1.png"))
]
web_image = pygame.image.load(os.path.join(file_path, "design\\web.png"))
water_images = [
    pygame.image.load(os.path.join(file_path, "design\\water_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\water_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\water_2.png"))
]
torch_images = [
    pygame.image.load(os.path.join(file_path, "design\\fire.png")),
]
light_image = pygame.image.load(os.path.join(file_path, "images\\light.png"))
light_image.set_alpha(80)


##### BACKGROUND
background_zero = pygame.image.load(os.path.join(file_path, "design\\0F.png"))


##### ITEM
potion_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_potion.png"))
coin_image = pygame.image.load(os.path.join(file_path, "design\\item\\coin.png"))
# coin_image = pygame.transform.rotozoom(coin_image, 0, 0.7)
box_image = pygame.image.load(os.path.join(file_path, "images\\box.png"))


# Punch Image
punch_d_image = pygame.image.load(os.path.join(file_path, "design\\punch.png"))


# Equip Image
battery_image = pygame.image.load(os.path.join(file_path, "design\\equips\\battery.png"))
banana_image = pygame.image.load(os.path.join(file_path, "images\\e_banana.png"))
pepper_image = pygame.image.load(os.path.join(file_path, "design\\equips\\pepper.png"))
ice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\ice_m.png"))
dice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\dice.png"))
sandclock_image = pygame.image.load(os.path.join(file_path, "images\\e_sandclock.png"))
apple_image = pygame.image.load(os.path.join(file_path, "images\\e_apple.png"))
greentea_image = pygame.image.load(os.path.join(file_path, "images\\e_greentea.png"))
mandoo_image = pygame.image.load(os.path.join(file_path, "images\\e_mandoo.png"))
a_book_image = pygame.image.load(os.path.join(file_path, "images\\e_a_book.png"))
bone_image = pygame.image.load(os.path.join(file_path, "images\\e_bone.png"))


# Others
story_images = [
    
]

tuto_images = [

]

shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png"))

sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png"))
cursor_images = [
    pygame.image.load(os.path.join(file_path, "images\\cursor.png")),
    pygame.image.load(os.path.join(file_path, "images\\cursor_is_picking.png"))
]
skill_c_image = pygame.image.load(os.path.join(file_path, "images\\skill_c.png"))
skill_v_image = pygame.image.load(os.path.join(file_path, "images\\skill_v.png"))


# 테스트 용
test_image = pygame.image.load(os.path.join(file_path, "images\\test_1.png"))
story_images = [
    pygame.image.load(os.path.join(file_path, "images\\test_0.png")),
    pygame.image.load(os.path.join(file_path, "images\\test_1.png")),
]

tuto_images = [
    pygame.image.load(os.path.join(file_path, "images\\test_0.png")),
    pygame.image.load(os.path.join(file_path, "images\\test_1.png")),
]