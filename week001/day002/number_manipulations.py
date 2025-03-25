from math import floor, ceil

weight = 64.3
height = 1.79
bmi = weight / (height * height)

print(bmi)
print(int(bmi)) # converting to int, causes it to be rounded down
print(round(bmi, 2)) # round() functions rounds up or down to the closest
print(floor(bmi)) # rounds down
print(ceil(bmi)) # rounds up
