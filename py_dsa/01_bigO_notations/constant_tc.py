def constant_time_example(arr):
    return arr[0]


arr = [1, 2, 3, 4, 5]
result = constant_time_example(arr)
print(result)  # This will always return 1, regardless of the array size.
