class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0
        }
        self.menu = {
            "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
        }

    def report(self):
        report_data = (
            f"Water: {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}g\n"
            f"Money: ${self.resources['money']:.2f}"
        )
        print(report_data)

    def check_resources(self, drink):
        for item in self.menu[drink]:
            if item != "cost" and self.resources[item] < self.menu[drink][item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = float(input("Quarters: ")) * 0.25
        total += float(input("Dimes: ")) * 0.10
        total += float(input("Nickels: ")) * 0.05
        total += float(input("Pennies: ")) * 0.01
        return total

    def is_transaction_successful(self, money_received, drink):
        if money_received < self.menu[drink]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        if money_received > self.menu[drink]["cost"]:
            change = round(money_received - self.menu[drink]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
        self.resources["money"] += self.menu[drink]["cost"]
        return True

    def make_coffee(self, drink):
        for item in self.menu[drink]:
            if item != "cost":
                self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink}. Enjoy!")