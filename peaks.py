# Various peak finding algorithms

# UNIMODALMAX:  Takes as input a unimodal list and outputs its max
# Input:        Unimodal list arr (monotonically increasing followed by monotonically decreasing)
# Ouput:        Max value of arr
def unimodalMax(arr):
    # Base Case
    if len(arr) == 1:
        return arr[0]

    # Recursive step
    # Get middle index
    mid = len(arr)//2-1
    # If middle element less than item to right, recurse right
    if arr[mid] < arr[mid+1]:
        return unimodalMax(arr[mid+1:])
    # Else, recurse left
    else:
        return unimodalMax(arr[:mid+1])


# Testing
# Expect to see 6
print(unimodalMax([1,2,3,4,5,6,5,4,3,2,1]))

# PEAKFIND:     Takes as input a numeric list and outputs a "peak" value (first one found)
# Input:        Numeric list arr
# Output:       Peak value in list (a_{i-1} <= a_i >=  a_{i+1})
def peakfind(arr):
    # Get length
    n = len(arr)

    # Check if single element
    if n == 1:
        return arr[0]

    # Find peak in case of only 2 elements
    if n == 2:
        if arr[0] >= arr[1]:
            return arr[0]
        else:
            return arr[1]

    # Recursive step
    # Check if middle is a peak
    if arr[n//2] >= arr[n//2-1] and arr[n//2] >= arr[n//2 + 1]:
        return arr[n//2]
    # If item to the right is larger, recurse right side of list
    elif arr[n//2] <= arr[n//2+1]:
        return peakfind(arr[n//2+1:])
    # If item to the left is larger, recurse left side of list
    else:
        return peakfind(arr[:n//2-1])


# Testing
# Expect to see 100
print(peakfind(list(range(100))))
# Expect to see 33
print(peakfind([0,1,33,2,56]))

# PEAKFIND2D:       Takes as input a numeric matrix and outputs the value at a peak
# Input:            Numeric list of lists (nxm matrix) mat
# Output:           Peak of mat
def peakfind2d(mat):
    # Get number of rows
    n = len(mat)

    # Since we operate row-wise, we want the number of our rows to be greater than the number of columns
    # Note that each max operation is O(m)
    # It is equivalent to find a peak in the transposed matrix
    # For very very large matrices, this is helpful
    if n < len(mat[0]):
        # Transpose matrix in this case
        mat = [list(i) for i in zip(*mat)]

    # Base case
    if n == 1:
        return max(mat[0])

    # Case for n = 2: only need to check below list
    if n == 2:
        # Get value and index of top row max
        (m,i) = max((v,i) for i,v in enumerate(mat[0]))
        # Save an extra max step if possible
        if m >= mat[1][i]:
            return m
        else:
            return peakfind2d(mat[1])

    # Recursive step
    # Get value and index of middle row max
    (m,i) = max((v,i) for i,v in enumerate(mat[n//2]))
    # Check same column value in rows above and below
    if m >= mat[n//2-1][i] and m >= mat[n//2+1][i]:
        return m
    # If max is less than value directly above, recurse over top half of matrix
    elif m <= mat[n//2-1][i]:
        return peakfind2d(mat[:n//2-1])
    # Else, recurse bottom half of matrix
    else:
        return peakfind2d(mat[n//2+1:])

# Expect to see 3
print(peakfind2d([[1,2,3],
                  [3,2,1]]))
# Expect to see 10
print(peakfind2d([[1,2,3],
                  [3,10,5],
                  [6,9,4]]))
