import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('enemy.png').convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.25, self.image.get_height()*0.25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 3
        self.vel_x = 0
        self.score_value = 5
        self.vel_y = random.randrange(3, 8)
        self.image.set_colorkey([0,255,0])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1        
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()