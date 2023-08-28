def main():
    # First task: Gather and display information about numbers
    numbers = gather_numbers()
    display_number_info(numbers)

    # Second task: Woefully inadequate security checker
    security_checker()


def gather_numbers():
    """Prompt the user for 5 numbers and return them in a list."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))  # Used float to handle both integer and decimal input
        numbers.append(number)
    return numbers


def display_number_info(numbers):
    """Display various details about the provided list of numbers."""
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


def security_checker():
    """Check if the provided username is in the authorized list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username_input = input("Enter your username: ")
    if username_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
