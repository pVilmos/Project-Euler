names = []

def alph_pos(string):
    sum = 0
    for i in range(0, len(string)):
        sum = sum + (ord(string[i])-64)
    return sum

file = open("problem22.txt", "r")
file1 = file.read().replace(",", " ")
names = file1.split()
file.close()
names.sort()
for i in range(0, len(names)):
    names[i] = names[i].replace('"', '')
total = 0
for x in names:
    product = alph_pos(x)*(names.index(x)+1)
    total = total + product
print(total)
