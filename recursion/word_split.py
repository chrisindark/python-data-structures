def substring_start(phrase, word):
    i = 0
    # print('pw', phrase, word)
    while i < len(word):
        if len(phrase) == 0:
            return False

        if word[i] != phrase[i]:
            return False
        else:
            i += 1
            continue

    return True


def word_split(phrase, list_of_words, output=None):
    # print('p', phrase)
    if output is None:
        output = []

    for word in list_of_words:
        # print('w', word)
        if substring_start(phrase, word):
            # break
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)

    return output


# print(word_split('themanran', ['the', 'man', 'ran']))
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
# print(word_split('themanran', ['clown', 'ran', 'man']))
