def main():
    password = get_password()
    print_stars_of_length(password)


def print_stars_of_length(length):
    """Print a number of asterisks/stars on one line"""
    print("*" * len(length))


def get_password():
    """Prompt user for a password 5 or more characters in length"""
    password = input("Password: ")
    while len(password) < 5:
        print("Password is too small, must be 5 or more characters")
        password = input("Password: ")
    return password


main()
