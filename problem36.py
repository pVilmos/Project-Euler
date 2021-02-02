from math import floor

def check_pal(number):
    for i in range(0, floor(len(number)/2)):
        if number[i] == number[-1*i - 1]:
            continue
        else:
            return False
    return True

sum = 0
for i in range(1, 1000000):
    if check_pal(str(i)) == True:
        if check_pal(bin(i)[2:]) == True:
            sum += i
print(sum)
