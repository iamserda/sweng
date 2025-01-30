# [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

**Difficulty:**Easy

**Topics:**Linked List, Recursion

## Companies

This problem is commonly used by tech companies like Google, Amazon, Facebook, and Microsoft to evaluate understanding of linked lists in coding interviews.

## Description

Given the head of a singly linked list, reverse the list and return the reversed list.

### Examples

**Example 1:**

- Input: `head = [1,2,3,4,5]`
- Output: `[5,4,3,2,1]`
- Visualization:

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Example 2:**

- Input: `head = [1,2]`
- Output: `[2,1]`

**Example 3:**

- Input: `head = []`
- Output: `[]`

### Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

### Follow-up

A linked list can be reversed either iteratively or recursively. Could you implement both methods?

## Approach

### Iterative Method

1. Initialize three pointers: `prev` as `NULL`, `current` as `head`, and `next` as `NULL`.
2. Iterate through the list and at each step:
   - Temporarily store the next node using `next = current->next`.
   - Reverse the current node's pointer to point to `prev`.
   - Move `prev` and `current` one step forward: `prev = current` and `current = next`.
3. `head` should now point to the new head of the list, which is the last node we encountered (stored in `prev`).

### Recursive Method

1. Base case: if `head` is `NULL` or `head->next` is `NULL`, return `head` as the new head of the reversed list.
2. Recursively reverse the rest of the list starting from the second node.
3. Set the next node's `next` pointer to point to the current node (effectively reversing the link).
4. Set the current node's `next` to `NULL` to break the original link.
5. Return the new head of the reversed list, which is the result of the recursive call with the second node.

Both methods effectively reverse the list by changing the direction of the pointers between the nodes.

### Credit, Source, Etc

- Source: [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
