import pygame
from pygame import mixer
import useful_methods
from game_logic import check_guess
from game_logic import show_secret_word
from game_logic import show_user_guess
from game_logic import is_word_already_guessed
import time

# Initializing the game
pygame.init()

# Creating the screen resolution, game title, background and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman!')
game_icon = pygame.image.load('./img_files/hangman-game.png')
pygame.display.set_icon(game_icon)
background = pygame.image.load('./img_files/bg.jpg')

# background sound
mixer.music.load('./sound_files/Stephen_Foster_-_Beautiful_Dreamer.wav')
mixer.music.play(-1)

# Font
big_font = pygame.font.Font('./game_files/SPACE_EXPLORER.ttf', 48)
mid_font = pygame.font.Font('./game_files/SPACE_EXPLORER.ttf', 24)

is_running = True
reset_game = False

# Initializing vars
score = 0
user_guess = []
secret_word = useful_methods.generate_word()
to_print_str = ['_' for char in secret_word]
guessed_counter = 0
guessed_chars = []
remaining_attempts = len(secret_word) * 2

while is_running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if remaining_attempts > 0:
            print(secret_word)

            if event.type is pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)

                if key_pressed.isalpha() and len(key_pressed) == 1 and len(user_guess) == 0:
                    user_guess.append(key_pressed)

                if key_pressed == 'backspace' and len(user_guess) > 0:
                    user_guess.pop()

                if len(user_guess) > 0 and (key_pressed == 'enter' or key_pressed == 'return'):
                    screen.fill((0, 0, 0))
                    guessed_counter, remaining_attempts = check_guess(user_guess, secret_word, to_print_str,
                                                                      guessed_counter, guessed_chars,
                                                                      remaining_attempts)

                if is_word_already_guessed(secret_word, guessed_counter):
                    secret_word = useful_methods.generate_word()
                    reset_game = False
                    user_guess = []
                    to_print_str = ['_' for char in secret_word]
                    guessed_counter = 0
                    guessed_chars = []
                    score += 1
                    remaining_attempts = len(secret_word) * 2

                if remaining_attempts == 0:
                    game_over_sound = mixer.Sound('./sound_files/game_over.wav')
                    game_over_sound.play()
                    game_over_to_screen = big_font.render('GAME OVER', True, (255, 255, 255))
                    screen.blit(game_over_to_screen, (200, 250))

                    is_running = False

    if remaining_attempts > 0:
        show_secret_word(screen, big_font, secret_word, to_print_str)
        show_user_guess(screen, user_guess, mid_font)

    useful_methods.show_remaining_attempts(screen, mid_font, remaining_attempts)
    useful_methods.show_score(screen, mid_font, score)

    pygame.display.update()
    if remaining_attempts == 0:
        time.sleep(3)