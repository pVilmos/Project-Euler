from itertools import permutations
i = 0

def divisible_by(number1, number2):
    numbers = []
    for x in range(1, 1000000000):
        numbers.append(x)
    numbers[number2-1] = 0
    j = 1
    while number2-1+j*number2 <1000000000:
        numbers[number2-1+j*number2] = 0
        j += 1
    if number1 in numbers:
        return True
    else:
        return False

#return n-digit pandigital numbers
def n_pandigitals(n):
    numbers = []
    digits = []
    for x in range(0, n+1):
        digits.append(x)
    perm = permutations(digits)
    for x in perm:
        numbers.append(int(''.join(map(str, x))))
    return numbers


for x in n_pandigitals(9):
    if x > 1000000000:
        product2 = int(str(x)[1]+str(x)[2]+str(x)[3])
        product3 = int(str(x)[2]+str(x)[3]+str(x)[4])
        product4 = int(str(x)[3]+str(x)[4]+str(x)[5])
        product5 = int(str(x)[4]+str(x)[5]+str(x)[6])
        product6 = int(str(x)[5]+str(x)[6]+str(x)[7])
        product7 = int(str(x)[6]+str(x)[7]+str(x)[8])
        product8 = int(str(x)[7]+str(x)[8]+str(x)[9])
        if product2 % 2 == 0 and product3 % 3 == 0 and product4 % 5 == 0 and product5 % 7 == 0 and product6 % 11 == 0 and product7 % 13 == 0 and product8 % 17 == 0:
            i = i+x
    else:
        pass
print(i)
