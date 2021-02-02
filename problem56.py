d = 0
for i in range(1, 101):
    for j in range(1, 101):
        a = i**j
        sum = 0
        for x in str(a):
            sum += int(x)
        if d < sum:
            d = sum
print(d)
