import math
import random
import time

def gcd(a, b):
    # Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    # Pollard's Rho algorithm
    if n % 2 == 0:
        return 2
    # Use f(x) = x^2 + 1 (mod n)
    x = random.randrange(2, n)
    y = x
    c = 1  # constant for the polynomial
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

def is_prime(n):
    # Checks for primality using trial division
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    # Recursively factorizes n using Pollard's Rho and trial division
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollards_rho(n)
    return factorize(factor) + factorize(n // factor)

# The number to factorize:
N = 600851475143

# Start timing the computation
start_time = time.time()

# Compute the factors and sort them
factors = factorize(N)
factors.sort()
print("Factors:", factors)

# End timing and print computation time
end_time = time.time()
print("Time taken: {:.6f} seconds".format(end_time - start_time))
