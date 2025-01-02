# [86. Partition List](https://leetcode.com/problems/partition-list/description/)

## Difficulty

Medium

## Topics

- Linked List
- Two Pointers

## Companies

This problem is a good test of understanding linked lists and has been used in interviews at tech companies that require a solid foundation in data structures, such as Google, Amazon, and Microsoft.

## Description

Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

You should preserve the original relative order of the nodes in each of the two partitions.

### Examples

**Example 1:**

```plaintext
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Explanation: 
All nodes with a value less than 3 are moved to the front of the list, preserving their original relative order. Similarly, all nodes with a value greater than or equal to 3 are moved to the back, preserving their original relative order.
```

**Example 2:**

```plaintext
Input: head = [2,1], x = 2
Output: [1,2]
Explanation:
The node with value 1 is moved before the node with value 2, preserving their original relative order.
```

### Constraints

- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Approach

The problem can be efficiently solved by maintaining two separate lists during traversal:

1. One list for nodes with values less than `x` (`less` list).
2. Another list for nodes with values greater than or equal to `x` (`greater` list).

Steps to solve the problem:

- Initialize two new linked list heads: one for `less` and another for `greater`.
- Traverse the original list, appending each node to the `less` list if its value is less than `x`, or to the `greater` list otherwise.
- After the traversal, connect the end of the `less` list to the head of the `greater` list.
- Return the head of the `less` list if it has nodes; otherwise, return the head of the `greater` list.

This approach ensures that we partition the list as required while maintaining the original relative order of the nodes in each partition.

- Source: [LeetCode](https://leetcode.com/problems/partition-list/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
