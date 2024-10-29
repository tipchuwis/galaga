import pygame
import constants as c

class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.img_heart_01 = pygame.image.load('heart_01.png').convert()
        self.img_heart_02 = pygame.image.load('heart_02.png').convert()
        self.img_heart_03 = pygame.image.load('heart_03.png').convert()
        self.img_heart_04 = pygame.image.load('heart_04.png').convert()
        self.img_heart_05 = pygame.image.load('heart_05.png').convert()
        self.anim_list = [self.img_heart_01,
                          self.img_heart_02,
                          self.img_heart_03,
                          self.img_heart_04,
                          self.img_heart_05]
        self.img_heart_01.set_colorkey([0,255,0])
        self.img_heart_02.set_colorkey([0,255,0])
        self.img_heart_03.set_colorkey([0,255,0])
        self.img_heart_04.set_colorkey([0,255,0])
        self.img_heart_05.set_colorkey([0,255,0])
        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 5
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 12

    def update(self):
        if self.frame_duration == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration
        self.frame_duration -= 1
        
