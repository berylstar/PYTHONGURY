import pygame
from file_image import *
##############################################################################################
##### stair class
class Field(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.position = position

        self.is_activated = 0

        self.rect = image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 데코용
class Torch(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.torch_image = torch_image
        self.light_image = light_images[0]
        self.position = position

        self.torch_rect = self.torch_image.get_rect(center=position)
        self.light_rect = self.light_image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.light_image, self.light_rect)
        screen.blit(self.torch_image, self.torch_rect)

    def image_update(self):
        if self.light_image == light_images[0]:
            self.light_image = light_images[1]
        else:
            self.light_image = light_images[0]
##############################################################################################

##### FIELD
stair_zero_floor = (640, 90)
stair = Field(stair_images[0], stair_zero_floor)

mand = Field(mushroom_image, stair_zero_floor)  #keys, rope field 만들어줘야함

torch_zero_pos = (440, 150)
torch = Torch(torch_zero_pos)

field_group = pygame.sprite.Group()