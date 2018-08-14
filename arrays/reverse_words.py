def rev_word(s):
    i = 0
    word_arr = []
    word = ''
    while i < len(s):
        if s[i] != ' ':
            word += s[i]
        else:
            if word != '':
                word_arr.append(word)
                word = ''

        if i == (len(s) - 1):
            if word != '':
                word_arr.append(word)
        # print(word_arr)
        i += 1

    i = len(word_arr) - 1
    word = ''
    while i >= 0:
        # print(word_arr[i])
        word += word_arr[i]
        if i != 0:
            word += ' '
        i -= 1

    return word


def strip_words(s):
    i = 0
    word_arr = []
    word = ''
    while i < len(s):
        if s[i] != ' ':
            word += s[i]
        else:
            if word != '':
                word_arr.append(word)
                word = ''

        if i == (len(s) - 1):
            if word != '':
                word_arr.append(word)
        i += 1
    # print(word_arr)
    return word_arr


def reverse_word(word_arr):
    # print(word_arr)
    l = len(word_arr)
    i = 0
    while i < l / 2:
        temp = word_arr[i]
        word_arr[i] = word_arr[l - i - 1]
        word_arr[l - i - 1] = temp
        i += 1

    return ' '.join(word_arr)


def rev_word2(s):
    word_arr = strip_words(s)
    return reverse_word(word_arr)


# print(rev_word('Hi John,     are you ready to go?'))
# print(rev_word('     space before'))
# print(rev_word('space after      '))
# print(rev_word('    Hello John    how are you     '))
# print(rev_word('1'))
print(rev_word2('Hi John,     are you ready to go?'))
print(rev_word2('    Hello John    how are you     '))