#truncutables below 100: 23, 37, 53, 73
import math

def check_prime(p):
    i = 2
    while i < p/2:
        if p % i ==0:
            return False
        else:
            i = i+1
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def check_truncatable(p):
    new = p
    while len(str(new)) != 0:
        if check_prime(new) == True:
            new = truncate_left(new)
        else:
            return False

    new = p
    while len(str(new)) != 0:
        if check_prime(new) == True:
            new = truncate_right(new)
        else:
            return False

    return True

results = []
print(check_truncatable(37))
i = 11
