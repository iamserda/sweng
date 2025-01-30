# num1 = 11
# num2 = num1

# print(num1, num2)  # 11, 11
# print(id(num1), id(num2))  # points to the same mem address.
# 20 is created and stored in a new memory address,
# and num1 POINTS to the new mem location.
num1 = 20
print(num1, num2)  # 20, 11
print(id(num1), id(num2))  # points to DIFF memory addresses
# num2 is still pointing to the first mem address
# However, num2 is now pointing to a new mem address.

# What about complex data structures like list, dict, tuples, etc...?
arr = [[1, 2], [3, 4]]
print(arr, "is at mem loc", id(arr))
print(id(arr) - id(arr[0]))

# each sub arr are stored in a
print(arr[0], "is at mem loc", id(arr[0]))
print(arr[1], "is at mem loc", id(arr[1]))
print(id(arr) - id(arr[0]))
print(id(arr[0]) - id(arr[1]))

# each int are stored contiguously BUT no where near their containers.
print(id(arr[0][0]), id(arr[0][1]), id(arr[1][0]), id(arr[1][1]))
arr[0][0] = 10
arr[0][1] = 20
arr[1][0] = 30
arr[1][1] = 40
print(arr)
print(id(arr))
print(id(arr[0]), id(arr[-1]))
print(id(arr[0][0]), id(arr[0][1]), id(arr[1][0]), id(arr[1][1]))
