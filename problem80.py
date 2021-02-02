import math

a = str(round(math.sqrt(2), 100))
t = 0
for x in a:
    if x != '.':
        t = t + int(x)

print(t)
