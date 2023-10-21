# tPythonMidTermCheckIn
tPythonMidTermCheckIn: What you should have so far...

Program Overview

Animals are arriving from zoos around the world, and your task is to give them names, calculate their birthdates, and organize them into habitats in your zoo. To accomplish this, you will write a Python program that performs the following tasks:

Reads information about arriving animals from an input text file (arrivingAnimals.txt).
Parses each line of input data into individual data pieces.
Calculates a birthday based on the input data.
Generates a name for each animal using names collected from a recent community fundraiser (animalNames.txt).
Creates a unique ID for each animal to be used in your zoo information system (unique IDs must be in the format: Hy01, Hy02, Li01, Li02, etc.).
Assigns each animal to an appropriate habitat using lists of lists.
Outputs a report (zooPopulation.txt) containing all zoo animals and their information.

Constraints

To limit the scope of the assignment and align it with the current class instruction, please work with the following constraints:

Limit the input to four animals from each of the four species (16 animals in total).

Programming Concepts to Demonstrate

You are required to demonstrate the following programming concepts in your Python program:

Clear, concise, and correct code: 
Your program must adhere to the class programming style guide.
File I/O: Utilize various file operations such as creating, writing to, opening, reading from, closing, deleting, and appending to files.
Exception Handling: Handle standard file I/O exceptions and create custom exceptions to handle adding an animal to a habitat that does not have enough room for the new animal.
Functions and Lists: Organize the data read from the input zoo document using functions and lists.
Input - File and String Handling: Parse string data from input files.
Output - Formatted Output: Generate a report listing zoo animals with their attributes and their habitats (zooPopulation.txt).

Data Structures

You will use the following data structures in your program:

Python lists and strings.
An Animal class with derived Hyena, Lion, Tiger, and Bear classes to represent different species of animals.

Step-by-Step Guide

Step 1: Understanding the Problem

Before diving into coding, it's essential to fully understand the problem and its requirements. Make sure you grasp the input format, output format, and the various tasks the program needs to perform.

Step 2: Define the Animal Classes

In Python, you can create classes to represent different species of animals. You mentioned creating an Animal class with derived Hyena, Lion, Tiger, and Bear classes. Here's a basic example of how you can define these classes:

Sample code...

class Animal:
    def __init__(self, species, age, birth_season, color, weight, originating_zoo):
        self.species = species
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo

class Hyena(Animal):
    # Hyena-specific attributes and methods

class Lion(Animal):
    # Lion-specific attributes and methods

class Tiger(Animal):
    # Tiger-specific attributes and methods

class Bear(Animal):
    # Bear-specific attributes and methods

These classes inherit from the Animal class and can have their attributes and methods specific to each species.

Step 3: Read Input Data

You'll need to read the information about arriving animals from the arrivingAnimals.txt file. Python provides file I/O operations for reading files. You can use open() to open a file and then read its content line by line.

Step 4: Parse Each Line from arrivingAnimals.txt
After reading each line from the input file, you can split it into individual data pieces using the split() function. Here's how:

Sample code...

with open('arrivingAnimals.txt', 'r') as file:
    for line in file:
        data = line.strip().split(', ')
        age = data[0]
        species = data[1]
... Continue parsing and processing the data to create Animal objects

Step 5: Implement Functions

Implement the required functions as described in the assignment. The output of these functions may be achieved with different code. For example, if you have the static class variables, numOfAnimals, numOfHyenas, numOfTigers, etc. working propery, your genUniqueID function would accept two string arguments (species, numOfAnimals) and return a string that is the first two characters of species, and str(numOfAnimals). For example:

genBirthDay()
Calculate the birthday from the information received from the originating zoo. Note that arriving animals come to you with an age and a birth season. Your genBirthDay() function will use this data to create a birthdate -- use the start of the season for the month and day, and subtract years old from the current date. Use the Python datetime module. 

genUniqueAnimalID()
Calculate a unique ID to uniquely identify each animal in your zoo.

genAnimalName()
Create an animal name based on input from a community fundraiser (animalNames.txt).

genZooHabitat()
Assign each new animal to a habitat. Think about how to organize your zoo. One solution is to create a list for each species.

Step 6: Organize Data and Populate Habitats

Now, let's discuss how you will create the habitats for different species of animals. One approach is to use lists of lists. You can have a list for each species, and within each list, you store instances of animals belonging to that species. Here's a Python code example of this list of lists:

Sample Python code...

## Initialize lists for each species
hyena_habitat = []
lion_habitat = []
tiger_habitat = []
bear_habitat = []

## Initialize a list to hold all animals
all_animals = [hyena_habitat, lion_habitat, tiger_habitat, bear_habitat]

Example: Adding a Hyena to the Hyena habitat
hyena = Hyena(...)
hyena_habitat.append(hyena)

Example: Adding a Lion to the Lion habitat
lion = Lion(...)
lion_habitat.append(lion)

Repeat similar steps for Tigers and Bears
This code helps you organize the animals into their respective habitats.

Step 7: Write Output to File
Generate a report (e.g., zooPopulation.txt) containing all zoo animals and their information. You can use file I/O to write this information to a new file.

Sample Python Code:

## Output all animals organized by species
with open('zooPopulation.txt', 'w') as output_file:
    for index, species_habitat in enumerate(all_animals):
        # Get the species name based on index
        species_name = ["Hyena", "Lion", "Tiger", "Bear"][index]  
        output_file.write(f"{species_name} Habitat:\n")
        
## Iterate through animals in the species habitat
for animal in species_habitat:
    output_file.write(f"{animal.unique_id}; {animal.name}; {animal.age} years old; birth date {animal.birth_date}; {animal.color} color; 
    {animal.gender}; {animal.weight} pounds; from {animal.originating_zoo}; arrived {animal.arrival_date}\n")

This code will help you generate the required report in the zooPopulation.txt file, organized by species.

Using Classes in Separate Files and Creating Custom Libraries
You can organize your code by placing each class in a separate .py file. For example, you can have animal.py, hyena.py, lion.py, tiger.py, and bear.py. Then, in your main program, you can import these classes using import statements like this:

Sample Python Code

from animal import Animal
from hyena import Hyena
from lion import Lion
from tiger import Tiger
from bear import Bear
This allows you to use these classes in your main program.

Creating Custom Libraries
To create custom libraries of Python code, you can create .py files with your functions or classes. You can place these files in a directory and then use them in other Python programs by importing them as demonstrated above.

Remember to encapsulate your code into functions and classes, and break down the tasks into manageable pieces. Good luck with your Python midterm assignment!

added mortgage calculator Oct 21, 2023


