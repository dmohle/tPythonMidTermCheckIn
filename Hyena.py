# Import the Animal class from the Animal module
from Animal import Animal

class Hyena(Animal):
    # create a static class variable to keep track of the number of hyenas created
    numOfHyenas = 0

    # create a class method that creates a list of hyena names from the animalNames.txt text file
    # a class method will not belond to an object of the class (notice the @classmethod decoration) and
    # look at the parameter of this class method, it is cls not self
    @classmethod
    def load_hyena_names(cls):
        # Define the file path
        file_path = r'C:\2023fall\python\dataFiles\animalNames.txt'

        # Initialize an empty list to store hyena names
        hyena_names = []

        # Open the file and read its content
        # using with will close the file after this code block is done executing
        with open(file_path, 'r') as file:
            lines = file.readlines()

        print("\n type of lines is " + str(type(lines)))

        # Iterate through the lines in the file
        for line in lines:
            if line.strip() == "Hyena Names:":
                is_hyena_section = True
            elif is_hyena_section and line.strip():
                # Add the hyena name to the list
                hyena_names.extend(line.strip().split(', '))

        # Print the list of hyena names
        print("Hyena Names:")
        for name in hyena_names:
            print(name)

    # __init__ is the constructor method. Note how "self" is used here. "self" refers to the object created
    def __init__(self, name, age, birth_season, color, weight, originating_zoo):
        # Increment the static variable numOfHyenas when a new Hyena object is created
        Hyena.numOfHyenas += 1

        # Call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("hyena", name, age, birth_season, color, weight, originating_zoo)

    def make_sound(self):
        return " laugh laugh "
