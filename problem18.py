pyramid = []
file = open("problem18.txt", "r")
for i in range(0, 15):
    pyramid.append(file.readline().split())
    pyramid[i] = list(map(int, pyramid[i]))
file.close()
for i in range(1, 15):
    pyramid[i][0] = pyramid[i-1][0] + pyramid[i][0]
    pyramid[i][-1] = pyramid[i-1][-1] + pyramid[i][-1]
    for j in range(1, len(pyramid[i])-1):
        pyramid[i][j] = max(pyramid[i][j]+pyramid[i-1][j-1], pyramid[i][j]+pyramid[i-1][j])

print(max(pyramid[14]))
