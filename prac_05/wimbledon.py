"""
Wimbledon
Estimated: 15 min
Elapsed:
"""
import csv

FILENAME = "wimbledon.csv"


def main():
    champion_to_number_of_wins, champion_country = process_file()
    print(champion_to_number_of_wins)
    display_champions(champion_to_number_of_wins)
    display_countries(champion_to_number_of_wins)


def process_file():
    """Read file and extract the number of wins for each champion as well as their country"""
    champion_to_number_of_wins = {}
    champion_country = []
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        for row in reader:
            if not (champion_to_number_of_wins.get(row[2])):
                champion_to_number_of_wins[row[2]] = 1
                champion_country.append([row[2], row[1]])
            else:
                champion_to_number_of_wins[row[2]] += 1
    return champion_to_number_of_wins, champion_country


def display_champions(champion_to_number_of_wins):
    """Display each champion and the number of wins accrued"""
    pass


def display_countries(champion_country):
    """Display all countries assigned to a champion"""
    pass

main()
