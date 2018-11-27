from itertools import permutations

def palindrome_swapper(s):
    for word in [''.join(p) for p in permutations(s)]:
        if word == word[::-1]:
            return word
    return -1

print(palindrome_swapper("ortator"))
