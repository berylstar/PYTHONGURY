import pygame

pygame.init()
##############################################################################################
# BGM
bgm_title = pygame.mixer.Sound('Soundtrack\\bgm\\title.wav')
bgm_story = pygame.mixer.Sound('Soundtrack\\bgm\\story.wav')

bgm_0f = pygame.mixer.Sound('Soundtrack\\bgm\\0f.wav')
bgm_first = pygame.mixer.Sound('Soundtrack\\bgm\\first.wav')
bgm_second = pygame.mixer.Sound('Soundtrack\\bgm\\second.wav')
bgm_third = pygame.mixer.Sound('Soundtrack\\bgm\\third.wav')
bgm_fourth = pygame.mixer.Sound('Soundtrack\\bgm\\fourth.wav')
bgm_fifth = pygame.mixer.Sound('Soundtrack\\bgm\\fifth.wav')

bgm_boss = pygame.mixer.Sound('Soundtrack\\bgm\\boss.wav')
bgm_finalboss = pygame.mixer.Sound('Soundtrack\\bgm\\boss_final.wav')
##############################################################################################
# EFFECT
sound_page = pygame.mixer.Sound('Soundtrack\\effect\\page.wav')
sound_pick = pygame.mixer.Sound('Soundtrack\\effect\\pick.wav')
sound_wasd = pygame.mixer.Sound('Soundtrack\\effect\\wasd.wav')
sound_exit = pygame.mixer.Sound('Soundtrack\\effect\\exit.wav')

sound_shop_open = pygame.mixer.Sound('Soundtrack\\effect\\shop_open.wav')
sound_shop_close = pygame.mixer.Sound('Soundtrack\\effect\\shop_close.wav')
sound_shop_buy = pygame.mixer.Sound('Soundtrack\\effect\\shop_buy.wav')
sound_shop_refresh = pygame.mixer.Sound('Soundtrack\\effect\\shop_reroll.wav')

sound_inven_open = pygame.mixer.Sound('Soundtrack\\effect\\inven_open.wav')
sound_inven_close = pygame.mixer.Sound('Soundtrack\\effect\\inven_close.wav')
sound_inven_click = pygame.mixer.Sound('Soundtrack\\effect\\inven_click.wav')
sound_inven_active = pygame.mixer.Sound('Soundtrack\\effect\\inven_active.wav')
sound_equip_remove = pygame.mixer.Sound('Soundtrack\\effect\\equip_remove.wav')

sound_nextfloor = pygame.mixer.Sound('Soundtrack\\effect\\next_floor.wav')

sound_coin = pygame.mixer.Sound('Soundtrack\\effect\\item_coin.wav')
sound_potion = pygame.mixer.Sound('Soundtrack\\effect\\item_potion.wav')
sound_box_open = pygame.mixer.Sound('Soundtrack\\effect\\box_open.wav')
sound_box_close = pygame.mixer.Sound('Soundtrack\\effect\\box_close.wav')
sound_box_get = pygame.mixer.Sound('Soundtrack\\effect\\box_get.wav')

sound_punch = pygame.mixer.Sound('Soundtrack\\effect\\punch.wav')
sound_skill = pygame.mixer.Sound('Soundtrack\\effect\\skill.wav')
sound_damaged = pygame.mixer.Sound('Soundtrack\\effect\\player_damaged.wav')
sound_die = pygame.mixer.Sound('Soundtrack\\effect\\player_die.wav')
sound_reborn = pygame.mixer.Sound('Soundtrack\\effect\\reborn.wav')
##############################################################################################
class SoundController():
    def __init__(self):
        self.bgm = None

        self.bgm_volume = 1
        self.effect_volume = 1

    def play_bgm(self, bgm):
        if self.bgm:
            self.stop_bgm()
        bgm.set_volume(self.bgm_volume)
        bgm.play(-1)
        self.bgm = bgm

    def stop_bgm(self):
        self.bgm.stop()
        self.bgm = None

    def play_sound(self, effect):
        effect.set_volume(self.effect_volume)
        effect.play()
##############################################################################################
sound_con = SoundController()
pygame.quit()