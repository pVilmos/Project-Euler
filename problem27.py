max_pair = [0, 0]
max_primes = 0
#create list of primes
primes = []
limit = 10000
for i in range(1, limit):
    primes.append(i)
for i in range(2, limit):
    for j in range(i*2-1, limit-1, i):
        primes[j] = 0

for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        n = 0
        while check_prime(n*n + i*n + j) == True:
            n += 1
        if n > max_primes:
            max_pair = [i, j]
            max_primes = n
print(max_pair[0]*max_pair[1])
