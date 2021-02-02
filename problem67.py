pyramid = []
file = open("problem67.txt", "r")
for i in range(0, 100):
    pyramid.append(file.readline().split())
    pyramid[i] = list(map(int, pyramid[i]))
file.close()
for i in range(1, 100):
    pyramid[i][0] = pyramid[i-1][0] + pyramid[i][0]
    pyramid[i][-1] = pyramid[i-1][-1] + pyramid[i][-1]
    for j in range(1, len(pyramid[i])-1):
        pyramid[i][j] = max(pyramid[i][j]+pyramid[i-1][j-1], pyramid[i][j]+pyramid[i-1][j])

print(max(pyramid[99]))
