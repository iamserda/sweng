# [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

**Difficulty:** Medium

**Topics:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree

## Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

### Note

- It is guaranteed that the tree can be constructed from the given traversals.
- The tree contains no duplicate values.

### Examples

**Example 1:**

```plaintext
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**

```plaintext
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

### Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

## Approach

To solve this problem, consider the following steps:

1. **Identify Root**: The first element in `preorder` is always the root of the tree (or subtree).
2. **Find Root in Inorder**: Locate the root in the `inorder` array. Elements to the left are in the left subtree; elements to the right are in the right subtree.
3. **Recurse**: Recursively repeat the process for left and right subtrees using the corresponding subarrays from `preorder` and `inorder`.

A hash map can be used to quickly find the index of any value in the `inorder` array, improving efficiency.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
