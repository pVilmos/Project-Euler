from itertools import count
counter = 0

for i in range(1, 1000):
    for base in count(1, 1):
        if len(str(base**i)) == i:
            counter += 1
        elif len(str(base**i)) < i:
            continue
        else:
            break
print(counter)

print(3**1000)
print(len(str(3**10000)))
