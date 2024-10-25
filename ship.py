import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite): # Esta es la clase que va a hacer que nuestra navecita se genere y aparezca
    def __init__(self):           # en la pantalla, también definimos la velocidad inicial de la nave en x y y.
        super(Ship, self).__init__() # Y comenzamos a importar la imagen que usaremos para la nave.
        self.image = pygame.image.load('ship.png').convert() # convert optimiza la imagen en el juego.
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.15, self.image.get_height()*0.15)) # transform utiliza a scale_by para escalar la imagen como nosotros necesitemos.
        self.rect = self.image.get_rect() # Así le decimos que obtenga las propiedades rectangulares de la imagen y las haga una propiedad de la imagen.
        self.rect.x = 640//2 # Con self.rect.x y self.rect.y le damos coordenadas a la nave y lo ubican en el centro
        self.rect.y = 480 - self.rect.height # abajo en la pantalla.
        self.vel_x = 0        # .get_rect() consigue las propiedades rectangulares de la imagen para que podamos
        self.vel_y = 0        # acceder a ellas fácilmente más tarde.
        self.speed = 5
        self.image.set_colorkey([0,255,23])

    def update(self): # Esta clase va a correr los frames de nuestro objeto, que es la nave.
        self.rect.x += self.vel_x # Por cada frame del juego, la coordenada en x y/o y se actualiza y aparenta
        self.rect.y += self.vel_y # estar animado el objeto.