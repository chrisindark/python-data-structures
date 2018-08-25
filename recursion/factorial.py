# n = 10
# factorial = 10 * 9 * 8 * .... * 1


def factorial(n):
    """
    returns factorial of n (n!)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(15))
