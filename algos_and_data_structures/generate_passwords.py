from itertools import permutations
from pprint import pprint as pp
array = list('ABCDEFabcdef123456')
count = 0
stored = {}

for i in range(0,6):
    for j in range(6,12):
        for k in range(12,18):
            for l in range(18):
                password = [array[i],array[j],array[k],array[l]]
                all_passwords = list(permutations(password))
                for p in all_passwords:
                    if p not in stored.keys():
                        stored[p] = True

print(len(stored.keys()))
