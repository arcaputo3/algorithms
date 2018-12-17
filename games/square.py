import numpy as np

def get_answer():
    full_sq = list(range(1, 10))
    squares = [(1, 2, 4, 5), (2, 3, 5, 6), (4, 5, 7, 8), (5, 6, 8, 9), (1, 3, 7, 9), (2, 4, 6, 8)]
    sums = [sum([full_sq[i-1] for i in sq]) for sq in squares]
    while sums != [20]*6:
        np.random.shuffle(full_sq)
        sums = [sum([full_sq[i-1] for i in sq]) for sq in squares]
    return full_sq, sums

print(get_answer())
