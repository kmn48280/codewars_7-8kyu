# Simple, remove the spaces from the string, then return the resultant string.

def no_space(str):
    result = ''
    no_space = str.split(' ')
    for phrase in no_space:
        result += phrase
    return result

print(no_space("Meow mix 3 5 6"))
#################################################################
def no_space(x):
    return x.replace(' ' ,'')