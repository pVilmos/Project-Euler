# This is the lazy way and it is faster
print((28433*2**7830457+1)%10000000000)

# more subtle way, and it is slower ? weird
remainder = 2
for i in range(1, 7830457):
    remainder = (remainder*2)%10000000000
print((28433*remainder+1)%10000000000)
