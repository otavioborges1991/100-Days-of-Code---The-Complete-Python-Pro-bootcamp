water_level = 50

if water_level > 80:
    print('Drain water')
else:
    print('Continue')


print('Wellcome to the rollercoaster!')
height = float(input('What is your height: '))
age = int(input("What is you age: "))
if height >= 1.20:
    print('You can ride rollercoaster')
    if age <= 12:
        ticket_price = 5.0
    elif  age <= 18:
        ticket_price = 7.0
    else:
        ticket_price = 12.0
    total_bill = ticket_price
    wants_photo = input("Do you want photos? y/N:")
    if wants_photo == 'y':
        total_bill = ticket_price + 3
    print(f'Total cost ${total_bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')

