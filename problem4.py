import useful_functions as uf

i = 999
j = 999
palindromes = []
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        if uf.check_if_palindrome(i*j) == True:
            palindromes.append(i*j)
            break
max = 0
for x in palindromes:
    if max < x:
        max = x
print(max)
