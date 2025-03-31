def get_int(msg=''):
    num = ''
    while True:
        try:
            num = int(input(msg))
            break
        except KeyboardInterrupt:
            print('Interrupted by user')
            break
        except:
            print('Type only integer numbers 0-9')
    return num

def get_float(msg):
    num = ''
    while True:
        try:
            num = float(input(msg))
            break
        except KeyboardInterrupt:
            print('Interrupted by user')
            break
        except:
            print('Type only numbers')
    return num


def list_choices(list):
    from utilities.console import clear
    choice = -1
    while True:
        clear()
        for number, option in enumerate(list):
            print(f'{number} - {option}')
        choice = get_int('select: ')
        if len(list) -1 >= choice >= 0:
            return list[choice]

def confirm(msg='Yes/No'):
    answer = str(input(msg)).lower()
    if answer == 'y':
        return True
    else:
        return False

def get_name(msg='Name: '):
    name = " ".join(str(input(msg)).title().strip().split())
    return name



