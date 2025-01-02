# Dynamic Array Implementation

## Intuition
The necessity to implement a dynamic array arises from the need for a data structure that can grow and shrink in size dynamically, unlike static arrays with a fixed capacity. The concept is inspired by dynamic arrays in languages like Java (ArrayList) and C++ (std::vector), where the array automatically resizes itself when it reaches its capacity.

## Approach
The `DynamicArray` class encapsulates the functionality of a dynamic array, including:
- **Initialization**: Starts with a specified capacity (defaults to 1 if not provided or zero).
- **Getter and Setter**: Access and modify elements at specific indices, ensuring the operations are performed within the current size bounds.
- **Push**: Adds an element to the end. If the array is at capacity, it resizes itself by doubling its capacity before adding the new element.
- **Pop**: Removes and returns the last element of the array, reducing the size by one.
- **Resize**: Doubles the array's capacity to accommodate more elements, copying existing elements to the new, larger array.

## Complexity
- **Time Complexity**:
  - **Getter/Setter**: $$O(1)$$ - Direct access by index.
  - **Push**: Amortized $$O(1)$$ - Most operations are $$O(1)$$, except when resizing is required, which is $$O(n)$$; however, since resizing doubles the capacity, the average cost of insertion remains constant.
  - **Pop**: $$O(1)$$ - Removing the last element.
  - **Resize**: $$O(n)$$ - Requires copying all elements to the new array.

- **Space Complexity**: $$O(n)$$ - The space required is proportional to the number of elements stored in the array.

## Code
The provided code demonstrates a practical implementation of a dynamic array in Python, including error handling for out-of-bound accesses and a testing arena to validate the functionality of each method.

```python
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity or 1
        self.arr = [None] * self.capacity
        self.size = 0

    def getter(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Error: Invalid index value.")
        return self.arr[i]

    def setter(self, i: int, n: int):
        if i < 0 or i >= self.size:
            raise IndexError("Error: Invalid index value.")
        self.arr[i] = n

    def push(self, n: int):
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from empty array.")
        item = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return item

    def resize(self):
        self.capacity *= 2
        arr_ptr = [None] * self.capacity
        for i in range(self.size):
            arr_ptr[i] = self.arr[i]
        self.arr = arr_ptr

    def get_size(self) -> int:
        return self.size

    def get_capacity(self) -> int:
        return self.capacity
```

### Credit, Source, Etc
- Inspired by dynamic array implementations in various programming languages, this custom Python class offers a simplified yet functional prototype for educational and practical use cases.
- Created and tested with care in a simulated environment to ensure correctness and reliability.

Made with passion and attention to detail, this dynamic array prototype aims to provide a foundational understanding of how dynamically resizable arrays operate under the hood.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
