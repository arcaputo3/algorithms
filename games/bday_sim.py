import numpy as np
import matplotlib.pyplot as plt

# Initialize counter
def sim_run():
    runs = []
    for r in range(1, 101):
        count = 0
        iters = 5000
        for _ in range(iters):
            room = np.random.randint(1, 366, r)
            if len(room) - np.unique(room).size != 0:
                count += 1
        runs.append(count/iters)
    return runs

plt.plot(sim_run())
plt.title('Simulated Probability of >= 1 Shared Birthday')
plt.xlabel('Number of People in Room')
plt.ylabel('SImulated Probability')
plt.show()
