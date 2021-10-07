import pygame
import useful_methods
import game_logic
from pygame import mixer

# Initializing the game
pygame.init()

# Creating the screen resolution, background and some on
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman!')
game_icon = pygame.image.load('./img_files/hangman-game.png')
pygame.display.set_icon(game_icon)

is_running = True
is_word_gen = False
score = 0

while is_running:

    if not is_word_gen:
        user_guess = []
        secret_word = useful_methods.generate_word()
        to_print_str = ['_' for char in secret_word]
        guessed_chars = 0
        print(secret_word)
        game_logic.show_secret_word(screen, secret_word, to_print_str)
        is_word_gen = True

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key)

            if key_pressed.isalpha() and len(key_pressed) == 1 and len(user_guess) == 0:
                user_guess.append(key_pressed.upper())
                print(user_guess)

            if key_pressed == 'backspace' and len(user_guess) > 0:
                screen.fill((0, 0, 0))
                user_guess.pop()

            if len(user_guess) > 0 and (key_pressed == 'enter' or key_pressed == 'return'):
                screen.fill((0, 0, 0))
                guessed_chars = game_logic.check_guess_in_word(user_guess, secret_word, to_print_str, guessed_chars)
                print(f'Guessed words: {guessed_chars}')

            game_logic.show_secret_word(screen, secret_word, to_print_str)
            game_logic.show_user_guess(screen, user_guess, key_pressed, secret_word, to_print_str)

            if game_logic.is_word_already_guessed(secret_word, guessed_chars):
                print('Word has been guessed!')
                screen.fill((0, 0, 0))
                # font = pygame.font.Font('freesansbold.ttf', 64)
                # game_over_location = (376, 450)
                # game_over_to_screen = font.render('GAME OVER', True, (255, 255, 255))
                # screen.blit(game_over_to_screen, game_over_location)

                is_word_gen = False
                user_guess = []
                to_print_str = ['_' for char in secret_word]
                guessed_chars = 0


    pygame.display.update()
