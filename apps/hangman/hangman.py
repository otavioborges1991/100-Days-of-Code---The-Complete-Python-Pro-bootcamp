from random import choice
from utilities.console import clear
from hangman_ascii_art import hangman


def main():
    file = open('hangman_words.txt')
    words = []
    for line in file.read().splitlines():
        words.append(f'{line}')

    word_list = words
    hidden_word = []
    result = 'wrong'
    number = 0
    misses = 0

    chosen_word = choice(word_list)
    for char in chosen_word:
        hidden_word.append('_')

    clear()
    while True:
        number = 0
        print(hangman[misses])
        result = 'wrong'
        print(''.join(hidden_word))
        print(f'{misses} tries left!')
        guess = input('Guess a letter: ').lower()
        clear()

        for pos, char in enumerate(chosen_word):
            if guess == char:
                hidden_word.pop(pos)
                hidden_word.insert(pos, char)
                result = "right"
                number += 1

        print(f"{''.join(hidden_word)}\n"
              f"You guessed {result}!\n"
              f"The hidden word has {number} letters '{guess.upper()}'")

        if number == 0:
            misses += 1
        if misses >= 6:
            print('GAME OVER!')
            print(hangman[misses])
            break

        missing_letters = hidden_word.count('_')

        if missing_letters > 0:
            print(f'You still need to find discover: ')
        else:
            print(f"{''.join(hidden_word)}")
            print('You Won!')
            break

if __name__ == "__main__":
    main()
