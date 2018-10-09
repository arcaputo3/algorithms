def minimumBribes(q):
    count = 0
    for i in range(len(q)-1):
        if q[i] > i+3:
            break
        elif q[i] > q[i+1]:
            count += 1
            q[i],q[i+1] = q[i+1],q[i]
    if q == list(range(1,len(q)+1)):
        print(count)
    else:
        print("Too chaotic")
    print(q)
from collections import Counter

minimumBribes([2,1,5,3,4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
print(list(range(len([1,2,3,4])-1,-1,-1)))
print(Counter([2,1,5,3,4]))
