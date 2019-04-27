""" Simulating various expectations. """

import numpy as np

def throw(iters=10000):
    """ Calculating expected number of die throws such that each side has shown up at least once. """
    count = 0
    for _ in range(iters):
        seen = set()
        while len(seen) < 6:
            count += 1
            seen.add(np.random.randint(6))

    return count/iters

print(f"Expected number of times needed to throw a die until all sides seen is roughly {throw()}")


def dist_btw_unif(iters=10000):
    d = 0
    for _ in range(iters):
        x, y = np.random.rand(), np.random.rand()
        x, y = min(x, y), max(x, y)
        d += max(x, y-x, 1-y)
    return d/iters

print(f"Expected length of longest side of stick after it is broken into three parts is roughly {dist_btw_unif()}")


def halve_integers(n=1000, iters=5000):
    count = 0
    for _ in range(iters):
        m = n
        while m > 0:
            m = np.random.randint(m)
            count += 1
    return count/iters

print(halve_integers(), sum(1/i for i in range(1, 1000)))


def digit_prod_sum(n=10000):
    ss = 0
    for i in range(n):
        prod = 1
        for v in str(i):
            prod *= 1 if v == '0' else int(v)
        ss += prod

    return ss

print(digit_prod_sum())


def coin_gamble(iters=100):
    total = 0
    for _ in range(iters):
        curr = 0
        H, T = 0, 0
        while H < 2 or T < 2:
            curr += 1
            if (H >= 2 and T == 1) or (H == 1 and T >= 2):
                total += curr
                break
            c1, c2 = np.random.rand(), np.random.rand()
            #if (c1 < 1/2 and c2 > 1/2) or (c1 > 1/2 and c2 < 1/2):
                #break
            if c1 > 1/2 and c2 > 1/2:
                T += 2
            elif c1 < 1/2 and c2 < 1/2:
                H += 2
            else:
                H += 1
                T += 1

    return total / iters

print(coin_gamble())
