from math import sqrt, floor

def sum_of_divisors(number):
    sum = 1
    for i in range(2, floor(sqrt(number)+1)):
        if number%i == 0:
            if i == sqrt(number):
                sum = sum + i
            else:
                sum = sum + i + number/i
    return sum

sum = 0

for x in range(4, 10001):
    if x == sum_of_divisors(sum_of_divisors(x)) and x != sum_of_divisors(x):
        print(x)
        print(sum_of_divisors(x))
        print("\n")
        sum = sum+x
print(sum)
