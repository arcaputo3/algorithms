""" Akuna interview questions. """
""" Retrieve the median of an array of elements less than a value k. """

import random
import numpy as np
# Measure time performance
from timeit import default_timer as timer


def quickselect(items, item_index):
    """ Selects the ith order statistic of items
    Args:
        items: numeric list
        item_index: ith order statistic
    Returns:
        ith order statistic of items
    """
    def select(lst, l, r, index):
        # Base case
        if r == l:
            return lst[l]
        # Choose random pivot
        pivot_index = random.randint(l, r)
        # Move pivot to beginning of list
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]
        # Partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]
        # recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)
    # Checks for empty list
    if items is None or len(items) < 1:
        return None
    # Checks for index out of bounds
    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()
    # Call helper function
    return select(items, 0, len(items) - 1, item_index)


def get_less_than_k(arr, k):
    """ Filters items less than k from arr. """
    return [x for x in arr if x < k]


def median_less_than_k(A, k):
    """ Gets median of array less than k. """
    arr = get_less_than_k(A, k)
    n = len(arr)
    mid = n//2
    return quickselect(arr, mid)


def sort_select(A, k):
     """ Gets median of items in A less than k. """
     arr = sorted(get_less_than_k(A, k))
     return arr[len(arr)//2]


def full_test(func, test_val, test_arr, test_dict):
    """ Test for correctness and run time.
    Args:
        func:       function
        test_val:   filter value
        test_arr:   list to be sorted
        test_dict:  dict for storing results
    Returns:
        Print statements based on success of sorting.
    """
    # Get sort_func name
    func_name = func.__name__
    # Measure time function takes
    start = timer()
    func(test_arr[:], test_val)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end - start
    print("{}: {} seconds".format(func_name, test_dict[func_name]))
    print()


if __name__ == "__main__":
    test = {}
    ARR = list(np.random.randint(1000, size=1000000))
    K = random.randint(0, 1000)
    full_test(sort_select, K, ARR, test)
    full_test(median_less_than_k, K, ARR, test)

    for key, val in sorted(test.items(), key=lambda kv: kv[1]):
        print('{} is {} times as fast as {}'.format('sort_select', val / test['sort_select'], key))
