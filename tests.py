from FirstProgram import Car

class Battery():
    """Simple model"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        """output info"""
        print("This car has a " + str(self.battery_size) + "-kWh battary.")
    def get_range(self):
        """ Output info"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go apporximatly " + str(range)
        message += "miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model, year)
        self.battery = Battery()


