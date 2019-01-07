""" Want to select the ith order statistic from an array quickly. """
from random import randrange


def sort_select(A, i):
    """ Naive method: Sort and then pick ith element. """
    A.sort()
    return A[i]


def partition(x, pivot_index = 0):
    """ Subroutine for selection. """
    i = 0
    # Initial swap
    if pivot_index !=0:
        x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x)-1):
        # If current value less than pivot
        if x[j+1] < x[0]:
            # Swap current value with pivot index
            x[j+1], x[i+1] = x[i+1], x[j+1]
            # Increment pivot index
            i += 1
    # Swap pivot value from front to pivot index
    x[0], x[i] = x[i], x[0]
    # Return newly partitioned array and
    return i


def r_select(x, k):
    if len(x) == 1:
        return x[0]
    else:
        j = partition(x, randrange(len(x)))
        if j == k:
            return x[j]
        elif j > k:
            return r_select(x[:j], k)
        else:
            k = k - j - 1
            return r_select(x[(j + 1):], k)


def k_th_median(arr, k):
    """
    Find the median of elements in an array less than k.
    """
    # First, get elements less than k with linear scan
    arr = [x for x in arr if x < k]


def rotate_mat_90(mat):
    """
    Rotates a matrix 90 degrees.
    """
    return [list(x) for x in zip(*[row[::-1] for row in mat])]

m = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
print([max(col) for col in zip(*m)])
