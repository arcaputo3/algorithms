import numpy as np
import matplotlib.pyplot as plt

# Create Brownian Motion
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
    # Define profit as 0 if no position taken
    max_profit = 0
    # Init strategy, buy and sell prices
    best_strat = None
    buy = 0
    sell = 0
    # change_buy = True if we are looking to enter
    change_buy = True
    # Iterate until second to last item
    for i in range(len(arr)-1):
        # Get next item
        sell = arr[i+1]
        if change_buy:
            # Buy if we are looking for entry
            buy = arr[i]
        # If sell is lower than buy,
        # we will want to instead buy at the sell entry
        if sell < buy:
            # Look for new entry
            change_buy = True
            continue
        else:
            # If this is best option so far,
            # set max_profit accordingly
            if sell - buy > max_profit:
                max_profit = sell - buy
                # Get current strategy, i.e. buy and sell indeces
                best_strat = (arr.index(buy), arr.index(sell))
            # No longer looking for new entry, just better sell
            change_buy = False
    return max_profit, best_strat[0], best_strat[1]


def best_short(arr):
    # Note that this is exactly the same as best_long,
    # just set prices negative.
    # This is identical to finding a good short.
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

# A best strategy will incorporate either a short or long position (or both)
# over a given time period.
def best_strategy(arr):
    # Get each parameter for each possible entry
    long_profit, long_entry, long_exit = best_long(arr)
    short_profit, short_entry, short_exit = best_short(arr)
    # If the strategies overlap, we will only choose the best one
    if set(range(long_entry,long_exit)) & set(range(short_entry,short_exit)):
        if long_profit >= short_profit:
            return 'long',long_profit, long_entry, long_exit
        else:
            return 'short',short_profit, short_entry, short_exit
    # Otherwise, we will both long and short according to chronological order.
    elif long_entry < short_entry:
        return 'long',long_profit, long_entry, long_exit, 'short',short_profit, short_entry, short_exit
    else:
        return 'short',short_profit, short_entry, short_exit,'long',long_profit, long_entry, long_exit


if __name__ == "__main__":
    prices = soln
    print(best_long(prices))
    print(best_short(prices))
    print(best_strategy(prices))
