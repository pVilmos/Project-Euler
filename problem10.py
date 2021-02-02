import useful_functions as uf
primes = []
limit = 2000000
for i in range(1, limit):
    primes.append(i)
for i in range(2, limit):
    for j in range(i*2-1, limit-1, i):
        primes[j] = 0

sum = 0
for x in primes:
    sum = sum + x

print(sum-1)
