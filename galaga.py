import pygame 

display = pygame.display.set_mode((640, 480)) # Utilizamos métodos y clases de pygame para hacer la pantalla. La sintáxis es altura por anchura.
running = True # Booleano que nos permite CORRER el juego.
fps = 60 # Variable para limitar los fps.
clock = pygame.time.Clock() # Utilizamos pygame para limitar los ticks en el juego.


while running: # Mientras que running es cierto, es decir, mientras SIGA CORRIENDO EL JUEGO, actualiza la pantalla.
    clock.tick(fps) # Especificamos los fps con nuestras respectivas variables.
    for event in pygame.event.get(): # Por cada evento que pase en el display, guárdalo,
       if event.type == pygame.QUIT:# y si te dicen que lo cierres, pues cierra el jueguito.
            pygame.quit() 
            quit()

    pygame.display.update()