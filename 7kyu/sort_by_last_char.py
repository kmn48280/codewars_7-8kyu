# Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

# If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

# All inputs will be valid.
################################################################################################
def last(x):
    listx = x.split(' ')
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sortedlastletter = []
    for g in alphabet:
        for q in listx:
            if q[-1] == g:
                sortedlastletter.append(q)
    return sortedlastletter


print(last("man i need a taxi up to ubud"))