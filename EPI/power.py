""" Various exponentiating algorithms with time tests. All powers must be >= 1. """

# Measure time performance
from timeit import default_timer as timer
# Test with random array
import numpy as np


def slow_pow(x, y):
    """ Computes x^y
    Args:
        x:  initial int
        y:  power x will be raised to
    Returns:
        x^y
    """
    if y == 1:
        return x
    return x * slow_pow(x, y - 1)


def recursive_power(x, y):
    """ Computes x^y
    Args:
        x:  initial int
        y:  power x will be raised to
    Returns:
        x^y
    """
    if y == 1:
        return x
    if y % 2 == 0:
        return recursive_power(x * x, y / 2)
    else:
        return x * recursive_power(x * x, y // 2)


def bit_power(x, y):
    """ Computes x^y
    Args:
        x:  initial int
        y:  power x will be raised to
    Returns:
        x^y
    """
    result, power = 1, y
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

def built_in_power(x, y):
    return x ** y

############## TESTING ###############

# Testing functions
def pass_test(power_func, num, pow):
    """ Compare power function with built-in exponentiation
    Args:
        power_func: function for exponentiation
        num:        initial int
        power:      power to exponentiate too
    Returns:
        Print statements based on success of function.
    """
    true_pow = num**pow
    # Print accordingly
    if true_pow == power_func(num, pow):
        print("Test Passed")
    else:
        print("Error: Test not passed")


def full_test(power_func, test_num, test_pow, test_dict):
    """ Test for correctness and run time.
    Args:
        power_func:     function for exponentiation
        test_num:       initial int
        test_pow:       power to exponentiate too
        test_dict:      dict for storage
    Returns:
        Prints time taken by power_func
    """
    # Get sort_func name
    func_name = power_func.__name__
    # Measure time function takes
    start = timer()
    power_func(test_num, test_pow)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end-start
    # Test for correctness
    pass_test(power_func, test_num, test_pow)
    print("{}: {} seconds".format(func_name, test_dict[func_name]))
    print()


if __name__ == "__main__":
    # Test time storage dictionary
    test = {}
    TEST_NUM = 99
    TEST_POW = 400
    full_test(slow_pow, TEST_NUM, TEST_POW, test)
    full_test(recursive_power, TEST_NUM, TEST_POW, test)
    full_test(bit_power, TEST_NUM, TEST_POW, test)
    full_test(built_in_power, TEST_NUM, TEST_POW, test)
    # Check how much faster built-in is
    for key, val in test.items():
        print('{} is {} times faster than {}'.format('built_in_power', val / test['built_in_power'], key))
