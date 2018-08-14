def test_unique(arr_pairs, first, second):
    dupl = False
    for l in arr_pairs:
        if (l[0] == first and l[1] == second):
            dupl = True
            break
    return dupl


def pair_sum(arr, k):
    arr_pairs = []

    i = 0
    while i <= len(arr) - 2:
        j = i + 1
        while j <= len(arr) - 1:
            if (arr[i] + arr[j]) == k:
                # print(arr[i], arr[j])
                if test_unique(arr_pairs, arr[i], arr[j]) == False:
                    arr_pairs.append((arr[i], arr[j],))
            j += 1
        i += 1
    return arr_pairs

def pair_sum1(arr, k):
    if len(arr) < 2:
        return []

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target in seen:
            output.add((num, target))
            seen.add(num)
        else:
            seen.add(num)

    return output

def pair_sum2(arr, k):
    if len(arr) < 2:
        return []

    seen = {}
    output = []

    for num in arr:
        target = k - num

        if seen.get(target, None):
            if seen.get(num, None):
                seen[num] += 1
            else:
                seen[num] = 0
                seen[num] += 1

            if seen[num] <= 2 and seen[target] <= 2:
                output.append((num, target))

        elif seen.get(num, None):
            seen[num] += 1
        else:
            seen[num] = 0
            seen[num] += 1

    return output


# arr_pairs = pair_sum([1, 3, 2, 2, 2, 2, 2], 4)
# arr_pairs = pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
# arr_pairs = pair_sum([1, 2, 3, 1], 3)

# arr_pairs = pair_sum1([1, 3, 2, 2, 2, 2, 2], 4)
# arr_pairs = pair_sum1([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
# arr_pairs = pair_sum1([1, 2, 3, 1], 3)

# arr_pairs = pair_sum2([1, 3, 2, 2, 2, 2, 2], 4)
arr_pairs = pair_sum2([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
# arr_pairs = pair_sum2([1, 2, 3, 1], 3)

print(arr_pairs)
print(len(arr_pairs))
