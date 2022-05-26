# Get the next prime number!

# You will get a numbern (>= 0) and your task is to find the next prime number.

# Make sure to optimize your code: there will numbers tested up to about 10^12.

# Examples
# 5   =>  7
# 12  =>  13


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if num % 1 == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


num = 99
for i in range(2, int(num**0.5)+1):
    if num % 1 == 0:
        print(i)



