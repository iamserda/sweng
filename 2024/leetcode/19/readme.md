# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

**Difficulty:** Medium

**Topic:** Linked List, Fast-Slow-Pointers

## Companies

This problem is a favorite among tech companies like Amazon, Google, and Facebook during coding interviews, focusing on testing understanding of linked lists and two-pointer techniques.

## Description

Given the head of a linked list, remove the `n`-th node from the end of the list and return its head.

### Examples

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

- Input: `head = [1,2,3,4,5], n = 2`
- Output: `[1,2,3,5]`
- Explanation: After removing the second node from the end, the linked list becomes `[1,2,3,5]`.

**Example 2:**

- Input: `head = [1], n = 1`
- Output: `[]`
- Explanation: After removing the first node from the end, the linked list becomes empty.

**Example 3:**

- Input: `head = [1,2], n = 1`
- Output: `[1]`
- Explanation: After removing the first node from the end, the linked list becomes `[1]`.

### Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

### Follow-up

Could you do this in one pass?

## Approach

To solve this problem, you can use the two-pointer technique, often described as the "fast and slow" pointer method. Here's a step-by-step guide:

1. Initialize two pointers, `fast` and `slow`, to the head of the linked list.
2. Move `fast` `n` steps ahead in the list.
3. Move both `fast` and `slow` together until `fast` reaches the last node. This ensures that `slow` is `n` nodes behind `fast` and exactly at the node preceding the node to be removed.
4. Adjust the `next` pointer of the `slow` node to skip the node to be removed.
5. If the node to be removed is the head itself, this approach will not directly work since `slow` will not be able to skip the head. To handle this, you can use a dummy head node.

This approach allows you to remove the `n`-th node from the end in a single pass through the linked list, meeting the problem's follow-up challenge and optimizing for both time and space efficiency.


### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
