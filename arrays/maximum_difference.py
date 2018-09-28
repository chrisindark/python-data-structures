def max_diff(a):
    diff = None
    for i in range(len(a)):
        for j in range(len(a)):
            temp_diff = abs(a[i] - a[j])
            if diff is None:
                diff = temp_diff
            elif temp_diff > diff:
                diff = temp_diff
            pass
    return diff


def max_diff2(a):
    max_num = None
    min_num = None
    for i in range(len(a)):
        if max_num is None:
            max_num = a[i]
        if min_num is None:
            min_num = a[i]
        if a[i] > max_num:
            max_num = a[i]
        if a[i] < min_num:
            min_num = a[i]

    return max_num - min_num


print(max_diff([2, 3, 10, 6, 4, 8, 1]))
print(max_diff([7, 9, 5, 6, 3, 2]))
print(max_diff2([2, 3, 10, 6, 4, 8, 1]))
print(max_diff2([7, 9, 5, 6, 3, 2]))
