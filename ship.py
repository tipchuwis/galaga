import pygame
from pygame.locals import *
from bullet import Bullet
import constants as c

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('ship.png').convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.15, self.image.get_height()*0.15))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2 
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.bullets = pygame.sprite.Group()
        self.vel_x = 0        
        self.vel_y = 0        
        self.speed = 5
        self.image.set_colorkey([0,255,23])

    def update(self):
        self.bullets.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)