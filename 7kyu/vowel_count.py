def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter == 'a':
            count += 1
        elif letter == 'e':
            count += 1
        elif letter == 'i':
            count += 1
        elif letter == 'o':
            count += 1
        elif letter == 'u':
            count += 1
        else:
            continue
    if count == 0:
        return 0
    return count

print(get_count("abracadabra"))