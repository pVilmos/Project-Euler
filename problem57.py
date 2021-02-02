limit = 1000

numerator = []
denominator = []

numerator.append(3)
denominator.append(2)
sum = 0

for i in range(1, limit):
    numerator.append(numerator[i-1]+2*denominator[i-1])
    denominator.append(numerator[i-1]+denominator[i-1])
    if len(str(numerator[-1])) > len(str(denominator[-1])):
        sum += 1

print(sum)
