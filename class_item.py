import pygame
import os
import random
##############################################################################################
##### ITEM CLASS
class Item(pygame.sprite.Sprite):
    def __init__(self, image, position, info):
        super().__init__()
        self.image = image
        self.position = position
        self.info = info

        self.rect = image.get_rect(center=position)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
##############################################################################################
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

PROB_PORTION = 10
PROB_COIN = 10

item_images = [
    pygame.image.load(os.path.join(file_path, "images\\portion.png")).convert_alpha(),
    pygame.image.load(os.path.join(file_path, "images\\coin.png")).convert_alpha()
]