"""
Emails
Estimated time: 10 min
Elapsed time:
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_to_email[name] = email
        email = input("Email: ")
    display_dictionary_items(name_to_email)


def extract_name(email):
    """Extract the most likely name from an email, otherwise ask the user for a name if this isn't the ideal name"""
    name = email.split('@')[0].replace('.', ' ').title()
    name_satisfaction = input(f"Is your name {name}? (Y/n) ").upper()
    if name_satisfaction not in ("Y", ""):
        name = input("Name: ")
    return name


def display_dictionary_items(key_to_value):
    """Run through and print each dictionary key and its value"""
    for key in key_to_value:
        print(f"{key} ({key_to_value[key]})")


main()
