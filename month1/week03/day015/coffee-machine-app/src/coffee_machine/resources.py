class Resources:
    def __init__(self):
        self.water = 300  # in ml
        self.milk = 200   # in ml
        self.coffee = 100  # in grams
        self.money = 0.0   # in dollars

    def report(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"

    def is_sufficient(self, water_needed, milk_needed, coffee_needed):
        if self.water < water_needed:
            print("Sorry there is not enough water.")
            return False
        if self.milk < milk_needed:
            print("Sorry there is not enough milk.")
            return False
        if self.coffee < coffee_needed:
            print("Sorry there is not enough coffee.")
            return False
        return True

    def update_resources(self, water_used, milk_used, coffee_used, money_earned):
        self.water -= water_used
        self.milk -= milk_used
        self.coffee -= coffee_used
        self.money += money_earned