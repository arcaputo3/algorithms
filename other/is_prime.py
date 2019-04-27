from math import sqrt

def is_prime(num):
    """ Determines whether or not a number is prime. """

    for i in range(2, int(sqrt(num)) + 2):
        if num % i == 0:
            return False
    return True


def find_primes(n):
    """ Finds all primes <= n. """
    # Base case
    if n < 2:
        return None
    # Begin with 2 and iteratively build
    primes = [2]
    for i in range(3, n+1):
        if i % 2 == 0:
            pass
        if all(i % p for p in primes):
            primes.append(i)
    return primes


def find_primes_sieve(n):
    """ Finds all primes < n. """

    A = [True for _ in range(n)]

    for i in range(2, int(sqrt(n)) + 2):
        if A[i]:
            for j in range(i**2, n, i):
                A[j] = False
    return [i+2 for i, v in enumerate(A[2:]) if v]
