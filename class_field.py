import pygame
from project_image import *
##############################################################################################

##############################################################################################
##### stair class
class Stair(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

##### web class
class f_Web(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)
        self.activated = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
##############################################################################################

field_web = f_Web(web_image, (540,550))