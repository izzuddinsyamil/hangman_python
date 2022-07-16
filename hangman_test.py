from hangman import *


def test_process_input_char_not_in_word():
    char = 'z'
    word = 'walk'
    masked_word = '____'
    lives = 5

    res_word, res_lives = process_input(char, word, masked_word, lives)

    assert res_lives == 4
    assert res_word == masked_word
