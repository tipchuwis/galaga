import pygame 
from ship import Ship
import constants as c
from background import BG

# Display setup
display = pygame.display.set_mode((c.DISPLAY_SIZE))
fps = 60
clock = pygame.time.Clock()
BLACK = (0, 0, 0)

# Object setup
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

running = True 
while running:
    # Tick Clock
    clock.tick(fps)
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            quit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = +player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.vel_x = 0
            if event.key == pygame.K_d:
                player.vel_x = 0
    
    # Update all the objects
    bg_group.update()
    sprite_group.update()

    # Render the display
    display.fill(BLACK)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    pygame.display.update()