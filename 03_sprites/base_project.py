import sys
import pygame

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
