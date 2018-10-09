def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    brk = int(n/k)
    parts = [string[i:i+brk] for i in range(0, n, brk)]

    for s in parts:
        s = ''.join(sorted(set(s), key=s.index))
        print(s)

print(merge_the_tools('AABCAAADA',3))
print(list(range(0,9+1,3)))
s = 'AABCAAADA'
print(s[0:3])
