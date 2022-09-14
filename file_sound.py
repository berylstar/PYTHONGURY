import pygame

pygame.init()

# BGM
bgm_intro = pygame.mixer.Sound('Sound\\Main_THEME_1.mp3')
bgm_intro.set_volume(0.1)

bgm_main = pygame.mixer.Sound('Sound\\BGM\\Stage_bgm\\Stage_bgm_3.mp3')
bgm_main.set_volume(0.01)

# EFFECT
punch_sound = pygame.mixer.Sound("Sound\\Sound_Effect\\Slime\\Skill\\Skill_punch_1.wav")


pygame.quit()