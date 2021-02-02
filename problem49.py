from itertools import permutations, combinations
from math import sqrt, floor

def check_prime(number):
    primes = []
    limit = 10000
    limit_sqr = floor(sqrt(10000)+1)
    for x in range(1, limit):
        primes.append(x)
    for i in range(2, limit_sqr):
        for j in range(i*2-1, limit-1, i):
            primes[j] = 0
    if number in primes:
        return True
    else:
        return False

list_of_primes = []
list_of_seq = []

for x in range(1000, 10000):
    if check_prime(x)==True:
        list_of_primes.append(x)

i = 0
comb = combinations(list_of_primes, 3)
while i < len(comb):
    if comb[i][2]-comb[i][1] == comb[i][1]-comb[i][0]:
        list_of_seq.append(comb[i])
    i = i+1

for x in list_of_seq:
    print(x)
