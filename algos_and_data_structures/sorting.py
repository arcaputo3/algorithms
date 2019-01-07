""" Various sorting algorithms with time tests. """

# Measure time performance
from timeit import default_timer as timer
# Test with random array
import numpy as np
import random
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
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    arr_sorted = []
    # Repeatedly pop min of array and append to output
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
        out.extend(arr1)
    else:
        out.extend(arr2)
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
    # Pre-allocate memory for k bins to store occurrences
    store = [[] for i in range(k)]
    # Iterate through arr and store each occurence in resp. bin
    for v in arr:
        store[v].append(v)
    # Initialize output
    output = []
    # Iterate through bins and add each list to output
    for i in range(k):
        if store[i]:
            output += store[i]
    return output


def partition(A, low, high):
    """ Partitions a list around a random pivot.
    A[i] <= A[pivot_index] <= A[j] for all 0 <= i < pivot_index < j < len(A). """
    # Randomly swap first element
    r = random.randint(low, high)
    A[low], A[r] = A[r], A[low]
    # Initialize pivot
    pivot = low
    for i in range(low + 1, high + 1):
        # If current element less than pivot element,
        # swap current with pivot index
        if A[i] < A[low]:
            # Increment pivot index
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]
    # Correctly place pivot
    A[pivot], A[low] = A[low], A[pivot]
    return pivot


def quicksort(A):
    """ Takes as input a real valued list and sorts the values from smallest to largest.
    Args:
        arr: float (int) list
    Returns:
        float (int) list sorted ascending.
    """
    def _quicksort(A, low, high):
        """ Sub-routine that supports indexing.
        """
        if high <= low:
            return A
        else:
            p = partition(A, low, high)
            _quicksort(A, low, p - 1)
            _quicksort(A, p + 1, high)
        return A
    return _quicksort(A, 0, len(A) - 1)


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
    if sort_func(arr[:]) == sort_array:
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
    sort_func(test_arr[:])
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
    ARR = list(np.random.randint(1000, size=5000))
    full_test(bubble_sort, ARR, test)
    full_test(insertion_sort, ARR, test)
    full_test(merge_sort, ARR, test)
    full_test(heap_sort, ARR, test)
    full_test(sorted, ARR, test)
    full_test(count_sort, ARR, test)
    full_test(selection_sort, ARR, test)
    full_test(quicksort, ARR, test)
    for key, val in sorted(test.items(), key=lambda kv: kv[1]):
        print('{} is {} times as fast as {}'.format('sorted', val / test['sorted'], key))
