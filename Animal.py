class Animal:
    # Static class variable to keep track of the number of animals
    numOfAnimals = 0

    def __init__(self, species, name=None, age=99, birth_season="season", color=" a color", weight="99 pounds",
                 originating_zoo=" from where?"):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo

        # Increment the static variable when a new object is created
        # this is the only place this field's value should be changed
        Animal.numOfAnimals += 1

    # Create a constructor that only takes two arguments
    # Notice the "method decoration" making this a class method (it will not below to an object)
    # also, note that the __init__ method will be used here, so an object created here will
    # have all the fields of __init__ We also must be careful not to increment numOfAnimals here, why? code
    # up numOfAnimals += 1 here and see what happens!
    @classmethod
    def create_with_species_and_name_only(cls, species: object, name: object) -> object:
        return cls(species, name)


# Example usage:
# Create an Animal with two arguments (species and name)
animal_01 = Animal.create_with_species_and_name_only('Hyena', 'Kamari')

# Create an Animal with six arguments
animal_02 = Animal('Lion', 'Kiara', 6, 'spring', 'tan', 305, 'Zanzibar, Tanzania')

animal_03 = Animal.create_with_species_and_name_only("Hyena", "Ed")

print("\n\n color of animal 03 is: " + animal_03.color)


# Create ten Animal objects using a for loop
# get the ten animals into a list named animals[]
animals = []

for i in range(10):
    if i % 2 == 0:
        # Create an Animal with two arguments (species and name)
        animal = Animal.create_with_species_and_name_only('Hyena', f'Name{i}')
    else:
        # Create an Animal with six arguments
        animal = Animal('Lion', f'Name{i}', i, 'spring', 'tan', 100 + i, 'Zoo{i}')

    animals.append(animal)

# Access the static variable numOfAnimals
print(f'Number of animals created: {Animal.numOfAnimals}')

# Print information about the created animals
for i, animal in enumerate(animals, start=1):
    print(f'Animal {i}: {animal.species}, {animal.name}, {animal.age} years old')


# Access the static variable numOfAnimals
print(f'Number of animals created: {Animal.numOfAnimals}')  # Output: Number of animals created: 2
