import pygame

pygame.init()
# BGM
bgm_intro = pygame.mixer.Sound('Sound\\Main_THEME_1.mp3')
bgm_intro.set_volume(0.2)

bgm_main = pygame.mixer.Sound('Sound\\BGM\\Stage_bgm\\Stage_bgm_3.mp3')
bgm_main.set_volume(0.2)

# EFFECT SOUND
punch_sound = pygame.mixer.Sound("Sound\\Effect_sound\\Player\\Skill\\punch_1.wav")
pygame.quit()