# Write a method, that will get an integer array as parameter and will process every number from this array.

# Return a new array with processing every number of the input-array like this:

# If the number has an integer square root, take this, otherwise square the number.

# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# Notes
# The input array will always contain only positive numbers, and will never be empty or null.
################################################################################################################################
import math

def square_or_square_root(arr):
    new_arr = []
    for num in arr:
        if math.sqrt(num) % 1 == 0:
            new_arr.append((math.sqrt(num)))
        else:
            new_arr.append((num**2))
    return new_arr

print(square_or_square_root([4,3,9,7,2,1]))

########################################################################
def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result
###################################################################################
from math import sqrt

def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]