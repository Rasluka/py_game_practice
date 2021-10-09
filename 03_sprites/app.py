import sys
import pygame


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('./img_files/bg_green.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Crosshair
crosshair = Crosshair(50, 50, 100, 100, (255, 0, 255))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    crosshair_group.draw(screen)
    clock.tick(60)
