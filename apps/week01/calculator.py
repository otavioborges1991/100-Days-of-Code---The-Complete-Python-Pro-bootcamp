def main():
    print("Welcome to the calculator app!")
    while True:
        try:
            expression = input("Enter a mathematical expression (or 'exit' to quit): ")
            if expression.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            result = eval(expression) # this is a simple calculator that evaluates mathematical expressions, but be careful with eval as it can execute arbitrary code
            # Note: In a production environment, you should use a safer alternative to eval, such as a library that parses and evaluates mathematical expressions safely.
            # For example, you can use the `sympy` library for symbolic mathematics or `asteval` for a safer eval.
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")





if __name__ == "__main__":
    main()