def print_spiral_order(mat):
    """ Prints a matrix represented as a list of lists in spiral order
    Args:
        mat:   list of lists
    Returns:
        matrix printed in spiral order.
    """
    while mat:
        for x in mat.pop(0):
            print(x)
        for v in mat:
            print(v.pop())
        if mat:
            for x in mat.pop()[::-1]:
                print(x)
        for v in mat[::-1]:
            print(v.pop(0))

print_spiral_order([[1,2,3,4],
                    [4,5,6,123],
                    [1,2,3,4],
                    [7,8,9,10]])
