import random
import pygame

def generate_word():
    """
        This method will take all the word in a .txt file to create a list and then return
        a random word within the list.
    """
    word_library_file = open('./game_files/word_library.txt', 'r')
    words_list = [word.strip() for word in word_library_file]
    word_library_file.close()

    return words_list[random.randint(0, len(words_list)-1)]




