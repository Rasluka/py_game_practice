import random


def generate_word():
    """
        This method will take all the word in a .txt file to create a list and then return
        a random word within the list.
    """
    word_library_file = open('./game_files/word_library.txt', 'r')
    words_list = [word.strip() for word in word_library_file]
    word_library_file.close()

    return words_list[random.randint(0, len(words_list) - 1)]


def calculate_x_position(secret_word):
    word_len_in_screen = len(secret_word) * 48
    x_positioning = (800 - word_len_in_screen) / 2

    return x_positioning, 250


def show_score(screen, font, score):
    score_to_screen = font.render(f'Guessed Words: {score}', True, (255, 255, 255))
    screen.blit(score_to_screen, (0, 0))

