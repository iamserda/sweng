
# [225. Implement Stack Using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)

## Problem Statement
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all standard stack operations (push, pop, top, and checking if empty).

## Approach and Methodology
The `MyStack` class simulates stack operations using two queue-like lists, `queue1` and `queue2`, due to their inherent first-in-first-out (FIFO) nature. The challenge lies in reversing this order to achieve the LIFO behavior of a stack. Here's how each operation is implemented:

- **`__init__(self)`**:
  Initializes the stack with two empty queues and a variable `topmost` to keep track of the top element of the stack for efficient access.

- **`push(self, x: int)`**:
  Inserts an element at the top of the stack. The new element is also stored as the `topmost` element since it's the last inserted element, directly mimicking the stack's push operation.

- **`pop(self)`**:
  Removes the top element from the stack. Since queues only allow removing the front element, this operation involves transferring all elements except the last from `queue1` to `queue2`, effectively reversing their order. The last element of `queue1` (the top of the stack) is popped and returned. The roles of `queue1` and `queue2` are then swapped to prepare for future operations.

- **`top(self)`**:
  Returns the top element of the stack without removing it, which is efficiently achieved using the `topmost` variable.

- **`empty(self)`**:
  Checks if the stack is empty by returning `True` if `queue1` is empty, otherwise `False`.

## Complexity Analysis
- **Time Complexity**:
  - **Push Operation**: $$O(1)$$ - Directly appending to `queue1` is a constant-time operation.
  - **Pop Operation**: $$O(n)$$ - Involves moving all but one element from `queue1` to `queue2`, where $$n$$ is the number of elements in the stack.
  - **Top Operation**: $$O(1)$$ - Returns the `topmost` element without traversal.
  - **Empty Operation**: $$O(1)$$ - Checks if `queue1` is empty, a constant-time operation.
  
- **Space Complexity**: $$O(n)$$ - The space complexity for maintaining the stack elements across the two queues, where $$n$$ is the number of elements in the stack.

## Code
```python
class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.topmost = None

    def push(self, x: int) -> None:
        self.topmost = x
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.topmost = self.queue1.pop(0)
            self.queue2.append(self.topmost)
        temp = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, []
        return temp

    def top(self) -> int:
        return self.topmost

    def empty(self) -> bool:
        return not self.queue1
```

## Remarks
This solution effectively demonstrates how to leverage queue operations to mimic a stack's behavior, emphasizing the versatility of basic data structures. While the approach introduces some inefficiency, particularly in the `pop` operation, it provides valuable insights into the principles of data structure design and adaptation.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)