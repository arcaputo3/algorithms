# This is a representation of heaps in python using arrays
import numpy as np


# MAX_HEAPIFY:      Corrects input of a list from node i down doing single correction
# Input:            numeric list A, int index i
# Output:           heapified list A
def max_heapify(A, i):
    # Get left index
    l = 2*i+1
    # Get right index
    r = 2*i+2
    # Get current index
    largest = i
    # Check if index in range and if item on left branch larger than parent
    if l < len(A) and A[l] > A[largest]:
        # If true, set largest to left item
        largest = l
    # Check if list is big enough and if item on right branch larger than largest
    if r < len(A) and A[r] > A[largest]:
        # If true, set largest to right item
        largest = r
    # If we changed largest,
    if largest != i:
        # Swap current parent with largest
        A[i], A[largest] = A[largest], A[i]
        # and traverse to node we swapped (i.e. least node visited so far)
        max_heapify(A,largest)


# BUILD_MAX_HEAP:   Takes any list and converts to a max heap
# Input:            numeric list A
# Output:           fully heapified list A
def build_max_heap(A):
    # Only need to heapify nodes with children: n//2 is largest index whose node has children
    for i in range(len(A)//2, -1, -1):
        # Build from the bottom up, visiting each node with children
        max_heapify(A, i)


# PTREE:    Builds a ptree out of heap A
# Input:    heap A
# Output:   visual representation of heap A
def ptree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        ptree(A, i * 2 + 1, indent + 1)
        ptree(A, i * 2 + 2, indent + 1)


# HEAP_SORT:    Takes as input a numeric list and outputs the list sorted (using a heap)
# Input:        (Unsorted) numeric list arr
# Output:       Sorted numeric list
def heap_sort(arr):
    build_max_heap(arr)
    out = []
    while arr:
        arr[0], arr[-1] = arr[-1], arr[0]
        last = arr.pop()
        out.insert(0, last)
        max_heapify(arr, 0)
    return out

# Test
'''
B = list(np.random.randint(100, size = 100))
print(heap_sort(B))
'''
