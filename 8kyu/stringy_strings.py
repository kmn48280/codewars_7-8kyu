# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.

# The size will always be positive and will only use whole numbers.
################################################################################################################################
def stringy(size):
    i = 0
    string = '1'
    if size == 0:
        return ''
    while i < size -1:
        if i % 2 == 0:
            string += '0'
            i += 1
        else:
            string += '1'
            i += 1
    return string

print(stringy(6))
################################################################################################################################
def stringy(size):
    s = ""
    for x in range (0, size):
        s+= str("1") if x%2 == 0 else str("0")
    return s