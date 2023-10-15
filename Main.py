# Main.py
# driver file for the animal zoo program
# last update 10/13/23 by dH
# last update 10/14/23


from Animal import Animal
from Hyena import Hyena

from _datetime import date

# Create lists of the species
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# This is needed for the calc birthday stuff.
current_date = date.today()
current_year = current_date.year


def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"

    return the_birth_day


def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_gender = ""
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    print(one_line)
    groups_of_words = one_line.strip().split(",")
    print(groups_of_words)
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_gender = single_words[3]
    a_species = single_words[4]
    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[2]
    color = groups_of_words[2].strip();
    weight = groups_of_words[3].strip();
    origin_01 = groups_of_words[4].strip();
    origin_02 = groups_of_words[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # Create a hyena object.
        my_hyena = Hyena("aName", "anID", birth_day, color, a_gender, weight, from_zoo, current_date)
        # fill in name and ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas)
        # add to the hyena list
        list_of_hyenas.append(my_hyena)


# Open arrivingAnimals.txt and read it one line at a time
# Open the file in read mode
file_path = r"C:\2023spring\pythonRoot\dataFiles\arrivingAnimals.txt"
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# Access the static variable numOfHyenas
print(f'Number of Hyenas created: {Hyena.numOfHyenas}')

# Access the static variable numOfAnimals
print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

# Output the static variable numOfHyenas
print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")

# output the animals

for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.gender + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))
