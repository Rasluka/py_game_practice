from typing import Collection
import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space_bg_2.jpg')

# Background sound
mixer.music.load('./sound_files/background.wav')
mixer.music.play(-1)

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

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    enemy_img.append(pygame.image.load('ufo.png'))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Importing Bullet img
bullet_img = pygame.image.load('bullet_2.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 0.35
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollition(e_x, e_y, b_x, b_y):
    distance = math.sqrt( (math.pow(e_x - b_x, 2)) + (math.pow(e_y - b_y, 2)))

    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    #screen.fill((153, 0, 0))

    # Background image
    screen.blit(background, (0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystoke is pressed check whether its right of left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

            if event.key == pygame.K_UP:
                player_y_change = -0.5

            if event.key == pygame.K_DOWN:
                player_y_change = 0.5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('./sound_files/laser.wav')
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)


    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_x_change = 0
                player_y_change = 0
    #
    player_x += player_x_change
    player_y += player_y_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if player_y <= 0:
        player_y = 0
    elif player_y >= 536:
        player_y = 536

    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemy_y[i] > 200:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000

            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i] 
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i] 

        # Collision
        collision = isCollition(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0,735)
            enemy_y[i] = random.randint(50,150)
            explosion_sound = mixer.Sound('./sound_files/explosion.wav')
            explosion_sound.play()

        enemy(enemy_x[i], enemy_y[i], i)

    # bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change


    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()