# 0 1 1 2 3 5 8 13 21 ....

numbers = []


def fibonacci(a, b, n):
    if not numbers:
        numbers.append(0)

    if n == 0:
        numbers.append(b)
        return numbers
    else:
        numbers.append(b)
        return fibonacci(b, a+b, n - 1)

print(fibonacci(0, 1, 10))
print(fibonacci(0, 1, 10))
