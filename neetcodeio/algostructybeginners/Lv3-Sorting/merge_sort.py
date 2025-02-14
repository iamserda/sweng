import math


def merge_sorted_arrays(arr1, arr2):
    if not arr1 and not arr2:
        return []
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    arr3 = []
    index1 = 0
    index2 = 0
    while index1 < len(arr1) or index2 < len(arr2):
        if index1 >= len(arr1):
            arr3.append(arr2[index2])
            index2 += 1
            continue
        if index2 >= len(arr2):
            arr3.append(arr1[index1])
            index1 += 1
            continue
        if arr1[index1] <= arr2[index2]:
            arr3.append(arr1[index1])
            index1 += 1
            continue
        if arr1[index1] >= arr2[index2]:
            arr3.append(arr2[index2])
            index2 += 1
            continue

    return arr3


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        half = int(math.ceil(len(arr) / 2))
        arr1 = merge_sort(arr[:half])
        arr2 = merge_sort(arr[half:])
        arr3 = merge_sorted_arrays(arr1, arr2)
        return arr3


arr1 = [11, 3, 5, 7, 0, 2, 4, -5, 7, 8]
arr2 = sorted(arr1)
arr3 = merge_sort(arr1)
print(arr3)
assert arr3 == arr2
