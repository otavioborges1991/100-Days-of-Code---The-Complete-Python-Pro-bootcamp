import unittest
from src.coffee_machine.machine import CoffeeMachine
from src.coffee_machine.resources import Resources
from src.coffee_machine.transactions import Transaction

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        self.machine = CoffeeMachine()
        self.resources = Resources()
        self.transaction = Transaction()

    def test_initial_resources(self):
        self.assertEqual(self.resources.water, 300)
        self.assertEqual(self.resources.milk, 200)
        self.assertEqual(self.resources.coffee, 100)
        self.assertEqual(self.resources.money, 0)

    def test_check_resources_sufficient(self):
        self.assertTrue(self.machine.check_resources('latte'))
        self.resources.water = 0
        self.assertFalse(self.machine.check_resources('latte'))

    def test_process_coins(self):
        self.assertEqual(self.transaction.process_coins(1, 2, 1, 2), 0.52)

    def test_transaction_successful(self):
        self.resources.money = 2.50
        self.assertTrue(self.transaction.check_transaction(2.50))
        self.assertFalse(self.transaction.check_transaction(3.00))

    def test_make_coffee(self):
        self.machine.make_coffee('espresso')
        self.assertEqual(self.resources.water, 250)
        self.assertEqual(self.resources.coffee, 90)
        self.assertEqual(self.resources.money, 1.50)

if __name__ == '__main__':
    unittest.main()