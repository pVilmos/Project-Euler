#upper bound: 1000000
fpowerdig = -1 #1 is not included
for x in range(1, 1000000):
    sum = 0
    for y in str(x):
        sum += int(y)**5
    if sum == x:
        fpowerdig = fpowerdig+x

print(fpowerdig)
