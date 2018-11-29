""" Karatsuba algorithm for multiplication. """

from math import *

def karatsuba(x,y):
    # Set B = 10
    B = 10

    # Recursion base case
    if x < 10 or y < 10:
        return x * y

    # m set to be length of x or y, whichever is maximum
    # This can be done using logarithms with base 10 or alternatively,
    # m = max(len(str(x)), len(str(y)))
    # But such a method will be inefficient for very large n
    m = max(int(log10(x) + 1), int(log10(y) + 1))

    # check whether m is even. If odd, set m lower by 1
    if m % 2 != 0:
        m -= 1
    m_2 = int(m / 2)

    a, b = divmod(x, B**m_2)
    c, d = divmod(y, B**m_2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10**m + bd + ad_bc * 10**m_2

print(karatsuba(1234, 5678))
