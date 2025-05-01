# [112. Path Sum](https://leetcode.com/problems/path-sum/description/)

**Difficulty:** Easy

**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Companies

This problem is commonly asked in interviews at companies that want to test your understanding of binary trees and recursive algorithms, such as Google, Amazon, Microsoft, and Facebook.

## Description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

## Examples

**Example 1:**

```plaintext
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with sum 22 is 5 -> 4 -> 11 -> 2.
```

**Example 2:**

```plaintext
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are no root-to-leaf paths with sum = 5.
```

**Example 3:**

```plaintext
Input: root = [1,2], targetSum = 0
Output: false
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Approach

To solve this problem, use a depth-first search (DFS) traversal. At each node, subtract the node's value from `targetSum` and recursively check the left and right subtrees. If you reach a leaf node and the remaining sum is zero, return `true`.

## Credits, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/path-sum/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
