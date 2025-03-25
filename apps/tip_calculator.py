def main():
    print('Tip Calculator')
    bill = float(input("What was the total bill? $"))
    tip = float(input("How much will you tip? $"))
    bill_with_tip = bill + tip
    payers = int(input("How many people are paying: "))
    total = round(bill_with_tip / payers, 2)
    print(f'Each person will pay ${total}.')


if __name__ == '__main__':
    main()