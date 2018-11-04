# NBIT ADDITION: Adds two n length binary integers represented as arrays of 0's and 1's
# Input:    Two binary arrays arr1, arr2
# Output:   Addition of arr1 and arr2
def nbit_add(arr1, arr2):
    n = len(arr1)
    arr = [0]*(n+1)
    for i in range(n):
        if arr1[i] == 1 and arr2[i] == 1:
            arr[i] = 1
        elif arr1[i] == 1 or arr1[i] == 1:
            arr[i+1] = 1
    return arr

print(nbit_add([1,1,1],[1,1,1]))
