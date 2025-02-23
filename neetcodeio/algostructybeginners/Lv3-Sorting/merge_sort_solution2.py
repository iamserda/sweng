import math, random


def merge_sort(arr):
    """sorts an array, in ascending order"""
    if not arr:
        print(ValueError("List is empty. Cannot sort an empty list."))
        return []

    if len(arr) == 1:
        return arr
    else:
        mid = int(math.ceil(len(arr) / 2))
        arr1 = merge_sort(arr[:mid])
        arr2 = merge_sort(arr[mid:])
        arr3 = merge_sorted_arrays(arr1, arr2)
        return arr3


def merge_sorted_arrays(sorted_arr1, sorted_arr2):
    sorted_arr3 = []
    i = 0
    j = 0
    while True:
        if i >= len(sorted_arr1) and j >= len(sorted_arr2):
            return sorted_arr3

        if i < len(sorted_arr1) and j >= len(sorted_arr2):
            sorted_arr3.append(sorted_arr1[i])
            i += 1
            continue

        if j < len(sorted_arr2) and i >= len(sorted_arr1):
            sorted_arr3.append(sorted_arr2[j])
            j += 1
            continue

        if sorted_arr1[i] <= sorted_arr2[j]:
            sorted_arr3.append(sorted_arr1[i])
            i += 1
            continue

        if sorted_arr1[i] > sorted_arr2[j]:
            sorted_arr3.append(sorted_arr2[j])
            j += 1
            continue
        break
    return sorted_arr3


# Testing Arenas:

arr = [random.randint(-10, 10) for i in range(10)]
print("before:", arr)
sorted_arr = merge_sort(arr)
sorted_arr_prime = sorted(arr)
assert sorted_arr == sorted_arr_prime
print("after:", sorted_arr)
