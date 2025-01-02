# 1. Arrays

## README for Arrays

Arrays are one of the simplest and most widely used data structures in computer science. An array is a collection of elements, all of the same type, stored in contiguous memory locations. The elements can be accessed randomly by indexing into the array. Due to their simplicity and direct access feature, arrays are highly efficient for operations that involve frequent access to elements based on their index.

### Key Operations
- **Access**: O(1)
- **Insertion/Deletion (at the end)**: O(1) amortized
- **Insertion/Deletion (at an arbitrary index)**: O(n)
- **Search**: O(n)

### Use Cases
- Storing and accessing elements sequentially or randomly with known indices.
- Basic data manipulation tasks.

```python
# Python code for Array implementation

# Initializing an array
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1

# Modifying an element
arr[2] = 10

# Iterating through an array
for element in arr:
    print(element)

# Adding an element to the end
arr.append(6)

# Inserting an element at a specific position
arr.insert(2, 15)

# Removing an element
arr.remove(15)

# Deleting an element at a specific index
del arr[2]
```

### Further Steps
- Practice implementing dynamic arrays that resize themselves as you add more elements.
- Explore multidimensional arrays and their applications.