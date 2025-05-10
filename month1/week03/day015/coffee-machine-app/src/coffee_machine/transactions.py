class Transaction:
    def __init__(self):
        self.coins_inserted = 0.0

    def insert_coins(self, quarters, dimes, nickels, pennies):
        self.coins_inserted += quarters * 0.25
        self.coins_inserted += dimes * 0.10
        self.coins_inserted += nickels * 0.05
        self.coins_inserted += pennies * 0.01

    def is_transaction_successful(self, drink_cost):
        return self.coins_inserted >= drink_cost

    def calculate_change(self, drink_cost):
        if self.is_transaction_successful(drink_cost):
            change = round(self.coins_inserted - drink_cost, 2)
            self.coins_inserted = 0.0  # Reset after transaction
            return change
        return 0.0

    def refund(self):
        refund_amount = round(self.coins_inserted, 2)
        self.coins_inserted = 0.0  # Reset after refund
        return refund_amount