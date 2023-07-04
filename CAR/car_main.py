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

print("\n\nCar year model: ", year_model)
print("Make of the car: ", make)

# call accelerate method five times, display data
print("\n...accelerating")
for i in range (5):
    car_speed.accelerate()
    car_speed.car_speed()

# call brake method five times, display data
print("\n...brake")
for i in range (5):
    car_speed.brake()
    car_speed.car_speed()