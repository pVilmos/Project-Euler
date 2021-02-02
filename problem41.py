from itertools import permutations
from math import sqrt
from math import floor

def n_pandigitals(n):
    numbers = []
    digits = []
    for x in range(1, n+1):
        digits.append(x)
    perm = permutations(digits)
    for x in perm:
        numbers.append(int(''.join(map(str, x))))
    return numbers

#ezzel sokkal lassabb
'''
primes = []
limit = 10000000
limit_sqr = 3200
for x in range(1, limit):
    primes.append(x)
for i in range(2, limit_sqr):
    for j in range(i*2-1, limit-1, i):
        primes[j] = 0

#nem kell az egészet megnézni
def check_prime(number):
    if primes[number-1]==0:
        return False
    else:
        return True
'''

def check_prime1(number):
    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False
    else:
        return True

max = 0
for i in n_pandigitals(7):
    if str(i)[-1] == 2 or str(i)[-1] == 4 or str(i)[-1] == 6 or str(i)[-1] == 8 or str(i)[-1] == 5:
        continue
    elif check_prime1(i) == True:
        if i > max:
            max = i

print(max)
