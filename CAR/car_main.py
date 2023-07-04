# import car class
from car_class import Car

# ask user
year_model = int(input("what is year model is your car? "))
make = input("Make of your car? ")

# create object
users_car = Car(year_model, make)

# call accelerate method five times, display data
# call brake method five times, display data

users_car.car_info()