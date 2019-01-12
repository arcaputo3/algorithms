""" Knapsack problem. """
from collections import defaultdict

def get_vw(filename):
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        values, weights = [], []
        for line in file.readlines():
            line = tuple(int(x) for x in line.split(" "))
            values.append(line[0])
            weights.append(line[1])
    size = values.pop(0)
    weights.pop(0)
    return size, values, weights


def knapsack(size, values, weights):
    n = len(values)
    A_prev = defaultdict(int)
    for i in range(n):
        A = defaultdict(int)
        for x in range(size+1):
            if x < weights[i]:
                A[x] = A_prev[x]
            else:
                A[x] = max(A_prev[x], A_prev[x - weights[i]] + values[i])
        A_prev = A
    return A[size]


#W, weights, values = get_vw("knapsack1.txt")
print(knapsack(*get_vw("knapsack1.txt")))
#print(knapsack(*get_vw("knapsack_big.txt")))
