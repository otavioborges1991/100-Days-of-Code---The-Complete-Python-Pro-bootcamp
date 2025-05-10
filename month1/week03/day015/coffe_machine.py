# coffe machine
# @todo 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# @todo 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “report” to see the current
# resources available.
# b. The current report should be displayed when “report” is typed in.
# @todo 3. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink. The resources are water, milk, and coffee.
# b. If there are enough resources, it should reduce the resources needed for
# the drink by the amount used.
# c. If there are not enough resources, the program should alert the user and
# then ask them if they would like to order a different drink.
# d. The prompt should show again to serve the next customer.
# e. The program should keep track of the resources and update them after each order.
# f. The program should also keep track of the money earned from each drink sold.
# @todo 4. Process coins.
# a. If the drink is available, the program should prompt the user to insert coins.
# b. The program should calculate the total amount of money inserted.
# c. The program should check if the money is enough to pay for the drink.
# d. If the money is enough, it should process the coins and give change if needed.
# e. If the money is not enough, it should alert the user and ask if they would like to
# order a different drink.
# f. The program should keep track of the money earned from each drink sold.
# @todo 5. Make Coffee.

def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def main():
    pass


if __name__ == "__main__":
    main()