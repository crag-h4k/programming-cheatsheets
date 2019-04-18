from pprint import pprint

#Lambda Functions
# use lambda anon functions as one time use funcs inside other funcs
cubed = lambda x : x * x * x

# Objects
class Dog:
# Constructor
    def __init__(self, name = '', breed = '', weight = int(0)):

        # Inner function()
        def lbs_to_kilos(lbs):
            kilos = float(lbs) / float(2.205) 
            return kilos

        # better to use anon function for smaller funcs
        kilos_to_lbs = lambda kilos : float(kilos) * float(2.205)

        self.name = name
        self.breed = breed
        self.weight = weight
        self.kilos = lbs_to_kilos(weight)
        self.lbs = kilos_to_lbs(self.kilos) 

    # Object function, will not run unless access directly
    def describe(self):
        pprint(vars(self))

# Dictionaries
dogs = {'pitbull': Dog('scarface', 'pitbull'), 'greyhound' : Dog('speedy', 'greyhound')}
# get keys and values from dictionary
def dict_info(dictionary):
    for key,value in dictionary.items():
        print(key, value)

# Lists
nums = [1, 2, 3, 4, 5]
nested = [
        [8, 7, 6],
        [5, 4, 3],
        [2, 1, 0],
        ]

#List comprehensions 
# returns a new lists/iterable from the original with functions applied to list elements that not be executed until each element is access. 
nums_cubed = [cubed(n) for n in nums]

# nested list comprehension 
nested_cubed = [cubed(n) for nums in nested for n in nums]

# with statments
# encasulates the execution of the code within the context manager "try, except, and finally "
with open('test-file.txt', 'w') as f:
    f.write('with statements are good')

# below is the long way to write the with statement above
f = open('test-file.txt', 'w')
try:
    f.write('with statements are good')
finally:
    f.close()

#File Handling
with open('alphabet.txt', 'r') as f:
        single_string = f.read()
        list_of_strings = f.readlines()


if __name__ == '__main__':
    # __name__ is a special variable what the interpretter always sets to the name of the module/file. 
    #Append at EoF, will not cause execution when importing functions in another file
    print(__name__)

    husky = Dog('Balto', 'Siberian Husky', 60)
    husky.describe()
    dict_info(dogs)
    pprint(nums_cubed)
    pprint(nested_cubed)

