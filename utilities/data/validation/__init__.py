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
