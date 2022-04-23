from FirstProgram import Car
from tests import ElectricCar

my_beetle = Car('VW', 'beetle', 2022)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())