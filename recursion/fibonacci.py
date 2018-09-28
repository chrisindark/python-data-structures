# 0 1 1 2 3 5 8 13 21 ....
import timeit

numbers = []


# recursive fibonacci to print the sequence
def fibonacci(a, b, n):
    if not numbers:
        numbers.append(0)

    if n == 0:
        numbers.append(b)
        return numbers
    else:
        numbers.append(b)
        return fibonacci(b, a + b, n - 1)


print(fibonacci(0, 1, 10))


# recursive fibonacci to print nth element in sequence
code_snippet1 = """
def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# print(fib_rec(10))
fib_rec(10)
"""
print(timeit.timeit(
    setup='',
    stmt=code_snippet1,
    number=10000
))


# dynamic fibonacci to save results of each recursive function
code_snippet2 = """
cache = {}


def fib_dyn(n):
    # print('notcache', n)
    if cache.get(n):
        # print('here', cache)
        # print('cache', n)
        return cache.get(n)

    if n == 0:
        cache[n] = 0
        return cache[n]
    elif n == 1:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
        return cache[n]


# print(fib_dyn(10))
fib_dyn(10)
"""
print(timeit.timeit(
    setup='',
    stmt=code_snippet2,
    number=10000
))


code_snippet3 = """
def fib_iter(n):
    a = 0
    b = 1
    out = 0
    for i in range(n):
        out = a + b
        a = b
        b = out
    return a


# print(fib_iter(10))
fib_iter(10)
"""
print(timeit.timeit(
    setup='',
    stmt=code_snippet3,
    number=10000
))
