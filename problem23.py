from math import sqrt, floor

def check_abundant(number):
    sum = 0
    for i in range(2, floor(sqrt(number))+1):
        if number % i == 0:
            if i == sqrt(number):
                sum += sqrt(number)
            else:
                sum += i + number/i
    if sum+1 > number:
        return True
    else:
        return False

abundants = []
numbers = []
for i in range(1, 28123):
    if check_abundant(i) == True:
        abundants.append(i)
        for j in abundants:
            a = i + j
            if a <= 28123:
                numbers.append(a)
numbers = list(dict.fromkeys(numbers))
numbers.sort()
print((28123*28124/2) - sum(numbers))
