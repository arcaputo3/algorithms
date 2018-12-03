""" Implementing quicksort. """
import random
import numpy as np


def partition(A, low, high):
    """ Partitions a list around a pivot.
    A[i] <= A[pivot_index] <= A[j] for all i < pivot_index < j < len(A). """
    r = random.randint(low, high)
    A[low], A[r] = A[r], A[low]
    pivot = low
    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]
    A[pivot], A[low] = A[low], A[pivot]
    return pivot


def quicksort(A):
    def _quicksort(A, low, high):
        if high <= low:
            return
        else:
            p = partition(A, low, high)
            _quicksort(A, low, p - 1)
            _quicksort(A, p + 1, high)
        return A
    return _quicksort(A, 0, len(A) - 1)


A = list(np.random.randint(1000, size=1000))
B = quicksort(A)
print(B)
