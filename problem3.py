def largest_pr_factor(number):
    for i in range(2, round(number**0.5+1)):
        if number % i==0:
            return max(i, largest_pr_factor(int(number/i)))
    return number

print(largest_pr_factor(600851475143))
