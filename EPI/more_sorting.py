def insertion_sort_dec(arr):
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
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr

print(insertion_sort_dec([1,2,3,4,5]))
