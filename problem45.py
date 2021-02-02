tri = []
pent = []
hex = []
limit = 100000
for i in range(1, limit):
    tri.append(int(i*(i+1)/2))
for i in range(1, limit):
    pent.append(int(i*(3*i-1)/2))
for i in range(1, limit):
    hex.append(i*(2*i-1))
d = 1
for x in tri:
    if x in pent:
        if x in hex:
            d += 1
            if d == 4:
                print(x)
                break
