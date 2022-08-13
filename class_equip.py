import pygame
import os
##############################################################################################
##############################################################################################
##### PUNCH CLASS
class Punch(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = image
        self.position = position
        self.direction = direction
        
        self.rect = image.get_rect(center=position)
        self.time = pygame.time.get_ticks()

    def get_time(self):
        return pygame.time.get_ticks() - self.time

    def draw(self, screen, object):
        if self.direction == "LEFT":
            self.rect = (object.rect.x-60, object.rect.y)
        elif self.direction == "RIGHT":
            self.rect = (object.rect.x+60, object.rect.y)
        elif self.direction == "UP":
            self.rect = (object.rect.x, object.rect.y-60)
        elif self.direction == "DOWN":
            self.rect = (object.rect.x, object.rect.y+60)

        screen.blit(self.image, self.rect)

### Shooter CLASS
class Shooter(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = image
        self.position = position
        self.direction = direction
        
        self.rect = image.get_rect(center=position)

    def draw(self, screen, object):
        if self.direction == "LEFT":
            self.rect = (object.rect.x-60, object.rect.y)
        elif self.direction == "RIGHT":
            self.rect = (object.rect.x+60, object.rect.y)
        elif self.direction == "UP":
            self.rect = (object.rect.x, object.rect.y-60)
        elif self.direction == "DOWN":
            self.rect = (object.rect.x, object.rect.y+60)

        screen.blit(self.image, self.rect)
##############################################################################################
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
file_path = os.path.dirname(__file__)

punch_d_image = pygame.image.load(os.path.join(file_path, "images\\punch.png")).convert_alpha()
punch_v_image = pygame.image.load(os.path.join(file_path, "images\\punch_v.png")).convert_alpha()
punch_f_image = pygame.image.load(os.path.join(file_path, "images\\punch_f.png")).convert_alpha()

sold_out_image = pygame.image.load(os.path.join(file_path, "images\\sold_out.png")).convert_alpha()