def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s) - 1] + reverse(s[0:len(s) - 1])


def reverse2(s):
    if len(s) == 1:
        return s
    return reverse2(s[1:]) + s[0]
    pass


# print(reverse('hello'))
# print(reverse('hello world'))
# print(reverse('1234567890'))

print(reverse('hello'))
print(reverse('hello world'))
print(reverse('1234567890'))
