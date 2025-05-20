from random import choice, shuffle
from os import system
from sys import platform

def clear_screen():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "darwin":
        system("clear")
    elif platform == "win32":
        system("cls")
    else:
        print("\n" * 100)  # Fallback for other platforms



def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while True:
        player_cards = [choice(cards), choice(cards)]
        computer_cards = [choice(cards), choice(cards)]

        player_score = sum(player_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        while player_score < 21:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                player_cards.append(choice(cards))
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
            else:
                break

        if player_score > 21:
            print("You went over. You lose!")
            continue

        while computer_score < 17:
            computer_cards.append(choice(cards))
            computer_score = sum(computer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        if player_score > computer_score:
            print("You win!")
        elif player_score < computer_score:
            print("You lose.")
        else:
            print("It's a draw.")
        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        if play_again != "y":
            break
        clear_screen()

        
if __name__ == "__main__":
    main()