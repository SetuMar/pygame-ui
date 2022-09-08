import pygame
import sys

import menu
 
screen_size = [800, 800]
pygame.init()
 
display = pygame.display.set_mode((screen_size))
clock = pygame.time.Clock()

m = menu.Menu(pygame.math.Vector2(200, 200))

while True:
    display.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    m.lerp_container(pygame.math.Vector2(500, 500), 0.1)

    m.draw_container(display)

    pygame.display.update()
    clock.tick(60)