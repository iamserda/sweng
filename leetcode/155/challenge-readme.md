# 155. Min Stack

**Difficulty:** Easy/Medium

**Topics:** Stack, Design

## Companies

This problem is popular among companies like Amazon, Microsoft, and Google during technical interviews, especially when they want to assess candidates' ability in designing data structures with specific operations.

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

### Examples

**Example 1:**

```plaintext
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

### Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top`, and `getMin` will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Approach

To achieve constant time complexity for each operation, including retrieving the minimum element, the `MinStack` can be designed using two stacks:

1. **Main Stack:** This stack stores all the elements of the stack as they are pushed or popped.
2. **Min Stack:** This stack keeps track of the minimum elements. Each element in the min stack corresponds to the minimum element of the main stack up to that point.

When pushing a new element onto the stack, compare it with the top of the min stack. If it's smaller or the min stack is empty, push it onto the min stack as well. For pop operations, check if the element being popped is the same as the top of the min stack; if so, pop from the min stack too. This ensures that the min stack's top always represents the minimum element of the main stack, allowing `getMin` to simply return the top of the min stack.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)