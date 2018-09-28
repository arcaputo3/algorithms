import random
import math

# SIM_CIRCLE:   Input: Radius r (positive real) and a number of iterations iters (large natural number)
#                      Default: radius 1, iters 100000
#               Output: Simulated area of the circle using Monte Carlo method
def sim_circle(r=1, iters=100000):
    count = 0
    for i in range(iters):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            count += 1
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