# Simulate problems for 30 sided die as seen by Jane Street interview questions
import numpy as np

# Get most likely outcome by returning most frequent occurences
def sum_to_300(iters = 10000):

    results = []
    for i in range(iters):
        sum = 0
        while sum < 300:
            die = np.random.randint(1,high=30)
            sum += die
        results.append(sum)
    return max(set(results), key=results.count)

print(sum_to_300())


f = lambda x: x/4 + 7

for x in range(100):
    if f(f(f(x)))
