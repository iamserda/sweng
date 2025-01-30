# Dynamic Array Implementation

Implement a dynamic array class named `DynamicArray` that simulates the behavior of a dynamic array, similar to the ArrayList in Java or vectors in C++. Your class should support the following operations:

1. **Constructor** - Initializes the dynamic array with an initial capacity. The capacity indicates how many elements the array can hold before it needs to resize.
2. **Getter** - Given a valid index, returns the value at that index.
3. **Setter** - Given a valid index, updates the value at that index with a new integer value.
4. **Push** - Appends a new item at the end of the array. If the array is at full capacity, it should automatically resize to accommodate the new item.
5. **Pop** - Removes the last item of the array and returns it. If the array is empty, return -1 or throw an exception.
6. **Resize** - Doubles the size of the array. This method is usually called internally when the array needs to expand.
7. **Get Size** - Returns the current number of elements in the dynamic array.
8. **Get Capacity** - Returns the current capacity of the dynamic array, which may be larger than the number of elements.

## Example

```plaintext
Input
["DynamicArray", "push", "push", "getter", "push", "get_capacity", "get_size", "pop", "get_size"]
[[2], [1], [2], [1], [3], [], [], [], []]

Output
[null, null, null, 2, null, 4, 3, 3, 2]

Explanation
DynamicArray dynamicArray = new DynamicArray(2); // Initialize a dynamic array with capacity = 2
dynamicArray.push(1); // array = [1]
dynamicArray.push(2); // array = [1, 2]
dynamicArray.getter(1); // return 2
dynamicArray.push(3); // Automatically resizes to capacity = 4, and array = [1, 2, 3]
dynamicArray.get_capacity(); // return 4
dynamicArray.get_size(); // return 3
dynamicArray.pop(); // Removes the last element (3), and returns it. Now array = [1, 2]
dynamicArray.get_size(); // return 2
```

## Constraints:

- 1 <= capacity, n <= 10^5
- 0 <= i < get_size()
- At most 10^4 calls in total will be made to push, pop, getter, setter, get_size, and get_capacity.

## Note:

- You may assume that for the getter and setter functions, the index `i` is always valid.
- Implement the resize operation efficiently to minimize the computational cost associated with expanding the array.
- Consider using exception handling for error management, such as attempting to pop from an empty array.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
