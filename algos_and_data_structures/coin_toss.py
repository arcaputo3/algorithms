import numpy as np

def coin_toss_double_half(n, C = 100):
    for _ in range(n):
        coin = np.random.random()
        if coin <=0.5:
            C *= 2
        else:
            C *= 0.5
    return C
m = 100000
print(sum(coin_toss_double_half(10) for i in range(m))/m)
print(100*(5/4)**10)
