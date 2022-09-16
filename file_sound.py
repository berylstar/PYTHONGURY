import pygame

pygame.init()

# BGM
bgm_title = pygame.mixer.Sound('Soundtrack\\bgm\\title.mp3')
bgm_story = pygame.mixer.Sound('Soundtrack\\bgm\\story.wav')

bgm_0f = pygame.mixer.Sound('Soundtrack\\bgm\\0f.wav')
bgm_first = pygame.mixer.Sound('Soundtrack\\bgm\\first.wav')

# EFFECT
sound_page = pygame.mixer.Sound('Soundtrack\\effect\\page.mp3')
sound_pick = pygame.mixer.Sound('Soundtrack\\effect\\pick.mp3')
sound_wasd = pygame.mixer.Sound('Soundtrack\\effect\\wasd.wav')

sound_shop_buy = pygame.mixer.Sound('Soundtrack\\effect\\shop_buy.mp3')

punch_sound = pygame.mixer.Sound("Sound\\Sound_Effect\\Slime\\Skill\\Skill_punch_1.wav")

class SoundController():
    def __init__(self):
        self.volume = 1
        self.playing = False

    def play_bgm(self, bgm):
        if not self.playing:
            bgm.play(-1)
            self.playing = True

    def stop_bgm(self, bgm):
        bgm.stop()
        self.playing = False

sound_con = SoundController()
pygame.quit()