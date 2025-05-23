from random import choice

def main():
    choices = ['rock', 'paper', 'scissors']

    player = int(input("[0]Rock, [1]Paper, [2]Scissors\nYour pick: "))
    computer = choice(choices)
    player = choices[player]

    print(f'Your choice is {player}, the computer is {computer}')
    if player == 'rock' and computer == 'rock':
        print('Its a Tie!')
    elif player == 'rock' and computer == 'paper':
        print('You Lose!')
    elif player == 'rock' and computer == 'scissors':
        print('You Win!')
    elif player == 'paper' and computer == 'rock':
        print('You Win!')
    elif player == 'paper' and computer == 'paper':
        print('Its a Tie!')
    elif player == 'paper' and computer == 'scissors':
        print('You Lose!')
    elif player == 'scissors' and computer == 'rock':
        print('You Lose!')
    elif player == 'scissors' and computer == 'paper':
        print('You Win!')
    elif player == 'scissors' and computer == 'scissors':
        print('Its a Tie!')

if __name__ == '__main__':
    main()