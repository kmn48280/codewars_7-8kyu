# You will be given two inputs: a string of words and a letter. For each string, return the alphabetic character after every instance of letter(case insensitive).

# If there is a number, punctuation or underscore following the letter, it should not be returned.

# If letter = 'r':
# comes_after("are you really learning Ruby?") # => "eenu"
# comes_after("Katy Perry is on the radio!")   # => "rya"
# comes_after("Pirates say arrrrrrrrr.")       # => "arrrrrrrr"
# comes_after("r8 your friend")                # => "i"
# Return an empty string if there are no instances of letter in the given string.

# def what_comes_after(l,string):
#     a_list = []
#     string.split(" ")
#     for l in string.lower():
#         if l == l:
#             a_list.append(a_list[l]+1)
#     return a_list

# print(what_comes_after('r',"are you really learning Ruby?"))
# import string
# print(list(string.ascii_lowercase))

# def what_comes_after(l,string):
#     new_string =string.lower()
#     a_list = []
#     while True:
#         for i in range(len(new_string)):
#             if i == new_string.index('r'):
#                 after_char = new_string.index('r') + 1
#                 a_list.append(new_string[after_char])
#                 i += 1
#             elif i != new_string.index('r'):
#                 continue
#         return a_list        

# print(what_comes_after('r',"are you really learning Ruby?"))
# string = "are you really learning Ruby?"
# n = string.lower()
# sub_n = 'r'
# index_r= n.count(sub_n)

# for l in n:
#     if l == 'r':
#         l_1 = n.index('r') + 1
#         print(n[l_1])

import re
def comes_after(stg, c): 
    return "".join(re.findall(fr"(?i)(?<={c})([a-z])", stg))