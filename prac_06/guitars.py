"""
Estimated time (for guitar, guitar_test, guitars): 25 min
Elapsed time: 30 min
"""
from guitar import Guitar


def main():
    print("My guitars!")
    guitars = get_guitars_from_user()
    display_guitars(guitars)


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
    print()
    return guitars


def display_guitars(guitars):
    """Loop through a list of guitars and display their information."""
    max_name_length = max([len(guitar.name) for guitar in guitars])
    max_cost_length = max([len(str(guitar.cost)) for guitar in guitars])
    print(max_name_length)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), worth $ {guitar.cost:>{max_cost_length},.2f} {vintage_string}")


main()
