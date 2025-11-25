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
    total_bill = 0.00
    print("Let's drive!")
    print(MENU)
    selection = input(">>> ").lower
    while selection != 'q':
        if selection == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            index = get_valid_taxi_index(taxis)
            current_taxi = taxis[index]
        if selection == 'd':
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: {total_bill}")
        print(MENU)
        selection = input(">>> ").lower
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)



def drive_taxi(taxi):
    taxi.start_fare()
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    print(f"Your {taxi.name} will cost you ${taxi.get_fare:.2f}")
    return taxi.get_fare()


def display_taxis(taxis):
    """Display all loaded taxis and their index."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def get_valid_taxi_index(taxis):
    """Get a valid taxi by its index."""
    index = int(input("Choose taxi: "))
    if not (0 >= index > len(taxis)):
        return None
    return index


main()
