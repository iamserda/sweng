# 225. Implement Stack using Queues

**Difficulty:** Easy

**Topics:** Stack,Design,Queue

## Description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes:**
- You must use **only** standard operations of a queue, which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

### Examples

**Example 1:**

```plaintext
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

### Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

## Follow-up

Can you implement the stack using only one queue?

## Approach

To implement a stack using queues, you can use two queues where one queue is used to store the whole stack and the other is used to temporarily hold elements for certain operations like `pop` and `push`. For a `pop` operation, you would dequeue everything except the last element from the primary queue into the temporary queue, dequeue the last element to return it, and then swap the roles of the two queues. For the `push` operation, you can directly enqueue to the primary queue. 

The `top` operation can be implemented similarly to `pop` but without dequeuing the last element. The `empty` operation directly checks if the primary queue is empty.

### Follow-up Solution

For the follow-up challenge of using only one queue, you can adjust the `push` operation to rotate the queue after adding a new element, effectively placing the new element at the front of the queue to simulate stack behavior. This way, the most recently added element is always at the front of the queue, mimicking the LIFO property of stacks. The `pop`, `top`, and `empty` operations can be straightforwardly implemented since the most recent element is always at the front.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
