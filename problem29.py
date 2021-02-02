powers = []
for i in range(2, 101):
    power = i
    for j in range(2, 101):
        if power*i not in powers:
            powers.append(power*i)
        i = power*i
print(len(powers))
