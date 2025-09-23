def main():
    password = get_password()
    print_stars_of_length(password)


def print_stars_of_length(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < 5:
        print("Password is too small, must be 5 or more characters")
        password = input("Password: ")
    return password


main()
