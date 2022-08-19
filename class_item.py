import pygame
from file_image import *
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

class ItemController():
    def __init__(self):
        self.prob_portion = 10
        self.prob_coin = 10
##############################################################################################

i_c = ItemController()

##### ITEM
item_group = pygame.sprite.Group()