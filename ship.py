import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite): # Esta es la clase que va a hacer que nuestra navecita se genere y aparezca
    def __init__(self):           # en la pantalla, también definimos la velocidad inicial de la nave en x y y.
        super(Ship, self).__init__() # Y comenzamos a importar la imagen que usaremos para la nave.
        self.image = pygame.image.load('ship.png').convert() # conver_alpha() sirve para que se optimice la
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.15, self.image.get_height()*0.15))
        self.rect = self.image.get_rect()                          # imagen en el juego y continue siendo transparente.
        self.vel_x = 0        # .get_rect() consigue las propiedades rectangulares de la imagen para que podamos
        self.vel_y = 0        # acceder a ellas fácilmente más tarde.
        self.speed = 5
        self.image.set_colorkey([0,255,23])

    def update(self): # Esta clase va a correr los frames de nuestro objeto, que es la nave.
        self.rect.x += self.vel_x # Por cada frame del juego, la coordenada en x y/o y se actualiza y aparenta
        self.rect.y += self.vel_y # estar animado el objeto.