from typing import List, Union


def kilograms_to_pounds(kgs: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Converts list of kilograms to list of pounds
    Args:
        kgs (List[Union[int, float]]): List of kgs
    Returns:
        (List[Union[int, float]]): List of kgs converted to pounds
    """
    return list(map((lambda x: x * 2.2), kgs))


def add_numbers_in_list(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Add all numbers in a list
    Args:
        numbers (List[Union[int, float]]): List of numbers
    Returns:
        Union[int, float]: Addition of all numbers in the list
    """
    return sum(numbers)


def check_if_number_in_range(number: Union[int, float], min_range: Union[int, float], max_range: Union[int, float]) \
        -> bool:
    """
    Check if a number exists in a range
    Args:
        number (Union[int, float]): Number to check
    Returns:
        bool: True if number exists in range, otherwise False
    :return:
    """
    x = range(min_range, max_range)
    return number in x


def check_if_number_is_prime(number: Union[int, float]):
    """
    Check if a number is prime
    Args:
        number (Union[int, float]): Number to check
    Returns:
        bool: True if number is prime, otherwise False
    """
    is_prime = False
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                break
        else:
            is_prime = True
    return is_prime


def check_if_string_is_palindrome(string: str) -> bool:
    """
    Check if string is a palindrome
    Args:
        string (str): String to check
    Returns:
        bool: True if string is a palindrome, otherwise False
    """
    reversed_string = string[::-1]
    return string == reversed_string



