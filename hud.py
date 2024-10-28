import pygame
import constants as c
from health_bar import HealthBar 
from score import Score
from lives import Lives

class HUD(pygame.sprite.Sprite):
    def __init__(self, hp, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load('hud_bg.png').convert()
        self.rect = self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.image.set_colorkey([0,255,0])
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 9
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.lives = Lives(num_lives)
        self.icon_group = pygame.sprite.Group()
        self.icon_group.add(self.lives)


    def update(self):
        self.health_bar_group.update()
        self.icon_group.update()
        self.score_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y