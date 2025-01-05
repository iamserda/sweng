# Time and Space Complexities

## Introduction

This document explains the concepts of time and space complexities with code examples. Time complexity measures the time an algorithm takes to run as a function of the input size, while space complexity measures the amount of memory it uses.

## Time Complexity

Time complexity is expressed in Big O notation, which describes the upper limit of the time required relative to the input size.

### Constant Time: O(1)

Code runs in constant time when it doesn't depend on the size of the input data.

```python
def check_first_element(list):
    return list[0] if list else None
```

### Logarithmic Time: O(log n)

An example is binary search, where the data set is halved each time.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
```

### Linear Time: O(n)

An algorithm running in linear time increases linearly with the input size.

```python
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
```

### Linearithmic Time: O(n log n)

An example is the Merge Sort algorithm.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

### Quadratic Time: O(n²)

A common example is the Bubble Sort algorithm.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### Exponential Time: O(2^n)

An example is the recursive calculation of Fibonacci numbers.

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Space Complexity

Space complexity measures the total amount of memory that an algorithm uses relative to the input size.

### Constant Space: O(1)

An algorithm uses a constant amount of space, irrespective of input size.

```python
def add(a, b):
    return a + b
```

### Linear Space: O(n)

An example is storing all elements of an input array.

```python
def clone_array(arr):
    clone = []
    for item in arr:
        clone.append(item)
    return clone
```

## Conclusion

Understanding time and space complexities is crucial for writing efficient algorithms. These concepts help in choosing the right algorithm for a given problem based on the constraints and requirements.

gh: [@iamserda](https://github.com/iamserda)

tw: [@iamserda](https://twitter.com/iamserda)

in: [@iamserda](https://linkedin.com/in/iamserda)