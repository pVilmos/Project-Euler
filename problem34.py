import useful_functions as uf
#is it enough to set 1000000 as limit?
fact_sum = -3 # 1, 2 not included
for x in range(1, 1000000):
    sum = 0
    for y in str(x):
        sum += uf.fact(int(y))
    if sum == x:
        fact_sum = fact_sum+x

print(fact_sum)
