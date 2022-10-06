import pygame
import os

file_path = os.path.dirname(__file__)
##############################################################################################
dummy = pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))
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
    # pygame.image.load(os.path.join(file_path, "design\\monster\\skel_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\skel_3.png")),
    ]
skel_atk_images = pygame.transform.rotozoom(pygame.image.load(os.path.join(file_path, "design\\monster\\skel_atk.png")), 0, 0.5)
skel_x = pygame.image.load(os.path.join(file_path, "design\\monster\\skel_x.png"))
skel_die = [skel_x, skel_x, skel_x]

##### SPIDER
mon_spider_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\spider_2.png")),
    ]
spider_atk_image = pygame.transform.rotozoom(pygame.image.load(os.path.join(file_path, "design\\field\\web.png")), 0, 0.5)
spider_x = pygame.image.load(os.path.join(file_path, "design\\monster\\spider_x.png"))
spider_die = [spider_x, spider_x, spider_x]

##### BAT
mon_bat_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\bat_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\bat_1.png")),
    ]
blind_image = pygame.image.load(os.path.join(file_path, "design\\etc\\blind.png"))
bat_x = pygame.image.load(os.path.join(file_path, "design\\monster\\bat_x.png"))
bat_die = [bat_x, bat_x, bat_x]

##### FROG
mon_frog_images = [    
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\frog_0.png")),
    ]
frog_x = pygame.image.load(os.path.join(file_path, "design\\monster\\frog_x.png"))
frog_die = [frog_x, frog_x, frog_x]
#########################
##### ZOMBIE
mon_zombie_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\zombie_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\zombie_1.png")),
    # pygame.image.load(os.path.join(file_path, "design\\monster\\zombie_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\zombie_3.png")),
]
zombie_x = pygame.image.load(os.path.join(file_path, "design\\monster\\zombie_x.png"))
zombie_die = [zombie_x, zombie_x, zombie_x]

##### GHOST
mon_ghost_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_1.png")),
]
ghost_x = pygame.image.load(os.path.join(file_path, "design\\monster\\ghost_x.png"))
ghost_die = [ghost_x, ghost_x, ghost_x]

##### WEREWOLF
mon_werewolf_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_3.png")),
]
werewolf_x = pygame.image.load(os.path.join(file_path, "design\\monster\\werewolf_x.png"))
werewolf_die = [werewolf_x, werewolf_x, werewolf_x]

##### SCARECROW
mon_scarecrow_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_1.png")),
]
crow_atk_image = pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_atk.png"))
scarecrow_x = pygame.image.load(os.path.join(file_path, "design\\monster\\scarecrow_x.png"))
scarecrow_die = [scarecrow_x, scarecrow_x, scarecrow_x]

#########################
##### GOLEM
mon_golem_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\golem_3.png")),
]
golem_x = pygame.image.load(os.path.join(file_path, "design\\monster\\golem_x.png"))
golem_die = [golem_x, golem_x, golem_x]

##### EMBER
mon_ember_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\ember_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ember_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\ember_2.png")),
    ]
fire_atk_image = pygame.image.load(os.path.join(file_path, "design\\monster\\ember_atk.png"))
ember_x = pygame.image.load(os.path.join(file_path, "design\\monster\\ember_x.png"))
ember_die = [ember_x, ember_x, ember_x]

##### FLAME SNAKE
mon_flamesnake_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\flamesnake_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\flamesnake_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\flamesnake_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\flamesnake_1.png")),
    ]
flamesnake_x = pygame.image.load(os.path.join(file_path, "design\\monster\\flamesnake_x.png"))
flamesnake_die = [flamesnake_x, flamesnake_x, flamesnake_x]

##### FIRE BAT
mon_firebat_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\firebat_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\firebat_1.png")),
]
firebat_x = pygame.image.load(os.path.join(file_path, "design\\monster\\firebat_x.png"))
firebat_die = [firebat_x, firebat_x, firebat_x]

##### WITCH
mon_witch_images = [
    dummy,
    dummy,
]
witch_x = dummy
witch_die = [witch_x, witch_x, witch_x]

##### BOOK
mon_book_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\book_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\book_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\book_2.png")),
]
book_x = pygame.image.load(os.path.join(file_path, "design\\monster\\book_x.png"))
book_die = [book_x, book_x, book_x]

##### MAGICIAN
mon_magician_images = [
    dummy,
    dummy,
    dummy,
]
magician_atk_image = dummy
magician_x = dummy
magician_die = [magician_x, magician_x, magician_x]

##### CANDLE
mon_candle_images = [
    pygame.image.load(os.path.join(file_path, "design\\monster\\candle_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\candle_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\monster\\candle_2.png")),
]
candle_x = pygame.image.load(os.path.join(file_path, "design\\monster\\candle_x.png"))
candle_die = [candle_x, candle_x, candle_x]

monster_die_images = [
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png")),
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png")),
    pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))
]

##### DEVIL
devil_images =[
    dummy,
    dummy,
    dummy
]
devil_x = dummy
devil_die = [devil_x, devil_x, devil_x, devil_x, devil_x]
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
    pygame.image.load(os.path.join(file_path, "design\\field\\grass.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\gravestone.png")),
]

portal_image = pygame.image.load(os.path.join(file_path, "images\\portal.png"))

lava_images = [
    pygame.image.load(os.path.join(file_path, "design\\field\\lava_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\lava_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\field\\lava_3.png")),
]

##############################################################################################
##### ITEM
potion_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_potion.png"))
coin_image = pygame.image.load(os.path.join(file_path, "design\\item\\coin.png"))
redcoin_image = pygame.image.load(os.path.join(file_path, "design\\item\\red_coin.png"))
box_image = pygame.image.load(os.path.join(file_path, "design\\item\\box.png"))
coins_image = pygame.image.load(os.path.join(file_path, "design\\item\\coins.png"))

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
ice_image = pygame.image.load(os.path.join(file_path, "design\\equips\\ice.png"))
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
skelhead_image = pygame.image.load(os.path.join(file_path, "design\\equips\\skeleton.png"))

##############################################################################################
##### BACKGROUND
background_zero = pygame.image.load(os.path.join(file_path, "design\\floor\\0_0.png"))
background_first = [
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\1_3.png"))
]
background_second = [
    pygame.image.load(os.path.join(file_path, "design\\floor\\2_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\2_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\2_3.png"))
]
background_third = [
    pygame.image.load(os.path.join(file_path, "design\\floor\\3_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\3_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\floor\\3_3.png"))
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

ending_images = [
    pygame.image.load(os.path.join(file_path, "design\\story\\e_01.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_02.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_03.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_04.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_05.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_06.png")),
    pygame.image.load(os.path.join(file_path, "design\\story\\e_07.png")),
]

player_blue_images = [
    pygame.image.load(os.path.join(file_path, "design\\ending\\blue_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\blue_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\blue_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\blue_1.png")),
]
blue_die_images = [
    pygame.image.load(os.path.join(file_path, "design\\ending\\die_0.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\die_1.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\die_2.png")),
    pygame.image.load(os.path.join(file_path, "design\\ending\\die_2.png")),
]
blue_inven = pygame.image.load(os.path.join(file_path, "design\\ending\\inven.png"))
blue_punch = pygame.image.load(os.path.join(file_path, "design\\ending\\blue_punch.png"))
##############################################################################################
# 테스트 용
player_icon = pygame.image.load(os.path.join(file_path, "design\\player\\main_1.png"))
monster_1_images = [pygame.image.load(os.path.join(file_path, "images\\monster_1.png"))]
monster_2_images = [pygame.image.load(os.path.join(file_path, "images\\monster_2.png"))]
monster_3_images = [pygame.image.load(os.path.join(file_path, "images\\monster_3.png"))]
monster_boss_images = [pygame.image.load(os.path.join(file_path, "images\\monster_boss.png"))]
runner_images = [pygame.image.load(os.path.join(file_path, "design\\skeleton.png"))]


test_image = pygame.image.load(os.path.join(file_path, "images\\test_1.png"))

