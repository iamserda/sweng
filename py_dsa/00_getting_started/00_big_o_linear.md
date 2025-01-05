# README: Understanding Linear Time Complexity (O(n))

## Introduction

Welcome to the guide on understanding Linear Time Complexity, also known as `O(n)`. This document is designed to explain this concept in a simple, easy-to-understand manner, often referred to as "Explain Like I'm 10" (ELI10). We will explore what linear time complexity means in the context of programming and provide multiple coding examples to illustrate this concept.

## What is Time Complexity?

Time complexity is a way to describe how the time it takes to run an algorithm increases as the size of the input increases. It's like measuring how much longer it takes to complete a task when the task becomes bigger.

## What Does O(n) Mean?

`O(n)` is a notation used to express that an algorithm's runtime grows linearly with the size of the input. In other words, if the input size doubles, the time it takes to complete the task also doubles. Think of it as a straight line going up.

## Why is Linear Time Complexity Important?

Understanding `O(n)` is crucial because it helps us predict how long an algorithm will take to run based on the size of its input. This is important for writing efficient programs, especially when dealing with large amounts of data.

## Coding Examples

### Example 1: Sum of an Array

In this example, we calculate the sum of all elements in an array. As the array's size (n) increases, the time to calculate the sum increases linearly.

```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Usage
print(sum_array([1, 2, 3, 4, 5]))  # Output: 15
```

### Example 2: Finding the Maximum Element

Here, we find the largest number in an array. The time to find the maximum increases linearly with the size of the array.

```python
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# Usage
print(find_max([3, 1, 4, 1, 5, 9]))  # Output: 9
```

### Example 3: Linear Search

This is an example of a linear search where we search for an element in an array. The worst-case time complexity is linear as we might have to look at every element once.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Usage
print(linear_search([5, 8, 1, 3, 2], 3))  # Output: 3
```

## Conclusion

Linear time complexity, or `O(n)`, is a fundamental concept in computer science. It represents a scenario where the time taken by an algorithm increases linearly with the size of the input. Understanding this concept helps in writing efficient code, especially for handling large datasets.

Feel free to experiment with the provided examples to deepen your understanding of linear time complexity. Happy coding!