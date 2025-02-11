def concate_arrays(arr: list):
    if not arr:
        return arr
    size = len(arr)
    new_size = size * 2
    new_arr = [None] * new_size
    for i, v in enumerate(arr):
        new_arr[i] = v
        new_arr[i + size] = v
    return new_arr


assert concate_arrays([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
assert concate_arrays([1, 3]) == [1, 3, 1, 3]
assert concate_arrays([1]) != [1, 2]
