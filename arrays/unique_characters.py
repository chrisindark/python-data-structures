def uni_char(s):
    hashmap = {}
    for i in s:
        if hashmap.get(i, None):
            return False
        else:
            hashmap[i] = i
    return True

def uni_char2(s):
    return len(set(s)) == len(s)


# print(uni_char('abcde'))
# print(uni_char('aabcde'))
print(uni_char2('abcde'))
print(uni_char2('aabcde'))
