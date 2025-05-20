# -*- coding: utf-8 -*-

from items import coffee_types, resources
import platform
from os import system

def clear():
    os = platform.system()
    if os == 'Windows':
        system('cls')
    else:
        system('clear')

    def handle_paying(value_paid, coffee_type):
        price = coffee_type['cost']
        if value_paid > price:
            return value_paid - price
        elif value_paid < price:
            print("Insufficient payment. Transaction refused.")
            return None
        else:
            return 0

def display_menu():
    print("Welcome to the Coffee Shop!")
    print("Here is the menu:")
    for number, item in enumerate(coffee_types):
        print(f"[{number + 1}] - {item['name'].capitalize():_<15}: R${item['cost']:.2f}")

def confirm_order(coffee_types):
    print(f"You have selected: {coffee_types['name'].capitalize()}")
    confirm = input("Would you like to proceed with the order? (yes/no): ").strip().lower()
    if confirm == 'yes':
        print("Order confirmed!")
        return True
    else:
        print("Order cancelled.")
        return False

def get_user_choice():
    while True:
        try:
            user_input = int(input("Please select a coffee by entering the corresponding number: "))
            choice = int(user_input)
            if choice == 0:
                sub_option = input("Enter 1 to shutdown the machine, 2 to refill resources, 3 to check resources or any other key to go back: ").strip()
                if sub_option == "1":
                    exit('Shutting down machine!')
                elif sub_option == "2":
                    return 'refill'
                elif sub_option == '3':
                    display_resources()
                    input('Continue...')
                    display_menu()
                else:
                    continue
            elif 1 <= choice <= len(coffee_types):
                accept = confirm_order(coffee_types[choice -1])
                if accept:
                    return coffee_types[choice - 1]
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



    
def make_coffee(coffee_type):
    # Check if enough resources are available
    for ingredient, required in coffee_type['ingredients'].items():
        # Find the resource in resources list
        resource = next((r for r in resources if r['name'] == ingredient), None)
        if resource is None:
            print(f"Resource '{ingredient}' not found.")
            return False
        if resource['amount'] < required:
            print(f"Sorry, not enough {ingredient}.")
            return False

    # Deduct the required ingredients from resources
    for ingredient, required in coffee_type['ingredients'].items():
        resource = next((r for r in resources if r['name'] == ingredient), None)
        resource['amount'] -= required


    print(f"Here is your {coffee_type['name'].capitalize()}! Enjoy!")
    return True


def display_resources():
    clear()
    print("Resource Management!")
    print("Here is the current resources:")
    print(f"1 {resources[0]['name']:<15} - {resources[0]['amount']:.3f} ml")
    print(f"2 {resources[1]['name']:<15} - {resources[1]['amount']:.3f} ml")
    print(f"3 {resources[2]['name']:<15} - {resources[2]['amount']} g")
    print(f"4 {resources[3]['name']:<15} - {resources[3]['amount']:.3f} ml")
    print(f"5 {resources[4]['name']:<15} R${resources[4]['amount']:.2f}")
    print(f"6 {resources[5]['name']:<15} - {resources[5]['amount']}")


def refill_resource():
    while True:
        display_resources()
        try:
            choice = int(input("Enter the number of the resource you want to refill (1-6), or 0 to exit: "))
            if choice == 0:
                print("Exiting refill menu.")
                break
            if 1 <= choice <= len(resources):
                resource = resources[choice - 1]
                amount = input(f"Enter the amount to add to {resource['name']}: ")
                try:
                    if isinstance(resource['amount'], int):
                        add_amount = int(amount)
                    else:
                        add_amount = float(amount)
                    resource['amount'] += add_amount
                    print(f"{resource['name']} refilled by {add_amount}. New amount: {resource['amount']}")
                    display_resources()
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            else:
                print("Invalid resource number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

''