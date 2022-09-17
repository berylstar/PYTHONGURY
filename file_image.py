import pygame
import os

# screen_width = 1280
# screen_height = 720
# screen = pygame.display.set_mode((screen_width, screen_height))

file_path = os.path.dirname(__file__)
##############################################################################################
##### PLAYER
player_images =[
    pygame.image.load(os.path.join(file_path, "design\\player\\main_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\main_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\main_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\main_1.png")),
]
player_damaged_image = pygame.image.load(os.path.join(file_path, "design\\player\\damaged_0.png"))
player_die_images = [
    pygame.image.load(os.path.join(file_path, "design\\player\\die_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\die_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\die_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\player\\die_2.png")),
]

punch_d_image = pygame.image.load(os.path.join(file_path, "design\\player\\punch.png"))

##############################################################################################
##### MONSTER
mon_skel_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\skel_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\skel_1.png")),
    ]

mon_spider_images = [
    
    ]

mon_bat_images = [
    
    ]

mon_frog_images = [
    
    ]

mon_ember_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ember_0.png")),
    ]
ember_attack_image = pygame.image.load(os.path.join(file_path, "design\\monster\\ember_attack.png"))

mon_ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]

##############################################################################################
##### NPC
father_slime_images = [
    pygame.image.load(os.path.join(file_path, "design\\npc\\kingslime_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\npc\\kingslime_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\npc\\kingslime_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\npc\\kingslime_1.png")),
]

coffin_images = [
    pygame.image.load(os.path.join(file_path, "design\\npc\\coffin_0.png")),
    # pygame.image.load(os.path.join(file_path, "design\\npc\\coffin_1.png"))
]

ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]

##############################################################################################
##### FIELD
stair_images = [
    pygame.image.load(os.path.join(file_path, "design\\field\\stair_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\stair_1.png"))
]

web_image = pygame.image.load(os.path.join(file_path, "design\\field\\web.png"))

water_image = pygame.image.load(os.path.join(file_path, "design\\field\\water_0.png"))

torch_image = pygame.image.load(os.path.join(file_path, "design\\field\\torch.png"))

light_images = [
    pygame.image.load(os.path.join(file_path, "images\\light.png")),
    pygame.image.load(os.path.join(file_path, "images\\light2.png"))
]
for l in light_images:
    l.set_alpha(80)

##############################################################################################
##### ITEM
potion_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_potion.png"))
coin_image = pygame.image.load(os.path.join(file_path, "design\\item\\coin.png"))
# coin_image = pygame.transform.rotozoom(coin_image, 0, 0.7)
box_image = pygame.image.load(os.path.join(file_path, "design\\item\\box.png"))

##############################################################################################
# Equip Image
trafficlight_image = pygame.image.load(os.path.join(file_path, "design\\equips\\trafficlight.png"))
banana_image = pygame.image.load(os.path.join(file_path, "design\\equips\\banana.png"))
straw_image = pygame.image.load(os.path.join(file_path, "design\\equips\\straw.png"))
battery_image = pygame.image.load(os.path.join(file_path, "design\\equips\\battery.png"))
pepper_image = pygame.image.load(os.path.join(file_path, "design\\equips\\pepper.png"))
ice_images = [
    pygame.image.load(os.path.join(file_path, "design\\equips\\ice.png")),
    pygame.image.load(os.path.join(file_path, "design\\equips\\ice_m.png"))
    ]
dice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\dice.png"))
heartstone_image = pygame.image.load(os.path.join(file_path, "design\\equips\\heartstone.png"))
thunder_image = pygame.image.load(os.path.join(file_path, "images\\equips\\thunder.png"))               ####
wax_image = pygame.image.load(os.path.join(file_path, "design\\equips\\wax.png"))
brokenstone_image = pygame.image.load(os.path.join(file_path, "design\\equips\\brokenstone.png"))
crescentmoon_image = pygame.image.load(os.path.join(file_path, "design\\equips\\crescentmoon.png"))
helmet_image = pygame.image.load(os.path.join(file_path, "images\\equips\\helmet.png"))                 ####
mushroom_image = pygame.image.load(os.path.join(file_path, "design\\equips\\mushroom.png"))             
pizza_image = pygame.image.load(os.path.join(file_path, "images\\equips\\pizza.png"))                   ####
gloves_image = pygame.image.load(os.path.join(file_path, "images\\equips\\gloves.png"))                 ####
turtleshell_image = pygame.image.load(os.path.join(file_path, "design\\equips\\turtleshell.png"))       
binoculars_image = pygame.image.load(os.path.join(file_path, "images\\equips\\binoculars.png"))         ####

##############################################################################################
##### BACKGROUND
background_zero = pygame.image.load(os.path.join(file_path, "design\\floor\\0F.png"))

##############################################################################################
# Others
title_image = pygame.image.load(os.path.join(file_path, "images\\title.png"))
cover_image = pygame.image.load(os.path.join(file_path, "images\\cover.png"))
story_images = [
    
]

tuto_images = [

]

# shop_image = pygame.image.load(os.path.join(file_path, "images\\shop.png"))

sold_out_image = pygame.image.load(os.path.join(file_path, "design\\sold_out.png"))
cursor_images = [
    pygame.image.load(os.path.join(file_path, "design\\cursor.png")),
    pygame.image.load(os.path.join(file_path, "design\\cursor_is_picking.png"))
]
skill_c_image = pygame.image.load(os.path.join(file_path, "design\\skill_c.png"))
skill_c_image = pygame.transform.rotozoom(skill_c_image, 0, 0.5)
skill_v_image = pygame.image.load(os.path.join(file_path, "design\\skill_v.png"))
skill_v_image = pygame.transform.rotozoom(skill_v_image, 0, 0.5)

##############################################################################################
# 테스트 용
player_icon = pygame.image.load(os.path.join(file_path, "design\\player\\main_1.png"))
monster_1_images = [pygame.image.load(os.path.join(file_path, "images\\monster_1.png"))]
monster_2_images = [pygame.image.load(os.path.join(file_path, "images\\monster_2.png"))]
monster_3_images = [pygame.image.load(os.path.join(file_path, "images\\monster_3.png"))]
monster_boss_images = [pygame.image.load(os.path.join(file_path, "images\\monster_boss.png"))]
runner_images = [pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))]
blind_image = pygame.image.load(os.path.join(file_path, "images\\blind.png"))
monster_die_images = [
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png")),
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png")),
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))
]

test_image = pygame.image.load(os.path.join(file_path, "images\\test_1.png"))
story_images = [
    pygame.image.load(os.path.join(file_path, "images\\test_0.png")),
    pygame.image.load(os.path.join(file_path, "images\\test_1.png")),
]

tuto_images = [
    pygame.image.load(os.path.join(file_path, "images\\test_0.png")),
    pygame.image.load(os.path.join(file_path, "images\\test_1.png")),
]