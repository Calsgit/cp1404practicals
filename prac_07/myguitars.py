"""
Estimated time (prac 07): 30 min
Elapsed time: TODO: Elapsed time
"""
from guitar import Guitar

IN_FILE = "guitars.csv"


def main():
    print("My guitars!")
    guitars = get_guitars_from_file()
    display_guitars(guitars)


def get_guitars_from_file():
    """Open IN_FILE and extract csv data to create a list of guitar objects."""
    guitars = []
    with open(IN_FILE) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def display_guitars(guitars):
    """Loop through a list of guitars and display their information."""
    max_name_length = max([len(guitar.name) for guitar in guitars])
    max_cost_length = max([len(str(guitar.cost)) for guitar in guitars])
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), worth $ {guitar.cost:>{max_cost_length},.2f} {vintage_string}")


main()
