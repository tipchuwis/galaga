import pygame
from pygame.locals import *
from bullet import Bullet
import constants as c
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('ship.png').convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.15, self.image.get_height()*0.15))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.bullets = pygame.sprite.Group()
        self.max_hp = 10
        self.lives = 3
        self.hp = self.max_hp
        self.hud = HUD(self.hp, self.lives)
        self.hud_group = pygame.sprite.Group()
        #self.hud_group.add(self.hud)
        self.vel_x = 0        
        self.vel_y = 0        
        self.speed = 5
        self.image.set_colorkey([0,255,23])

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 1
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)
    
    def get_hit(self):
        self.hp -= 1
        self.hud.health_bar.decrease_hp_value()
        if self.hp <=0:
            self.hp = 0
            self.death()

    def death(self):
        self.lives -=1
        if self.lives <=0:
            self.lives = 0
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()