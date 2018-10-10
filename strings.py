# Needs to be commented

from itertools import groupby

# COMPRESS_INT: Compresses a large int into list of tuples
# Input:    int n
# Output:   list of int tuples (a,b) such that a is the number of occurences of b
def compress_int(n):
    n = list(str(n))

    return [(len(list(i)),int(k)) for k, i in groupby(n)]

print(*compress_int(112222233356))
print(1 in (1,2))


from itertools import combinations

def prob_of_comb(N,arr,K):
    count = 0
    arr = arr.split()
    for i in combinations(arr,K):
        if 'a' in i:
            count += 1

    return count/len(list(combinations(arr,K)))

print(prob_of_comb(4,'a a b c',2))

#print(max(map(abs, )))
#print(list(map(abs,map(int,'-1 2 3 4 5'.split()))))

from itertools import product

print(list(product(*([1,2,3],[5,5,6],[7,8,9]))))

s = 'kkkk'
print([s[i:j+1] for i in range(len(s)) for j in range(i,len(s))])
