grid = []
file = open('problem11.txt', 'r')
for i in range(0, 20):
    grid.append(file.readline().split())
file.close()

for i in range(0, 20):
    grid[i] = list(map(int, grid[i]))
max_product = 1

for i in range(0, 20):
    for j in range(0, 17):
        product = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if product > max_product:
            max_product = product

for i in range(0, 20):
    for j in range(0, 17):
        product = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
        if product > max_product:
            max_product = product

for i in range(0, 17):
    for j in range(0, 17):
        product = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if product > max_product:
            max_product = product

for i in range(3, 20):
    for j in range(0, 17):
        product = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
        if product > max_product:
            max_product = product

print(max_product)
