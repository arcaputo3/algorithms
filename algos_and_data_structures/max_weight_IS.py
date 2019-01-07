""" Computing max weight independent sets. """

def get_weights(filename="mwis.txt"):
    """ Upload weights."""
    arr = []
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        for line in file.readlines():
            arr.append(int(line))
    return arr


def max_weight_IS(arr):
    """ Determines the max weight independent set of an array.
    Args:
        arr: numeric list representing node weights of linear graph
    Returns:
        MWIS itself according to index (non zero indexed).
    """
    n = len(arr)
    # Check base cases
    if n == 1:
        return arr[0], arr
    if n == 2:
        s = max(arr[0], arr[1])
        return s, [s]
    # Init A for max value book keeping
    A = [0]*(n + 1)
    A[1] = arr[0]
    # Dynamic for loop
    for i in range(2, n+1):
        A[i] = max(A[i-1], A[i-2] + arr[i-1])
    # Init V for MWIS values
    V = set()
    # Back propogate to populate V
    while n >= 1:
        # If max A_{i-1} >= max A_{i-2} + arr_i,
        # then arr_i is not a member of V
        if A[n-1] >= A[n-2] + arr[n-1]:
            n -= 1
        # Otherwise, it is and we know that we need not consider arr_{i-2}
        else:
            V.add(n)
            n -= 2
    return V


if __name__ == "__main__":
    V = max_weight_IS(get_weights())
    out = ""
    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        out += "1" if i in V else "0"
    print(out)
