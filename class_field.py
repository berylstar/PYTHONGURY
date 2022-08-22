import pygame
from file_image import *
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
        self.is_collision = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
##############################################################################################

##### FIELD
stair_zero_floor = (640, 90)
stair = Stair(stair_images[0], stair_zero_floor)

field_web = f_Web(web_image, (540,550))

field_group = pygame.sprite.Group()
field_group.add(field_web)