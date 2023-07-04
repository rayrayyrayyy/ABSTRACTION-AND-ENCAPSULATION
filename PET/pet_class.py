# create pet class
class Pet:
    def __init__(self, name, age, animal_type):
        self.__name = name
        self.__age = age
        self.__animal_type = animal_type
    
    # define methods (create setter and getter)
    # getters
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
    # setters
    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # define function to show data
    def pet_data(self):
        print('\033[1;35m' + "Name:", '\033[4m' + self.__name + '\033[0m', '\033[1;35m' + "\nAge:", '\033[4m' + self.__age + '\033[0m', '\033[1;35m' + "\nType:", '\033[4m' + self.__animal_type + '\033[0m')