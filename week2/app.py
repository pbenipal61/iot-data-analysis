from week2.exs import *


def main():
    some_dummy_list = [1, 2.2, 3]
    # Convert kilograms to pounds
    print(kilograms_to_pounds(some_dummy_list))

    # Sum of all numbers in a list
    print(add_numbers_in_list(some_dummy_list))

    # Check if a number is in a range
    print(check_if_number_in_range(some_dummy_list[0], -1, 3))

    # Check if a number is prime
    print(check_if_number_is_prime(17))

    # Check if a string is palindrome
    print(check_if_string_is_palindrome("madam"))


if __name__ == "__main__":
    main()
