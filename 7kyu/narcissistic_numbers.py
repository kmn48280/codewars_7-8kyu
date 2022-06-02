# A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. 
# If this seems confusing, refer to the example below.

# Ex: 153, where l = 3 ( the number of digits in 153 )
# 13 + 53 + 33 = 153

# Write a function that, given n, returns whether or not n is a Narcissistic Number.
################################################################################################################################
def is_narcissistic(num):
    string = str(num)
    l = len(string)
    num_list = []
    i = 0
    while i < len(string):
        for digit in string:
            new_num = int(digit)**l
            num_list.append(new_num)
            i += 1
    nums = sum(num_list)
    print(num_list)
    print(nums)
    if nums == num:
        return True
    else:
        return False

print(is_narcissistic(153))
############################################################################
def is_narcissistic(n):
    num = str(n)
    length = len(num)
    return sum(int(a) ** length for a in num) == n


