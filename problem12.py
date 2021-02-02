from itertools import count
from math import sqrt, floor

for i in count(1, 1):
    triangle_num = i*(i+1)/2
    div = 0
    for j in range(1, floor(sqrt(triangle_num)+1)):
        if j == sqrt(triangle_num):
            div += 1
        elif triangle_num % j == 0:
            div += 2
    if div > 500:
        print(triangle_num)
        break
