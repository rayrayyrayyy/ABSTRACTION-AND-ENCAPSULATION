# import modules for design
from colorama import Fore, Style
import time
import pyfiglet

# import pet class
from pet_class import Pet

# ask user for the pet's name, age, and type of pet
pet_name = input("What's your pet's name? ")
pet_age = input("How old is he/she? ")
pet_type = input("What animal is it? ")

# create object
user_pet = Pet(pet_name, pet_age, pet_type)
pet_text = pyfiglet.figlet_format("My Pet ", font = 'small', width = 30, justify = 'center')

# display data
print("...processing data")
time.sleep(2)
print('\n\033[1;33m' + '==='*10 + '\033[0m')
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + pet_text + Style.RESET_ALL)
print('\033[1;33m' + '==='*10 + '\033[0m')
user_pet.pet_data()
print('\033[1;33m' + '==='*10)