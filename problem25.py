import useful_functions as uf

index = 2
ith_fib_1 = 1
ith_fib_2 = 1
while uf.count_digits(ith_fib_2) <1000:
    n = ith_fib_2
    ith_fib_2 = ith_fib_1 + ith_fib_2
    ith_fib_1 = n
    index += 1
print(index)
