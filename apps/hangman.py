from random import choice
from utilities.console import clear


def main():
    word_list = ['aardvark', 'baboon', 'camel', 'balloon', 'raven', 'game', 'python', 'snake', 'water']
    hidden_word = []
    result = 'wrong'
    number = 0
    lives = 6


    chosen_word = choice(word_list)
    for char in chosen_word:
        hidden_word.append('_')

    clear()
    print(''.join(hidden_word))
    while True:
        number = 0
        result = 'wrong'
        print(f'{lives} tries left!')
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
            lives -= 1
        if lives <= 0:
            print('GAME OVER!')
            break

        missing_letters = hidden_word.count('_')

        if missing_letters > 0:
            print(f'You still need to find discover: ')
        else:
            print('You Won!')
            break


if __name__ == "__main__":
    main()
