# Various sorting algorithms

# INSERTION_SORT:   Takes as input a real valued list and sorts the values from smallest to largest
# Input:            ARR float (int) list
# Output:           float (int) list sorted ascending
def insertion_sort(arr):
    for j in range(1,len(arr)):
        # Current node
        key = arr[j]
        # New index
        i = j-1
        # Iterate while list behind key is unsorted
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


# MERGE:        (Sub Routine) Takes as input two sorted lists and merges them
# Input:        ARR1, ARR2, sorted float (int) lists
# Output:       A single merged list containing each element of ARR1 and ARR2
def merge(arr1, arr2):
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


# MERGE_SORT:       Takes as input a real valued list and sorts the values from smallest to largest
# Input:            float (int) list
# Output:           float (int) list sorted ascending
def merge_sort(arr):
    n = len(arr)
    # Base case
    if n == 1:
        return arr
    else:
        # Recursive step: sort each half of the elements
        return merge(merge_sort(arr[:n//2]),merge_sort(arr[n//2:]))


# TESTING

# Measure time performance
from timeit import default_timer as timer

# Test with random array
import numpy as np

# Test time storage dictionary
test = {}

# Large test array
arr = list(np.random.randint(1000,size=3000))

# Testing functions
def pass_test(sort_func,arr):
    # Compare sorted function with true sorted array
    sort_array = sorted(arr)
    # Print accordingly
    if sort_func(arr) == sort_array:
        print("Test Passed")
    else:
        print("Error: Test not passed")


def full_test(sort_func, test_arr, test_dict):
    # Get sort_func name
    func_name = sort_func.__name__
    # Measure time function takes
    start= timer()
    ans = sort_func(arr)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end-start
    # Test for correctness
    pass_test(sort_func,arr)
    print("{}: {} seconds".format(func_name,test_dict[func_name]))
    print()


full_test(insertion_sort, arr, test)
full_test(merge_sort, arr, test)
