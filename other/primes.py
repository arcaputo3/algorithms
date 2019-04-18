def PrimeMover(num):
    primes = [2]
    cur = primes[-1]
    while len(primes) < num:
        cur += 1
        if all(cur % p for p in primes):
            primes.append(cur)
    return cur

print(PrimeMover(5000))
