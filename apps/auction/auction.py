from os import system

def main():
    print("Welcome to the Auction App!")
    print("This is a simple auction application.")
    print("You can place bids on items and see the highest bid.")
    print("Good luck!")

    # Auction logic goes here
    # For example, you could create a class for items and bids

    # Placeholder for auction logic
    item = "Antique Vase"
    highest_bid = 0
    highest_bidder = ""

    while True:
        bidder = input("Enter your name (or 'exit' to quit): ")
        if bidder.lower() == 'exit':
            break
        bid = float(input(f"Enter your bid for {item}: "))
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
            print(f"New highest bid of {highest_bid} by {highest_bidder}!")
        else:
            print(f"Your bid of {bid} is too low. Current highest bid is {highest_bid} by {highest_bidder}.")


if __name__ == "__main__":
    main()
    system("pause")
    system("cls")
