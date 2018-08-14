import time

def large_cont_sum(arr):
    output_dict = {}
    largest_sum = 0
    output_dict['start'] = 0
    for i in range(len(arr)):
        temp_largest_sum = 0
        for j in range(i, len(arr)):
            temp_largest_sum += arr[j]
            # print(i, j, largest_sum, temp_largest_sum)
            if temp_largest_sum > largest_sum:
                largest_sum = temp_largest_sum
                # print(i, j, largest_sum, temp_largest_sum)
                output_dict['start'] = i
                output_dict['end'] = j
                output_dict['sum'] = largest_sum

    return output_dict

def large_cont_sum2(arr):
    largest_sum = 0
    temp_largest_sum = 0

    i = 0
    j = 0
    while i < len(arr):
        if arr[i] > 0:
            temp_largest_sum += arr[i]
            if temp_largest_sum > largest_sum:
                largest_sum = temp_largest_sum
            # print(largest_sum)
        else:
            temp_largest_sum += arr[i]
            if temp_largest_sum > largest_sum:
                largest_sum = temp_largest_sum
            # print(largest_sum)
        i += 1
        if i == len(arr) -1:
            j += 1
            i = j
            temp_largest_sum = 0
        if j == len(arr):
            break
    return largest_sum

def large_cont_sum3(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for i in arr[1:]:
        current_sum = max(current_sum + i, i)
        max_sum = max(current_sum, max_sum)

    return max_sum

# print(large_cont_sum([1,2,-1,3,4,-1]))
# print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
# print(large_cont_sum([-1,1]))

# print(large_cont_sum2([1,2,-1,3,4,-1]))
# print(large_cont_sum2([1,2,-1,3,4,10,10,-10,-1]))
# print(large_cont_sum2([-1,1]))

# print(large_cont_sum3([1,2,-1,3,4,-1]))
print(large_cont_sum3([1,2,-1,3,4,10,10,-10,-1]))
# print(large_cont_sum3([-1,1]))
