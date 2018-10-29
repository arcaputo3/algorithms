# COUNT_BITS:   Counts the number of bits set to one in an int
# Input:        int n
# Output:       int b, number of bits in n

def count_bits(x):
    num_bits = 0
    while x > 0:
        num_bits += 1
        x >> 1
    return num_bits

if __name__ == "__main__":
    print(count_bits(7))
