# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

#order list from small --> larges
#remove last two integers
#sum the values

a_list = [10, 14, 2, 23, 19]
a_list.sort()
large_nums = a_list[-2:]
print(sum(large_nums))






    
    



