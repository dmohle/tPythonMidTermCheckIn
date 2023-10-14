# Main.py
# driver file for the animal zoo program
# last update 10/13/23 by dH

from Hyena import Hyena
from Animal import Animal

# Create two Hyena objects
hyena_01 = Hyena("Shenzi", 5, "winter", "brown color", "75 pounds", "from Friguia Park")
hyena_02 = Hyena("Banzai", 3, "summer", "tan color", "80 pounds", "from Friguia Park")

# Think about this: How many arguments were used to create hyena_01? Does the Hyena class have a constructor
# with five parameters? Will this code work if you create a hyena with five arguments?

# Output information about the Hyena object
print(f"Hyena Name: {hyena_01.name}")
print(f"Species: {hyena_01.species}")
print(f"Age: {hyena_01.age}")
print(f"Color: {hyena_01.color}")
print(f"Weight: {hyena_01.weight}")
print(f"Originating Zoo: {hyena_01.originating_zoo}")
print(f"Sound made: {hyena_01.make_sound()}")

# Access the static variable numOfHyenas
print(f'Number of Hyenas created: {Hyena.numOfHyenas}')

# we know the Hyena class here (because we imported it) so we can call the class method that gets the hyena names
# call the class method named load_hyena_names()
print("******************")
# hyena_01.load_hyena_names()
print("******************")
# Hyena.load_hyena_names()
print("******************")

# Create a list of animals
animals = []

# Create an Animal with seven arguments
animal = Animal("lion", "Scar", 3, "spring", "tan", "425 pounds", "Zanzibar")
# add the new animal to the end of the list
animals.append(animal)

# Create another hyena
another_hyena = Hyena("Zig", 5, "summer", "black spots", "80 pounds", "Zanzibar")
# add the new hyena to the animals list
animals.append(another_hyena)


# Create an animal with two arguments
my_new_animal = Animal.create_with_species_and_name_only("bear", "Smokey")
animals.append(my_new_animal)

# Print information about the created objects in the animals list
for i, animal in enumerate(animals):
    print(f"Animal {i}: {animal.species}, {animal.name}, {animal.age} years old")

# Access the static variable numOfAnimals
print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

# Output the static variable numOfHyenas
print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")