from utilities.data.validation import list_choices, get_int

def encrypt(text, cipher, direction):
    original_text = text
    new_text = ''
    if direction == 'encode':
        for character in original_text:
            asc = ord(character)
            new_text += chr(asc + cipher)
        return new_text
    elif direction == 'decode':
        for character in original_text:
            asc = ord(character)
            new_text += chr(asc - cipher)
        return new_text



def main():
    direction = ['encode', 'decode', 'exit']

    while True:
        choice = list_choices(direction)
        if choice == 'exit':
            exit()
        text = str(input("Type in your text: "))
        cipher = get_int('Type in the cipher: ')
        output = encrypt(text, cipher, choice)
        print(f'Output:\n{output}')




if __name__ == '__main__':
    main()