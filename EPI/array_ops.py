""" Array operations from Elements of Programming Interviews in Python. """

def plus_one(A):
    """ Takes as input an array of digits encoding a non-negative integer D
    and updates the array to represent the integer D + 1.
    Args:
        A:  int array representing integer D
    Returns:
        A representing integer D + 1
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


def add_binary_nums(x, y):
    """ This function adds two binary
    strings return the resulting string """
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # initialize the result
    result = ''

    # initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1     # Compute the carry.

    if carry !=0 : result = '1' + result

    return result.zfill(max_len)


def multiply(num_1, num_2):
    """ Multiplies two numbers represented as arrays. """
    # Get sign (-1 if only one of heads is negative)
    sign = -1 if (num_1[0] < 0) ^ (num_2[0] < 0) else 1
    # Convert to absolute val
    num_1[0], num_2[0] = abs(num_1[0]), abs(num_2[0])
    # Initialize result
    result = [0]*(len(num_1) + len(num_2))
    # Double for loop
    for i in reversed(range(len(num_1))):
        for j in reversed(range(len(num_2))):
            # Intialize current operation
            result[i + j + 1] += num_1[i] * num_2[j]
            # Carry over leftover digits
            result[i + j] += result[i + j + 1] // 10
            # Keep only digits less than 10
            result[i + j + 1] %= 10
    # Remove leading zeroes
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return result[sign * result[0]] + result[1:]


def delete_duplicates(A):
    """ Deletes duplicate entries in A in-place and in O(n) time O(1) space. """
    if not A:
        return 0
    write_index = 1
    # Iterate through list, writing over duplicate entries.
    for i in range(1, len(A)):
        # Write over if we haven't seen this entry yet.
        # Notice that if we've seen an entry, write_index does not increment.
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]


def index_equals_value(A):
    """ Given a sorted array, determines if there exists index i such that
        A[i] == i. """
    def binary_search(A, low, high):
        if high >= low:
            mid = (low + high)//2
        else:
            return -1
        if mid is A[mid]:
            return mid
        if mid >= A[mid]:
            return binary_search(A, (mid + 1), high)
        else:
            return binary_search(A, low, (mid - 1))
    return binary_search(A, 0, len(A) - 1)

print(index_equals_value([-1, 0, 2]))
