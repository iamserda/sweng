# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

**Difficulty:** Easy

**Topics:**Linked List,Two Pointers,Floyd's Tortoise and Hare

## Companies

This problem is a staple in coding interviews, especially in companies focusing on data structures, algorithms, and coding challenges such as Google, Amazon, and Facebook.

## Description

Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if a node can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that the tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Examples

**Example 1:**

- Input: `head = [3,2,0,-4], pos = 1`
- Output: `true`
- Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

![Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

- Input: `head = [1,2], pos = 0`
- Output: `true`
- Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

- Input: `head = [1], pos = -1`
- Output: `false`
- Explanation: There is no cycle in the linked list.

![Example 3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

### Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

### Follow-up

Can you solve it using O(1) (i.e., constant) memory?

## Approach

To solve this problem within the O(1) memory constraint, you can use the Floyd's Tortoise and Hare algorithm. This algorithm involves two pointers that move at different speeds (a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time). If there is a cycle, the fast pointer will eventually meet the slow pointer. Otherwise, the fast pointer will reach the end of the list.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)