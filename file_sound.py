import pygame

pygame.init()
##############################################################################################
# BGM
bgm_title = pygame.mixer.Sound('Soundtrack\\bgm\\title.wav')
bgm_story = pygame.mixer.Sound('Soundtrack\\bgm\\story.wav')

bgm_0f = pygame.mixer.Sound('Soundtrack\\bgm\\0f.wav')
bgm_first = pygame.mixer.Sound('Soundtrack\\bgm\\first.wav')
##############################################################################################
# EFFECT
sound_page = pygame.mixer.Sound('Soundtrack\\effect\\page.wav')
sound_pick = pygame.mixer.Sound('Soundtrack\\effect\\pick.wav')
sound_wasd = pygame.mixer.Sound('Soundtrack\\effect\\wasd.wav')
sound_exit = pygame.mixer.Sound('Soundtrack\\effect\\exit.wav')

sound_shop_buy = pygame.mixer.Sound('Soundtrack\\effect\\buy.wav')

sound_nextfloor = pygame.mixer.Sound('Soundtrack\\effect\\next_floor.wav')

sound_coin = pygame.mixer.Sound('Soundtrack\\effect\\item_coin.wav')
sound_potion = pygame.mixer.Sound('Soundtrack\\effect\\item_potion.wav')
sound_box = pygame.mixer.Sound('Soundtrack\\effect\\item_box.wav')

sound_punch = pygame.mixer.Sound('Soundtrack\\effect\\player_punch.wav')
sound_damaged = pygame.mixer.Sound('Soundtrack\\effect\\player_damaged.wav')
##############################################################################################
class SoundController():
    def __init__(self):
        self.bgm = None

        self.bgm_volume = 1.0
        self.effect_volume = 1.0        

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