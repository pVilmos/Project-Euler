sum = 0
for x in range(1, 1001):
    sum = sum + x**x

print(sum%10000000000)
