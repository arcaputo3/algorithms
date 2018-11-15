# Suppose we want to compute the number of set bits in n (i.e. the number of bitwise 1's)
# We can implement an O(n) algorithm as follows:
def ok_count_bits(n):
    num_bits = 0
    while n:
        # Adds one if last bit is 1
        num_bits += n&1
        # Shifts n to the right once
        n >>= 1
    return num_bits


# A better way to count bits is to use the fact that n&(n-1) drops the last set bit
# We can then improve the run time to O(k) where k = count_bits(n), k <= n
def good_count_bits(n):
    num_bits = 0
    while n:
        num_bits += 1
        n = n&(n-1)
    return num_bits


# We now define the parity of an integer:
# Let n be an integer represented bitwise
# The parity of n is 1 if the number of 1's in n are odd
# otherwise, the parity is even

# Naive / Brute force algorithm
def bad_parity(n):
    result = 0
    while n:
        # result = 0, last_bit = 1: result = 1
        # result = 1, last_bit = 0: result = 1
        # result = 0, last_bit = 0: result = 0
        # result = 1, last_bit = 1: result = 0
        result ^= n&1
        # Shift n to the right once
        n >>= 1
    return result


# We can do better by only needing to operate k times,
# where k is the number of set bits in n, i.e. k = count_bits(n).
# Note that for any integer n, n&(n-1) drops the lowest set bit of n

# Better algorithm
def better_parity(n):
    result = 0
    while n:
        # If we count even times
        # Result will equal 0
        # If we count odd times
        # Result = 1
        result ^= 1
        # Drop last set bit
        n = n&(n-1)
    return result


# We can do even better if we use the fact that the XOR of a group of bits
# is equal to the parity of the bits. Thus, we can split a very large integer
# into two halves of bits. Consider 1001. The parity is equal to
# 10 XOR 01 = 11
# 1 XOR 1 = 0
# We can do this many times to achieve O(log(n)) runtime
def best_parity(n):
    n ^= n>>32
    n ^= n>>16
    n ^= n>>8
    n ^= n>>4
    n ^= n>>2
    n ^= n>>1
    return n & 0x1


# Now, consider the problem of checking whether or not a number is a power of 2.
# Note that any power of 2 is of the form ...000010000.... where n contains only a single 1
# i.e. check if n = 2^x for some x. We can simply use the n&(n-1) operator and check if the result is 0
def pow_of_two(n):
    n = n&(n-1)
    return (n==0)


# We consider the case when we want to swap two bits in a number.
# We imagine the number as an array representation of bits
# This reduces the problem to array swapping. But there is a more creative way and in O(1) time!
def swap_bits(n, i, j):
    # Extract the i-th and j-th bits, see if they differ.
    if (n >> i) & 1 != (n >> j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        # Select the bits with bit_mask. Since n^1 = 0 if n=1 and n^1 = 1 if n=0
        # We can perform a bit swap using XOR
        bit_mask = (1 << i) | (1 << j)
        n ^= bit_mask
    return n
