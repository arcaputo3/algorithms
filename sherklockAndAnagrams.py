import math
from collections import Counter

# Quite slow version
def sherlockAndAnagrams(s):
    count = 0
    subsets = [s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]
    similar = {}

    while len(subsets) > 1:
        p = subsets.pop()
        similar[p] = 1
        for string in subsets:
            if Counter(p) == Counter(string):
                subsets.remove(string)
                similar[p] += 1
    f = math.factorial
    for val in similar.values():
        if val > 1:
            count += int(f(val) / f(2) / f(val-2))

    return count

# Faster version
def sherlockAndAnagrams_(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count


print(sherlockAndAnagrams_('ifailuhkqqasdfkljhwiertionbeqtbkjklsbndvkjhaoshdwierhkjet'))
#print(sherlockAndAnagrams('ifailuhkqqasdfkljhwiertionbeqtbkjklsbndvkjhaoshdwierhkjet'))
