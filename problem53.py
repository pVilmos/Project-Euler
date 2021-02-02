from math import factorial
sum = 0
for x in range(0, 101):
    for y in range(0, x+1):
        comb = factorial(x)/(factorial(y)*factorial(x-y))
        if comb > 1000000:
            sum += 1

print(sum)
