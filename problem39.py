#first method primitive
from math import gcd

number_for_perimeters = []

def triplet_count(perimeter):
    stop = False
    counter = 0
    p_parameter = 1
    q_parameter = 1
    plus_parameter = 1
    while stop == False:
        print(p_parameter)
        print(q_parameter)
        print("\n")
        a = (2*q_parameter*q_parameter+2*q_parameter*p_parameter) * plus_parameter
        if gcd(p_parameter, q_parameter) ==1 and p_parameter % 2 != q_parameter % 2:
            if a == perimeter:
                counter = counter+1
                p_parameter = p_parameter+1
                q_parameter = p_parameter
                plus_parameter = 1
                print(counter)
                print("\n")
            elif q_parameter-p_parameter == 0 and a >= perimeter:
                stop = True
            elif a >= perimeter:
                plus_parameter = 1
                if a >= perimeter:
                    p_parameter = p_parameter+1
                    q_parameter = p_parameter
                else:
                    q_parameter = q_parameter+1
            else:
                plus_parameter = plus_parameter+1
        else:
            if q_parameter-p_parameter == 0 and a >= perimeter:
                stop = True
            elif a >= perimeter:
                plus_parameter = 1
                if a >= perimeter:
                    p_parameter = p_parameter+1
                    q_parameter = p_parameter
                else:
                    q_parameter = q_parameter+1
            else:
                plus_parameter = plus_parameter+1
    return counter

print(triplet_count(15))
