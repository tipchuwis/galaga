import pygame 
from ship import Ship # Del archivo de ship, importa la clase Ship, que es nuestro jugador.


display = pygame.display.set_mode((640, 480)) # Utilizamos métodos y clases de pygame para hacer la pantalla. La sintáxis es altura por anchura.
running = True # Booleano que nos permite CORRER el juego.
fps = 60 # Variable para limitar los fps.
clock = pygame.time.Clock() # Utilizamos pygame para limitar los ticks en el juego.
player = Ship() # Nuestro jugador es la nave, por lo que habrá una variable que acceda a la clase importada.

sprite_group = pygame.sprite.Group() # Accedemos a la propiedad sprite de pygame para poder mover a un grupo de
sprite_group.add(player)             # sprites, y le agregamos el método .Group(). Añadimos al jugador al grupo.

while running: # Mientras que running es cierto, es decir, mientras SIGA CORRIENDO EL JUEGO, actualiza la pantalla.
    # Tick Clock
    clock.tick(fps) # Especificamos los fps con nuestras respectivas variables.
    # Handle Events
    for event in pygame.event.get(): # Por cada evento que pase en el display, guárdalo,
       if event.type == pygame.QUIT:# y si te dicen que lo cierres, pues cierra el jueguito.
            pygame.quit() 
            quit()
    
    # Actualizamos los objetos / Update all the objects
    sprite_group.update()

    # Renderizamos la pantalla / Render the display
    sprite_group.draw(display)

    pygame.display.update()