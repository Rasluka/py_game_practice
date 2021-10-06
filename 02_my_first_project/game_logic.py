import pygame
import useful_methods


def show_secret_word(scr, secret_word):
    """
        This method will render the word to the screen
    """
    to_print_str = ['_' for char in secret_word]

    font = pygame.font.Font('freesansbold.ttf', 48)
    secret_word_location = (200, 250)
    word_to_screen = font.render(' '.join(to_print_str), True, (255, 255, 255))
    scr.blit(word_to_screen, secret_word_location)


def show_user_guess(scr, usr_input, key_pressed, secret_word):
    font = pygame.font.Font('freesansbold.ttf', 48)
    guess_word_location = (200, 450)
    guess_to_screen = font.render(''.join(usr_input), True, (255, 255, 255))

    scr.blit(guess_to_screen, guess_word_location)

    if key_pressed == 'backspace' and len(usr_input) > 0:
        scr.fill((0, 0, 0))
        show_secret_word(scr, secret_word)
        usr_input.pop()
        guess_to_screen = font.render(''.join(usr_input), True, (255, 255, 255))
        scr.blit(guess_to_screen, guess_word_location)
