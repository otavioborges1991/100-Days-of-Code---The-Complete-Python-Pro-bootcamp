import menu
from time import sleep

wallet = 50.60

def main():
    while True:
        menu.display_menu()
        pedido = menu.get_user_choice()
        if pedido == 'refill':
            menu.refill_resource()
        else:
            order_completed = menu.make_coffee(pedido)
            if order_completed:
                print("Have a good day!")
                sleep(3)
            else:
                print("Please, ask a employee to refil the machine resources")
                sleep(3)
    

    




if __name__ == "__main__":
    main()