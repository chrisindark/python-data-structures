def anagram(s1, s2):
    is_anagram = True

    hmap = {}
    for i in s1:
        i = i.lower()
        if i == ' ':
            continue
        if hmap.get(i, None) is None:
            hmap[i] = 1
        else:
            hmap[i] += 1

    #print('hmap', hmap)

    for i in s2:
        i = i.lower()
        if i == ' ':
            continue
        if hmap.get(i, None) is None:
            is_anagram = False
            break
        elif hmap[i]-1 < 0:
            is_anagram = False
            break
        else:
            hmap[i] -= 1

    #print(hmap)

    for i in hmap.keys():
        if hmap[i] > 0:
            is_anagram = False
            break

    return is_anagram


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


print(anagram('dog', 'god'))
print(anagram('public relations', 'crap built on lies'))
print(anagram('clint eastwood', 'old west action'))

