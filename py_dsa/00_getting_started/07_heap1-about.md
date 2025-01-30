# Heaps

## README for Heaps

Heaps are a special tree-based data structure that satisfy the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (the root node) contains the largest key (max heap) or the smallest key (min heap). Heaps are commonly used to implement priority queues, where the node with the highest priority is always at the front.

## Key Operations

- **Insertion**: O(log n), as elements need to be compared upwards along the path from the inserted node to the root.
- **Deletion (Removing the root)**: O(log n), due to the need to reheapify the tree.
- **Find Max/Min**: O(1), as the max/min element is always at the root.
- **Search**: O(n), as heaps are not ordered and a full traversal is necessary to find an element.

## Use Cases

- Implementing priority queues.
- Sorting elements using heap sort.
- Finding the kth largest/smallest element in a collection.

## Python Implementation (Min Heap Example)

Python's `heapq` module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Below is a simple example demonstrating how to use `heapq` to create a min heap:

```python
import heapq

# Create a min heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)

# View the smallest element
print("Smallest element:", min_heap[0])  # Output: Smallest element: 1

# Remove and return the smallest element
print("Removed element:", heapq.heappop(min_heap))  # Output: Removed element: 1

# After removing the smallest element
print("Smallest element now:", min_heap[0])  # Output: Smallest element now: 3

# If you need a max heap, you can insert and pop elements with their sign inverted or use a custom class to invert the comparison.
```

## Further Steps

- Experiment with implementing a max heap by inverting the values during insertions and deletions.
- Explore heap sort algorithm and its implementation using heaps.
- Implement a priority queue for more complex scheduling tasks.

Heaps are a powerful tool for managing data in applications where time efficiency of access, insertion, and deletion (especially for the root element) is critical, such as in priority queues. Next Up Graphs?


## Using the `heapq` Module in Python

The `heapq` module in Python provides an easy-to-use implementation of the heap queue algorithm, which is a type of priority queue. Heaps are binary trees for which every parent node has a value less than or equal to any of its children (min heap). This implementation uses arrays for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all `k`, counting elements from zero. This is an efficient way of implementing a priority queue, allowing for easy insertion and removal of items while maintaining the heap property.

### Basic Operations

#### Creating a Heap

You can start by creating an empty list to represent the heap. The `heapq` module provides functions like `heappush` to add elements to the heap.

```python
import heapq

# Create an empty heap
heap = []
```

#### Adding Elements: `heappush`

To add an element to the heap, use the `heappush` method. This method adds the element while maintaining the heap property.

```python
heapq.heappush(heap, item)
```

#### Removing Elements: `heappop`

To remove and return the smallest element from the heap, use the `heappop` method. This operation also maintains the heap property.

```python
smallest = heapq.heappop(heap)
```

#### Finding the Smallest Element: Accessing the Root

In a heap, the smallest element can always be found at the root (i.e., heap[0]). This operation does not remove the element.

```python
smallest = heap[0]
```

#### Transforming a List into a Heap: `heapify`

If you have a populated list that you want to turn into a heap, you can use the `heapify` method. This method rearranges the elements in the list to satisfy the heap property.

```python
heapq.heapify(heap)
```

### Example: Creating a Min Heap

```python
import heapq

# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Transform the list into a heap
heapq.heapify(numbers)

# Add an element
heapq.heappush(numbers, 0)

# Remove and return the smallest element
smallest = heapq.heappop(numbers)

print(f"Smallest element: {smallest}")
print(f"Remaining heap: {numbers}")
```

### Additional Functions

- **`heapq.heappushpop(heap, item)`**: Pushes a new item on the heap, then pops and returns the smallest item from the heap. The combined action runs more efficiently than `heappush()` followed by `heappop()`.
- **`heapq.heapreplace(heap, item)`**: Pops and returns the smallest item from the heap, and then pushes the new item. The heap size does not change. If the heap is empty, `IndexError` is raised.
- **`heapq.nlargest(n, iterable)`** and **`heapq.nsmallest(n, iterable)`**: Return a list with the n largest and n smallest elements from the dataset defined by iterable, respectively.

The `heapq` module is a simple yet powerful tool for creating and managing heaps in Python. It's particularly useful for implementing priority queues, where the order of objects is determined by their priority.

## Python's `heapq` Module Guide

The `heapq` module in Python provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Heaps are a type of binary tree where the parent node is smaller than or equal to its child nodes (in a min heap), or greater than or equal to its child nodes (in a max heap), though the Python implementation focuses on min heaps. The `heapq` module allows for easy manipulation of these heap-structured lists.

### Functions Provided by `heapq`

#### `heapq.heappush(heap, elem)`

- **Purpose**: Adds an element `elem` to the heap while maintaining the heap invariant.
- **Usage**:
    ```python
    import heapq
    heap = []
    heapq.heappush(heap, value)
    ```

#### `heapq.heappop(heap)`

- **Purpose**: Removes and returns the smallest element from the heap.
- **Usage**:
    ```python
    smallest = heapq.heappop(heap)
    ```

#### `heapq.heapify(x)`

- **Purpose**: Transforms list `x` into a heap, in-place, in linear time.
- **Usage**:
    ```python
    heapq.heapify(x)
    ```

#### `heapq.heapreplace(heap, elem)`

- **Purpose**: Pops and returns the smallest element from the heap, and then pushes the new `elem` onto the heap. The heap size is not changed.
- **Usage**:
    ```python
    replaced_element = heapq.heapreplace(heap, new_elem)
    ```

#### `heapq.heappushpop(heap, elem)`

- **Purpose**: Pushes a new `elem` onto the heap, then pops and returns the smallest element from the heap. The combined action runs more efficiently than `heappush()` followed by `heappop()`.
- **Usage**:
    ```python
    result = heapq.heappushpop(heap, elem)
    ```

#### `heapq.nlargest(n, iterable, key=None)`

- **Purpose**: Returns the n largest elements from the `iterable`. The `key` parameter allows specifying a function of one argument that is used to extract a comparison key from each element in the iterable.
- **Usage**:
    ```python
    largest = heapq.nlargest(n, iterable, key=lambda x: x.attribute)
    ```

#### `heapq.nsmallest(n, iterable, key=None)`

- **Purpose**: Returns the n smallest elements from the `iterable`. Similar to `nlargest`, but for finding the smallest elements.
- **Usage**:
    ```python
    smallest = heapq.nsmallest(n, iterable, key=lambda x: x.attribute)
    ```

### Example Usage

```python
import heapq

# Create a min heap
heap = []
heapq.heappush(heap, (5, 'rest'))
heapq.heappush(heap, (2, 'work'))
heapq.heappush(heap, (4, 'study'))

# Find the three smallest items
three_smallest = heapq.nsmallest(3, heap)

print(three_smallest)
```

### When to Use `heapq`

The `heapq` module is ideal for applications that require frequent access to the smallest (or largest, using `nlargest`) items from a collection without needing to maintain the entire collection in sorted order. Common use cases include:

- Implementing priority queues.
- Scheduling tasks based on priority.
- Managing bandwidth or processing time in resource-constrained environments.

