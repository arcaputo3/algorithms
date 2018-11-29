""" Counts number of inversions in a list.
Note that the number of inversions of a list A is the number of pairs (i, j),
i < j such that A[i] > A[j].
The maximum number of inversions a list of length n can have is
(n choose 2) = n(n - 1)/2. This happens when A is in descending order.
 """

def merge_count(arr1, arr2, count=0):
    """ (Sub Routine) Takes as input two sorted lists and merges them.
    Args:
        arr1, arr2:     sorted float (int) lists
        count:          default to 0, count of inversions
    Returns:
        - A single merged list containing each element of arr1 and arr2.
        - The number of inversions found from merging the lists.
    """
    out = []
    # Iterate while neither list is empty
    while arr1 and arr2:
        # Compare heads, pop smallest head and append to output
        if arr1[0] <= arr2[0]:
            out.append(arr1.pop(0))
        else:
            count += len(arr1)
            out.append(arr2.pop(0))
    # Concat whichever array has more elements
    if arr1:
        out += arr1
    else:
        out += arr2
    return out, count


def count_sort(arr):
    """ Sorts arr AND counts number of inversions in arr in O(n log n) time.
    Arg:
        arr: int (float) list
    Returns:
        - arr sorted in increasing order.
        - Number of inversions in arr.
    """
    n = len(arr)
    # Base case
    if n == 1:
        return arr, 0
    # Recursive call on left half
    left, x = count_sort(arr[:n//2])
    # Recursive call on right half
    right, y = count_sort(arr[n//2:])
    # Merge recursive calls and add counts
    full, z = merge_count(left, right)
    return full, x + y + z


print(count_sort(list(range(100,-1,-1))))
