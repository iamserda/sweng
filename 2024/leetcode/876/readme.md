# [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description)

**Difficulty:** Easy

**Topics:** Linked List, Two Pointers

## Companies

This is a common question in interviews for tech companies, especially those focusing on data structures and algorithms.

## Description

Given the head of a singly linked list, the task is to return the middle node of the linked list. If there are two middle nodes, you are asked to return the second middle node.

### Examples

**Example 1:**

- Input: `head = [1,2,3,4,5]`
- Output: `[3,4,5]`
- Explanation: The middle node of the list is node 3.

![Example 1](https://assets.leetcode.com/uploads/2020/09/02/ex1.jpg)

**Example 2:**

- Input: `head = [1,2,3,4,5,6]`
- Output: `[4,5,6]`
- Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

![Example 2](https://assets.leetcode.com/uploads/2020/09/02/ex2.jpg)

### Constraints

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

## Approach

A straightforward way to solve this problem is by using the "Tortoise and Hare" strategy, which involves two pointers moving at different speeds (the slow pointer moves one node at a time, while the fast pointer moves two nodes at a time). When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list. This method allows for finding the middle node in a single pass, thereby ensuring an efficient solution.

## Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/description)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
