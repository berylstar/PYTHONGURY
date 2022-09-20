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

    if ready:
        sound_con.play_bgm(bgm_title)
    while ready:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ready = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0 :
                        index = 2
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > 2:
                        index = 0
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 0:
                        ready = False
                        sound_con.stop_bgm(bgm_title)
                        scene_story(True)
                    elif index == 1:
                        scene_esc(True)
                    elif index == 2:
                        ready = False
                        running = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen_message("SLIME PUNCH", GREEN, (screen_width//2,200), game_font_l)    # 타이틀 로고 이미지로 대체
        screen_message(option[0], color[0], (screen_width//2,500), game_font_m)
        screen_message(option[1], color[1], (screen_width//2,550), game_font_m)
        screen_message(option[2], color[2], (screen_width//2,600), game_font_m)
        pygame.display.update()

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
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0:
                        index = 3
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > 3:
                        index = 0
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 0:
                        doing = False
                    elif index == 1:
                        pygame.display.toggle_fullscreen()
                        pygame.display.update()
                    elif index == 2:
                        scene_sound_setting(True)
                    elif index == 3:
                        doing = False
                        running = False
                        pygame.quit()
                if event.key == pygame.K_ESCAPE:
                    doing = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen_message(option[0], color[0], (screen_width//2, 480), game_font_m)
        screen_message(option[1], color[1], (screen_width//2, 530), game_font_m)
        screen_message(option[2], color[2], (screen_width//2, 580), game_font_m)
        screen_message(option[3], color[3], (screen_width//2, 630), game_font_m)

        pygame.display.update()

def scene_sound_setting(doing):
    global running

    
    color = [GRAY, GRAY, GRAY, GRAY]
    index = 0

    while doing:
        option = ["BGM : {0:.1f}".format(sound_con.bgm_volume), "EFFECT : {0:.1f}".format(sound_con.effect_volume), "ALL MUTE", "RETURN"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0:
                        index = 3
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > 3:
                        index = 0

                if event.key == pygame.K_LEFT:
                    if index == 0:
                        sound_con.bgm_volume = max(sound_con.bgm_volume-0.1, 0)
                        sound_con.bgm.set_volume(sound_con.bgm_volume)
                    elif index == 1:
                        sound_con.effect_volume = max(sound_con.effect_volume-0.1, 0)
                if event.key == pygame.K_RIGHT:
                    if index == 0:
                        sound_con.bgm_volume = min(sound_con.bgm_volume+0.1, 1)
                        sound_con.bgm.set_volume(sound_con.bgm_volume)
                    elif index == 1:
                        sound_con.effect_volume = min(sound_con.effect_volume+0.1, 1)
                    
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 2:
                        sound_con.bgm_volume = 0
                        sound_con.effect_volume = 0
                    elif index == 3:
                        doing = False
                if event.key == pygame.K_ESCAPE:
                    doing = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen_message(option[0], color[0], (screen_width//2, 480), game_font_m)
        screen_message(option[1], color[1], (screen_width//2, 530), game_font_m)
        screen_message(option[2], color[2], (screen_width//2, 580), game_font_m)
        screen_message(option[3], color[3], (screen_width//2, 630), game_font_m)

        pygame.display.update()
    
def display_info_ui():
    pygame.draw.rect(screen, BLACK, ((140,60), (200, 600)))     # 인포 이미지로 대체
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)
    screen_message(f"{floor}F", WHITE, (240,90), game_font_l)                              #FLOOR

    screen_message(f"HP: {int(player.hp)}/{player.max_hp}", WHITE, (240,190), game_font_m)                  #HP

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
    # pygame.draw.rect(screen, D_GRAY, ((950, 70), (180, 160)), 1)

    for equip in equip_con.equipped_group:
        equip.draw(screen)                                                                  #EQUIP

    if is_inven_overlapped(equip_con.equipped_group):
        screen_message("장비 확인 !", RED, (1040,150), game_font_s)

def scene_story(doing):
    global running

    index = 0
    fin = len(story_images)-1

    sound_con.play_bgm(bgm_story)
    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_page)
                    if index >= fin:
                        sound_con.stop_bgm(bgm_story)
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    scene_esc(True)

        story_rect = story_images[index].get_rect(center=(screen_width//2, screen_height//2))

        screen.fill(BLACK)          # 스토리 배경 이미지로 대체 - 타이틀 배경 이미지나 검은화면도 가능
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
        display_info_ui()
        display_inven_ui()
        pygame.display.update(full_rect)

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

    picked_num = 0

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if picked_num == 1:
                        purchase_equip(0)
                        sound_con.play_sound(sound_shop_buy)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[0]:
                            picked_num = 1

                if event.key == pygame.K_2:
                    if picked_num == 2:
                        purchase_equip(1)
                        sound_con.play_sound(sound_shop_buy)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[1]:
                            picked_num = 2

                if event.key == pygame.K_3:
                    if picked_num == 3:
                        purchase_equip(2)
                        sound_con.play_sound(sound_shop_buy)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[2]:
                            picked_num = 3

                if event.key == pygame.K_0:
                    if player.coin >= 0:
                        player.coin -= 0
                        random_for_sale()

                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    doing = False
                    if is_inven_overlapped(equip_con.equipped_group):
                        scene_inventory(True)
                    else:
                        equip_effect()

        screen.blit(test_image, (340,60))      # 상점 이미지로 대체
        display_info_ui()
        display_inven_ui()

        if picked_num:
            screen_message(equip_con.for_sale[picked_num-1].msg_name, WHITE, (640,90), game_font_m)
            screen_message(equip_con.for_sale[picked_num-1].msg_info, WHITE, (640,130), game_font_kor)
            screen_message(equip_con.for_sale[picked_num-1].msg_eff, YELLOW, (640,180), game_font_kor)

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

    inven_img.set_alpha(180)
    screen.blit(inven_img, (340,60))

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                running = False
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.clicking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i or event.key == pygame.K_ESCAPE:
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

        display_inven_ui()

        screen_message(f"AP : {player.ap}", WHITE, (640,100), game_font_s)
        screen_message(f"DP : {player.dp}", WHITE, (640,130), game_font_s)
        screen_message(f"SPEED : {player.speed}", WHITE, (640,160), game_font_s)
        screen_message(f"TIME DAMAGE : {player.damaged_time}", WHITE, (640,190), game_font_s)

        screen_message(f"POTION EFF : {item_con.potion_eff}", WHITE, (640,270), game_font_s)
        screen_message(f"POTION PROB : {item_con.prob_potion}%", WHITE, (640,300), game_font_s)
        screen_message(f"COIN PROB : {item_con.prob_coin}%", WHITE, (640,330), game_font_s)

        screen_message(f"SHOP RARE : {equip_con.perc_rare}%", WHITE, (640,390), game_font_s)
        screen_message(f"SHOP UNIQUE : {equip_con.perc_unique}%", WHITE, (640,420), game_font_s)
        
        

        if picked_equip and not is_inven_overlapped(equip_con.equipped_group):
            screen_message(picked_equip.msg_name, WHITE, (1040,90), game_font_m)
            screen_message(picked_equip.msg_info, WHITE, (1040,130), game_font_kor)
            screen_message(picked_equip.msg_eff, YELLOW, (1040,180), game_font_kor)
            screen_message(picked_equip.msg_eff_2, YELLOW, (1040,200), game_font_kor)

        screen_message("PRESS 'I' TO BACK", WHITE, (640,640), game_font_m)
    
        cursor.draw(screen)
        pygame.display.update(full_rect)

def scene_treasure_box(doing):
    global running

    player.stop()
    choice = True

    if len(equip_con.normal_equips) >= 2:
        choice_equip = [equip_con.normal_equips[-1], equip_con.normal_equips[-2]]
    else:
        doing  = False

    picked_num = 0

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                doing = False
            if event.type == pygame.KEYDOWN:
                if choice:
                    if event.key == pygame.K_1:
                        if picked_num == 1:
                            equip_con.equipped_group.append(choice_equip[0])
                            equip_con.normal_equips.remove(choice_equip[0])
                            choice = False
                            picked_num = 0
                        else:
                            picked_num = 1

                    if event.key == pygame.K_2:
                        if picked_num == 2:
                            equip_con.equipped_group.append(choice_equip[1])
                            equip_con.normal_equips.remove(choice_equip[1])
                            choice = False  
                            picked_num = 0
                        else:
                            picked_num = 2

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

        if picked_num:
            screen_message(choice_equip[picked_num-1].msg_name, WHITE, (640,90), game_font_m)
            screen_message(choice_equip[picked_num-1].msg_info, WHITE, (640,130), game_font_kor)
            screen_message(choice_equip[picked_num-1].msg_eff, YELLOW, (640,180), game_font_kor)
        
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
        
        pygame.display.update(main_rect)
        pygame.display.update(inven_rect)

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
    equip_reset()
    saved_floor = 1

    item_con = ItemController()
    equip_con = EquipController()
    skill_con = SkillController()
    monster_con = MonsterController()
    # sound_con = SoundController()
    random_for_sale()

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

    if not skill_con.active_escaperope:
        player.hp = player.max_hp
    else:
        skill_con.active_escaperope = False

def floor_zero():
    global floor

    sound_con.play_bgm(bgm_0f)

    if floor != 0:
        make_floor_zero()

    for deco in deco_group:
        deco.draw(screen)
    for npc in npc_group:
        npc.draw(screen)

    for punch in punch_group:
        if pygame.sprite.collide_mask(punch, npc_kingslime):
            player.stop()
            scene_tutorial(True)

        if pygame.sprite.collide_mask(punch, npc_coffin):
            player.stop()
            scene_shop(True)

    if pygame.sprite.collide_mask(player, stair):
        # scene_treasure_box(True)
        floor = saved_floor - 1

def next_floor(pos):
    global floor

    floor += 1

    if floor % 10 == 0:
        player.hp += 10

    item_group.empty()
    shooting_group.empty()

    stair.image = stair_images[1]

    monster_setting(pos, floor)
    random_field_setting()

    if e_battery in equip_con.equipped_group and e_battery.charge_times < 3:
        if floor - e_battery.floor >= 1:
            print("충전중" + str(e_battery.charge_times))
            player.speed += 0.05
            e_battery.floor = floor
            e_battery.charge_times += 1
            # 충전됨에 따라 배터리 이미지도 바꾸기

    if e_ice in equip_con.equipped_group and e_ice.charge_times < 3:
        if floor - e_ice.floor >= 1:
            print("녹는중" + str(e_ice.charge_times))
            player.speed -= 0.05
            e_ice.floor = floor
            e_ice.charge_times += 1
            if e_ice.charge_times == 2:
                remove_from_equipped_group(e_ice)
            # 녹음에 따라 얼음 이미지도 바꾸기

    if e_crescentmoon in equip_con.equipped_group:
        e_crescentmoon.prob_revival()

    e_goldenkey.target = floor

def display_background(floor):
    if floor >= 0:
        background = background_zero
    else:
        background = None

    screen.blit(background, (340,60))

def show_animation():
    player.image_update()
    for deco in deco_group:
        deco.image_update()
    for npc in npc_group:
        npc.image_update()
    for monster in monster_group:
        monster.image_update()

def random_for_sale():
    random.shuffle(equip_con.normal_equips)
    random.shuffle(equip_con.rare_equips)
    random.shuffle(equip_con.unique_equips)

    normal_index = 0
    rare_index = 0
    unique_index = 0

    for i in range(3):
        percent = random.randrange(1,101)

        if percent <= equip_con.perc_rare:
            if rare_index >= len(equip_con.rare_equips):
                pass
            else:
                equip_con.for_sale[i] = equip_con.rare_equips[rare_index]
                rare_index += 1
        elif (100 - equip_con.perc_unique) <= percent:
            if unique_index >= len(equip_con.unique_equips):
                pass
            else:
                equip_con.for_sale[i] = equip_con.unique_equips[unique_index]
                unique_index += 1
        else:
            equip_con.for_sale[i] = equip_con.normal_equips[normal_index]
            normal_index += 1

        equip_con.can_buy[i] = True

def purchase_equip(index):
    equip = equip_con.for_sale[index]
    if equip_con.can_buy[index] and player.coin >= equip.price:
        equip_con.equipped_group.append(equip)
        player.coin -= equip.price
        equip_con.can_buy[index] = False
        equip_con.for_sale[index] = None

        if equip.grade == 0:
            equip_con.normal_equips.remove(equip)
        elif equip.grade == 1:
            equip_con.rare_equips.remove(equip)
        elif equip.grade == 2:
            equip_con.unique_equips.remove(equip)

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

def drop_item(monster):
    randprob = random.randrange(1,101) # 1~100
    # position = put_on_pixel(position)

    if monster.type == "boss":
        item_group.add(Item(box_image, monster.position, "box"))
    else:
        if randprob <= item_con.prob_potion: # 확률 <= 포션드롭률
            item_group.add(Item(potion_image, monster.position, "potion"))
        elif (100 - item_con.prob_coin) < randprob: # 100-코인드롭률 <= 확률
            if item_con.red_coin and 98 < randprob:
                item_group.add(Item(redcoin_image, monster.position, "red_coin"))
            else:
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
    elif item.info == "coin":
        player.coin += 1
    elif item.info == "red_coin":
        player.coin += 3
    elif item.info == "box":
        scene_treasure_box(True)

def equip_effect():
    # mushroom
    # crescentmoon
    # banana

    if e_wax in equip_con.equipped_group:
        if not e_wax.is_effected:
            player.ap += 2
            e_wax.is_effected = True

    if e_pepper in equip_con.equipped_group:
        if not e_pepper.is_effected:
            player.ap += 3            
            e_pepper.is_effected = True

    if e_heartstone in equip_con.equipped_group:
        if not e_heartstone.is_effected:
            player.max_hp += 20
            e_heartstone.is_effected = True

    if e_halfstone in equip_con.equipped_group:
        if not e_halfstone.is_effected:
            player.max_hp += 10
            e_halfstone.is_effected = True

    if e_ice in equip_con.equipped_group:
        if not e_ice.is_effected:
            player.speed += 0.1
            e_ice.floor = floor
            e_ice.is_effected = True

    if e_battery in equip_con.equipped_group:
        if not e_battery.is_effected:
            e_battery.floor = floor
            e_battery.is_effected = True

    if e_rollerskate in equip_con.equipped_group:
        if not e_rollerskate.is_effected:
            player.speed += 0.1
            e_rollerskate.is_effected = True

    if e_boxerglove in equip_con.equipped_group:
        if not e_boxerglove.is_effected:
            big_punch_image = pygame.transform.scale(punch_d_image, (90,90))
            player.punch = big_punch_image
            e_boxerglove.is_effected = True

    if e_helmet in equip_con.equipped_group:
        if not e_helmet.is_effected:
            player.dp += 0.2
            e_helmet.is_effected = True

    if e_turtleshell in equip_con.equipped_group:
        if not e_turtleshell.is_effected:
            player.damaged_time -= 0.3
            e_turtleshell.is_effected = True

    if e_pizza in equip_con.equipped_group:
        if not e_pizza.is_effected:
            monster_con.b_speed -= 2
            e_pizza.is_effected = True

    if e_3dglasses in equip_con.equipped_group:
        if not e_3dglasses.is_effected:
            monster_con.dont_alpha = True
            e_3dglasses.is_effected = True

    if e_talisman in equip_con.equipped_group:
        if not e_talisman.is_effected:
            monster_con.dont_dash = True
            e_talisman.is_effected = True

    if e_ticket in equip_con.equipped_group:
        if not e_ticket.is_effected:
            equip_con.perc_rare += 5
            e_ticket.is_effected = True

    if e_straw in equip_con.equipped_group:
        if not e_straw.is_effected:
            item_con.potion_eff += 5
            e_straw.is_effected = True

    if e_machine in equip_con.equipped_group:
        if not e_machine.is_effected:
            item_con.prob_potion += 3
            e_machine.is_effected = True

    if e_piggybank in equip_con.equipped_group:
        if not e_piggybank.is_effected:
            item_con.red_coin = True
            e_piggybank.is_effected = True

    if e_metaldetector in equip_con.equipped_group:
        if not e_metaldetector.is_effected:
            item_con.prob_coin += 3
            e_metaldetector.is_effected = True

    if e_binoculars in equip_con.equipped_group:
        if not e_binoculars.is_effected:
            item_con.prob_potion += 3
            item_con.prob_coin += 3
            e_binoculars.is_effected = True

    # trafficlight
    # thunder
    # dice
    # magiccloak
    # goldenkey
    # rope

def remove_from_equipped_group(equip):
    global e_mushroom, e_crescentmoon, e_banana, e_wax, e_pepper, e_heartstone, e_halfstone, e_ice, e_battery, e_rollerskate
    global e_boxerglove, e_helmet, e_turtleshell, e_pizza, e_3dglasses, e_talisman
    global e_ticket, e_straw, e_machine, e_piggybank, e_metaldetector, e_binoculars, e_trafficlight, e_thunder, e_dice
    global e_magiccloak, e_goldenkey, e_escaperope

    equip_con.equipped_group.remove(equip)
    if equip.is_active_c:
        player.equip_c = None
    elif equip.is_active_v:
        player.equip_v = None
        
    # if equip == e_mushroom:
    #     e_mushroom = E_Mushroom()

    # elif equip == e_crescentmoon:
    #     e_crescentmoon = E_CrescentMoon()

    # elif equip == e_banana:
    #     e_banana = E_Banana()

    elif equip == e_wax:
        player.ap -= 2
        # e_wax = E_Wax()

    elif equip == e_pepper:
        player.ap -= 3
        # e_pepper = E_Pepper()

    elif equip == e_heartstone:
        player.max_hp -= 20
        player.hp = min(player.hp, player.max_hp)
        # e_heartstone = E_HeartStone()

    elif equip == e_halfstone:
        player.max_hp -= 10
        player.hp = min(player.hp, player.max_hp)
        # e_halfstone = E_HalfStone()

    elif equip == e_ice:
        if e_ice.charge_times == 0:
            player.speed -= 0.1
        elif e_ice.charge_times == 1:
            player.speed -= 0.05
        # e_ice = E_Ice()

    elif equip == e_battery:
        player.speed -= 0.1 * e_battery.charge_times
        e_battery.charge_times = 0
        # e_battery = E_Battery()

    elif equip == e_rollerskate:
        player.speed -= 0.1
        # e_rollerskate = E_RollerSkate()

    elif equip == e_boxerglove:
        player.punch = punch_d_image
        # e_boxerglove = E_BoxerGlove()
    
    elif equip == e_helmet:
        player.dp -= 0.2
        # e_helmet = E_Helmet()

    elif equip == e_turtleshell:
        player.damaged_time += 0.3
        # e_turtleshell = E_TurtleShell()

    elif equip == e_pizza:
        monster_con.b_speed += 2
        # e_pizza = E_Pizza()

    elif equip == e_3dglasses:
        monster_con.dont_alpha = False
        # e_3dglasses = E_3DGlasses()

    elif equip == e_talisman:
        monster_con.dont_dash = False
        # e_talisman = E_Talisman()

    elif equip == e_ticket:
        equip_con.perc_rare -= 5
        # e_ticket = E_Ticket()

    elif equip == e_straw:
        item_con.potion_eff -= 5
        # e_straw = E_Straw()

    elif equip == e_machine:
        item_con.prob_potion -= 3
        # e_machine = E_Machine()
    
    elif equip == e_piggybank:
        item_con.red_coin = False
        # e_piggybank = E_PiggyBank()

    elif equip == e_metaldetector:
        item_con.prob_coin -= 3
        # e_metaldetector = E_MetalDetector()

    elif equip == e_binoculars:
        item_con.prob_potion -= 3
        item_con.prob_coin -= 3
        # e_binoculars = E_Binoculars()

    # elif equip == e_trafficlight:
    #     e_trafficlight = E_TrafficLight()

    # elif equip == e_thunder:
    #     e_thunder = E_Thunder()
    
    # elif equip == e_dice:
    #     e_dice = E_Dice()

    # elif equip == e_magiccloak:
    #     e_magiccloak = E_MagicCloak()
    
    # elif equip == e_goldenkey:
    #     e_goldenkey = E_GoldenKey()

    # elif equip == e_escaperope:
    #     e_escaperope = E_EscapeRope()

    equip.reset()

    if equip.grade == 0:
        equip_con.normal_equips.append(equip)
    elif equip.grade == 1:
        equip_con.rare_equips.append(equip)
    elif equip.grade == 2:
        equip_con.unique_equips.append(equip)    

    print(f"remove + {equip}")
    print(equip.is_active_c)
    print(equip.is_active_v)

def setting_active_skill(key, picked_equip):
    if key == "c" and picked_equip.active:
        for equip in equip_con.equipped_group:
            equip.is_active_c = False
        picked_equip.is_active_c = True
        picked_equip.is_active_v = False
        player.equip_c = picked_equip
        if player.equip_v == player.equip_c:
            player.equip_v = None

    if key == "v" and picked_equip.active:
        for equip in equip_con.equipped_group:
            equip.is_active_v = False
        picked_equip.is_active_c = False
        picked_equip.is_active_v = True
        player.equip_v = picked_equip
        if player.equip_c == player.equip_v:
            player.equip_c = None

def monster_move():
    if monster_group:
        for monster in monster_group:
            if not monster.is_die:
                if monster.direction == "LEFT":
                    monster.move(-monster.speed, 0, fps)
                elif monster.direction == "RIGHT":
                    monster.move(monster.speed, 0, fps)
                elif monster.direction == "UP":
                    monster.move(0,-monster.speed, fps)
                elif monster.direction == "DOWN":
                    monster.move(0,monster.speed, fps)

def monster_action():
    randprob = random.randrange(1,101)

    for monster in monster_group:
        if not monster.is_die:
            if monster.type == "shooter":
                if 0 <= randprob <= 70:
                    if monster.direction == "LEFT":
                        image = monster.bullet
                    elif monster.direction == "RIGHT":
                        image = pygame.transform.flip(monster.bullet, True, False)
                    elif monster.direction == "UP":
                        image = pygame.transform.rotozoom(monster.bullet, 270, 1)
                    elif monster.direction == "DOWN":
                        image = pygame.transform.rotozoom(monster.bullet, 90, 1)
                    else:
                        break
                    shooting_group.add(Bullet(image, monster.position, monster.direction, monster.b_speed, monster.b_damage))

            if monster.type == "alpha":
                if 0 <= randprob <= 50 and not monster_con.dont_alpha:
                    for image in monster.image_group:
                        image.set_alpha(60)
                elif 80 < randprob or monster_con.dont_alpha:
                    for image in monster.image_group:
                        image.set_alpha(255)

            if monster.type == "runner" and not monster_con.dont_dash:
                if 0 <= randprob <= 30:
                    monster.speed += 0.4
                    monster.curr_dir = monster.direction

                if monster.curr_dir and (not monster.curr_dir == monster.direction):
                    monster.speed -= 0.4
                    monster.curr_dir = None

def monster_die(monster):
    if not monster.is_die:
        monster.is_die = True
        monster.change_image_group(monster_die_images)
    if monster.i_i == 2:    #마지막 인덱스
        drop_item(monster)
        monster_group.remove(monster)

    # if monster.type == "slime":
    #     pass
    # else:
    #     drop_item(monster)
    # monster_group.remove(monster)

def field_effect(field):
    global saved_floor

    if pygame.sprite.collide_mask(field, player):
        if field.image == web_image and not field.is_activated:
            player.stop()

        # if field.image == rope_field_image:
        #     player.stop()
        #     saved_floor = floor
        #     floor_zero()

        # if field.image == keys_field_image:
        #     player.stop()
        #     monster_group.empty()
        #     shooting_group.empty()
        #     item_group.empty()
        #     field_group.empty()
        #     next_floor(player.position)

##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image_group, position):
        Character.__init__(self, image_group, position)

        self.life = 3
        self.hp = 100
        self.coin = 888
        self.ap = 10
        self.max_hp = 100
        self.speed = 0.3
        self.punch = punch_d_image
        self.dp = 0
        self.damaged_time = 1

        self.equip_c = None
        self.equip_v = None

    def space_bar(self):
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
            self.equip_c.active_skill()
    
    def skill_v(self):
        if self.equip_v:
            self.equip_v.active_skill()

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

#### SHOOTING CLASS
class Bullet(Punch):
    def __init__(self, image, position, direction, speed, damage):
        Punch.__init__(self, image, position, direction)
        self.speed = max((speed + monster_con.b_speed), 0)
        self.damage = damage

    def shoot(self):
        if not skill_con.active_trafficlight[0]:
            if self.direction == "LEFT":
                self.rect.x -= self.speed
            elif self.direction == "RIGHT":
                self.rect.x += self.speed
            elif self.direction == "UP":
                self.rect.y -= self.speed
            elif self.direction == "DOWN":
                self.rect.y += self.speed
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
game_font_kor = pygame.font.Font("fonts\\DungGeunMo.ttf", 15)
game_font_s = pygame.font.Font("fonts\\DungGeunMo.ttf", 20)
game_font_m = pygame.font.Font("fonts\\DungGeunMo.ttf", 30)
game_font_l = pygame.font.Font("fonts\\DungGeunMo.ttf", 60)
start_ticks = pygame.time.get_ticks()
a_counter = 0
b_counter = 0

#### GAME SYSTEM
WHITE = (255,255,255)
D_GRAY = (64,64,64)
GRAY = (127,127,127)
BLACK = (0,0,0)
RED = (127,0,0)
GREEN = (0,255,0)
BLUE = (0,0,127)
YELLOW = (255,255,0)
floor = 0
saved_floor = 1

main_rect = pygame.Rect(((340,60), (600, 600)))
info_rect = pygame.Rect(((140,60), (200, 600)))
inven_rect = pygame.Rect(((940,60), (200, 600)))
full_rect = pygame.Rect((140,60), (1000,600))


##### PLAYER
player_first_position = (700, 360)
player = Player(player_images, player_first_position)

punch_group = pygame.sprite.Group()

##### MONSTER
shooting_group = pygame.sprite.Group()

##### EQUIP
e_banana.target = player
e_dice.target = player
e_thunder.target = monster_group
e_magiccloak.target = player
##############################################################################################
ready = True
running = True
random_for_sale()
while running:
    fps = clock.tick(30)

    scene_title_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene_esc(True)

            if not player.is_die:
                if event.key == pygame.K_SPACE:
                    player.space_bar()
                if event.key == pygame.K_c and floor > 0:
                    player.skill_c()
                if event.key == pygame.K_v and floor > 0:
                    player.skill_v()
                if event.key == pygame.K_i:
                    scene_inventory(True)

        if not player.is_die:
            player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3], fps)
    
    display_background(floor)                                                           #BACKGROUND

    milli_time = int((pygame.time.get_ticks() - start_ticks) / 500)
    if a_counter != milli_time:
        #for 0.5 second
        show_animation()
        skill_con.active_time()
    a_counter = milli_time

    if floor == 0:
        floor_zero()      

    elif floor > 0:
        sound_con.stop_bgm(bgm_0f)
        sound_con.play_bgm(bgm_first)

        second_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if b_counter != second_time:
            #for 1 second
            player.hp -= player.damaged_time
            
            if not skill_con.active_trafficlight[0]:
                random_monster_direction()
                # forward_monster_direction(player)
                monster_action()
        b_counter = second_time

        if monster_con.dontmove:
            monster_con.dontmove = False

        if not skill_con.active_trafficlight[0]:
            monster_move()

    for field in field_group:
        field.draw(screen)                                                              #FIELD
        field_effect(field)

    if not monster_group:
        stair.draw(screen)                                                              #STAIR

        if pygame.sprite.collide_mask(player, stair):
            next_floor(player.position)

    for monster in monster_group:
        monster.draw(screen)                                                           #MONSTER
        if pygame.sprite.collide_mask(player, monster) and not monster.is_die:
            player.hp -= max((monster.ap - player.dp), 0)
            if not player.is_die:
                player.image = player_damaged_image
        if monster.hp <= 0:
            monster_die(monster)
            if len(monster_group) == 0:
                random_away_position(player.position, stair)

    for punch in punch_group:
        if not player.is_die:
            punch.draw(screen)                                                         #PUNCH

        if punch.get_time() > 2 * fps:
            punch_group.remove(punch)

        for monster in monster_group:
            if pygame.sprite.collide_mask(monster, punch):
                punch_group.remove(punch)
                monster.hp -= player.ap

    for bullet in shooting_group:
        bullet.shoot()
        bullet.draw(screen)                                                              #MONSTER SHOOING
        if pygame.sprite.collide_mask(bullet, player):
            player.hp -= bullet.damage
            if not player.is_die:
                player.image = player_damaged_image
            shooting_group.remove(bullet)

    for item in item_group:
        item.draw(screen)                                                               #ITEM
        if pygame.sprite.collide_mask(item, player):
            if item.info == "box":
                if len(monster_group):
                    continue
            item_effect(item)
            item_group.remove(item)

    # GAME OVER
    if player.hp <= 0:
        if e_crescentmoon.revival:
            player.hp = player.max_hp
            e_crescentmoon.prob_revival()
        else:
            player.hp = 0
            player.stop()
            if not player.is_die:
                saved_floor = floor
                player.is_die = True
                player.change_image_group(player_die_images)
        
    if player.image == player_die_images[3]:
        sound_con.stop_bgm(bgm_first)
        pygame.time.delay(2000)
        player.image_group = player_images
        player.is_die = False
        player.life -= 1
        
        if player.life <= 0 and e_mushroom in equip_con.equipped_group:
            player.life += 1
            remove_from_equipped_group(e_mushroom)
            scene_player_dead(True)
        elif player.life <= 0:
            scene_game_over(True)
        else:
            scene_player_dead(True)

    # blind_rect = blind_image.get_rect(center=player.position)
    # screen.blit(blind_image, blind_rect)          # 시야 제한 구현 가능
    player.draw(screen)                                                                 #PLAYER

    screen.blit(cover_image, (0,0))
    display_info_ui()
    display_inven_ui()
    
    if running: 
        pygame.display.update()

pygame.quit()