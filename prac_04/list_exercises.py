def first_exercise():
    numbers = get_numbers()
    print_information(numbers)


def get_numbers():
    """Prompt the user for a specific number of integers"""
    numbers = []
    count = 1
    number = 0
    while number >= 0:
        number = int(input(f"Number {count}: "))
        numbers.append(number)
        count += 1
    # Technically, the practice question does not state anything about not parsing the negative number at the end of the list
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


def second_exercise():
    username = input("Username: ")
    if is_authorised(username):
        print("Access Granted")
    else:
        print("Access Denied")


def is_authorised(username):
    """Check whether username is in list of authorised usernames"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    return username in usernames


first_exercise()
second_exercise()
