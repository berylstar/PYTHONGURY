import pygame
import random
import sys

from class_equip import *
from class_character import *
from class_item import *
from class_field import *

from file_sound import *

from project_floor import *
##############################################################################################
def scene_title_game():
    global ready
    
    option = ["START", "OPTION", "EXIT"]
    color = [GRAY, GRAY, GRAY]
    index = 0

    if ready:
        if not sound_con.bgm == bgm_title:
            sound_con.play_bgm(bgm_title)

    while ready:
        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen.blit(title_logo, (screen_width//2-title_logo.get_width()//2,100))
        screen_message_3(option[0], color[0], (screen_width//2,500), game_font_m)
        screen_message_3(option[1], color[1], (screen_width//2,550), game_font_m)
        screen_message_3(option[2], color[2], (screen_width//2,600), game_font_m)
        screen.blit(team_logo, (900,600))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0 :
                        index = len(option)-1
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > len(option)-1:
                        index = 0
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 0:
                        ready = False
                        if not game_con.ending:
                            scene_story(True)
                        else:
                            game_restart()
                    elif index == 1:
                        scene_esc(True)
                    elif index == 2:
                        scene_exit(True)
                if event.key == pygame.K_ESCAPE:
                    scene_exit(True)

def scene_esc(doing):
    global ready

    option = ["RESUME", "HELP", "TOGGLE SCREEN", "SOUND SETTING", "RESTART", "EXIT"]
    color = [GRAY, GRAY, GRAY, GRAY, GRAY, GRAY]
    index = 0

    player.stop()
    
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0:
                        index = len(option)-1
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > len(option)-1:
                        index = 0
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 0:
                        doing = False
                        pygame.display.update()
                    elif index == 1:
                        doing = False
                        scene_help(True)
                    elif index == 2:
                        pygame.display.toggle_fullscreen()
                        pygame.display.update()
                    elif index == 3:
                        scene_sound_setting(True)
                    elif index == 4:
                        doing = False
                        game_restart()
                    elif index == 5:
                        scene_exit(True)
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    doing = False
                    pygame.display.update()

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen.blit(title_logo, (screen_width//2-title_logo.get_width()//2,100))
        screen_message_3(option[0], color[0], (screen_width//2, 380), game_font_m)
        screen_message_3(option[1], color[1], (screen_width//2, 430), game_font_m)
        screen_message_3(option[2], color[2], (screen_width//2, 480), game_font_m)
        screen_message_3(option[3], color[3], (screen_width//2, 530), game_font_m)
        screen_message_3(option[4], color[4], (screen_width//2, 580), game_font_m)
        screen_message_3(option[5], color[5], (screen_width//2, 630), game_font_m)
        screen.blit(team_logo, (900,600))

        pygame.display.update()

def scene_sound_setting(doing):
    
    color = [GRAY, GRAY, GRAY, GRAY]
    index = 0

    while doing:
        option = ["BGM : {0:.1f}".format(sound_con.bgm_volume), "EFFECT : {0:.1f}".format(sound_con.effect_volume), "ALL MUTE", "RETURN"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sound_con.play_sound(sound_wasd)
                    index -= 1
                    if index < 0:
                        index = len(option)-1
                if event.key == pygame.K_DOWN:
                    sound_con.play_sound(sound_wasd)
                    index += 1
                    if index > len(option)-1:
                        index = 0
                if event.key == pygame.K_LEFT:
                    if index == 0:
                        sound_con.bgm_volume = max(sound_con.bgm_volume-0.1, 0)
                        sound_con.bgm.set_volume(sound_con.bgm_volume)
                    elif index == 1:
                        sound_con.effect_volume = max(sound_con.effect_volume-0.1, 0)
                        sound_con.play_sound(sound_wasd)
                if event.key == pygame.K_RIGHT:
                    if index == 0:
                        sound_con.bgm_volume = min(sound_con.bgm_volume+0.1, 1)
                        sound_con.bgm.set_volume(sound_con.bgm_volume)
                    elif index == 1:
                        sound_con.effect_volume = min(sound_con.effect_volume+0.1, 1)
                        sound_con.play_sound(sound_wasd)
                if event.key == pygame.K_SPACE:
                    if index == 2:
                        sound_con.play_sound(sound_pick)
                        sound_con.bgm_volume = 0
                        sound_con.bgm.set_volume(sound_con.bgm_volume)
                        sound_con.effect_volume = 0
                    elif index == 3:
                        sound_con.play_sound(sound_pick)
                        doing = False
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    doing = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.blit(title_image, (0,0))
        screen.blit(title_logo, (screen_width//2-title_logo.get_width()//2,100))
        screen_message_3(option[0], color[0], (screen_width//2, 480), game_font_m)
        screen_message_3(option[1], color[1], (screen_width//2, 530), game_font_m)
        screen_message_3(option[2], color[2], (screen_width//2, 580), game_font_m)
        screen_message_3(option[3], color[3], (screen_width//2, 630), game_font_m)
        screen.blit(team_logo, (900,600))

        pygame.display.update()

def scene_exit(doing):
    global running

    exit_rect = pygame.Rect((520,310),(240,100))

    option = ["YES", "NO"]
    color = [GRAY, GRAY]
    index = 0

    sound_con.play_sound(sound_exit)

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sound_con.play_sound(sound_wasd)
                    index = 0
                if event.key == pygame.K_RIGHT:
                    sound_con.play_sound(sound_wasd)
                    index = 1
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    if index == 0:
                        sys.exit()
                    elif index == 1:
                        doing = False
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    doing = False

        for i in range(len(color)):
            color[i] = GRAY
        color[index] = GREEN

        screen.fill(BLACK)
        screen_message("EXIT THE GAME", WHITE, (640,335), game_font_m)
        screen_message(option[0], color[0], (590,385), game_font_m)
        screen_message(option[1], color[1], (690,385), game_font_m)
        pygame.display.update(exit_rect)
    
def display_info_ui():
    pygame.draw.rect(screen, BLACK, ((140,60), (200, 600)))
    pygame.draw.rect(screen, WHITE, ((140,60), (200, 600)), 1)
    screen_message(f"{game_con.floor}F", WHITE, (240,90), game_font_l)                              #FLOOR

    screen_message(f"HP: {int(player.hp)}/{player.max_hp}", WHITE, (240,190), game_font_m)                  #HP

    coin_image_rect = coin_image.get_rect(center=(215, 290))
    screen.blit(coin_image, coin_image_rect)
    screen_message(f"       x{player.coin}", WHITE, (220,290), game_font_m)                 #COIN

    life_image_rect = player_icon.get_rect(center=(220, 390))
    screen.blit(player_icon, life_image_rect)
    screen_message(f"      x{player.life}", WHITE, (220,390), game_font_m)                  #LIFE
    
def display_inven_ui():
    pygame.draw.rect(screen, BLACK, ((940,60), (200, 600)))
    screen.blit(inven_image, (940,60))

    for equip in equip_con.equipped_group:
        equip.draw(screen)                                                                  #EQUIP

    if is_inven_overlapped(equip_con.equipped_group):
        screen_message("?????? ?????? !", RED, (1040,220), game_font_s)

def scene_story(doing):

    index = 0
    fin = len(story_images)-1

    sound_con.play_bgm(bgm_story)
    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_page)
                    if index >= fin:
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    scene_esc(True)

        screen.fill(BLACK)

        if -1 < index < 3 :
            screen.blit(story_images[0], (200,100))
            if index > 0:
                screen.blit(story_images[1], (680,50))
                if index > 1:
                    screen.blit(story_images[2], (680,300))
        elif index == 3:
            screen.blit(story_images[3], (240,80))
        elif 3 < index < 7:
            screen.blit(story_images[4], (200,100))
            if index > 4:
                screen.blit(story_images[5], (680,50))
                if index > 5:
                    screen.blit(story_images[6], (680,300))
        elif index == 7:
            screen.blit(story_images[7], (240,80))
        elif 7 < index < 11:
            screen.blit(story_images[8], (200,100))
            if index > 8:
                screen.blit(story_images[9], (680,50))
                if index > 9:
                    screen.blit(story_images[10], (680,300))
        elif index == 11:
            screen.blit(story_images[11], (240,80))
        elif 11 < index:
            screen.blit(story_images[12], (100,50))
            if 12 < index:
                screen.blit(story_images[13], (400,100))
        
        pygame.display.update()

def scene_help(doing):

    index = 0
    fin = len(help_images)-1

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_page)
                    if index >= fin:
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    scene_esc(True)

        screen.fill(BLACK)

        screen.blit(help_images[index], (-50,136))
        if index == 0:
            screen_message_2("1. ?????? ??????", WHITE, (700, 50), game_font_m)
            screen_message_2("?????? : ???????????????", WHITE, (700, 200), game_font_s)
            screen_message_2("       ??????, HP, ??????, ?????? ??????", WHITE, (700, 230), game_font_s)
            screen_message_2("?????? : ?????? ?????? ??????", WHITE, (700, 290), game_font_s)
            screen_message_2("????????? : ????????????", WHITE, (700, 350), game_font_s)
            screen_message_2("         ????????? ?????? ??????", WHITE, (700, 380), game_font_s)
        elif index == 1:
            screen_message_2("2. ?????? ??????", WHITE, (700, 50), game_font_m)
            screen_message_2("???????????? : ?????????", WHITE, (700, 200), game_font_s)
            screen_message_2("'?????????' - ??????", WHITE, (700, 260), game_font_s)
            screen_message_2("'???????????? ???' - ??????", WHITE, (700, 320), game_font_s)
            screen_message_2("'??????' : ?????? ??? ????????????", WHITE, (700, 350), game_font_s)
            screen_message_2("'C' or 'V' : ????????? ?????? ??????", WHITE, (700, 410), game_font_s)
            screen_message_2("             ?????? ????????? ?????????????????? ???????????????.", WHITE, (700, 440), game_font_s)
        elif index == 2:
            screen_message_2("3. ??????", WHITE, (700, 50), game_font_m)
            screen_message_2("'1' or '2' or '3' - ?????? ??????", WHITE, (700, 200), game_font_s)
            screen_message_2("                    ????????? ?????? ?????? / ?????? ", WHITE, (700, 230), game_font_s)
            screen_message_2("                    ?????? / ????????? / ?????? ??????", WHITE, (700, 260), game_font_s)
            screen_message_2("                    ?????? ??? ?????? ??????", WHITE, (700, 290), game_font_s)
            screen_message_2("'R' - ?????? ????????????", WHITE, (700, 350), game_font_s)
            screen_message_2("      ?????? 1??? ??????", WHITE, (700, 380), game_font_s)
            screen_message_2("'???????????? ???' - ?????? ?????????", WHITE, (700, 440), game_font_s)
        elif index == 3:
            screen_message_2("4. ????????????", WHITE, (700, 50), game_font_m)
            screen_message_2("'1' or '2' - ?????? ??????", WHITE, (700, 200), game_font_s)
            screen_message_2("             ?????? ??????", WHITE, (700, 230), game_font_s)
            screen_message_2("             ?????? ??? ?????? ??????", WHITE, (700, 260), game_font_s)
            screen_message_2("'???????????? ???' - ?????? ??????", WHITE, (700, 320), game_font_s)
            screen_message_2("?????? ?????? ????????? ???????????? ???????????????.", WHITE, (700, 380), game_font_s)
        elif index == 4:
            screen_message_2("5. ????????????", WHITE, (700, 50), game_font_m)
            screen_message_2("'I' - ???????????? ??????/??????", WHITE, (700, 200), game_font_s)
            screen_message_2("??????????????? '??????'??? ?????? ??????", WHITE, (700, 260), game_font_s)
            screen_message_2("'???????????? ???' - ?????? ??????", WHITE, (700, 320), game_font_s)
            screen_message_2("'?????????' - ????????? ?????? ??????", WHITE, (700, 380), game_font_s)
            screen_message_2("           ????????? ????????? ?????? ???????????????.", WHITE, (700, 410), game_font_s)
            screen_message_2("'R' - ????????? ?????? ??????", WHITE, (700, 470), game_font_s)
            screen_message_2("      ????????? ????????? ????????? ??? ????????????.", WHITE, (700, 500), game_font_s)
            screen_message_2("      ????????? ????????? ???????????? ?????? ???????????????.", WHITE, (700, 530), game_font_s)
            screen_message_2("'C' or 'V' - ????????? ?????? ??????/?????? ?????? ??????", WHITE, (700, 590), game_font_s)
            screen_message_2("?????? ?????? : ????????? ???????????? (?????????)", WHITE, (700, 650), game_font_s)
            screen_message_2("?????? ?????? : ????????? ??????", WHITE, (700, 680), game_font_s)
        elif index == 5:
            screen_message_2("5. ???", WHITE, (700, 50), game_font_m)
            screen_message_2("???????????? ??????????????? ???????????????.", WHITE, (700, 200), game_font_s)
            screen_message_2("?????????, ????????????, ????????? ?????? ??? ????????? ??????", WHITE, (700, 230), game_font_s)
            screen_message_2("????????? ????????? ????????? ?????? ????????? ???????????????.", WHITE, (700, 260), game_font_s)
            screen_message_2("????????? ?????? - ??????, ??????", WHITE, (700, 320), game_font_s)
            screen_message_2("1????????? HP -1", WHITE, (700, 380), game_font_s)
            screen_message_2("??? ?????? ????????? HP +5", WHITE, (700, 410), game_font_s)
            screen_message_2("?????????, ????????? ?????? ??????????????? ???????????????.", WHITE, (700, 440), game_font_s)
            screen_message_2("?????? - 0??? ?????? ?????? ??????", WHITE, (700, 500), game_font_s)
        elif index == 6:
            screen_message_2("6. ??????", WHITE, (700, 50), game_font_m)
            screen_message_2("20????????? ?????? ????????? ??????", WHITE, (700, 200), game_font_s)
            screen_message_2("?????? ???????????? ?????? ?????? ??????", WHITE, (700, 260), game_font_s)
            screen_message_2("100????????? ????????? ??? ???????????? ?", WHITE, (700, 320), game_font_s)

        pygame.display.update()

def scene_tutorial(doing, tuto):

    player.stop()
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    punch_group.empty()
    punch_group.draw(screen)

    if tuto == "intro":
        if not game_con.tutorial:
            msg = [
                ("                      ?????????",    ".........?", "?????????..... ?????????....?"),
                ("??? ?????????",                       "??? ?????? ??????????????? ????????? ????????? ?????????.", "??? ?????? ???????????? ????????? ?????????.", ),
                ("                      ?????????",    "????????? ?????? ??? ???????????? ????????? ?????????.", "?????? ???????????? ???????????????."),
                ("??? ?????????",                       "???... ????????? ????????? ??????.", "?????? ?????? ???????????? ?????? ??????????????????."),
                ("??? ?????????",                       "??????, '?????????'??? ????????? ??? ?????? ??? ????????? ?", "????????? '???????????? ???'??? ????????? ????????????."),
                ("??? ?????????",                       "????????? ??? ??? ??????, ???????????? ???????????????", "??????????????? ????????? ???????????? ??? ??????."),
                ("??? ?????????",                       "????????? ?????? ??????????????? ??? ?????? ???~??? ?????????", "????????? ?????? ??? ????????? ?????? ????????? ?????????."),
                ("                      ?????????",    ".........?", "????????? ?????? ?"),
                ("??? ?????????",                       "?????? ????????? ??????????????????.", "??? ????????? ???????????? ??????????????? ??? ???????????????."),
                ("??? ?????????",                       "?????????, HP?????? ???????????? ???????????????,", "????????? ???????????? ????????? ??? ?????? ??? ????????? ?????????"),
                ("??? ?????????",                       "????????? ???????????? ?????????,", "???~ ?????? ?????? ??????????????? ???."),
                ("                      ?????????",    "??????????????? ?????????! ?????? ?????? ????????????.", "????????? ????????? ~"),
                ("??? ?????????",                       "??? - ??? !", "?????? ??? ??? ??? ???????????? ???????????????"),
                ("??? ?????????",                       "??? ?????? ????????? ????????? ???????????????", "?????????????????? ?????? ???????????? ??? ????????????."),
                ("??? ?????????",                       "?????? ????????? ??? ?????????, ??? ?????? ??????????????? ???.", ""),
                ("??? ?????????",                       "???????????? ?????? ??? ?????????", "'ESC' -> 'HELP'??? ?????????"),
                ("??? ?????????",                       "?????? ??? ????????????.", ""),
            ]
        else:
            msg = [
                    ("??? ?????????",                       "?????? ??? ??????", "?????? ??????")
                ]
    elif tuto == "shop":
        msg = [
                ("??? ?????????",                       "??? ????????? ?????? ?????????", "??? ?????? ????????????????"),
                ("                      ?????????",    "???????????? ???????????? ????????? ?", ""),
                ("??? ?????????",                       "?????? ??? ???????????? ???????????? ?????????.", "??? ??? ??????????????????"),
                ("??? ?????????",                       "??? ??????????????? ?????? ?????? ???", "???????????? ????????? ??? ??? ??? ????????????"),
                ("??? ?????????",                       "????????? ????????? ?????? ????????????", "'1','2','3'????????? ?????? ?????????"),
                ("                      ?????????",    "?????????...", "?????? ????????? ?????? ??????????????? ?"),
                ("??? ?????????",                       "?????? ????????? ?????? ??? ??? ????????????", "'R' ????????? ?????????"),
                ("??? ?????????",                       "?????? 1?????? ?????????", "????????? ????????? ?????? ?????? ?"),
                ("??? ?????????",                       "??? ????????? '??????'?????? '??????'????????????", "'I'?????? ???????????? ??? ??? ?????????"),
                ("??? ?????????",                       "'??????'??? ???????????? ????????????", "'??????'??? ?????? ?????? ???????????? ????????????"),
                ("??? ?????????",                       "?????? ?????? ?????? ??? ??????", "??? ?????????"),
            ]
    elif tuto == "inven":
        msg = [
                ("                      ?????????",    "??????-", "??? ?????? ??????????????? ?"),
                ("??? ?????????",                       "?????? ??? ??? ??? ????????? ?????????", "'I' ???????????? ??? ??? ?????????"),
                ("??? ?????????",                       "'???????????????'??? ????????? ??? ?????????", "???????????? ??????????????? ??????????????????"),
                ("                      ?????????",    "??????-", "????????? ??? ?????? ??? ?????? ?????????."),
                ("??? ?????????",                       "?????? ??? 'R'???????????? ??????????????????", "?????? ??????????????????"),
                ("??? ?????????",                       "??? ????????? ?????? ?????? ???????????? ??????", "'C'??? 'V'??? ???????????? ????????????"),
                ("??? ?????????",                       "??? ?????? ??? ??? ???????????? ????????? ?????????", "?????? ?????? ?????????"),
            ]
    elif tuto == "box":
        pass

    index = 0
    fin = len(msg)-1

    corpus_rect = pygame.Rect((350,450), (580,200))

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_wasd)
                    if index >= fin:
                        doing = False
                        if not game_con.tutorial:
                            sound_con.play_sound(sound_coin)
                            player.coin += 10
                            game_con.tutorial = True
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    doing = False
                    scene_esc(True)

        screen.blit(corpus_image, (350,450))
        screen_message_2(msg[index][0], YELLOW, (400, 470), game_font_m)
        screen_message_2(msg[index][1], WHITE, (400,550), game_font_s)
        screen_message_2(msg[index][2], WHITE, (400,590), game_font_s)
        pygame.display.update(corpus_rect)

def scene_boss(doing):

    if not sound_con.bgm == bgm_boss:
        sound_con.play_bgm(bgm_boss)

    player.stop()
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    monster_con.boss_scene = True
    init_time = pygame.time.get_ticks()

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)

        second_time = pygame.time.get_ticks()

        if second_time - init_time > 2000:
            doing = False

        screen.fill(BLACK)
        cut_rect = pygame.Rect((340,200), (600,100))
        if game_con.floor == 100:
            screen_message("FINAL BOSS STAGE", RED, (640,250), game_font_l)
        else:
            screen_message("BOSS STAGE", RED, (640,250), game_font_l)
        pygame.display.update(cut_rect)

def scene_finalboss(doing):

    player.stop()
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    if not game_con.devil:
        msg =[
            ("??????",                            "???????????? ??????????????????...", "?????? ????????? ???????????????"),
            ("??????",                            "????????? ???????????? ??????????????? ?", "?????? ????????????."),
            ("                      ?????????",    ".....?", "???????????? ???????????? ?"),
            ("??????",                            "????????? ????????? ??? ?????? ??????.", "????????? ????????? ???????????????."),
            ("                      ?????????",    "......", "??? ?????? ?????? ???????????? ?????? ?????? ???????????? ?"),
            ("??????",                            "?????? ????????? ?????????...", ""),
        ]
    else:
        msg = [
            ("??????",                            "??????..!", "??? ??????????????????"),
            ("??????",                            "????????? ????????? ???????????????", "??? ????????? ??????"),
        ]

    index = 0
    fin = len(msg)-1

    corpus_rect = pygame.Rect((350,450), (580,200))

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_wasd)
                    if index >= fin:
                        doing = False
                        if not game_con.devil:
                            spawn_monster(player.position, Boss_devil_first())
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    doing = False
                    scene_esc(True)

        screen.fill(BLACK)
        screen_message_2(msg[index][0], YELLOW, (400, 470), game_font_m)
        screen_message_2(msg[index][1], WHITE, (400,530), game_font_s)
        screen_message_2(msg[index][2], WHITE, (400,570), game_font_s)
        pygame.display.update(corpus_rect)

    game_con.devil = True

def scene_player_dead(doing):
    monster_con.is_blind = False
    monster_con.boss_scene = False
    sound_con.play_sound(sound_die)

    if game_con.ending:
        player.image_group = player_blue_images

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    doing = False
                    sound_con.play_sound(sound_reborn)
                    floor_zero()
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    scene_esc(True)

        screen.fill(BLACK)
        screen_message("YOU DIE", RED, (screen_width//2, screen_height//2), game_font_l)
        screen_message("PRESS 'R' TO GO 0F", WHITE, (640,640), game_font_m)
        display_info_ui()
        display_inven_ui()
        pygame.display.update()

def scene_game_over(doing):

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_pick)
                    doing = False
                    game_restart()
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    scene_esc(True)

        screen.fill(BLACK)
        screen_message("GAME OVER", RED, (screen_width//2, screen_height//2), game_font_l)
        screen_message(f"REACHED AT {game_con.floor} FLOOR", WHITE, (screen_width//2, screen_height//2 + 50), game_font_m)
        screen_message(f"BEATED {monster_con.mon_count} MONSTERS", WHITE, (screen_width//2, screen_height//2 + 100), game_font_m)
        screen_message("PRESS 'SPACE BAR' TO MAIN", WHITE, (640,640), game_font_m)
        pygame.display.update()

def scene_shop(doing):
    sound_con.play_sound(sound_shop_open)
    picked_num = 0

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if picked_num == 1:
                        purchase_equip(0)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[0]:
                            sound_con.play_sound(sound_wasd)
                            picked_num = 1

                if event.key == pygame.K_2:
                    if picked_num == 2:
                        purchase_equip(1)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[1]:
                            sound_con.play_sound(sound_wasd)
                            picked_num = 2

                if event.key == pygame.K_3:
                    if picked_num == 3:
                        purchase_equip(2)
                        picked_num = 0
                    else:
                        if equip_con.for_sale[2]:
                            sound_con.play_sound(sound_wasd)
                            picked_num = 3

                if event.key == pygame.K_r:
                    if player.coin >= 1:
                        sound_con.play_sound(sound_shop_refresh)
                        player.coin -= 1
                        random_for_sale()
                        picked_num = 0

                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_shop_close)
                    if is_inven_overlapped(equip_con.equipped_group):
                        scene_inventory(True)
                    else:
                        doing = False
                        equip_effect()

        screen.blit(shop_image, (340,60))
        display_info_ui()
        display_inven_ui()

        if picked_num:
            equip = equip_con.for_sale[picked_num-1]
            screen_message(equip.msg_name, WHITE, (540,100), game_font_m)
            screen_message(equip.msg_info, WHITE, (540,150), game_font_s)
            screen_message(equip.msg_eff, YELLOW, (540,200), game_font_s)
            screen_message(equip.msg_eff_2, YELLOW, (540,230), game_font_s)
            screen_message(equip_con.equip_grade(equip)[0], equip_con.equip_grade(equip)[1], (820,160), game_font_s)
            coin_image_r = pygame.transform.rotozoom(coin_image, 0, 0.5)
            coin_rect = coin_image_r.get_rect(center=(800, 200))
            screen.blit(coin_image_r, coin_rect)
            screen_message(f"x {equip.price}", WHITE, (850,200), game_font_m)\

        shop_showcase(0, equip_con.for_sale[0])
        shop_showcase(1, equip_con.for_sale[1])
        shop_showcase(2, equip_con.for_sale[2])

        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)
        pygame.display.update()

        if not game_con.shop:
            scene_tutorial(True, "shop")
            game_con.shop = True

def shop_showcase(index, equip):
    if equip_con.can_buy[index] and equip_con.for_sale[index]:
        equip_rect = equip.image.get_rect(center=(460+180*index, 420))
        screen.blit(equip.image, equip_rect)
    else:
        case_rect = sold_out_image.get_rect(center=(460 + 180*index, 420))
        screen.blit(sold_out_image, case_rect)

def scene_inventory(doing):
    sound_con.play_sound(sound_inven_open)

    player.stop()
    monster_con.dontmove = True
    for monster in monster_group:
        monster.direction = "NONE"

    cursor = Cursor(cursor_images[0], (980,270))
    picked_equip = None

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                cursor.move(event)
                if cursor.clicking:
                    picked_equip.inven_move(event)

                if event.key == pygame.K_i or event.key == pygame.K_ESCAPE:
                    if not is_inven_overlapped(equip_con.equipped_group):
                        sound_con.play_sound(sound_inven_close)
                        equip_effect()
                        doing = False

                if event.key == pygame.K_r:
                    if picked_equip:
                        remove_from_equipped_group(picked_equip)
                        cursor.clicking = False
                        cursor.image = cursor_images[0]
                        picked_equip = None

                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_inven_click)
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

        display_info_ui()
        display_inven_ui()

        pygame.draw.rect(screen, BLACK, ((490,280), (300,300)))
        pygame.draw.rect(screen, WHITE, ((490,280), (300,300)), 1)
        screen_message(f"????????? : {player.ap}", WHITE, (640,300), game_font_s)
        screen_message("????????? : {0:.2f}".format(player.dp), WHITE, (640,330), game_font_s)
        screen_message("?????? ?????? : {0:.2f}".format(player.speed), WHITE, (640,360), game_font_s)
        screen_message("?????? ????????? : {0:.2f}".format(player.damaged_time), WHITE, (640,390), game_font_s)

        screen_message(f"?????? ????????? : {item_con.potion_eff}", WHITE, (640,450), game_font_s)
        screen_message(f"?????? ?????? ?????? : {item_con.prob_potion}%", WHITE, (640,480), game_font_s)
        screen_message(f"?????? ?????? ?????? : {item_con.prob_coin}%", WHITE, (640,510), game_font_s)

        pygame.draw.rect(screen, BLACK, ((440,90),(400,160)))
        pygame.draw.rect(screen, WHITE, ((440,90),(400,160)), 1)
        if picked_equip:
            screen_message(picked_equip.msg_name, WHITE, (640,120), game_font_m)
            screen_message(equip_con.equip_grade(picked_equip)[0], equip_con.equip_grade(picked_equip)[1], (800,120), game_font_s)
            screen_message(picked_equip.msg_info, WHITE, (640,160), game_font_kor)
            screen_message(picked_equip.msg_eff, YELLOW, (640,210), game_font_kor)
            screen_message(picked_equip.msg_eff_2, YELLOW, (640,230), game_font_kor)
    
        screen_message_3("     PRESS 'I' TO BACK     ", WHITE, (640,640), game_font_m)
        cursor.draw(screen)
        pygame.display.update()

        if not game_con.inven:
            scene_tutorial(True, "inven")
            game_con.inven = True
            screen.fill(BLACK)

def scene_treasurebox(doing, reward):
    sound_con.play_sound(sound_box_open)
    player.stop()

    if reward == "normal":
        choice_equip = [equip_con.normal_equips[-1], equip_con.normal_equips[-2]]
    elif reward == "boss":
        choice_equip = [e_coins, e_potion]

    picked_num = 0
    choice = True
    exit_flag = False

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if choice:
                    if event.key == pygame.K_1:
                        exit_flag = False
                        if picked_num == 1:
                            if reward == "normal":
                                sound_con.play_sound(sound_box_get)
                                equip_con.equipped_group.append(choice_equip[0])
                                equip_con.equip_on(choice_equip[0])
                            elif reward == "boss":
                                player.coin += 15
                            choice = False
                            picked_num = 0
                        else:
                            sound_con.play_sound(sound_wasd)
                            picked_num = 1

                    if event.key == pygame.K_2:
                        exit_flag = False
                        if picked_num == 2:
                            sound_con.play_sound(sound_box_get)
                            if reward == "normal":
                                equip_con.equipped_group.append(choice_equip[1])
                                equip_con.equip_on(choice_equip[1])
                            elif reward == "boss":
                                player.hp = min(player.hp+50, player.max_hp)
                            choice = False  
                            picked_num = 0
                        else:
                            sound_con.play_sound(sound_wasd)
                            picked_num = 2

                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if not choice:
                        sound_con.play_sound(sound_box_close)
                        doing = False
                        if is_inven_overlapped(equip_con.equipped_group):
                            scene_inventory(True)
                        else:
                            equip_effect()
                    elif not exit_flag:
                        exit_flag = True
                    elif exit_flag:
                        doing = False

        screen.fill(BLACK)
        screen.blit(treasurebox_image, (340,60))
        display_info_ui()
        display_inven_ui()

        zero_rect = choice_equip[0].image.get_rect(center=(540,420))
        one_rect = choice_equip[1].image.get_rect(center=(740,420))

        if picked_num and not exit_flag:
            screen_message(choice_equip[picked_num-1].msg_name, WHITE, (640,100), game_font_m)
            screen_message(choice_equip[picked_num-1].msg_info, WHITE, (640,150), game_font_kor)
            screen_message(choice_equip[picked_num-1].msg_eff, YELLOW, (640,200), game_font_kor)
            screen_message(choice_equip[picked_num-1].msg_eff_2, YELLOW, (640,230), game_font_kor)
        else:
            if exit_flag:
                screen_message("ARE YOU SURE TO QUIT ?", WHITE, (640,150), game_font_m)
                picked_num = 0
            elif choice:
                screen_message("CHOICE '1' or '2' !", WHITE, (640,150), game_font_m)
        
        if choice:
            screen.blit(choice_equip[0].image, zero_rect)
            screen.blit(choice_equip[1].image, one_rect)
            
        screen_message("PRESS 'SPACE BAR' TO BACK", WHITE, (640,640), game_font_m)
        
        pygame.display.update()

def scene_ending(doing):

    index = 0
    fin = len(ending_images)

    sound_con.play_bgm(bgm_story)

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_con.play_sound(sound_page)
                    if index >= fin:
                        doing = False
                    else:
                        index += 1
                if event.key == pygame.K_ESCAPE:
                    sound_con.play_sound(sound_pick)
                    scene_esc(True)
                if event.key == pygame.K_r:
                    doing = False

        screen.fill(BLACK)

        if -1 < index < 3:
            screen.blit(ending_images[0], (200,50))
            if index > 0:
                screen.blit(ending_images[1], (200, 350))
                if index > 1:
                    screen.blit(ending_images[2], (600,100))
        elif index == 3:
            screen.blit(ending_images[3], (240,100))
        elif 3 < index < 6:
            screen.blit(ending_images[4], (200,50))
            if index > 4:
                screen.blit(ending_images[5], (600, 80))
        elif index == 6:
            screen.blit(ending_images[6], (240,100))
        elif index == 7:
            screen_message("TO BE CONTINUE...", (WHITE), (screen_width//2, screen_height//2), game_font_l)
            
        
        pygame.display.update()

    scene_credit(True)

def scene_credit(doing):
    global ready
    
    pos_bottom = screen_height + 100        # pos_bottom = 820    
    credit_speed = 0.5
    ii = 0
    credit_time = pygame.time.get_ticks()

    if not sound_con.bgm == bgm_title:
        sound_con.play_bgm(bgm_title)

    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene_exit(True)

        screen.fill(BLACK)

        msg = [
            ("", pos_bottom), 

            ("", pos_bottom+200),
            ("CODE DESIGNER", pos_bottom+350),
            ("KIM MINSANG", pos_bottom+400), 

            ("", pos_bottom+500),
            ("GAME DIRECTOR", pos_bottom+650),
            ("BAE SUNGHYUN", pos_bottom+700), 

            ("", pos_bottom+800),
            ("SOUND DESIGNER", pos_bottom+950),
            ("SHIN JUNHA", pos_bottom+1000), 

            ("", pos_bottom+1100),
            ("GRAPHIC DESIGNER", pos_bottom+1250),
            ("LEE SOOBIN", pos_bottom+1300), 

            ("SPECIAL THANKS TO", pos_bottom+1550),
            ("AJOUANEY & TEAM GSS", pos_bottom+1600),

            ("", pos_bottom+1900),
            ("HANYANG UNIV. ERICA", pos_bottom+2050),

            ("THANKS FOR PLAYING", pos_bottom+2500),
            ("AND NEW ADVENTURE JUST BEGINS NOW...", pos_bottom+2700),
        ]

        screen.blit(title_logo, (screen_width//2-title_logo.get_width()//2, msg[0][1]))

        screen.blit(coffin_images[0], (screen_width//2-350, msg[1][1]+60))
        screen.blit(mon_frog_images[ii], (screen_width//2-200, msg[1][1]+60))
        screen.blit(player_images[ii], (screen_width//2-100, msg[1][1]))
        screen.blit(mon_golem_images[ii], (screen_width//2+100, msg[1][1]+60))
        screen.blit(mon_candle_images[ii], (screen_width//2+200, msg[1][1]))

        screen_message(msg[2][0], WHITE, (screen_width//2, msg[2][1]), game_font_m)
        screen_message(msg[3][0], WHITE, (screen_width//2, msg[3][1]), game_font_l)

        screen.blit(mon_book_images[ii], (screen_width//2-300, msg[4][1]+60))
        screen.blit(mon_spider_images[ii], (screen_width//2-200, msg[4][1]+60))
        screen.blit(father_slime_images[ii], (screen_width//2-100, msg[4][1]))
        screen.blit(mon_magician_images[ii], (screen_width//2+100, msg[4][1]+60))
        screen.blit(mon_flamesnake_images[ii+1], (screen_width//2+200, msg[4][1]))

        screen_message(msg[5][0], WHITE, (screen_width//2, msg[5][1]), game_font_m)
        screen_message(msg[6][0], WHITE, (screen_width//2, msg[6][1]), game_font_l)

        screen.blit(mon_spider_images[ii], (screen_width//2-300, msg[7][1]+60))
        screen.blit(mon_firebat_images[ii], (screen_width//2-200, msg[7][1]+60))
        screen.blit(mon_zombie_images[ii], (screen_width//2-100, msg[7][1]))
        screen.blit(mon_witch_images[ii], (screen_width//2+100, msg[7][1]+60))
        screen.blit(mon_scarecrow_images[ii], (screen_width//2+200, msg[7][1]))

        screen_message(msg[8][0], WHITE, (screen_width//2, msg[8][1]), game_font_m)
        screen_message(msg[9][0], WHITE, (screen_width//2, msg[9][1]), game_font_l)

        screen.blit(mon_skel_images[ii], (screen_width//2-300, msg[10][1]+60))
        screen.blit(mon_ember_images[ii], (screen_width//2-200, msg[10][1]+60))
        screen.blit(mon_ghost_images[ii], (screen_width//2-100, msg[10][1]))
        screen.blit(stair_images[2], (screen_width//2+100, msg[10][1]+60))
        screen.blit(devil_images[ii], (screen_width//2+200, msg[10][1]))

        screen_message(msg[11][0], WHITE, (screen_width//2, msg[11][1]), game_font_m)
        screen_message(msg[12][0], WHITE, (screen_width//2, msg[12][1]), game_font_l)

        screen_message(msg[13][0], WHITE, (screen_width//2, msg[13][1]), game_font_m)
        screen_message(msg[14][0], WHITE, (screen_width//2, msg[14][1]), game_font_l)

        screen.blit(team_logo, (screen_width//2-team_logo.get_width()//2, msg[15][1]))
        screen_message(msg[16][0], WHITE, (screen_width//2, msg[16][1]), game_font_m)

        screen_message(msg[17][0], WHITE, (screen_width//2, msg[17][1]), game_font_l)
        screen_message(msg[18][0], (0,200,200), (screen_width//2, msg[18][1]), game_font_l)

        pos_bottom -= credit_speed

        if pygame.time.get_ticks() - credit_time > 500:
            ii += 1
            credit_time = pygame.time.get_ticks()
            if ii > 1:
                ii = 0
        
        pygame.display.update()

        if pos_bottom < -2800:
            doing = False
            game_con.ending = True
            version_blue()
            ready = True
##############################################################################################
def screen_message(writing, color, position, font):
    msg = font.render(writing, True, color)
    msg_rect = msg.get_rect(center=position)
    screen.blit(msg, msg_rect)
    
def screen_message_2(writing, color, position, font):
    msg = font.render(writing, True, color)
    screen.blit(msg, position)

def screen_message_3(writing, color, position, font):
    msg = font.render(writing, True, color, BLACK)
    msg_rect = msg.get_rect(center=position)
    pygame.draw.rect(screen, WHITE, msg_rect, 0, 10)
    screen.blit(msg, msg_rect)

def game_restart():
    global player
    # global item_con, equip_con, skill_con, monster_con

    while equip_con.equipped_group:
        for equip in equip_con.equipped_group:
            remove_from_equipped_group(equip)
            equip.reset()

    player.reset()

    if game_con.tutorial:
        player.coin += 10
    
    make_floor_zero()
    game_con.saved_floor = 1

    random_for_sale()

    # item_con = ItemController()
    # equip_con = EquipController()
    # skill_con = SkillController()
    # monster_con = MonsterController()

def version_blue():
    global player_images, player_die_images, punch_d_image, player_icon, inven_image, title_image, title_logo

    player_images = player_blue_images
    player.image_group = player_blue_images

    player_die_images = blue_die_images
    player.die_images = blue_die_images

    punch_d_image = blue_punch
    player.punch = blue_punch

    player_icon = player_images[1]
    inven_image = blue_inven
    title_image = title_2_image
    title_logo = title_logo_2

def make_floor_zero():

    game_con.floor = 0

    monster_group.empty()
    shooting_group.empty()
    item_group.empty()
    field_group.empty()

    stair.image = stair_images[0]
    stair.rect = stair.image.get_rect(center=stair_zero_floor)

    random_for_sale()

    item_con.first_box = True

    player.rect = player.image.get_rect(center=player_first_position)

    if not skill_con.active_skelhead:
        player.hp = player.max_hp
    else:
        skill_con.active_skelhead = False

def floor_zero():

    if not sound_con.bgm == bgm_0f:
        sound_con.play_bgm(bgm_0f)

    if game_con.floor != 0:
        make_floor_zero()

    game_con.background = background_zero

    for deco in deco_group:
        deco.draw(screen)
    for npc in npc_group:
        npc.draw(screen)

    if item_con.first_box and game_con.shop:
        item_group.add(Item(box_image, (400,500), "normal_box"))
        item_con.first_box = False

    if pygame.sprite.collide_mask(player, stair):
        game_con.floor = game_con.saved_floor - 1

    for punch in punch_group:
        if pygame.sprite.collide_mask(punch, npc_kingslime):
            player.stop()
            scene_tutorial(True, "intro")

        if pygame.sprite.collide_mask(punch, npc_coffin) and game_con.tutorial:
            player.stop()
            scene_shop(True)

def floor_81():
    if not game_con.devil:
        npc_devil.direction = "RIGHT"
        npc_devil.draw(screen)

        for punch in punch_group:
            if pygame.sprite.collide_mask(punch, npc_devil):
                scene_finalboss(True)

def next_floor(pos):
    sound_con.play_sound(sound_nextfloor)

    game_con.floor += 1
    player.hp = min(player.hp+5, player.max_hp)

    item_group.empty()
    shooting_group.empty()

    if game_con.floor == 99:
        stair.image = stair_images[2]
    elif (game_con.floor % 20 == 19):
        stair.image = stair_images[0]
    else:
        stair.image = stair_images[1]

    monster_setting(pos, game_con.floor)

    random_field_setting(game_con.floor)

    game_con.background = setting_background(game_con.floor)

    monster_con.boss_scene = False

    if e_crescentmoon in equip_con.equipped_group:
        e_crescentmoon.prob_revival()

    e_goldenkey.target = game_con.floor

def setting_background(floor):
    randprob = random.randrange(0,3)
    if floor == 0 or floor == 81 or floor == 100:
        background = background_zero
    elif 0 < floor <= 20 or 81 < floor <= 85:
        background = background_first[randprob]
    elif 20 < floor <= 40 or 85 < floor <= 90:
        background = background_second[randprob]
    elif 40 < floor <= 60 or 90 < floor <= 95:
        background = background_third[randprob]
    elif 60 < floor <= 80 or 95 < floor <= 99:
        background = background_fourth[randprob]
    else:
        background = background_zero

    return background

def bgm_setting(floor):
    if 0 < floor < 20 and not sound_con.bgm == bgm_first:
        sound_con.play_bgm(bgm_first)
    elif 20 < floor < 40 and not sound_con.bgm == bgm_second:
        sound_con.play_bgm(bgm_second)
    elif 40 < floor < 60 and not sound_con.bgm == bgm_third:
        sound_con.play_bgm(bgm_third)
    elif 60 < floor < 80 and not sound_con.bgm == bgm_fourth:
        sound_con.play_bgm(bgm_fourth)
    elif floor == 81 and not sound_con.bgm == bgm_finalboss:
        sound_con.play_bgm(bgm_finalboss)
    elif 81 < floor < 100 and not sound_con.bgm == bgm_fifth:
        sound_con.play_bgm(bgm_fifth)

def show_animation():
    player.image_update()
    for deco in deco_group:
        deco.image_update()
    for npc in npc_group:
        npc.image_update()
    for monster in monster_group:
        if not monster.is_die:
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

        if (100 - equip_con.perc_unique) <= percent and not unique_index >= len(equip_con.unique_equips):
            equip_con.for_sale[i] = equip_con.unique_equips[unique_index]
            unique_index += 1
            equip_con.can_buy[i] = True
        elif percent <= equip_con.perc_rare and not rare_index >= len(equip_con.rare_equips):
            equip_con.for_sale[i] = equip_con.rare_equips[rare_index]
            rare_index += 1
            equip_con.can_buy[i] = True
        else:
            if normal_index >= len(equip_con.normal_equips):
                equip_con.can_buy[i] = False
            else:
                equip_con.for_sale[i] = equip_con.normal_equips[normal_index]
                normal_index += 1
                equip_con.can_buy[i] = True

def purchase_equip(index):
    equip = equip_con.for_sale[index]
    if equip_con.can_buy[index] and player.coin >= equip.price:
        sound_con.play_sound(sound_shop_buy)
        equip_con.equipped_group.append(equip)
        player.coin -= equip.price
        equip_con.can_buy[index] = False
        equip_con.for_sale[index] = None

        equip_con.equip_on(equip)

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

    if "boss" in monster.type:
        item_group.add(Item(box_image, monster.position, "boss_box"))
    elif "mini" in monster.type:
        pass
    elif "devil_final" in monster.type:
        item_group.add(Item(crown_image, monster.position, "crown"))
    else:
        if randprob <= item_con.prob_potion: # ?????? <= ???????????????
            item_group.add(Item(potion_image, monster.position, "potion"))
        elif (100 - item_con.prob_coin) < randprob: # 100-??????????????? <= ??????
            if item_con.red_coin and 98 < randprob:
                item_group.add(Item(redcoin_image, monster.position, "red_coin"))
            else:
                item_group.add(Item(coin_image, monster.position, "coin"))

def item_effect(item):
    if item.info == "potion":
        sound_con.play_sound(sound_potion)
        player.hp = min(player.hp + item_con.potion_eff, player.max_hp)
    elif item.info == "coin":
        sound_con.play_sound(sound_coin)
        player.coin += 1
    elif item.info == "red_coin":
        sound_con.play_sound(sound_coin)
        player.coin += 3
    elif item.info == "boss_box":
        scene_treasurebox(True, "boss")
    elif item.info == "normal_box":
        scene_treasurebox(True, "normal")
    elif item.info == "crown":
        scene_ending(True)

def equip_effect():
    # mushroom
    # crescentmoon
    # banana
    # mandoo

    if e_wax in equip_con.equipped_group:
        if not e_wax.is_effected:
            player.ap += 2
            e_wax.is_effected = True

    if e_pepper in equip_con.equipped_group:
        if not e_pepper.is_effected:
            player.ap += 4            
            e_pepper.is_effected = True
    
    if e_battery in equip_con.equipped_group:
        if not e_battery.is_effected:
            player.ap += 5
            player.speed += 0.1
            e_battery.is_effected = True

    if e_heartstone in equip_con.equipped_group:
        if not e_heartstone.is_effected:
            player.hp += 50
            player.max_hp += 50
            e_heartstone.is_effected = True

    if e_halfstone in equip_con.equipped_group:
        if not e_halfstone.is_effected:
            player.hp += 20
            player.max_hp += 20
            e_halfstone.is_effected = True

    if e_poisonapple in equip_con.equipped_group:
        if not e_poisonapple.is_effected:
            player.hp += 10
            player.max_hp += 10
            player.damaged_time += 0.2
            e_poisonapple.is_effected = True

    if e_ice in equip_con.equipped_group:
        if not e_ice.is_effected:
            player.speed += 0.1
            e_ice.is_effected = True

    if e_boxerglove in equip_con.equipped_group:
        if not e_boxerglove.is_effected:
            big_punch_image = pygame.transform.scale(punch_d_image, (90,90))
            player.punch = big_punch_image
            e_boxerglove.is_effected = True

    if e_helmet in equip_con.equipped_group:
        if not e_helmet.is_effected:
            player.dp += 0.3
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
            item_con.prob_potion += 5
            e_machine.is_effected = True

    if e_piggybank in equip_con.equipped_group:
        if not e_piggybank.is_effected:
            item_con.red_coin = True
            e_piggybank.is_effected = True

    if e_metaldetector in equip_con.equipped_group:
        if not e_metaldetector.is_effected:
            item_con.prob_coin += 5
            e_metaldetector.is_effected = True

    if e_binoculars in equip_con.equipped_group:
        if not e_binoculars.is_effected:
            item_con.prob_potion += 3
            item_con.prob_coin += 3
            e_binoculars.is_effected = True

    if e_rollerskate in equip_con.equipped_group:
        if not e_rollerskate.is_effected:
            e_rollerskate.activate = True
            e_rollerskate.is_effected = True

    # trafficlight
    # thunder
    # dice
    # magiccloak
    # goldenkey
    # rope

def remove_from_equipped_group(equip):
    sound_con.play_sound(sound_equip_remove)

    equip_con.equipped_group.remove(equip)

    if equip.is_effected:
        if equip.is_active_c:
            player.equip_c = None
        elif equip.is_active_v:
            player.equip_v = None

        if equip == e_wax:
            player.ap -= 2

        elif equip == e_pepper:
            player.ap -= 4

        elif equip == e_battery:
            player.ap -= 5
            player.speed -= 0.1

        elif equip == e_heartstone:
            player.max_hp -= 50
            player.hp = min(player.hp, player.max_hp)

        elif equip == e_halfstone:
            player.max_hp -= 20
            player.hp = min(player.hp, player.max_hp)

        elif equip == e_poisonapple:
            player.hp -= 10
            player.max_hp -= 10
            player.damaged_time -= 0.2

        elif equip == e_ice:
            player.speed -= 0.1

        elif equip == e_boxerglove:
            player.punch = punch_d_image

        elif equip == e_helmet:
            player.dp -= 0.3

        elif equip == e_turtleshell:
            player.damaged_time += 0.3

        elif equip == e_pizza:
            monster_con.b_speed += 2

        elif equip == e_3dglasses:
            monster_con.dont_alpha = False

        elif equip == e_talisman:
            monster_con.dont_dash = False

        elif equip == e_ticket:
            equip_con.perc_rare -= 5

        elif equip == e_straw:
            item_con.potion_eff -= 5

        elif equip == e_machine:
            item_con.prob_potion -= 5
        
        elif equip == e_piggybank:
            item_con.red_coin = False

        elif equip == e_metaldetector:
            item_con.prob_coin -= 5

        elif equip == e_binoculars:
            item_con.prob_potion -= 3
            item_con.prob_coin -= 3
        
        elif equip == e_rollerskate:
            e_rollerskate.activate = False

        equip.reset()

    equip_con.equip_off(equip)

def setting_active_skill(key, picked_equip):
    if picked_equip.active:
        sound_con.play_sound(sound_inven_active)
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

def random_monster_direction():
    if monster_group and not monster_con.dontmove:
        for monster in monster_group:
            if not monster.is_die:
                if not "toward" in monster.type:
                    rand = random.randrange(0,10)

                    if rand <= 1:
                        monster.direction = "LEFT"
                    elif 1 < rand and rand <= 3:
                        monster.direction = "RIGHT"
                    elif 3 < rand and rand <= 5:
                        monster.direction = "UP"
                    elif 5 < rand and rand <= 7:
                        monster.direction = "DOWN"
                    else:
                        monster.direction = "NONE"

                    if monster.rect.centerx <= 340 + (monster.rect.width // 2):
                        monster.direction = "RIGHT"
                    elif monster.rect.centerx >= 940 - (monster.rect.width // 2):
                        monster.direction = "LEFT"

                    if monster.rect.centery <= 60 + (monster.rect.height // 2):
                        monster.direction = "DOWN"
                    elif monster.rect.centery >= 660 - (monster.rect.height // 2):
                        monster.direction = "UP"
                else:
                    forward_monster_direction(monster, player)

def forward_monster_direction(monster, target):
    x = target.position[0] - monster.position[0]
    y = target.position[1] - monster.position[1]
    rand = random.randrange(1,10)

    if rand <= 5:
        if x < -30 :
            monster.direction = "LEFT"
        elif x > 30:
            monster.direction = "RIGHT"
        else:
            monster.direction = "NONE"
    else:
        if y < -30:
            monster.direction = "UP"
        elif y > 30:
            monster.direction = "DOWN"
        else:
            monster.direction = "NONE"

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
    for monster in monster_group:
        randprob = random.randrange(1,101)

        if not monster.is_die:
            if "shooter" in monster.type:
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
                    shooting_group.add(Bullet(image, monster.position, monster.direction, monster.b_speed, monster.b_damage, monster.b_type))
            elif "shooter_four" in monster.type:
                if 0 <= randprob <= 50:
                    u_image = pygame.transform.rotozoom(monster.bullet, 270, 1)
                    shooting_group.add(Bullet(u_image, monster.position, "UP", monster.b_speed, monster.b_damage, monster.b_type))
                    d_image = pygame.transform.rotozoom(monster.bullet, 90, 1)
                    shooting_group.add(Bullet(d_image, monster.position, "DOWN", monster.b_speed, monster.b_damage, monster.b_type))
                    shooting_group.add(Bullet(monster.bullet, monster.position, "LEFT", monster.b_speed, monster.b_damage, monster.b_type))
                    r_image = pygame.transform.flip(monster.bullet, True, False)
                    shooting_group.add(Bullet(r_image, monster.position, "RIGHT", monster.b_speed, monster.b_damage, monster.b_type))

            if "alpha" in monster.type:
                if 0 <= randprob <= 50 and not monster_con.dont_alpha:
                    monster.alpha(60)
                elif 80 < randprob or monster_con.dont_alpha:
                    monster.alpha(255)

            if "runner" in monster.type and not monster_con.dont_dash:
                if 0 <= randprob <= 30 and not monster.is_dashed:
                    monster.speed += 0.4
                    monster.is_dashed = True

                if monster.is_dashed:
                    monster.dashes += 1
                    if monster.dashes >= 2:
                        monster.speed -= 0.4
                        monster.dashes = 0
                        monster.is_dashed = False

            if "mon_candle" in monster.type:
                if 0 <= randprob < 30:
                    spawn_monster(player.position, Mon_ember_m())

            if "boss" in monster.type:
                boss_action(monster)

            if "devil_final" in monster.type:
                devil_action(monster)

def boss_action(monster):
    if "boss_spider" in monster.type:       # field spawner
        web = Field(web_image, (0,0))
        random_away_position(monster.position, web)
        field_group.add(web)
    elif "boss_frog" in monster.type:       # monster spawner
        monster.cycle += 1
        if monster.cycle == 3:
            spawn_monster(player.position, Mon_frog_m())
            monster.cycle = 0
    elif "boss_bat" in monster.type:        # blind
        monster_con.is_blind = True
    elif "boss_skel" in monster.type:    # boss shooter
        if monster.direction == "LEFT" or monster.direction == "RIGHT":
            image = pygame.transform.rotozoom(monster.bullet, 90, 1)
            shooting_group.add(Bullet(image, monster.position, "UP", monster.b_speed, monster.b_damage, monster.b_type))
            shooting_group.add(Bullet(image, monster.position, "DOWN", monster.b_speed, monster.b_damage, monster.b_type))
        else:
            shooting_group.add(Bullet(monster.bullet, monster.position, "LEFT", monster.b_speed, monster.b_damage, monster.b_type))
            shooting_group.add(Bullet(monster.bullet, monster.position, "RIGHT", monster.b_speed, monster.b_damage, monster.b_type))

    elif "boss_ghost" in monster.type:
        monster_con.is_blind = True
    elif "boss_scarecrow" in monster.type:
        u_image = pygame.transform.rotozoom(monster.bullet, 270, 1)
        shooting_group.add(Bullet(u_image, monster.position, "UP", monster.b_speed, monster.b_damage, monster.b_type))
        d_image = pygame.transform.rotozoom(monster.bullet, 90, 1)
        shooting_group.add(Bullet(d_image, monster.position, "DOWN", monster.b_speed, monster.b_damage, monster.b_type))
        shooting_group.add(Bullet(monster.bullet, monster.position, "LEFT", monster.b_speed, monster.b_damage, monster.b_type))
        r_image = pygame.transform.flip(monster.bullet, True, False)
        shooting_group.add(Bullet(r_image, monster.position, "RIGHT", monster.b_speed, monster.b_damage, monster.b_type))

    elif "boss_ember" in monster.type:
        monster.cycle += 1
        if monster.cycle == 2:
            lava = Field(lava_images[1], (0,0))
            random_away_position(monster.position, lava)
            field_group.add(lava)
            monster.cycle == 0
    elif "boss_flamesnake" in monster.type:
        monster.cycle += 1
        if monster.cycle == 3:
            spawn_monster(player.position, Mon_ember_m())
            monster.cycle = 0

    elif "boss_magician" in monster.type:
        if not monster.activate:
            player.speed -= 0.15
            monster.activate = True
    elif "boss_candle" in monster.type:
        monster.cycle += 1
        if monster.cycle > 3:
            spawn_monster(player.position, Mon_ember())
            monster.cycle = 0

def devil_action(monster):
    if monster.cycle == 2:
        spawn_monster(player.position, Mon_spider())
        spawn_monster(player.position, Mon_zombie())
        spawn_monster(player.position, Mon_ember())
        spawn_monster(player.position, Mon_witch())
    elif 6 < monster.cycle < 15 :
        u_image = pygame.transform.rotozoom(magician_atk_image, 270, 1)
        shooting_group.add(Bullet(u_image, monster.position, "UP", 10, 10, "magic"))
        d_image = pygame.transform.rotozoom(magician_atk_image, 90, 1)
        shooting_group.add(Bullet(d_image, monster.position, "DOWN", 10, 10, "magic"))
        shooting_group.add(Bullet(magician_atk_image, monster.position, "LEFT", 10, 10, "magic"))
        r_image = pygame.transform.flip(magician_atk_image, True, False)
        shooting_group.add(Bullet(r_image, monster.position, "RIGHT", 10, 10, "magic"))
    elif monster.cycle == 18:
        for i in range(5):
            web = Field(web_image, (0,0))
            random_away_position(monster.position, web)
            field_group.add(web)
    elif monster.cycle == 21:
        monster_con.is_blind = True
    elif monster.cycle == 28:
        monster_con.is_blind = False
    elif monster.cycle == 33:
        spawn_monster(player.position, Mon_frog())
        spawn_monster(player.position, Mon_werewolf())
        spawn_monster(player.position, Mon_firebat())
        spawn_monster(player.position, Mon_book())
    elif 38 < monster.cycle < 44 :
        u_image = pygame.transform.rotozoom(fire_atk_image, 270, 1)
        shooting_group.add(Bullet(u_image, monster.position, "UP", 15, 5, "magic"))
        d_image = pygame.transform.rotozoom(fire_atk_image, 90, 1)
        shooting_group.add(Bullet(d_image, monster.position, "DOWN", 15, 5, "magic"))
        shooting_group.add(Bullet(fire_atk_image, monster.position, "LEFT", 15, 5, "magic"))
        r_image = pygame.transform.flip(fire_atk_image, True, False)
        shooting_group.add(Bullet(r_image, monster.position, "RIGHT", 15, 5, "magic"))
    elif monster.cycle == 49:
        lava = Field(lava_images[2], (0,0))
        random_away_position(monster.position, lava)
        field_group.add(lava)

    elif monster.cycle > 50:
        monster.cycle = 0
    monster.cycle += 1

def monster_die(monster):
    if "boss" in monster.type:
        monster_con.is_blind = False

    if "boss_zombie" in monster.type and monster_con.boss_zombie < 2:
        monster_group.remove(monster)
        spawn_monster(player.position, Boss_zombie())
        monster_con.boss_zombie += 1
    elif "boss_magician" in monster.type and not monster.is_die:
        if monster.activate:
            player.speed += 0.15
    elif "devil_first" in monster.type and not monster.is_die:
        scene_finalboss(True)

    if not monster.is_die:
        monster.is_die = True
        monster.image = monster.die_image
        monster.die_time = pygame.time.get_ticks()

    if pygame.time.get_ticks() - monster.die_time > 300:
        monster_con.mon_count += 1
        drop_item(monster)
        monster_group.remove(monster)

def field_effect(field):
    if not e_rollerskate.activate:
        if field.image == web_image and not field.is_activated:
            player.stop()
        if field.image in lava_images and not field.is_activated:
            player.hp -= 0.2
            if not player.is_die:
                player.image = player_damaged_image

    if field == portal:
        player.stop()
        game_con.saved_floor = game_con.floor
        floor_zero()

    if field == key_field:
        player.stop()
        monster_group.empty()
        shooting_group.empty()
        item_group.empty()
        field_group.empty()
        next_floor(player.position)
        
def bullet_effect(bullet):
    if bullet.type == "web":
        player.stop()
    else:
        pass

##############################################################################################
##### PLAYER CLASS
class Player(Character):
    def __init__(self, image_group, position):
        Character.__init__(self, image_group, position)

        self.life = 5
        self.hp = 100
        self.max_hp = 100
        self.coin = 0
        self.ap = 10
        self.speed = 0.3
        self.punch = punch_d_image
        self.dp = 0
        self.damaged_time = 1

        self.equip_c = None
        self.equip_v = None

        self.time = 0
        self.die_images = player_die_images

    def reset(self):
        self.life = 5
        self.hp = 100
        self.max_hp = 100
        self.coin = 0
        self.ap = 10
        self.speed = 0.3
        self.punch = punch_d_image
        self.dp = 0
        self.damaged_time = 1

        self.equip_c = None
        self.equip_v = None

        self.time = 0
        self.die_images = player_die_images

    def space_bar(self):
        sound_con.play_sound(sound_punch)
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
            sound_con.play_sound(sound_skill)
            self.equip_c.active_skill()
    
    def skill_v(self):
        if self.equip_v:
            sound_con.play_sound(sound_skill)
            self.equip_v.active_skill()

    def damage_sound(self):
        if not self.time:
            self.time = pygame.time.get_ticks()
            sound_con.play_sound(sound_damaged)

        if pygame.time.get_ticks() - self.time > 500:
            self.time = 0

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
    def __init__(self, image, position, direction, speed, damage, type):
        Punch.__init__(self, image, position, direction)
        self.speed = max((speed + monster_con.b_speed), 1)
        self.damage = damage
        self.type = type

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

class GameController():
    def __init__(self):
        self.floor = 0
        self.saved_floor = 1
        self.background = background_zero

        self.tutorial = False
        self.shop = False
        self.inven = False
        self.box = False

        self.devil = False

        self.ending = False
##############################################################################################
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RE : SLIME")
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
D_GREEN = (0,50,0)
BLUE = (0,0,127)
YELLOW = (255,255,0)

main_rect = pygame.Rect(((340,60), (600, 600)))
info_rect = pygame.Rect(((140,60), (200, 600)))
inven_rect = pygame.Rect(((940,60), (200, 600)))
full_rect = pygame.Rect((140,60), (1000,600))

##### PLAYER
player_first_position = (700, 360)
player = Player(player_images, player_first_position)

punch_group = pygame.sprite.Group()

game_con = GameController()

##### MONSTER
shooting_group = pygame.sprite.Group()

##### EQUIP
e_banana.target = player
e_mandoo.target = player
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
            scene_exit(True)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sound_con.play_sound(sound_pick)
                scene_esc(True)

            if not player.is_die:
                if event.key == pygame.K_SPACE:
                    player.space_bar()
                if event.key == pygame.K_c and game_con.floor > 0:
                    player.skill_c()
                if event.key == pygame.K_v and game_con.floor > 0:
                    player.skill_v()
                if event.key == pygame.K_i and game_con.shop:
                    scene_inventory(True)
                # if event.key == pygame.K_o:
                #     if monster_group:
                #         for monster in monster_group:
                #             monster.hp -= 1000
                if event.key == pygame.K_p:
                    scene_ending(True)

        if not player.is_die:
            player_move_key()

    player.move(player.to[0] + player.to[1], player.to[2] + player.to[3], fps)
    
    screen.blit(game_con.background, (340,60))                                                           #BACKGROUND

    milli_time = int((pygame.time.get_ticks() - start_ticks) / 500)
    if a_counter != milli_time:
        #for 0.5 second
        show_animation()
        skill_con.active_time()
    a_counter = milli_time

    if game_con.floor == 0:
        floor_zero()      

    elif game_con.floor > 0:
        bgm_setting(game_con.floor)

        second_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if b_counter != second_time:
            #for 1 second
            player.hp -= player.damaged_time
            
            if not skill_con.active_trafficlight[0]:
                random_monster_direction()
                monster_action()
        b_counter = second_time

        if monster_con.dontmove:
            monster_con.dontmove = False

        if not skill_con.active_trafficlight[0]:
            monster_move()

    for field in field_group:
        field.draw(screen)                                                              #FIELD
        if pygame.sprite.collide_mask(field, player):
            field_effect(field)

    if not monster_group:
        if not game_con.shop:
            pass
        elif game_con.floor > 80 and not game_con.devil:
            pass
        elif game_con.floor == 100:
            pass
        else:
            stair.draw(screen)                                                              #STAIR

            if pygame.sprite.collide_mask(player, stair):
                next_floor(player.position)

    for monster in monster_group:
        monster.draw(screen)                                                           #MONSTER
        if pygame.sprite.collide_mask(player, monster) and not monster.is_die:
            player.hp -= max((monster.ap - player.dp), 0)
            if not player.is_die and not skill_con.active_magiccloak[0]:
                player.damage_sound()
                player.image = player_damaged_image
        if monster.hp <= 0:
            monster_die(monster)
            if len(monster_group) == 0:
                if game_con.floor == 99:
                    stair.rect = stair_images[2].get_rect(center=(screen_width//2, 120))
                else:
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
                monster.damaged(screen)

    for bullet in shooting_group:
        bullet.shoot()
        bullet.draw(screen)                                                              #MONSTER SHOOING
        if pygame.sprite.collide_mask(bullet, player):
            player.hp -= bullet.damage
            bullet_effect(bullet)
            if not player.is_die and not skill_con.active_magiccloak[0]:
                player.damage_sound()
                player.image = player_damaged_image
            shooting_group.remove(bullet)

    for item in item_group:
        item.draw(screen)                                                               #ITEM
        if pygame.sprite.collide_mask(item, player):
            if item.info == "boss_box":
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
                game_con.saved_floor = game_con.floor
                player.is_die = True
                player.change_image_group(player.die_images)
        
    if player.image == player_die_images[3]:
        sound_con.stop_bgm()
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

    if monster_con.is_blind:
        blind_rect = blind_image.get_rect(center=player.position)
        screen.blit(blind_image, blind_rect)
    player.draw(screen)                                                                 #PLAYER

    if game_con.floor > 0 and game_con.floor % 20 == 0 and not monster_con.boss_scene:
        scene_boss(True)
    elif game_con.floor == 81:
        floor_81()

    screen.blit(cover_image, (0,0))
    display_info_ui()
    display_inven_ui()
    
    if running: 
        pygame.display.update()

pygame.quit()