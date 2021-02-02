import useful_functions as uf

constant = 1
constant = str(constant)
i = 2
while len(constant) < 1000000:
    constant = constant + str(i)
    i+=1
    
print(int(constant[0])*int(constant[9])*int(constant[99])*int(constant[999])*int(constant[9999])*int(constant[99999])*int(constant[999999]))
