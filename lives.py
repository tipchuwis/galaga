import pygame
import constants as c

class Lives(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()
        self.num_lives = num_lives
        self.width = 80
        self.height = 40
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey([0,0,0])
        self.ship_image = pygame.image.load('ship.png').convert()
        self.ship_image = pygame.transform.scale_by(self.ship_image, (self.ship_image.get_width()*0.07, self.ship_image.get_height()*0.07))
        self.ship_image.set_colorkey([0,255,23])

        self.image.blit(self.ship_image, (40, 10))
        self.font_size = 20
        self.font = pygame.font.Font(None, self.font_size)
        self.font_color = (255, 255, 255)
        self.lives_counter = self.font.render(f'x {self.num_lives}', False, self.font_color, False)
        self.image.blit(self.lives_counter, (10,15))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def decrement_life(self):
        self.num_lives -= 1
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey([0,0,0])
        self.image.blit(self.ship_image, (40, 10))
        self.lives_counter = self.font.render(f'x {self.num_lives}', False, self.font_color, False)
        self.image.blit(self.lives_counter, (10,15))

