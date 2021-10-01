import pygame
import os

os.system('clear')

# Initialize the pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Star Invaders')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480

player_x_change = 0
player_y_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((153, 0, 0))

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystoke is pressed check whether its right of left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print('Pressing left arrow')
                player_x_change = -0.5
            
            if event.key == pygame.K_RIGHT:
                # print('Pressing right arrow')
                player_x_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('Keystoke has been released')
                player_x_change = 0
    #
    player_x += player_x_change
    
    if player_x <= 0:
        player_x = 0
        print('Reach the left limit')

    if player_x >= 736:
        player_x = 736
        print('Reach the right limit')
    
    player(player_x, player_y)
    pygame.display.update()