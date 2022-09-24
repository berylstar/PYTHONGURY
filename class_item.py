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
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

class ItemController():
    def __init__(self):
        self.prob_potion = 10
        self.potion_eff = 10

        self.prob_coin = 10
        self.red_coin = False
##############################################################################################

item_con = ItemController()

##### ITEM
item_group = pygame.sprite.Group()