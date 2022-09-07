import pygame
import random

from class_equip import *
from class_character import *
from class_item import *
from class_field import *

from file_sound import *

from project_floor import *
##############################################################################################
def scene_title_game():
    global running, ready
    
    option = ["START", "OPTION", "EXIT"]
    color = [GRAY, GRAY, GRAY]
    index = 0

    while ready:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ready = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    index -= 1
                    if index < 0 :
                        index = 2
                if event.key == pygame.K_DOWN:
                    index += 1
                    if index > 2:
                        index = 0
                if event.key == pygame.K_SPACE:
                    if index == 0:
                        ready = False
                        scene_story(True)
                    elif index == 1:
                        scene_esc(True)
                    elif index == 2:
                        ready = False
                        running = False

        bgm_sound.play(-1)

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.fill((60,60,60))     # 타이틀 배경 이미지로 대체
        screen_message("SLIME PUNCH", GREEN, (screen_width//2,200), game_font_l)    # 타이틀 로고 이미지로 대체
        screen_message(option[0], color[0], (screen_width//2,500), game_font_m)
        screen_message(option[1], color[1], (screen_width//2,550), game_font_m)
        screen_message(option[2], color[2], (screen_width//2,600), game_font_m)
        pygame.display.update()
    
def display_info_ui():
    pygame.draw.rect(screen, BLACK, ((140,60), (200, 600)))     # 인포 이미지로 대체
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)
    screen_message(f"{floor} F", WHITE, (240,90), game_font_m)                              #FLOOR

    screen_message(f"HP: {int(player.hp)}", WHITE, (240,190), game_font_m)                  #HP

    coin_image_rect = coin_image.get_rect(center=(215, 290))
    screen.blit(coin_image, coin_image_rect)
    screen_message(f"       x{player.coin}", WHITE, (220,290), game_font_m)                 #COIN

    life_image_rect = player_icon.get_rect(center=(220, 390))
    screen.blit(player_icon, life_image_rect)
    screen_message(f"      x{player.life}", WHITE, (220,390), game_font_m)                  #LIFE

def display_inven_ui():
    pygame.draw.rect(screen, BLACK, ((940,60), (200, 600)))     # 인벤 이미지로 대체
    pygame.draw.rect(screen, WHITE, ((940,60), (200, 600)), 1) 
    for i in range(MAX_COL+2):
        pygame.draw.line(screen, D_GRAY, (950 + 60*i, 240), (950 + 60*i, 600))
    for i in range(MAX_ROW+2):
        pygame.draw.line(screen, D_GRAY, (950, 240 + 60*i), (1130, 240 + 60*i))
    pygame.draw.rect(screen, D_GRAY, ((950, 70), (180, 160)), 1)

    for equip in equip_con.equipped_group:
        equip.draw(screen)                                                                  #EQUIP

    if is_inven_overlapped(equip_con.equipped_group):
        screen_message("CHECK EQUIPS !", RED, (1040,150), game_font_s)

def scene_story(doing):
    global running

    index = 0
    fin = len(story_images)-1

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if index >= fin:
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        story_rect = story_images[index].get_rect(center=(screen_width//2, screen_height//2))

        screen.fill(BLACK)          # 스토리 배경 이미지로 대체 - 타이틀 배경 이미지도 가능
        screen.blit(story_images[index], story_rect)                                        #STORY IMAGE
        pygame.display.update()

def scene_tutorial(doing):
    global running

    index = 0
    fin = len(tuto_images)-1

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if index >= fin:
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        tuto_rect = tuto_images[index].get_rect(center=(640, 360))
        msg = "NEXT"
        if index >= fin:
            msg = "PRESS 'SPACE BAR' TO BACK"

        screen.blit(tuto_images[index], tuto_rect)                                          # TUTORIAL
        screen_message(msg, WHITE, (640,640), game_font_m)
        pygame.display.update(main_rect)

def scene_player_dead(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    doing = False
                    floor_zero()
                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        screen.blit(test_image, (340,60))      # 죽을 때 배경 이미지로 대체
        screen_message("YOU DIE", RED, (screen_width//2, screen_height//2), game_font_l)
        screen_message("PRESS 'R' TO GO 0F", WHITE, (640,640), game_font_m)
        pygame.display.update(main_rect)

def scene_game_over(doing):
    global running, ready

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doing = False
                    game_restart()
                    ready = True
                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        screen.fill(BLACK)      # 게임 오버 이미지로 대체 해도되고 그냥 검은 화면으로 해도 되고
        screen_message("GAME OVER", RED, (screen_width//2, screen_height//2), game_font_l)
        screen_message(f"REACHED AT {floor} FLOOR", WHITE, (screen_width//2, screen_height//2 + 50), game_font_m)
        screen_message("PRESS 'SPACE BAR' TO MAIN", WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_shop(doing):
    global running

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    equip_for_sale(0, equip_con.for_sale[0])

                if event.key == pygame.K_2:
                    equip_for_sale(1, equip_con.for_sale[1])

                if event.key == pygame.K_3:
                    equip_for_sale(2, equip_con.for_sale[2])

                if event.key == pygame.K_0:
                    if player.coin >= 4:
                        player.coin -= 4
                        random_for_sale()

                if event.key == pygame.K_SPACE:
                    doing = False
                    if is_inven_overlapped(equip_con.equipped_group):
                        scene_inventory(True)
                    else:
                        equip_effect()

                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        screen.blit(test_image, (340,60))      # 상점 이미지로 대체
        display_info_ui()
        display_inven_ui()

        shop_showcase(0, equip_con.for_sale[0])
        shop_showcase(1, equip_con.for_sale[1])
        shop_showcase(2, equip_con.for_sale[2])

        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)
        pygame.display.update()

def shop_showcase(index, equip):           # 상점 가판대 이미지로 대체
    sero = 350
    pygame.draw.rect(screen, WHITE, ((420 + 150*index,sero),(140,260)), 2)
    screen_message(str(index+1), WHITE, (490 + 150*index,sero+20), game_font_m)

    if equip_con.can_buy[index]:
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+40), (550 + 150*index, sero+40))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+100), (550 + 150*index, sero+100))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+160), (550 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (430 + 150*index, sero+40), (430 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (490 + 150*index, sero+40), (490 + 150*index, sero+160))
        pygame.draw.line(screen, GRAY, (550 + 150*index, sero+40), (550 + 150*index, sero+160))
        # equip_image = pygame.transform.rotozoom(equip.image, 0, 30/60)
        equip_rect = equip.image.get_rect(left=430 + 150*index, top=sero+40)
        screen.blit(equip.image, equip_rect)

        screen_message(equip.name, WHITE, (490 + 150*index, sero+185), game_font_s)

        coin_image_r = pygame.transform.rotozoom(coin_image, 0, 0.5)
        coin_rect = coin_image_r.get_rect(center=(470 + 150*index,sero+230))
        screen.blit(coin_image_r, coin_rect)

        screen_message(f"x{equip.price}", WHITE, (500 + 150*index, sero+230), game_font_m)
    else:
        case_rect = sold_out_image.get_rect(center=(490 + 150*index,sero+130))
        screen.blit(sold_out_image, case_rect)

def scene_inventory(doing):
    global running

    player.stop()

    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    cursor = Cursor(cursor_images[0], (980,270))
    picked_equip = None

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                running = False
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.clicking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i:
                    if not is_inven_overlapped(equip_con.equipped_group):
                        equip_effect()
                        doing = False

                if event.key == pygame.K_r:
                    if picked_equip:
                        remove_from_equipped_group(picked_equip)
                        cursor.clicking = False
                        cursor.image = cursor_images[0]
                        picked_equip = None

                if event.key == pygame.K_SPACE:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_images[0]
                        picked_equip = None

                    else:
                        for equip in equip_con.equipped_group:
                            if pygame.sprite.collide_mask(equip, cursor):
                                cursor.clicking = True
                                cursor.image = cursor_images[1]
                                picked_equip = equip

                if event.key == pygame.K_c:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_images[0]
                        setting_active_skill("c", picked_equip)
                        picked_equip = None

                if event.key == pygame.K_v:
                    if cursor.clicking:
                        cursor.clicking = False
                        cursor.image = cursor_images[0]
                        setting_active_skill("v", picked_equip)
                        picked_equip = None

                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)
                    doing = False

        display_inven_ui()

        if picked_equip and not is_inven_overlapped(equip_con.equipped_group):
            screen_message(picked_equip.msg_name, WHITE, (1040,90), game_font_m)
            screen_message(picked_equip.msg_info, WHITE, (1040,130), game_font_s)
            screen_message(picked_equip.msg_eff, WHITE, (1040,180), game_font_s)
    
        cursor.draw(screen)
        pygame.display.update(inven_rect)

def scene_treasure_box(doing):
    global running

    player.stop()
    choice = True
    if len(equip_con.able_equip_group) >= 2:
        choice_equip = [equip_con.able_equip_group[-1], equip_con.able_equip_group[-2]]

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if choice:
                    if event.key == pygame.K_1:
                        equip_con.equipped_group.append(choice_equip[0])
                        equip_con.able_equip_group.remove(choice_equip[0])
                        choice = False

                    if event.key == pygame.K_2:
                        equip_con.equipped_group.append(choice_equip[1])
                        equip_con.able_equip_group.remove(choice_equip[1])
                        choice = False

                if event.key == pygame.K_SPACE and not choice:
                    doing = False
                    if is_inven_overlapped(equip_con.equipped_group):
                        scene_inventory(True)
                    else:
                        equip_effect()

                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        screen.blit(test_image, (340,60))
        display_inven_ui()

        zero_rect = choice_equip[0].image.get_rect(center=(490,450))
        one_rect = choice_equip[1].image.get_rect(center=(790,450))
        
        if choice:          # 보물 상자 이미지 대체
            screen_message("<1>", WHITE, (490, 350), game_font_m)
            screen.blit(choice_equip[0].image, zero_rect)
            screen_message(choice_equip[0].name, WHITE, (490,550), game_font_m)

            screen_message("OR", WHITE, (640,450), game_font_m)

            screen_message("<2>", WHITE, (790, 350), game_font_m)
            screen.blit(choice_equip[1].image, one_rect)
            screen_message(choice_equip[1].name, WHITE, (790,550), game_font_m)

            screen_message("CHOICE ONE EQUIP !", WHITE, (640,640), game_font_m)
        else:
            screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)

        shop_rect = shop_image.get_rect(center=(640, 200))
        screen.blit(shop_image, shop_rect)      # 보물상자 이미지 대체
        
        pygame.display.update(main_rect)
        pygame.display.update(inven_rect)

def scene_esc(doing):
    global running

    option = ["RESUME", "TOGGLE SCREEN", "SOUND SETTING", "EXIT"]
    color = [GRAY, GRAY, GRAY, GRAY]
    index = 0

    player.stop()
    
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    index -= 1
                    if index < 0 :
                        index = 3
                if event.key == pygame.K_DOWN:
                    index += 1
                    if index > 3:
                        index = 0
                if event.key == pygame.K_SPACE:
                    if index == 0:
                        doing = False
                    elif index == 1:
                        pygame.display.toggle_fullscreen()
                        pygame.display.update()
                    elif index == 2:
                        pass
                    elif index == 3:
                        doing = False
                        running = False
                if event.key == pygame.K_ESCAPE:
                    doing = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.fill((60,60,60))     # ESC 이미지로 대체

        screen_message(option[0], color[0], (screen_width//2, 480), game_font_m)
        screen_message(option[1], color[1], (screen_width//2, 530), game_font_m)
        screen_message(option[2], color[2], (screen_width//2, 580), game_font_m)
        screen_message(option[3], color[3], (screen_width//2, 630), game_font_m)

        pygame.display.update(main_rect)

##############################################################################################
def screen_message(writing, color, position, font):
    msg = font.render(writing, True, color)
    msg_rect = msg.get_rect(center=position)
    screen.blit(msg, msg_rect)

def game_restart():
    global player, saved_floor
    global item_con, equip_con, skill_con, monster_con

    player = Player(player_images, player_first_position)
    make_floor_zero()
    saved_floor = 1

    item_con = ItemController()
    equip_con = EquipController()
    skill_con = SkillController()
    monster_con = MonsterController()

def make_floor_zero():
    global floor

    floor = 0
    monster_group.empty()
    shooting_group.empty()
    item_group.empty()
    field_group.empty()
    stair.image = stair_images[0]
    stair.rect = stair.image.get_rect(center=stair_zero_floor)
    random_for_sale()
    player.rect = player.image.get_rect(center=player_first_position)
    player.hp = player.max_hp

def floor_zero():
    if floor != 0:
        make_floor_zero()

    torch.draw(screen)
    npc_group.draw(screen)

    for punch in punch_group:
        if pygame.sprite.collide_mask(punch, npc_kingslime):
            player.stop()
            scene_tutorial(True)

        if pygame.sprite.collide_mask(punch, npc_coffin):
            player.stop()
            scene_shop(True)

def next_floor(pos):
    global floor

    floor += 1

    if floor % 10 == 0:
        player.hp += 10

    item_group.empty()

    stair.image = stair_images[1]

    floor_setting(pos, floor)

    # if equip_battery in equip_con.equipped_group:
    #     if floor - equip_battery.floor == 2:
    #         print("충전")
    #         player.speed += 0.1
    #         equip_battery.floor = floor


def display_background(floor):
    if floor >= 0:
        background = background_zero
    else:
        background = None

    screen.blit(background, (340,60))

def show_animation():
    player.image_update()
    for npc in npc_group:
        npc.image_update()
    for monster in monster_group:
        monster.image_update()

def random_for_sale():
    random.shuffle(equip_con.able_equip_group)

    total_number = min(len(equip_con.able_equip_group), len(equip_con.for_sale))

    for i in range(total_number):
        equip_con.for_sale[i] = equip_con.able_equip_group[i]
        equip_con.can_buy[i] = True

def equip_for_sale(index, equip):
    if equip_con.can_buy[index] and player.coin >= equip.price:
        equip_con.equipped_group.append(equip)
        player.coin -= equip.price
        equip_con.can_buy[index] = False
        equip_con.able_equip_group.remove(equip)

def player_move_key():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.to[0] -= player.speed
            player.direction = "LEFT"
        if event.key == pygame.K_RIGHT:
            player.to[1] += player.speed
            player.direction = "RIGHT"
        if event.key == pygame.K_UP:
            player.to[2] -= player.speed
            player.direction = "UP"
        if event.key == pygame.K_DOWN:
            player.to[3] += player.speed
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

def monster_move():
    if monster_group:
        for monster in monster_group:
            if monster.direction == "LEFT":
                monster.move(-monster.speed, 0, fps)
            elif monster.direction == "RIGHT":
                monster.move(monster.speed, 0, fps)
            elif monster.direction == "UP":
                monster.move(0,-monster.speed, fps)
            elif monster.direction == "DOWN":
                monster.move(0,monster.speed, fps)

def drop_item(monster):
    randprob = random.randrange(0,101)
    # position = put_on_pixel(position)

    if monster.type == "boss":
        item_group.add(Item(box_image, monster.position, "box"))
    else:
        if randprob <= item_con.prob_potion:
            item_group.add(Item(potion_image, monster.position, "potion"))
        elif item_con.prob_potion < randprob <= item_con.prob_potion + item_con.prob_coin:
            item_group.add(Item(coin_image, monster.position, "coin"))

# def put_on_pixel(position):
#     x = position[0]
#     y = position[1]

#     x_ahrt = x // 60
#     x_skajwl = round((x % 60) / 60)

#     y_ahrt = y // 60
#     y_skajwl = round((y % 60) / 60)

#     fin_x = (x_ahrt + x_skajwl) * 60 + 10
#     fin_y = (y_ahrt + y_skajwl) * 60 + 30

#     pixel_position = (fin_x,fin_y)

#     return pixel_position

def item_effect(item):
    if item.info == "potion":
        player.hp = min(player.hp + item_con.potion_eff, player.max_hp)
    if item.info == "coin":
        player.coin += 1
    if item.info == "box":
        scene_treasure_box(True)

def equip_effect():
    if equip_pepper in equip_con.equipped_group:
        if not equip_pepper.is_effected:
            player.ap += 3            
            equip_pepper.is_effected = True

    if equip_ice in equip_con.equipped_group:
        if not equip_ice.is_effected:
            player.speed += 0.1
            equip_ice.is_effected = True

    if equip_dice in equip_con.equipped_group:
        if not equip_dice.is_effected:
            item_con.prob_coin += 5
            equip_dice.is_effected = True

    if equip_apple in equip_con.equipped_group:
        if not equip_apple.is_effected:
            big_punch_image = pygame.transform.scale(punch_d_image, (90,90))
            player.punch = big_punch_image
            equip_apple.is_effected = True

    if equip_mandoo in equip_con.equipped_group:
        if not equip_mandoo.is_effected:
            player.life += 1
            equip_mandoo.is_effected = True

    if equip_ancientbook in equip_con.equipped_group:
        if not equip_ancientbook.is_effected:
            player.damaged_time -= 0.5
            equip_ancientbook.is_effected = True

    if equip_bone in equip_con.equipped_group:
        if not equip_bone.is_effected:
            player.ap += 0.1
            equip_bone.is_effected = True

    ######
    if equip_straw in equip_con.equipped_group:
        if not equip_straw.is_effected:
            item_con.potion_eff += 5
            equip_straw.is_effected = True

    if equip_battery in equip_con.equipped_group:
        if not equip_battery.is_effected:
            player.speed += 0.1
            equip_battery.floor = floor
            print(floor)
            equip_battery.is_effected = True

def remove_from_equipped_group(equip):
    if equip == equip_pepper:
        player.ap -= 3

    elif equip == equip_ice:
        player.speed -= 0.1

    elif equip == equip_dice:
        item_con.prob_coin -= 5

    elif equip == equip_apple:
        player.punch = punch_d_image

    # not remove effect mandoo

    elif equip == equip_ancientbook:
        player.damaged_time += 0.5

    elif equip == equip_bone:
        player.ap += 0.1

    #####
    if equip == equip_straw:
        item_con.potion_eff -= 5
        equip_straw.is_effected = False

    elif equip == equip_battery:
        player.speed -= 0.1
        equip_battery.is_effected = False

    equip_con.equipped_group.remove(equip)
    equip_con.able_equip_group.append(equip)

def setting_active_skill(key, picked_equip):
    if key == "c":
        for equip in equip_con.equipped_group:
            equip.is_active_c = False
        picked_equip.is_active_c = True
        picked_equip.is_active_v = False
        player.equip_c = picked_equip
        if player.equip_v == player.equip_c:
            player.equip_v = None

    if key == "v":
        for equip in equip_con.equipped_group:
            equip.is_active_v = False
        picked_equip.is_active_c = False
        picked_equip.is_active_v = True
        player.equip_v = picked_equip
        if player.equip_c == player.equip_v:
            player.equip_c = None

def monster_shooting():
    randprob = random.randrange(0,101)

    for monster in monster_group:
        if monster.type == "boss" or monster.type == "shooter":
            if 0 <= randprob <= 70:
                if monster.direction == "LEFT":
                    image = ember_attack_image
                elif monster.direction == "RIGHT":
                    image = pygame.transform.flip(ember_attack_image, True, False)
                elif monster.direction == "UP":
                    image = pygame.transform.rotozoom(ember_attack_image, 270, 1)
                elif monster.direction == "DOWN":
                    image = pygame.transform.rotozoom(ember_attack_image, 90, 1)
                else:
                    break
                shooting_group.add(Punch(image, monster.position, monster.direction))

def monster_clocking():
    randprob = random.randrange(0,101)

    for monster in monster_group:
        if monster.type == "alpha":
            if 0 <= randprob <= 50:
                for image in monster.image_group:
                    image.set_alpha(60)
            elif 80 < randprob:
                for image in monster.image_group:
                    image.set_alpha(255)

def monster_dash():
    randprob = random.randrange(0,101)

    for monster in monster_group:
        if monster.type == "runner":
            if 0 <= randprob <= 30:
                monster.speed += 0.4
                monster.curr_dir = monster.direction

            if monster.curr_dir and not monster.curr_dir == monster.direction:
                monster.speed -= 0.4
                monster.curr_dir = None

def monster_die(monster):
    # monster.image_group = monster.die_images
    # if monster.image == monster.die_images[-1]:
    #     drop_item(monster)
    if monster.type == "slime":
        pass
    else:
        drop_item(monster)
    monster_group.remove(monster)

def effect_field(field):
    if pygame.sprite.collide_mask(field, player):
        if field.image == web_image and not field.is_activated:
            player.stop()
            player.speed /= 2
            field.is_activated = pygame.time.get_ticks()

    else:
        if field.is_activated and (pygame.time.get_ticks() - field.is_activated) > 3000:
            player.speed *= 2
            field.is_activated = 0


##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image_group, position):
        Character.__init__(self, image_group, position)

        self.is_die = False

        self.life = 3
        self.hp = 100
        self.coin = 99

        self.equip_c = None
        self.equip_v = None

        self.ap = 10
        self.max_hp = 100
        self.speed = 0.3
        self.punch = punch_d_image
        self.damaged_enemy = 0.7
        self.damaged_time = 1

    def space_bar(self):
        punch_sound.play()
        image = self.punch

        if self.direction == "LEFT":
            position = (self.rect.centerx-40, self.rect.centery)
        elif self.direction == "RIGHT":
            image = pygame.transform.flip(image, True, False)
            position = (self.rect.centerx+40, self.rect.centery)
        elif self.direction == "UP":
            image = pygame.transform.rotozoom(image, 270, 1)
            position = (self.rect.centerx, self.rect.centery-40)
        elif self.direction == "DOWN":
            image = pygame.transform.rotozoom(image, 90, 1)
            position = (self.rect.centerx, self.rect.centery+40)

        punch_group.add(Punch(image, position, self.direction))
    
    def skill_c(self):
        if self.equip_c:
            self.equip_c.active_skill(player)
    
    def skill_v(self):
        if self.equip_v:
            self.equip_v.active_skill(player)

    def die_motion(self):
        flag = True
        # while flag:
        self.image = player_die_images[0].convert_alpha()
        self.draw(screen)
        pygame.display.update(self.rect)
        pygame.time.delay(1000)

        self.image = player_die_images[1].convert_alpha()
        self.draw(screen)
        pygame.display.update(self.rect)
        pygame.time.delay(1000)

        self.image = player_die_images[2].convert_alpha()
        self.draw(screen)
        pygame.display.update(self.rect)
        pygame.time.delay(1000)

        if self.life <= 0:
            flag = False
            scene_game_over(True)
        else:
            flag = False
            scene_player_dead(True)

#### PUNCH CLASS
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
        if self.rect.right < 340 or 940 < self.rect.left or self.rect.bottom < 60 or 660 < self.rect.top:
            pass
        else:
            screen.blit(self.image, self.rect)

    def shoot(self):
        if self.direction == "LEFT":
            self.rect.x -= 5
        elif self.direction == "RIGHT":
            self.rect.x += 5
        elif self.direction == "UP":
            self.rect.y -= 5
        elif self.direction == "DOWN":
            self.rect.y += 5
        elif self.direction == "NONE":
            pass

        if self.rect.left < 340 or 940 < self.rect.right or self.rect.top < 60 or 660 < self.rect.bottom:
            shooting_group.remove(self)
##############################################################################################
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("No More Slime")
clock = pygame.time.Clock()
game_font_s = pygame.font.Font("fonts\\DungGeunMo.ttf", 20)
game_font_m = pygame.font.Font("fonts\\DungGeunMo.ttf", 30)
game_font_l = pygame.font.Font("fonts\\DungGeunMo.ttf", 50)
start_ticks = pygame.time.get_ticks()
a_counter = 0
b_counter = 0

#### GAME SYSTEM
WHITE = (255,255,255)
D_GRAY = (64,64,64)
GRAY = (127,127,127)
BLACK = (0,0,0)
RED = (127,0,0)
GREEN = (0,127,0)
BLUE = (0,0,127)
floor = 0
saved_floor = 1

##### PLAYER
player_first_position = (700, 360)
player = Player(player_images, player_first_position)

punch_group = pygame.sprite.Group()

##### MONSTER
shooting_group = pygame.sprite.Group()

main_rect = pygame.Rect(((340,60), (600, 600)))
info_rect = pygame.Rect(((140,60), (200, 600)))
inven_rect = pygame.Rect(((940,60), (200, 600)))
full_rect = pygame.Rect((140,60), (1000,600))

##############################################################################################
ready = True
running = True
random_for_sale()
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
                player.skill_c()
            if event.key == pygame.K_v:
                player.skill_v()
            if event.key == pygame.K_i:
                scene_inventory(True)
            if event.key == pygame.K_ESCAPE:
                scene_esc(True)

        if not player.is_die:
            player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3], fps)
    
    screen.fill(BLACK)      # 메인 배경 이미지로 대체
    display_background(floor)                                                           #BACKGROUND
    field_group.draw(screen)                                                            #FIELD

    milli_time = int((pygame.time.get_ticks() - start_ticks) / 500)
    if a_counter != milli_time:
        #for 0.4 second
        show_animation()
        skill_con.active_time()
    a_counter = milli_time

    if floor == 0:
        bgm_sound.stop()
        floor_zero()      

    elif floor > 0:
        second_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if b_counter != second_time:
            #for 1 second
            # if monster_group:
            player.hp -= player.damaged_time
            
            if not skill_con.active_sandclock[0]:
                random_monster_direction()
                # forward_monster_direction(player)
                monster_shooting()
                monster_clocking()
                monster_dash()

            # skill_con.active_time()
        b_counter = second_time

        if monster_con.dontmove:
            monster_con.dontmove = False

        if not skill_con.active_sandclock[0]:
            monster_move()

    if not monster_group:
        stair.draw(screen)                                                              #STAIR

        if pygame.sprite.collide_mask(player, stair):
            # if saved_floor and floor == 0:
            if floor == 0:
                scene_treasure_box(True)
                floor = saved_floor - 1
            next_floor(player.position)

    for monster in monster_group:
        monster.draw(screen)                                                           #MONSTER
        if pygame.sprite.collide_mask(player, monster):
            player.hp -= player.damaged_enemy
            if not player.is_die:
                player.image = player_damaged_image

    for punch in punch_group:
        if not player.is_die:
            punch.draw(screen)                                                         #PUNCH

        if punch.get_time() > 2 * fps:
            punch_group.remove(punch)

        for monster in monster_group:
            if pygame.sprite.collide_mask(monster, punch):
                punch_group.remove(punch)
                monster.hp -= player.ap
                if monster.hp <= 0:
                    monster_die(monster)
                    if len(monster_group) == 0:
                        random_away_position(player.position, stair)

    for shoot in shooting_group:
        shoot.shoot()
        shoot.draw(screen)                                                              #MONSTER SHOOING
        if pygame.sprite.collide_mask(shoot, player):
            player.hp -= 5
            if not player.is_die:
                player.image = player_damaged_image
            shooting_group.remove(shoot)

    for item in item_group:
        item.draw(screen)                                                               #ITEM
        if pygame.sprite.collide_mask(item, player):
            if item.info == "box":
                if len(monster_group):
                    continue
            item_effect(item)
            item_group.remove(item)

    for field in field_group:
        effect_field(field)

    # GAME OVER
    if player.hp <= 0:
        player.hp = 0
        display_info_ui()
        player.stop()
        if not player.is_die:
            player.life -= 1
            saved_floor = floor
            player.is_die = True
            player.i_i = 0
            player.image_group = player_die_images
        else:
            if player.image == player_die_images[3]:
                pygame.time.delay(2000)
                player.image_group = player_images
                player.is_die = False
                if player.life <= 0:
                    scene_game_over(True)
                else:
                    scene_player_dead(True)

        # player.die_motion()

    # blind_rect = blind_image.get_rect(center=player.position)
    # screen.blit(blind_image, blind_rect)          # 시야 제한 구현 가능
    player.draw(screen)                                                                 #PLAYER

    # 배경 껍데기 이미지 필요함 - 펀치 나가는거 안보이는 용도
    display_info_ui()
    display_inven_ui()

    if running: 
        pygame.display.update()

pygame.quit()