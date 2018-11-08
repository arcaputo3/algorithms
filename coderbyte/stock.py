import numpy as np
import matplotlib.pyplot as plt


def Brownian(N):
    dt = 1./N                                    # time step
    b = np.random.normal(0., 1., int(N))*np.sqrt(dt)  # brownian increments
    W = np.cumsum(b)                             # brownian path
    return W, b


# GBM Exact Solution

# Parameters
#
# So:     initial stock price
# mu:     returns (drift coefficient)
# sigma:  volatility (diffusion coefficient)
# W:      brownian motion
# T:      time period
# N:      number of increments

def GBM(So, mu, sigma, W, T, N):
    t = np.linspace(0.,1.,N+1)
    S = []
    S.append(So)
    for i in range(1,int(N+1)):
        drift = (mu - 0.5 * sigma**2) * t[i]
        diffusion = sigma * W[i-1]
        S_temp = So*np.exp(drift + diffusion)
        S.append(S_temp)
    return S, t

N = 100
So = 55.25
mu = 0.15
sigma = 0.4
W = Brownian(N)[0]
T = 1.


soln = GBM(So, mu, sigma, W, T, N)[0]    # Exact solution
t = GBM(So, mu, sigma, W, T, N)[1]       # time increments for  plotting
plt.plot(t, soln)
plt.ylabel('Stock Price, $')
plt.title('Geometric Brownian Motion')
plt.show()


def best_long(arr):
    max_profit = 0
    best_strat = None
    buy = 0
    sell = 0
    change_buy = True
    for i in range(0,len(arr)-1):
        sell = arr[i+1]
        if change_buy:
            buy = arr[i]
        if sell < buy:
            change_buy = True
            continue
        else:
            if sell-buy>max_profit:
                max_profit = sell-buy
                best_strat = (arr.index(buy),arr.index(sell))
            change_buy = False
    return max_profit,best_strat[0],best_strat[1]


def best_short(arr):
    arr = list(map(lambda x: -x, arr))
    best_strat = None
    max_profit = 0
    buy = 0
    sell = 0
    change_buy = True
    for i in range(0,len(arr)-1):
        sell = arr[i+1]
        if change_buy:
            buy = arr[i]
        if sell < buy:
            change_buy = True
            continue
        else:
            if sell-buy>max_profit:
                max_profit = sell-buy
                best_strat = (arr.index(buy),arr.index(sell))
            change_buy = False
    return max_profit,best_strat[0],best_strat[1]


def best_strategy(arr):
    long_profit, long_entry, long_exit = best_long(arr)
    short_profit, short_entry, short_exit = best_short(arr)
    if set(range(long_entry,long_exit)) & set(range(short_entry,short_exit)):
        if long_profit >= short_profit:
            return 'long',long_profit, long_entry, long_exit
        else:
            return 'short',short_profit, short_entry, short_exit
    elif long_entry < short_entry:
        return 'long',long_profit, long_entry, long_exit, 'short',short_profit, short_entry, short_exit
    else:
        return 'short',short_profit, short_entry, short_exit,'long',long_profit, long_entry, long_exit

prices = soln
print(best_long(prices))
print(best_short(prices))
print(best_strategy(prices))
