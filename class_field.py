import pygame
from file_image import *
##############################################################################################

##############################################################################################
##### stair class
class Field(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.rect = image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
##############################################################################################

##### FIELD
stair_zero_floor = (640, 90)
stair = Field(stair_images[0], stair_zero_floor)

field_group = pygame.sprite.Group()