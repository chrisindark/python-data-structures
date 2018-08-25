def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s) - 1] + reverse(s[:len(s) - 1])


print(reverse('hello'))
print(reverse('hello world'))
print(reverse('1234567890'))
