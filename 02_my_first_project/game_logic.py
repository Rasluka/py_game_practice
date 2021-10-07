import pygame
import useful_methods
from pygame import mixer


def show_secret_word(scr, secret_word, to_print_str):
    """
        This method will render the word to the screen
    """
    font = pygame.font.Font('freesansbold.ttf', 48)
    secret_word_location = useful_methods.calculate_x_position(secret_word)
    word_to_screen = font.render(' '.join(to_print_str), True, (255, 255, 255))
    scr.blit(word_to_screen, secret_word_location)


def show_user_guess(scr, usr_input, key_pressed, secret_word, to_print_str):
    font = pygame.font.Font('freesansbold.ttf', 48)
    guess_word_location = (376, 450)
    guess_to_screen = font.render(''.join(usr_input), True, (255, 255, 255))

    scr.blit(guess_to_screen, guess_word_location)


def check_guess_in_word(usr_input, secret_word, to_print_str, guessed_words):
    was_found = False

    for i in range(len(secret_word)):

        if usr_input[0].lower() == secret_word[i].lower():
            to_print_str[i] = secret_word[i].upper()
            was_found = True
            guessed_words += 1

    if was_found:
        guessed_sound = mixer.Sound('./sound_files/unlock_word.wav')
    else:
        guessed_sound = mixer.Sound('./sound_files/failed_word.wav')

    guessed_sound.play()

    usr_input.pop()

    return guessed_words


def is_word_already_guessed(secret_word, guessed_words):
    return guessed_words >= len(secret_word)
