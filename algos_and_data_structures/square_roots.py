""" Calculating square roots with Newton's Method. """

import math


def sqrt(n, iters=10):
    """ Calculates the approximated square root of n.
    Args:
        n:          int (float)
        iters:      int [Increasing gives better accuracy]
    Returns:
        Approximate square root of n.
    """

    # Choose arbitrary initialization
    x = n/3
    # Repeat Newton's method
    for _ in range(iters):
        x = (1/2)*(x + n/x)
    return x


if __name__ == "__main__":
    print(sqrt(17))
    print(math.sqrt(17))
