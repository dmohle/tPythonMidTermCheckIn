class Animal:
    # Static class variable to keep track of the number of animals
    numOfAnimals = 0

    def __init__(self, species="no species", name="no name", age=99, birth_season="a season", color="a color",
                 weight="99 pounds", originating_zoo="from where?"):

    # def __init__(self, species, name, age, birth_season, color, weight, originating_zoo):

        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo

        # Increment the static variable when a new object is created
        # this is the only place this field's value should be change
        Animal.numOfAnimals += 1

    # Create a constructor that only takes two arguments
    # Notice the "method decoration" making this a class method (it will not belong to an object)
    # also, note that the __init__ method will be used here, so an object created here will
    # have all the fields of __init__ We also must be careful not to increment numOfAnimals here, why? code
    # up numOfAnimals += 1 here and see what happens!
    @classmethod
    def create_with_species_and_name_only(cls, species: object, name: object):
        return cls(species, name)


