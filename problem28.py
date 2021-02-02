grid = []
a = 1001*1001+1
for i in range(1, a):
    grid.append(i)

sum = 0
current_position = 0
step = 2
i = 2
counter = 0

while i < a:
    sum = grid[i] + sum
    if counter == 3:
        step += 2
        counter = 0
    else:
        counter += 1
    i += step
print(sum + 1)
