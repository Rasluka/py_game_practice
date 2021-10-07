import pygame
import useful_methods
from pygame import mixer


def show_secret_word(scr, font, secret_word, to_print_str):
    """
        This method will render the word to the screen
    """
    secret_word_location = useful_methods.calculate_x_position(secret_word)
    word_to_screen = font.render(' '.join(to_print_str).upper(), True, (255, 255, 255))
    scr.blit(word_to_screen, secret_word_location)


def show_user_guess(scr, usr_input, font):
    guess_word_location = (376, 450)
    guess_to_screen = font.render(''.join(usr_input).upper(), True, (255, 255, 255))
    scr.blit(guess_to_screen, guess_word_location)


def check_guess(usr_input, secret_word, to_print_str, guessed_counter, guessed_chars):
    was_found = False

    for i in range(len(secret_word)):
        if usr_input[0] == secret_word[i] and not usr_input[0] in guessed_chars:
            to_print_str[i] = secret_word[i]
            was_found = True
            guessed_counter += 1

    if was_found:
        guessed_chars.append(usr_input[0])
        guessed_sound = mixer.Sound('./sound_files/unlock_word.wav')
    else:
        guessed_sound = mixer.Sound('./sound_files/failed_word.wav')

    guessed_sound.play()

    usr_input.pop()

    return guessed_counter


def is_word_already_guessed(secret_word, guessed_counter):
    return guessed_counter >= len(secret_word)
