# See https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem for problem statement

def jumpingOnClouds(c):
    jumps = 0
    while len(c) > 3:
        if c[2] == 0:
            jumps += 1
            c = c[2:]
        else:
            jumps += 1
            c = c[1:]
    jumps += 1
    return jumps

print(jumpingOnClouds([0,1,0]))
p = [1,2,3,4,5]
p.remove(1)
print(p[0:1])

def ordered_subsets(s):
    length = len(s)
    return [s[i:j+1] for i in range(length) for j in range(i,length)]

print(ordered_subsets('abba'))
s = 'abbq'
print(s[::-1])
