import pygame 
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner

# Pygame Initialization
pygame.font.init()

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
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()

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
    enemy_spawner.update()
    particle_spawner.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score()
        pos = (bullet.rect.x, bullet.rect.y)
        particle_spawner.spawn_particles(pos)
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        player.get_hit()
        enemy[0].hp = 0
        enemy[0].get_hit()
          


    # Render the display
    display.fill(BLACK)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)
    pygame.display.update()