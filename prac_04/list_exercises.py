def main():
    numbers = get_numbers(5)
    print(numbers)


def get_numbers(number_of_numbers):
    numbers = []
    for i in range(number_of_numbers):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


main()
