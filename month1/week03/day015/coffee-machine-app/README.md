# Coffee Machine App

This project is a simple coffee machine application that allows users to select their desired coffee drinks, check resources, and process transactions. The application is structured into several modules for better organization and maintainability.

## Project Structure

```
coffee-machine-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── coffee_machine
│   │   ├── __init__.py        # Initializes the coffee_machine package
│   │   ├── machine.py         # Contains the CoffeeMachine class
│   │   ├── resources.py       # Manages resources like water, milk, coffee, and money
│   │   └── transactions.py     # Handles coin insertion and transaction processing
├── tests
│   ├── __init__.py            # Initializes the tests package
│   └── test_machine.py        # Unit tests for the CoffeeMachine class
├── requirements.txt           # Lists dependencies for the project
└── README.md                  # Documentation for the project
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the application using the command:
   ```
   python src/main.py
   ```
2. Follow the prompts to select your desired coffee drink (espresso, latte, cappuccino).
3. Insert coins as prompted and enjoy your coffee!

## Features

- Check available resources before making a drink.
- Handle transactions and provide change if necessary.
- Generate reports of current resources and earnings.

## Testing

To run the tests, use the following command:

```
python -m unittest discover -s tests
```

This will execute all unit tests defined in the `tests` directory.

## License

This project is open-source and available under the MIT License.