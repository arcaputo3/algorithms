# Examples of the power of itertools

from itertools import combinations
from itertools import groupby
from itertools import product

# COMPRESS_INT: Compresses a large int into list of tuples
# Input:    int n
# Output:   list of int tuples (a,b) such that a is the number of occurences of b
def compress_int(n):
    n = list(str(n))
    return [(len(list(i)),int(k)) for k, i in groupby(n)]


# Test of compress_int
print(*compress_int(112222233356))

# PROB_OF_COMBO:    Determines the probability that a letter is in any combination of the values in a string
# Input:            string elt, space seperated string arr, int length of combinations K
# Output:           probability that elt is in any combination of arr of length K
def prob_of_comb(elt,arr,K):
    count = 0
    arr = list(arr)
    for i in combinations(arr,K):
        if elt in i:
            count += 1
    return count/len(list(combinations(arr,K)))


# Test of prob_of_comb
print(prob_of_comb('a','aabc',2))

# All possible cartesian products from each list represented as tuples
print(list(product(*([1,2,3],[4,5,6],[7,8,9]))))

# All possible order-preserving combinations of any string
s = 'abcd'
print([s[i:j+1] for i in range(len(s)) for j in range(i,len(s))])
