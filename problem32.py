import useful_functions as uf

multiplicand = 2
multiplier = 1
sums = []
x = True
while x ==True:
    x = False
    while uf.count_digits(uf.concatenate(uf.concatenate(multiplier, multiplicand), multiplicand*multiplier)) <= 9:
        if uf.being_pandigital(uf.concatenate(uf.concatenate(multiplier, multiplicand), multiplicand*multiplier)) == True:
            sums.append(multiplicand* multiplier)
            multiplicand += 1
        else:
            multiplicand += 1
        x = True #it should only be executed once
    if multiplicand-multiplier==1:
        x = False
    else:
        multiplier+=1
        multiplicand =multiplier+1
        x = True
i = 0
sums1 = []
for x in sums:
    z = False
    for y in sums1:
        if y == x:
            z = True
            break
    if z == False:
        sums1.append(x)
sum = 0
for x in sums1:
     sum += x
print(sum)
