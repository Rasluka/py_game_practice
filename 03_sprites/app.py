import sys
import pygame
from pygame import mixer
import random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gun_shoot = mixer.Sound('./sound_files/gunshot.wav')

    def shoot(self):
        self.gun_shoot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('./img_files/bg_blue.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair('./img_files/crosshair_white.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('./img_files/target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
