# Write a function that returns a string in which firstname is swapped with last name.

# name_shuffler('john McClane'); => "McClane john"
################################################################################################################################
def name_shuffler(name):
    shuffle = name.split(" ")
    new_name = ''
    new_name += shuffle[-1]
    new_name += ' ' + shuffle[0]
    return new_name 


print(name_shuffler("john McClane"))