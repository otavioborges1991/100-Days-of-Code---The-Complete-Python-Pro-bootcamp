from random import randint
def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = randint(1, 100)
    
    # Set the number of attempts based on difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == "easy" else 5
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {secret_number}.")
            break
        
        attempts -= 1
        
        if attempts == 0:
            print("You've run out of guesses. You lose.")
            print(f"The correct number was {secret_number}.")
            



if __name__ == "__main__":
    main()