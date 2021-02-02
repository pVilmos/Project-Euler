import numpy as np

modulo = 1000000007
seq_length = 100000000
initial_seq = []

def add_and_modulo(a, b):
    return (a+b)%modulo

zeroes = []
coefficients = []
for i in range(0, seq_length):
    zeroes.append(1)

'''
for i in range(0, seq_length):
    new = zeroes.copy()   # Ha ide nem rakom a copy()-t akkor nem működik????
    new[i] = 1
    new_length = seq_length
    for i in range(0, new_length-1):
        new.pop(0)
        new_length = new_length-1
        for j in range(1, new_length):
            new[j] = add_and_modulo(new[j], new[j-1])
    coefficients.append(new[0])
print(coefficients)

# Making the Lucas sequence
initial_seq.append(1)
initial_seq.append(3)
for i in range(2, seq_length):
    initial_seq.append(initial_seq[i-1]+initial_seq[i-2])

final_list = []
for i in range(0, seq_length):
    final_list.append((coefficients[i]* initial_seq[i])%modulo)

for i in range(0, seq_length-1):
    initial_seq.pop(0)
    seq_length = seq_length-1
    for j in range(1, seq_length):
        initial_seq[j] = add_and_modulo(initial_seq[j], initial_seq[j-1])

print(initial_seq)
print(sum(final_list)%modulo)
'''
for i in range(0, seq_length-1):
    zeroes.pop(0)
    seq_length = seq_length-1
    for j in range(1, seq_length):
        zeroes[j] = add_and_modulo(zeroes[j], zeroes[j-1])
