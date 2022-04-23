from FirstProgram import Car, ElectricCar


my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = Car('volkswagen', 'beetle', 2022)
print(my_beetle.get_descriptive_name())


















