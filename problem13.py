import useful_functions as uf

file1 = open('problem13.txt', 'r')
Lines = file1.readlines()
sum = 0
for x in Lines:
    sum = uf.add_(sum, int(x))
print(sum)
