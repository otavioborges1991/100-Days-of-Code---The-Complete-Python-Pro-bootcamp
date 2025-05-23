def question(msg):
    """
    -> Questions for answer yes or no, any answer other than y returns false
        answer y returns true
    :param msg:
    :return:
    """
    answer = input(msg).lower().strip()
    if answer == 'y':
        return True
    else:
        return False

def main():
    from random import choices

    eligible_characters = []
    lower_case = "abcdefghijklmnopqrstuvxwyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    number = '0123456789'
    especial_character = '\,.;/]~[´ç=-|<>:?}^{`+_)(*&¨%$#@!"₢°º/?°ª§¬¢£³²¹' + "'"

    lenght = int(input('How long do you want your password to be: '))

    if question('Use lower case letters Y/n: '):
        eligible_characters.extend(lower_case)
    if question('Use upper case letters Y/n: '):
        eligible_characters.extend(upper_case)
    if question('Use numbers Y/n: '):
        eligible_characters.extend(number)
    if question('Use especial characters Y/n: '):
        eligible_characters.extend(especial_character)

    password = "".join(choices(eligible_characters, k=lenght))
    print(f'Your password {password}.')


if __name__ == '__main__':
    main()