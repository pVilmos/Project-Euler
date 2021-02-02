#nem túl gyors iterációval lehetne gyorsítani
import useful_functions as uf
max = 1
max_col_length = 1
for i in range(1, 1000000):
    a = uf.collatz_length(i)
    if a > max_col_length:
        max = i
        max_col_length = a
print(max)
