""" Various sorting algorithms with time tests. """

# Measure time performance
from timeit import default_timer as timer
# Test with random array
import numpy as np
# Get heap_sort
from heaps import heap_sort


def bubble_sort(arr):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
        IN PLACE
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    for i, v_i in enumerate(arr):
        for j, v_j in enumerate(arr):
            if v_i > v_j:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    arr_sorted = []
    while arr:
        lowest = arr[0]
        low_ind = 0
        for i, v in enumerate(arr[1:]):
            if v < lowest:
                lowest = v
                low_ind = i+1
        arr_sorted.append(arr.pop(low_ind))
    return arr_sorted


def insertion_sort(arr):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
        IN PLACE
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    for j in range(1, len(arr)):
        # Current node
        key = arr[j]
        # New index
        i = j - 1
        # Iterate while list behind key is unsorted
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


def merge(arr1, arr2):
    """ (Sub Routine) Takes as input two sorted lists and merges them.
    Args:
        arr1, arr2: sorted float (int) lists
    Returns:
        A single merged list containing each element of arr1 and arr2.
    """
    out = []
    # Iterate while neither list is empty
    while arr1 and arr2:
        # Compare heads, pop smallest head and append to output
        if arr1[0] <= arr2[0]:
            out.append(arr1.pop(0))
        else:
            out.append(arr2.pop(0))
    # Concat whichever array has more elements
    if arr1:
        out += arr1
    else:
        out += arr2
    return out


def merge_sort(arr):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    n = len(arr)
    # Base case
    if n == 1:
        return arr
    # Recursive step: sort each half of the elements
    return merge(merge_sort(arr[:n//2]), merge_sort(arr[n//2:]))


# If we have that each element in the list is an integer,
# i.e. for all i in list, i in {0,1,...,k-1}
# we can use count sort to get O(n) sorting time
def count_sort(arr, k=1000):
    """ Takes as input an INTEGER list and an int k such that k-1 is largest possible element.
    Args:
        arr: int list
        k:   int
    Returns:
        int list sorted.
    """
    store = [[] for i in range(k)]
    for v in arr:
        store[v].append(v)
    output = []
    for i in range(k):
        if store[i]:
            output += store[i]
    return output


############## TESTING ###############

# Testing functions
def pass_test(sort_func, arr):
    """ Compare sorted function with true sorted array
    Args:
        sort_func:  function for sorting
        arr:        list to be sorted
    Returns:
        Print statements based on success of sorting.
    """
    sort_array = sorted(arr[:])
    # Print accordingly
    if sort_func(arr) == sort_array:
        print("Test Passed")
    else:
        print("Error: Test not passed")


def full_test(sort_func, test_arr, test_dict):
    """ Test for correctness and run time.
    Args:
        sort_func:  function for sorting
        test_arr:   list to be sorted
        test_dict:  dict for storing results
    Returns:
        Print statements based on success of sorting.
    """
    # Get sort_func name
    func_name = sort_func.__name__
    # Measure time function takes
    start = timer()
    sort_func(test_arr)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end - start
    # Test for correctness
    pass_test(sort_func, test_arr)
    print("{}: {} seconds".format(func_name, test_dict[func_name]))
    print()


if __name__ == "__main__":
    # Test time storage dictionary
    test = {}
    # Large test array
    ARR = list(np.random.randint(1000, size=1000))
    full_test(bubble_sort, ARR, test)
    full_test(insertion_sort, ARR, test)
    full_test(merge_sort, ARR, test)
    full_test(heap_sort, ARR, test)
    full_test(sorted, ARR, test)
    full_test(count_sort, ARR, test)
    full_test(selection_sort, ARR, test)
    for key, val in test.items():
        print('{} is {} times as fast as {}'.format('sorted', val / test['sorted'], key))
