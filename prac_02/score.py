"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

def main():
    score = float(input("Enter score: "))
    print(determine_score_category(score))

    print(determine_score_category(randint(0,100)))


def determine_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()