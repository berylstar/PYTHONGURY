import pygame
import os

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
##### SKEL
mon_skel_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\skel_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\skel_1.png")),
    ]
skel_atk_images = pygame.image.load(os.path.join(file_path, "design\\bone.png"))
skel_die = []

##### SPIDER
mon_spider_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_2.png")),
    ]
spider_atk_image = pygame.image.load(os.path.join(file_path, "design\\field\\web.png"))

##### BAT
mon_bat_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\bat_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\bat_1.png")),
    # pygame.image.load(os.path.join(file_path, "design\\monster\\bat_0.png")),
    ]
bat_die = []

##### FROG
mon_frog_images = [    
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_0.png")),
    ]
frog_die = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_x.png")),
]

##### EMBER
mon_ember_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ember_0.png")),
    ]
ember_atk_image = pygame.image.load(os.path.join(file_path, "design\\monster\\ember_attack.png"))

##### GHOST
mon_ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]

##### WEREWOLF
mon_werewolf_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_3.png")),
]
werewolf_die = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_x.png")),
]

##### SCARECROW
mon_scarecrow_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_1.png")),
]
crow_atk_image = pygame.image.load(os.path.join(file_path, "images\\crow.png"))
scarecrow_die = []

##### GOLEM
mon_golem_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_3.png")),
]
golem_die = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_x.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_x.png")),
]

##### FIRE BAT
mon_firebat_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\firebat_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\firebat_1.png")),
]
scarecrow_die = []
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
water_image.set_alpha(140)

torch_image = pygame.image.load(os.path.join(file_path, "design\\field\\torch.png"))
light_images = [
    pygame.image.load(os.path.join(file_path, "design\\field\\torch_light_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\torch_light_1.png"))
]

graveyard_deco = [
    pygame.image.load(os.path.join(file_path, "design\\field\\grass_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\grass_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\grass_3.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\grass_4.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\grass_5.png")),
]

portal_image = pygame.image.load(os.path.join(file_path, "images\\portal.png"))

##############################################################################################
##### ITEM
potion_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_potion.png"))
coin_image = pygame.image.load(os.path.join(file_path, "design\\item\\coin.png"))
redcoin_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_coin.png"))
box_image = pygame.image.load(os.path.join(file_path, "design\\item\\box.png"))

##############################################################################################
##### EQUIP
mushroom_image = pygame.image.load(os.path.join(file_path, "design\\equips\\mushroom.png"))
crescentmoon_image = pygame.image.load(os.path.join(file_path, "design\\equips\\crescentmoon.png"))
banana_image = pygame.image.load(os.path.join(file_path, "design\\equips\\banana.png"))
mandoo_image = pygame.image.load(os.path.join(file_path, "design\\equips\\mandoo.png"))
wax_image = pygame.image.load(os.path.join(file_path, "design\\equips\\wax.png"))
pepper_image = pygame.image.load(os.path.join(file_path, "design\\equips\\pepper.png"))
heartstone_image = pygame.image.load(os.path.join(file_path, "design\\equips\\heartstone.png"))
halfstone_image = pygame.image.load(os.path.join(file_path, "design\\equips\\halfstone.png"))
poisonapple_image = pygame.image.load(os.path.join(file_path, "design\\equips\\poisonapple.png"))
ice_images = [
    pygame.image.load(os.path.join(file_path, "design\\equips\\ice.png")),
    pygame.image.load(os.path.join(file_path, "design\\equips\\ice_m.png"))
]
battery_image = pygame.image.load(os.path.join(file_path, "design\\equips\\battery.png"))
rollerskate_image = pygame.image.load(os.path.join(file_path, "design\\equips\\rollerskate.png"))
gloves_image = pygame.image.load(os.path.join(file_path, "design\\equips\\gloves.png"))
helmet_image = pygame.image.load(os.path.join(file_path, "design\\equips\\helmet.png"))
turtleshell_image = pygame.image.load(os.path.join(file_path, "design\\equips\\turtleshell.png"))
pizza_image = pygame.image.load(os.path.join(file_path, "design\\equips\\pizza.png"))
sdglasses_image = pygame.image.load(os.path.join(file_path, "design\\equips\\3dglasses.png"))
talisman_image = pygame.image.load(os.path.join(file_path, "design\\equips\\talisman.png"))
ticket_image = pygame.image.load(os.path.join(file_path, "design\\equips\\ticket.png"))
straw_image = pygame.image.load(os.path.join(file_path, "design\\equips\\straw.png"))
machine_image = pygame.image.load(os.path.join(file_path, "design\\equips\\machine.png"))
piggybank_image = pygame.image.load(os.path.join(file_path, "design\\equips\\piggybank.png"))
metaldetector_image = pygame.image.load(os.path.join(file_path, "design\\equips\\metaldetector.png"))
binoculars_image = pygame.image.load(os.path.join(file_path, "design\\equips\\binoculars.png"))
trafficlight_image = pygame.image.load(os.path.join(file_path, "design\\equips\\trafficlight.png"))
thunder_image = pygame.image.load(os.path.join(file_path, "design\\equips\\thunder.png"))
dice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\dice.png"))
magiccloak_image = pygame.image.load(os.path.join(file_path, "design\\equips\\magiccloak.png"))
goldenkey_image = pygame.image.load(os.path.join(file_path, "design\\equips\\goldenkey.png"))
rope_image = pygame.image.load(os.path.join(file_path, "images\\equips\\rope.png"))

##############################################################################################
##### BACKGROUND
background_zero = pygame.image.load(os.path.join(file_path, "design\\floor\\0.png"))
background_sec = [
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_3.png"))
]

##############################################################################################
# ETC
title_image = pygame.image.load(os.path.join(file_path, "design\\etc\\title.png"))
cover_image = pygame.image.load(os.path.join(file_path, "images\\cover.png"))
story_images = [
    pygame.image.load(os.path.join(file_path, "design\\story\\00.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\01.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\02.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\03.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\04.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\05.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\06.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\07.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\08.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\09.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\10.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\11.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\12.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\13.png")),
]
shop_image = pygame.image.load(os.path.join(file_path, "design\\etc\\shop.png"))
sold_out_image = pygame.image.load(os.path.join(file_path, "design\\etc\\sold_out.png"))
treasurebox_image = pygame.image.load(os.path.join(file_path, "design\\etc\\treasurebox.png"))
inven_image = pygame.image.load(os.path.join(file_path, "design\\etc\\inven.png"))
cursor_images = [
    pygame.image.load(os.path.join(file_path, "design\\etc\\cursor.png")),
    pygame.image.load(os.path.join(file_path, "design\\etc\\cursor_is_picking.png"))
]
skill_c_image = pygame.image.load(os.path.join(file_path, "design\\etc\\skill_c.png"))
skill_v_image = pygame.image.load(os.path.join(file_path, "design\\etc\\skill_v.png"))

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

tuto_images = [
    pygame.image.load(os.path.join(file_path, "images\\test_0.png")),
    pygame.image.load(os.path.join(file_path, "images\\test_1.png")),
]

inven_img = pygame.image.load(os.path.join(file_path, "images\\inven.png"))
dummy = pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))

block_1 = pygame.image.load(os.path.join(file_path, "design\\block_1.png"))