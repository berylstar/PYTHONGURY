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

class Torch(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.torch_image = torch_images[0]
        self.light_image = light_image
        self.position = position

        self.torch_rect = self.torch_image.get_rect(center=position)
        self.light_rect = self.light_image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.light_image, self.light_rect)
        screen.blit(self.torch_image, self.torch_rect)
##############################################################################################

##### FIELD
stair_zero_floor = (640, 90)
stair = Field(stair_images[0], stair_zero_floor)

light_pos = (440, 150)
torch = Torch(light_pos)

field_group = pygame.sprite.Group()
field_group.add(torch)