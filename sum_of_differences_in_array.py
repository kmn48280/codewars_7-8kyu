# Your task is to sum the differences between consecutive pairs in the array in descending order.

# Example
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]

# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell ).

########################################################################################################
def sum_of_differences(arr):
    arr.sort(reverse=True)
    i = 0
    sum = 0
    if len(arr) == 0:
        return 0
    else:
        while i != len(arr) - 1:
            sum = sum + (arr[i] - arr[i + 1])
            i += 1
    return sum


print(sum_of_differences([2,1, 10]))
        
