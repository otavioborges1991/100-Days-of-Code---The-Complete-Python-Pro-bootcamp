import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.PI)

random_number_0_to_1 = random.random() * 1000
print(random_number_0_to_1)

random_uniform = random.uniform(1, 10)
print(random_uniform)