class person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.owned_cars = []

class car():

    def __init__(self, model, year):
        self.model = model
        self.year = year


car1 = car("Toyota", 2020)
person1 = person("John", 30)
print(f"{person1.name} drives a {car1.model}")  # Output: John