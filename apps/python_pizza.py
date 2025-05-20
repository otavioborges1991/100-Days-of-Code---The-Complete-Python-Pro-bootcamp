def main():
    print("Python Pizza Deliveries.")
    size = input('What size pizza do you want? S, M or L: ').upper().strip()
    pepperoni = input('Do you want pepperoni? Y or N: ').upper().strip()
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper().strip()
    bill = 0

    if size == 'S':
        bill += 15
    elif size == 'M':
        bill += 20
    else:
        bill += 25

    if pepperoni == "Y" and size == 'S':
        bill += 2
    elif pepperoni == "Y" and size == 'M' or size == "L":
        bill +=3

    if extra_cheese == "Y":
        bill += 1

    round(bill, 2)
    print(f'Your bill is ${bill:.2f}')

if __name__ == "__main__":
    main()