# [1836. Remove Duplicates From an Unsorted Linked List](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/)

**Difficulty:** Medium

**Topics:** Linked List, Hash Table, Two-Pointers

## Companies

This problem tests a candidate's ability to manipulate linked lists and manage duplicates, which is essential for companies that deal with data cleanup or require efficient data storage and retrieval, such as database companies or companies working with large datasets (e.g., Google, Amazon, Facebook).

## Description

Given the head of a linked list, remove all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

### Examples

**Example 1:**

```plaintext
Input: head = [1, 2, 3, 2]
Output: [1, 3]
Explanation: 
2 appears twice in the linked list, so all 2's are removed. The remaining elements 1 and 3 are unique, so we return [1, 3].
```

**Example 2:**

```plaintext
Input: head = [2, 1, 1, 2]
Output: []
Explanation: 
2 and 1 both appear twice, so all nodes are removed. The linked list is left empty, so we return an empty list.
```

**Example 3:**

```plaintext
Input: head = [3, 2, 2, 1, 3, 2, 4]
Output: [1, 4]
Explanation: 
3 and 2 both appear more than once. Removing them leaves [1, 4], with 1 and 4 being unique.
```

### Constraints

- The number of nodes in the list is in the range `[0, 10^5]`.
- `-10^5 <= Node.val <= 10^5`

## Approach

To solve this problem, you can use a two-pass approach with a hash table:

1. **First Pass:** Traverse the linked list and use a hash table (or a hash map) to count the occurrence of each value.
2. **Second Pass:** Re-traverse the list and use the hash table to remove nodes with values that have an occurrence greater than 1. This requires careful manipulation of the previous and current pointers to ensure nodes are correctly removed and the list remains connected.

### Implementation Details

- Initialize a dummy node to act as the new head of the list. This simplifies edge cases where the head of the list needs to be removed.
- Use a hash table to count occurrences of each value in the first pass.
- In the second pass, check the hash table to determine if a node should be removed. If so, adjust pointers to skip the current node. Otherwise, move to the next node.
- Return the next of the dummy node, which points to the head of the modified list.

This approach efficiently removes all duplicates from the list, ensuring that only unique values are left in the resulting linked list.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
