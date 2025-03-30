
print('Hello'[0])
print(123.456789)
print(type('abc'))
print(type(123))
print(type(3.14))
print(type(True))

print('123' + '456') # concatenation
print(2 * 'abc')
print(int('123') + int('456')) # math operation

print('Number of letters in your name: ' + str(len(input('Enter your name: '))))

username = input('Enter your name: ')
username_length = len(username)
print('Number of letters in your name: ' + str(username_length))
print(f'Number of letters in your name: ' + str(username_length))