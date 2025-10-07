from random import randint

NUMBER_OF_NUMBERS = 6
MIN_VALUE = 1
MAX_VALUE = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_of_quick_picks)


def generate_quick_picks(number):
    """Generate a specified number of lists with a set amount and numbers randomised within a certain range"""
    for i in range(number):
        quick_picks = []
        for j in range(NUMBER_OF_NUMBERS):
            pick = randint(MIN_VALUE, MAX_VALUE)
            while pick in quick_picks:
                pick = randint(MIN_VALUE, MAX_VALUE)
            quick_picks.append(pick)
        for pick in sorted(quick_picks):
            print(f"{pick:>2}", end=" ")
        print("")


main()
