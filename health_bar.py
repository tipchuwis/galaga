import pygame
import constants as c

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar, self).__init__()
        self.image = pygame.image.load('healthbar.png').convert()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.image.set_colorkey([0,255,0])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y