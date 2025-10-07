def main():
    numbers = get_numbers(5)
    print_information(numbers)


def get_numbers(number_of_numbers):
    """Prompt the user for a specific number of integers"""
    numbers = []
    for i in range(number_of_numbers):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def print_information(numbers):
    """Display information about a list of numbers"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    total = 0
    average = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    print(f"The average of the numbers is {average}")


main()
