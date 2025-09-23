"""
CP1404/CP5632 - Practical
Multi-use program related to setting and evaluating score
"""

MENU = """(G)et a valid score (0-100)
(P)rint results
(S)how stars
(Q)uit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score(0, 100)
        elif choice == "p":
            print(determine_score_category(score))
        elif choice == "s":
            print_stars_of_length(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    print("Goodbye")


def get_valid_score(lower_bound, upper_bound):
    """Return a valid input within specified range"""
    score = int(input("Enter score: "))
    while not (lower_bound <= score <= upper_bound):
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score_category(score):
    """Determine category/grade of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars_of_length(length):
    """Print a number of asterisks/stars on one line"""
    print("*" * length)

main()
