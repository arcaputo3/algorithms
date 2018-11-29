""" Ways to reverse digits in python. """

def digit_reverse_string(x):
    """ Reverses an int x.
    Args:
        x:  int
    Returns:
        x in reversed digit order.
    """
    x = str(x)[::-1]
    if x[-1] == '-':
        x = '-' + x[:-1]
    return int(x)


def digit_reverse_math(x):
    """ Reverses an int x.
    Args:
        x:  int
    Returns:
        x in reversed digit order.
    """
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


if __name__ == "__main__":
    print(digit_reverse_string(12910283459023498123904045981125875089352631285155529235871239058356123651785668746189640981437028934738902741023984778596812635891603))
    print(digit_reverse_math(12910283459023498123904045981125875089352631285155529235871239058356123651785668746189640981437028934738902741023984778596812635891603))
