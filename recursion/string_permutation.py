# ab => ab, ba
# ac => ac, ca
# bc => bc, cb
# abc => abc, acb, bac, bca, cab, cba
# dog => dog, dgo, odg, ogd, gdo, god


def permute(s):
    # current permutation list
    out = []

    # base case
    if len(s) == 0:
        return []

    if len(s) == 1:
        return [s]

    for i in range(len(s)):
        s_start = s[i]
        s_remaining = s[:i] + s[i+1:]
        # print('first loop', s_start, s_remaining)
        for perm in permute(s_remaining):
            # print('second loop', s_start, s_remaining)
            # print(j)
            out += [s_start + perm]
    return out
    # print(s[0] + permute(s[1:]))
    # return s[0] + permute(s[1:])


print(permute('abc'))
print(permute('dog'))
print(permute('abcd'))
