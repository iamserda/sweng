def merge_sorted_arrays(arr1, arr2):
    arr3 = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(arr1) or ptr2 < len(arr2):
        if ptr1 >= len(arr1) or arr1[ptr1] >= arr2[ptr2]:
            arr3.append(arr2[ptr2])
            ptr2 += 1
            continue
        if ptr2 >= len(arr2) or arr1[ptr1] <= arr2[ptr2]:
            arr3.append(arr1[ptr1])
            ptr1 += 1
            continue
        break

    return arr3


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 4, 5, 7, 8]
arr3 = merge_sorted_arrays(arr1, arr2)
print(arr3)
assert arr3 == sorted([*arr1, *arr2])
