def finder(arr1, arr2):
    missing_elem = None
    for i in arr1:
        miss = True
        for j in arr2:
            if i == j:
                miss = False
                break
        if miss:
            missing_elem = i
            return i


def finder1(arr1, arr2):
    hashmap = {}
    arr3 = arr1 + arr2
    for i in arr3:
        if hashmap.get(i, None) is None:
            hashmap[i] = 1
        else:
            hashmap.pop(i)
    return [*hashmap][0]


def finder2(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[i + 1]


# print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
# print(finder1([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
print(finder2([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
