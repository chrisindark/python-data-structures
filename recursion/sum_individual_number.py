def sum_ind(n):
    dig = int(n % 10)
    if n == 0:
        return 0

    return dig + sum_ind(n // 10)


print(sum_ind(54321))
print(sum_ind(1))
print(sum_ind(0))
