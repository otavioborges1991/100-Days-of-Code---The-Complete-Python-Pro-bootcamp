from game_data import data
from random import choice
def get_random_account():
    """Get random account from data"""
    return choice(data)

def format_data(account):
    """Format account into printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    """Check if user's guess is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def play_game():
    print("Welcome to the game!")
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print("VS")
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a['followers']
        b_followers = account_b['followers']
        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")



if __name__ == "__main__":
    play_game()