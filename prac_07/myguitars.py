"""
Estimated time (prac 07): 30 min
Elapsed time: 35 min?
"""
from guitar import Guitar

GUITARS_FILE = "guitars.csv"


def main():
    print("My guitars!")
    guitars = get_guitars_from_file()
    new_guitars = get_guitars_from_user()
    if new_guitars:
        guitars += new_guitars
    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars)


def get_guitars_from_file():
    """Open specified file and extract csv data to create a list of guitar objects."""
    guitars = []
    with open(GUITARS_FILE) as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def get_guitars_from_user():
    """Repeatedly prompts user for guitar information until a blank name is entered."""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.")
        name = input("Name: ")
    return guitars


def display_guitars(guitars):
    """Loop through a list of guitars and display their information."""
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_cost_length = max(len(str(guitar.cost)) for guitar in guitars)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), worth $ {guitar.cost:>{max_cost_length},.2f} {vintage_string}")


def save_guitars(guitars):
    """Save all stored guitars to the specified file."""
    with open(GUITARS_FILE, 'w') as out_file:
        for guitar in guitars:
            end_of_file_string = "" if guitar == guitars[-1] else "\n"
            guitar_string = f"{guitar.name},{guitar.year},{guitar.cost}{end_of_file_string}"
            out_file.write(guitar_string)


main()
