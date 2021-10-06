import pygame
import useful_methods
import game_logic

pygame.init()

# Creating the screen resolution, background and some on
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman!')
game_icon = pygame.image.load('./img_files/hangman-game.png')
pygame.display.set_icon(game_icon)

is_running = True
is_word_gen = False

secret_word = useful_methods.generate_word()
print(secret_word)

# user guess
user_guess = []

while is_running:

    if not is_word_gen:
        game_logic.show_secret_word(screen, secret_word)
        is_word_gen = True

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key)

            if key_pressed.isalpha() and len(key_pressed) == 1:
                user_guess.append(key_pressed)
                print(user_guess)
                game_logic.show_user_guess(screen, user_guess, key_pressed, secret_word)

            if key_pressed == 'backspace' and len(user_guess) > 0:
                game_logic.show_user_guess(screen, user_guess, key_pressed, secret_word)
                print(user_guess)


    pygame.display.update()
