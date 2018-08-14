def string_compression(s):
    hasharray = []
    j = 0
    for i in s:
        if len(hasharray) == 0:
            hasharray.append([i, 1])
        elif hasharray[j][0] == i:
            hasharray[j][1] += 1
        else:
            hasharray.append([i, 1])
            j += 1

    # print(hasharray)

    s = ''
    for i in hasharray:
        s += i[0]
        s += str(i[1])
    return s


def string_compression2(s):
    l = len(s)

    if l == 0:
        return ''
    elif l == 1:
        return s + '1'

    r = ''
    i = 1
    count = 1
    while i < l:
        if s[i] == s[i - 1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i += 1

    r = r + s[i - 1] + str(count)
    return r

# print(string_compression('AAAABBBBCCCCCDDEEEE'))
# print(string_compression('AAB'))
# print(string_compression('AAAaaa'))
# print(string_compression('AAAAABBBBCCCC'))
print(string_compression2('AAAABBBBCCCCCDDEEEE'))
print(string_compression('AAB'))
print(string_compression('AAAaaa'))
print(string_compression('AAAAABBBBCCCC'))