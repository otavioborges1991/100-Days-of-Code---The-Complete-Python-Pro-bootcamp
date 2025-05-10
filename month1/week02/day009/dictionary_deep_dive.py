programming_dictionary = {'Bug': 'An error in a program that prevents the program from running as expected.',
                          'Function': 'A piece of code that you can easily call over and over again.',}

for key, value in programming_dictionary.items():
    print(f'{key}: {value}')

programming_dictionary['Loop'] = 'The action of doing something over and over again.'

for key, value in programming_dictionary.items():
    print(f'{key}: {value}')


empty_list = []
empty_dictionary = {}

empty_dictionary['Filling'] = 'Not empty anymore.'
print(empty_dictionary)
programming_dictionary = {} # reseting the dicionary
print(programming_dictionary)