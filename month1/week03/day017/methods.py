class Car:
    
    def race_mode(self):
        if self.race_mode_on:
            self.race_mode_on = False
            self.seats = 5
        else:
            self.race_mode_on = True
            self.seats = 2

    def __init__(self):
        self.race_mode_on = False
        self.seats = 5


vehicle = Car()
print(vehicle.seats)
vehicle.race_mode()
print(vehicle.seats)
vehicle.race_mode()
print(vehicle.seats)