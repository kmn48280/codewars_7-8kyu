# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# Examples
# 'a' and 'g' returns 1

# 'A' and 'C' returns 1

# 'b' and 'G' returns 0

# 'B' and 'g' returns 0

# '0' and '?' returns -1
########################################################################
# def same_case(a,b):
#     alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     alpha2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     for char in alpha:
#         if char != a or char !=b:
#             return -1
#         elif char == a & char 
#########################################################################
def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    return 1 if a.islower() and b.islower() or a.isupper() and b.isupper() else 0
print(same_case('?','Z'))
    