"""Filter users from a JSON file based on different criteria.

This module provides functions to filter users from a JSON file based on
their name, age, or email. The filtered results are printed to stdout.

Functions:
    filter_users_by_name(name): Filter users by matching names
        case-insensitive
    filter_users_by_age(age): Filter users by matching age
    filter_users_by_email(email): Filter users by matching email
"""

import json


def filter_users_by_name(name):
    """Filter and print users by matching names case-insensitive.

    Args:
        name (str): The name to filter users by

    Returns:
        None: Prints matching user records to stdout

    Example:
        >>> filter_users_by_name("John")
        {'id': 1, 'name': 'Joe', 'age': 30, 'email': 'joe@example.com'}
    """
    with open("users.json", "r", encoding="utf8") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filter and print users by matching age.

    Args:
        age (int): The age to filter users by

    Returns:
        None: Prints matching user records to stdout

    Example:
        >>> filter_users_by_age(30)
        {'id': 1, 'name': 'Joe', 'age': 30, 'email': 'joe@example.com'}
    """
    with open("users.json", "r", encoding="utf8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Filter and print users by matching e-mail.

    Args:
        email (str): The email to filter users by

    Returns:
        None: Prints matching user records to stdout

    Example:
        >>> filter_users_by_email('joe@example.com')
        {'id': 1, 'name': 'Joe', 'age': 30, 'email': 'joe@example.com'}
    """
    with open("users.json", "r", encoding="utf8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def main():
    filter_option = (
        input("What would you like to filter by? ('name', 'age' or 'email'): ")
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an e-mail to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
