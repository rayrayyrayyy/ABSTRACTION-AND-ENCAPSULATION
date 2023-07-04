# import modules for design
from colorama import Fore, Style
import time
import pyfiglet

# import car class
from car_class import Car

# ask user
year_model = int(input("what is year model is your car? "))
make = input("Make of your car? ")

# create object
car_speed = Car()
print('\n' + '==='*15)
print(Fore.LIGHTCYAN_EX + "Car year model: " + Style.RESET_ALL + '\033[1;33m', year_model, '\033[0m')
print(Fore.LIGHTCYAN_EX + "Make of the car: " + Style.RESET_ALL + '\033[1;33m', make, '\033[0m')
print('==='*15)

# call accelerate method five times, display data
print("\n...accelerating")
time.sleep(2)
for i in range (5):
    car_speed.accelerate()
    car_speed.car_speed()

# call brake method five times, display data
print("\n...brake")
time.sleep(2)
for i in range (5):
    car_speed.brake()
    car_speed.car_speed()