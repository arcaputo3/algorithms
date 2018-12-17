""" Algorithms for finding maximum subarry. """


import math
from timeit import default_timer as timer
import numpy as np


########## BRUTE FORCE ##########


def brute(A):
    """ Brute force algorithm for finding maximum subarray.
    Solves in O(n^2) time. """
    max_sum = 0
    best_i, best_j = None, None
    # Iterate over all (n choose 2) possibilities
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if sum(A[i:j]) > max_sum:
                max_sum = sum(A[i:j])
                best_i, best_j = i, j - 1
    return best_i, best_j, max_sum


########## DIVIDE AND CONQUER ##########


def find_max_crossing_subarray(A, low, mid, high):
    """ We now use divide and conquer. First, define the necessary subroutine. """
    left_sum = -math.inf
    ssum = 0
    # Traverse over left half of array
    for i in reversed(range(low, mid + 1)):
        ssum += A[i]
        if ssum > left_sum:
            left_sum = ssum
            max_left = i
    right_sum = -math.inf
    ssum = 0
    # Traverse over right half of array
    for j in range(mid + 1, high + 1):
        ssum += A[j]
        if ssum > right_sum:
            right_sum =  ssum
            max_right = j
    # The max crossing subarray sums to left_sum + right_sum
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
    """ Implement full routine. """
    if high == low:
        return (low, high, A[low])
    mid = (low + high) // 2
    # Recurse left half of array.
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    # Recurse right half of array.
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
    # Check for crossing.
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
    # Return best sums.
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else: # cross_sum >= left_sum and cross_sum >= right_sum
        return (cross_low, cross_high, cross_sum)


def wrap_find_max_subarray(A):
    """ Wrapper function to init low and high. """
    return find_max_subarray(A, 0, len(A) - 1)


########## DYNAMIC PROGRAMMING ##########


def dyn_max_subarray(A):
    """ Dynamic programming method. """
    # Initialize counters
    max_so_far = A[0]
    curr_max = A[0]
    start, end = 0, 1
    for i, v in enumerate(A):
        curr_max = max(v, curr_max + v)
        if curr_max == v:
            start = i
        max_so_far = max(max_so_far, curr_max)
        if max_so_far == curr_max:
            end = i
    return start, end, max_so_far


########## TESTING ##########


def full_test(func, test_arr, test_dict):
    """ Tests runtime of our functions. """
    # Get func name
    func_name = func.__name__
    # Measure time function takes
    start= timer()
    ans = func(test_arr)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end - start
    # Test for correctness
    print("{}: {} seconds".format(func_name, test_dict[func_name]))
    print(ans)
    print()


if __name__ == "__main__":
    test = {}
    TEST_ARR = np.random.randint(-100, high=100, size=15 )
    full_test(brute, TEST_ARR, test)
    full_test(wrap_find_max_subarray, TEST_ARR, test)
    full_test(dyn_max_subarray, TEST_ARR, test)
    for key, val in sorted(test.items(), key=lambda kv: kv[1]):
        print('{} is {} times as fast as {}'.format('dyn_max_subarray', val / test['dyn_max_subarray'], key))
