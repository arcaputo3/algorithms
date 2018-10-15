# Import relevant packages (no numpy, math package only for testing)
import random
import math
import numpy as np
import matplotlib.pyplot as plt
# SIM_CIRCLE:   Input: Radius r (positive real) and a number of iterations iters (large natural number)
#                      Default: radius 1, iters 100000
#               Output: Simulated area of the circle using Monte Carlo method
def sim_circle(r=1, iters=100000):
    count = 0
    for i in range(iters):
        x = random.random()
        y = random.random()
        # This simulates a point in the quarter circle region of the first quadrant
        if x**2 + y**2 <= 1:
            count += 1
    # Return number of counts that landed in circle divided by total iterations
    # Visually, this is the area of the circle incribed in an r x r square
    return 4*r**2*count/iters

# Testing
print(sim_circle(r=4))
print(math.pi*4**2)

# ALL_PRIMES_BEFORE_N:  Input: N (natural number)
#                       Output: Each prime number preceding N printed in order
def all_primes_before_N(N):
    for p in range(2,N+1):
        for i in range(2,p):
            if p%i == 0:
                break
        else:
            print(p)
            print(is_prime(p)) # Test function

# IS_PRIME:     Input: num (positive integer)
#               Output: string explaining whether or not num is is_prime
#                       and if not, a string containing two factors whose product is num
# SOURCE: https://www.programiz.com/python-programming/examples/prime-number
def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       # only need to check up to sqrt(num)
       for i in range(2, int(math.sqrt(num))+1):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")

# Testing
print(all_primes_before_N(100))
print(is_prime(497))

# COIN_TOSS_GAME:   Computes the value of a game where our values increase (depending on ) evertime we flip heads and the game stops when we flip tails
#          Input:   Function of growth, iters (int)
#          Output:  Simulated result averaged over number of iters

def coin_toss_game(f = lambda x: x + 1, init = False, iters = 10000):
    total_winnings = 0
    for _ in range(iters):
        winnings = 0
        # Set initial toss for multiplicative functions
        if init:
            coin = random.random()
            if coin <= 0.5:
                winnings = 1
                coin = random.random()
                while coin <= 0.5:
                    winnings = f(winnings)
                    coin = random.random()
        else:
            coin = random.random()
            while coin <= 0.5:
                winnings = f(winnings)
                coin = random.random()

        total_winnings += winnings

    return total_winnings/iters

print(coin_toss_game())
for i in range(2,10):
    print(coin_toss_game(f = lambda x: x + i))
    # We see that E_{X_t}[f(x)=x+i] = i

x = []
for i in range(1000):
    x.append(coin_toss_game(f = lambda x: 2*x, init=True))
    # Although E_{X_t}[f(x)=2*x] = 1/2 + 1/2 + ... = infinity,
    # our game always terminates here, since the probability of a sequence of infinite heads vanishes as n -> inf.
    # Plotting, we get very high variance.

plt.plot(np.array(x))
plt.show()
