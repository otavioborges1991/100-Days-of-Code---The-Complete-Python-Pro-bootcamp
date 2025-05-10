# filepath: coffee-machine-app/src/main.py

from coffee_machine.machine import CoffeeMachine

def main():
    coffee_machine = CoffeeMachine()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            coffee_machine.print_report()
        else:
            coffee_machine.make_coffee(choice)

if __name__ == "__main__":
    main()