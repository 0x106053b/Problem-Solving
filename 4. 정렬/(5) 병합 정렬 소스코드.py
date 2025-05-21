import random

def merge(arr1, arr2):
    res = []
    index1 = index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            res.append(arr1[index1])
            index1 += 1
        else:
            res.append(arr2[index2])
            index2 += 1
    if index1 == len(arr1):
        res += arr2[index2:]
    else:
        res += arr1[index1:]
    return res

def merge_sort(arr):
    if len(arr) == 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = [random.randrange(100) for _ in range(20)]
print(merge_sort(arr))
