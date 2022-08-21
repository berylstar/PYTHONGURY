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

        # self.rect = image.get_rect(center=position)
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

class ItemController():
    def __init__(self):
        self.prob_portion = 10
        self.portion_eff = 5


        self.prob_coin = 10
##############################################################################################

item_con = ItemController()

##### ITEM
item_group = pygame.sprite.Group()

item_portion = Item(item_images[0], (0,0), "portion")
item_coin = Item(item_images[1], (0,0), "coin")

item_box = Item(box_image, (0,0), "box")