# HINDEX: Takes as input a list of integers and outputs the "H-index", i.e. the number h such that there are h numbers in the list with value at least h
# Input:    int list
# Output:   h_index: int as described above
def h_index(arr):
    n = len(arr)
    arr = sorted(arr)
    for i in range(n):
        if arr[i] >= n - i:
            return arr[i]
    return 0

# There are 4 numbers that are greater than or equal to 4
print(h_index([1,4,1,4,2,1,3,5,6]))
