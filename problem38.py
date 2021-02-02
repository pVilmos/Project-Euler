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

#function for deciding if it has digit d
def has_digit(number, d):
    for x in str(number):
        if int(x) == d:
            return True
    return False

#function for deciding whether a number is 1 to 9 pandigital
def being_pandigital(number):
    if count_digits(number) != 9:
        return False
    else:
        i = 1
        while i < 10:
            if has_digit(number, i) == True:
                i = i+1
            else:
                return False
        return True

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

#array for pandigit product of n
#it suffices to look for numbers lower than 10000 because below that the second concatanetion would give a number with at least 10 digits
products = []
i = 1
while i < 10000:
    products.append(pandigit_product(i))
    i = i + 1
#get maximum element
max = -1
for x in products:
    if x > max:
        max = x

print(max)
