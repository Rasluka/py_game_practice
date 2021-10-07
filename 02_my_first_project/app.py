import pygame
import useful_methods
from game_logic import check_guess
from game_logic import show_secret_word
from game_logic import show_user_guess
from game_logic import is_word_already_guessed

# Initializing the game
pygame.init()

# Creating the screen resolution, game title, background and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman!')
game_icon = pygame.image.load('./img_files/hangman-game.png')
pygame.display.set_icon(game_icon)

# Font
big_font = pygame.font.Font('freesansbold.ttf', 64)
mid_font = pygame.font.Font('freesansbold.ttf', 32)

is_running = True
reset_game = False

# Initializing vars
score = 0
user_guess = []
secret_word = useful_methods.generate_word()
to_print_str = ['_' for char in secret_word]
guessed_counter = 0
guessed_chars = []

while is_running:

    if not reset_game:
        reset_game = True

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key)

            if key_pressed.isalpha() and len(key_pressed) == 1 and len(user_guess) == 0:
                user_guess.append(key_pressed)

            if key_pressed == 'backspace' and len(user_guess) > 0:
                screen.fill((0, 0, 0))
                user_guess.pop()

            if len(user_guess) > 0 and (key_pressed == 'enter' or key_pressed == 'return'):
                screen.fill((0, 0, 0))
                guessed_counter = check_guess(user_guess, secret_word, to_print_str, guessed_counter, guessed_chars)

            if is_word_already_guessed(secret_word, guessed_counter):
                screen.fill((0, 0, 0))

                # game_over_location = (376, 450)
                # game_over_to_screen = font.render('GAME OVER', True, (255, 255, 255))
                # screen.blit(game_over_to_screen, game_over_location)

                reset_game = False
                user_guess = []
                to_print_str = ['_' for char in secret_word]
                guessed_counter = 0
                guessed_chars = []
                score += 1

    show_secret_word(screen, big_font, secret_word, to_print_str)
    show_user_guess(screen, user_guess, mid_font)
    useful_methods.show_score(screen, mid_font, score)
    pygame.display.update()
