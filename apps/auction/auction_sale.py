from random import choices, randint, choice
from utilities.data.validation import get_int, confirm

def create_bidders(num=5, credit=None,):
    if credit is None:
        credit = [1000, 5000]

    file = open('buyers_names.txt')

    names = choices(file.read().splitlines(), k=num)
    bidders = dict()
    for name in names:
        bidders[name] = randint(credit[0], credit[1])
    file.close()
    return bidders

def create_bids(num=5, price=None):
    if price is None:
        price = [100, 1000]

    file = open('itens.txt')
    itens = choices(file.read().splitlines())
    bids = dict()
    for item in itens:
        bids[item] = randint(price[0], price[1])
    file.close()
    return bids



def main():
    auction_types = ['English', 'Dutch', 'sealed first-price']
    name = str(input('Name: '))
    personal_credit = randint(1000, 5000)

    # randomly creating bidders to compete against the player for auctions
    bidders = create_bidders()
    bids = create_bids()

    # announcing bidders and bid
    print('The bidders for today auction:')
    for bidder, credit in bidders.items():
        print(f'    {bidder} ${credit}')
    print(f'    {name} ${personal_credit}')
    print('\nThe item for today auction:')
    for bid, price in bids.items():
        print(f'    {bid} ${price}')
    print('Every bid needs to be at least 10% higher than the previous one')
    # auction loop
    for bid, price in bids.items():
        print(f'The Current bid is {bid}, the starting price is ${price}')
        highest_bidder = None
        bid_name = bid
        bid_price = price
        while True:
            for bidder, credit in bidders.items():
                if bid_price * 1.10 > credit:
                    print(f'{bidder} say: the price {bid_price} + 10% for the {bid_name} is greater than the money i have '
                          f'{credit}, i cant bid.')
                    continue
                else:
                    yn = ['yes', 'no']
                    if choice(yn) == 'yes':
                        price = round(price * 1.1)
                        print(f'{bidder} say: i will pay {price}')
                        highest_bidder = bidder

            if highest_bidder == name:
                print(f'You got the {bid_name}!\nReady for the next?')
                break

            if confirm('Will you bid? Y/n: '):
                your_bid = get_int('Will you bid how much: ')
                if your_bid > personal_credit:
                    print('You dont have that much money')
                else:
                    bid_price = your_bid
                    highest_bidder = name
            if highest_bidder != name:
                print(f'{highest_bidder} got the {bid_name}\nReady for the next? ')
                break

    credit = 5000


if __name__ == '__main__':
    main()