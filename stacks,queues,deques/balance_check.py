def balance_check(s):
    l = []

    for i in s:
        if i == '(' or i == '{' or i == '[':
            l.append(i)
        elif i == ')' and l.pop() == '(':
            continue
        elif i == '}' and l.pop() == '{':
            continue
        elif i == ']' and l.pop() == '[':
            continue
        else:
            return False
        # print(l)

    # print(l)
    return l == []

print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))

print(balance_check('[](){([[[]]])}('))
print(balance_check('[{{{(())}}}]((()))'))
print(balance_check('[[[]])]'))


import unittest


class TestBalanceCheck(unittest.TestCase):
    def test(self, balance_check):
        self.assertEqual(balance_check('[](){([[[]]])}('), False)
        self.assertEqual(balance_check('[{{{(())}}}]((()))'), True)
        self.assertEqual(balance_check('[[[]])]'), False)
        print('All test cases passed')

t = TestBalanceCheck()
t.test(balance_check)
