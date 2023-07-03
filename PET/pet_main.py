# import pet class
from pet_class import Pet

# ask user for the pet's name, age, and type of pet
pet_name = input("What's your pet's name? ")
pet_age = input("How old is he/she? ")
pet_type = input("What animal is it? ")

# create object
user_pet = Pet(pet_name, pet_age, pet_type)

# display data

