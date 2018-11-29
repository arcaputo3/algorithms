""" Algorithms for checking if integer is a palindrome. """

import math
from reverse_digits import digit_reverse_math


def palindrome(x):
    """ Checks if int x is a palindrome.
    Args:
        x:  int
    Returns:
        True if x is a palindrome else False.
    """
    # If x < 0, x cannot be a palindrome
    if x <= 0:
        return x == 0
    # Get number of digits using built-in library math
    num_digits = math.floor(math.log10(x)) + 1
    # msd_mask used to extract most significant digit
    msd_mask = 10**(num_digits - 1)
    # Check if digits at each end match for each possibility
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        # Remove most significant digit
        x %= msd_mask
        # Remove least significant digit
        x //= 10
        # x is now two digits smaller,
        # so msd_mask must also be two digits smaller
        msd_mask //= 100
    return True


def palindrome_rev(x):
    """ Checks if int x is a palindrome.
    Args:
        x:  int
    Returns:
        True if x is a palindrome else False.
    """
    # If x < 0, x cannot be a palindrome
    if x <= 0:
        return x == 0
    # Simply check if x equals its reverse
    y = digit_reverse_math(x)
    if x == y:
        return True
    return False


print(palindrome(123454321))
print(palindrome_rev(123454321))
