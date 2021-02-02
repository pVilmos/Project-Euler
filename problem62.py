from itertools import permutations

cubes = []
limit = 100000

for x in range(1, limit):
    cubes.append(x*x*x)
cubes = list(map(str, cubes))

i = 0
while i < limit-1:
    cubes[i] = ''.join(sorted(cubes[i]))
    i += 1
cubes = sorted(cubes)


d = 1
while d < 4:
    start = cubes[0]
    cubes.pop(0)
    if start == cubes[0]:
        d += 1
    else:
        d = 0

print(start)

cubes1 = []
for x in range(1, limit):
    cubes1.append(x*x*x)
cubes1 = list(map(str, cubes1))

i = 0
while i < limit-1:
    cubes1[i] = ''.join(sorted(cubes1[i]))
    i += 1

bool = False
i = 0
while bool == False:
    if cubes1[i] == start:
        bool = True
        print((i+1)**3)
    else:
        i += 1
