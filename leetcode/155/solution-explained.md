# MinStack: Stack with Min Function

## Intuition
Designing a stack that supports push, pop, top, and retrieving the minimum element in constant time presents an interesting challenge. The conventional stack operations are straightforward, but efficiently tracking the minimum element requires additional consideration. The key insight is to maintain parallel storage that keeps track of the minimum value at each level of the stack.

## Approach
The `MinStack` class implements a standard stack with enhanced functionality to track the minimum value. It uses two lists:
- `stack`: To store the actual stack elements.
- `minStack`: To keep track of the minimum element at each stage of the stack.

The operations are as follows:
- **push(val)**: Adds an element to the top of the stack. It also updates the `minStack` by comparing the new value with the current minimum (top of the `minStack`) and storing the new minimum.
- **pop()**: Removes the top element from the stack. If the popped element is the current minimum, it recalculates the minimum by iterating over the remaining stack elements. This step ensures the `minStack` accurately reflects the next minimum.
- **top()**: Returns the top element of the stack without removing it.
- **getMin()**: Returns the minimum element in the stack.

## Complexity
- **Time Complexity**:
  - **push**: $$O(1)$$ for adding an element and updating the minimum.
  - **pop**: $$O(n)$$ in the worst case when the minimum element is removed, necessitating a recalculation of the minimum over the stack.
  - **top**: $$O(1)$$ for retrieving the top element.
  - **getMin**: $$O(1)$$ for retrieving the current minimum.
- **Space Complexity**: $$O(n)$$, where $$n$$ is the number of elements in the stack. The space is used by both the `stack` and `minStack` to store elements and their corresponding minimums.

## Code
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

## Remarks
This solution elegantly balances the efficiency of stack operations with the requirement to track the minimum element. It demonstrates the power of auxiliary data structures in enhancing the functionality of basic data structures. The primary limitation arises during the `pop` operation when the minimum is removed, leading to a less efficient recalculation step. However, this implementation provides a practical balance between time complexity and the functionality offered by the `MinStack` class.

### Credit, Source, Etc
- This implementation of `MinStack` is a classic problem solution that illustrates key concepts in data structure design, particularly how to efficiently augment standard structures with additional features.
- It is designed for educational purposes, highlighting techniques for managing auxiliary information parallel to primary data structures.

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
