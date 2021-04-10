import random
import math

words = [
    'abruptly', 'absurd',
    'bagpipes', 'bandwagon',
    'cycle', 'dwarves',
    'kayak', 'zigzag',
    'subway', 'matrix',
    'galaxy'
]

hangman = {
    5 : """
    |----
    |   |
    |
    |
    |
    |
    """,
    4: """
    |----
    |   |
    |   O
    |  
    |
    |
    """,
    3: """
    |----
    |   |
    |   O
    |  /|
    |
    | 
    """,
    2: """
    |----
    |   |
    |   O
    |  /|\\
    |
    |
    """,
    1: """
    |----
    |   |
    |   O
    |  /|\\
    |  /
    |
    """,
    0: """
    |----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    """
}

def main():
    # get word randomly from words
    # then generate masked word from the chosed word
    idx = random.randint(0, len(words) - 1)
    word = words[idx]

    masked_word = generate_masked_word(word)

    lives = len(hangman) - 1

    while True:
        if '_' not in masked_word:
            break
            
        if lives <= 0:
            print(hangman[lives])
            break
        
        print(hangman[lives])
        print(masked_word)
        print('Lives :', lives)
        user_input = input('Input your guess: ')
        masked_word, lives = process_input(user_input, word, masked_word, lives)

        print('')
    
    if lives <= 0:
        print('You run out of lives, guess better next time')
    else:
        print('You guessed the word!')

    print('The word is:', word)

def generate_masked_word(word):
    masked_word = '_' * len(word)

    masked_word_arr = [i for i in masked_word]

    word_chars = list(set(word))

    # the number of revelead words will be 50% of the word's length
    revelead_char_length = math.floor(0.5 * len(word_chars))

    # pick one random char from word_chars
    picked_char = []
    while len(picked_char) < revelead_char_length:
        rand_char = random.choice(word_chars)
        if rand_char not in picked_char:
            picked_char.append(rand_char)


    for c in picked_char:
        for i in range(len(word)):
            if word[i] == c:
                masked_word_arr[i] = c

    return ''.join(masked_word_arr)


def process_input(input_char, word, masked_word, lives):
    if input_char not in word:
        lives -= 1
        return masked_word, lives

    masked_word_arr = [i for i in masked_word]

    for i in range(len(word)):
        if word[i] == input_char:
            masked_word_arr[i] = input_char

    return ''.join(masked_word_arr), lives


if __name__ == "__main__":
    main()
