from itertools import permutations
#I should do my own permutation function sometime

#function for counting digits
def count_digits(number):
    x = False
    tenpower = 10
    digits = 1
    while x == False:
        if tenpower <= number:
            digits = digits+1
            tenpower = tenpower*10
        else:
            x = True
            return digits

#function for concatenate two numbers
def concatenate(number1, number2):
    return int(str(number1)+str(number2))

#function for deciding whether a number is 1 to 9 pandigital
def being_pandigital(number):
    i = 1
    while i < len(str(number))+1:
        if has_digit(number, i) == True:
            i = i+1
        else:
            return False
    return True

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

#function for making the pandigital product
def pandigit_product(number):
    i = 2
    new_number = number
    while count_digits(concatenate(new_number, number * i)) <= 9:
        new_number = concatenate(new_number, number * i)
        i = i + 1
    if count_digits(new_number) == 9:
        if being_pandigital(new_number) == True:
            return new_number
        else:
            return -1
    else:
        return -1

#function for deciding if it has digit d
def has_digit(number, d):
    for x in str(number):
        if int(x) == d:
            return True
    return False

#function for check if palindrome
def check_if_palindrome(number):
    number = str(number)
    k = 0
    while k < len(number):
        if number[k] != number[-1*k-1]:
            return False
            break
        k += 1
    return True

#adding two numbers, de ez felesleges simán gyorsabb
def add_(number1, number2):
    number1=str(number1)
    number2=str(number2)
    remainder = 0
    new_number = []
    if len(number1)< len(number2):
        longer = number2
        shorter = number1
    else:
        longer = number1
        shorter = number2
    for i in range(1, len(longer)-len(shorter) +1):
        shorter = "0"+shorter
    for i in range(1, len(longer)+1):
        if int(longer[-1*i])+int(shorter[-1*i])+remainder>9:
            new_number.insert(0, str(int(longer[-1*i])+int(shorter[-1*i])+remainder)[-1])
            remainder = 1
        else:
            new_number.insert(0, str(int(longer[-1*i])+int(shorter[-1*i])+remainder))
            remainder = 0
    if remainder == 1:
        new_number.insert(0, 1)
    return int(''.join(map(str, new_number)))

#collatz chain length of number
def collatz_length(number):
    chain = 1
    while number != 1:
        if number % 2 == 0:
            number = number/2
            chain += 1
        else:
            number = number*3 +1
            chain += 1
    return chain

#factorial
def fact(number):
    x = 1
    for i in range(2, number+1):
        x = x*i
    return x

#prime checking function: slow
def check_prime(number):
    primes = []
    limit = 10000000
    limit_sqr = 3200
    for x in range(1, limit):
        primes.append(x)
    for i in range(2, limit_sqr):
        for j in range(i*2-1, limit-1, i):
            primes[j] = 0
    if number in primes:
        return True
    else:
        return False
