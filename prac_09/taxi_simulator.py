"""
Time estimate: 30 min
Time elapsed:
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Display various menu options for user to interact with to drive their virtual taxis."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    selection = input(">>> ").lower
    while selection != 'q':
        if selection == 'c':
            display_taxis_by_index(taxis)
            current_taxi = get_valid_taxi_index(taxis)


def display_taxis_by_index(taxis):
    """Display all loaded taxis and their index."""
    print("Taxis available:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")

def get_valid_taxi_index(taxis):
    """Get a valid taxi by its index."""
    valid = False
    index = input("Choose taxi: ")
    while not valid:
        try:
            if 0 <= int(index) < len(taxis):
                valid = True
            else:
                print("Invalid taxi choice")
                index = input("Choose taxi: ")
        except TypeError:
            print("Invalid taxi choice")
            index = input("Choose taxi: ")
    return index





main()
