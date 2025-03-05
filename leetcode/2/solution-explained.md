# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## Challenge:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: `l1 = [2,4,3], l2 = [5,6,4]`

Output: `[7,0,8]`

Explanation: `342 + 465 = 807`

Example 2:

Input: `l1 = [0], l2 = [0]`

Output: `[0]`

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

## Constraints:

## Intuition

When tasked with implementing a linked list from the ground up, the immediate thought is to capture the essence of a linked list's structure and operations. The focus is on creating a flexible, efficient data structure that allows dynamic insertion and deletion of elements. The primary challenge lies in correctly managing pointers to ensure the integrity of the list across various operations.

## Approach

The implementation strategy revolves around defining a `Node` class to represent individual elements in the list and a `MyLinkedList` class for managing the list. Key operations include:

- **Initialization**: Set up an initially empty list, characterized by a `head` and `tail` pointer, and a `length` counter for tracking the list's size.
- **Add at Head**: Insert a new element at the beginning of the list, adjusting the `head` pointer and handling edge cases for an initially empty list.
- **Add at Tail**: Append a new element at the end, utilizing the `tail` pointer for efficient access.
- **Add at Index**: Insert a new element at a specified position, which involves traversing the list to the correct location before insertion.
- **Delete at Index**: Remove an element from a specified position, with special attention to maintaining list integrity when removing the head or tail.
- **Get**: Retrieve the value of an element at a specified index by traversing the list from the head.

## Complexity

## Code

```python
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_head = ListNode(None)
        visitor = l3_head
        carry_over = 0
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            if carry_over:
                temp += carry_over
            if temp >= 10:
                carry_over = temp // 10
                temp = temp % 10
            else:
                carry_over = 0
            visitor.next = ListNode(temp)
            visitor = visitor.next
            if not l1 and not l2 and carry_over:
                visitor.next = ListNode(carry_over)
        return l3_head.next

# Testing Arena:
arr1 = [ListNode(random.randint(0,9)) for in in range(random.randint(1,9))]
arr2 = [ListNode(random.randint(0,9)) for in in range(random.randint(1,9))]
pre = ListNode("pre")
for elem in arr1:
    pre.next = elem
    pre = pre.next
pre = ListNode("pre")
for elem in arr2:
    pre.next = elem
    pre = pre.next

sol = Solution()
l1, l2 = arr1[0], arr2[0]
l3 = sol.addTwoNumbers(arr1[0], arr2[0])
temp = l3
while temp:
    print(temp.val)
    temp = temp.next
```

### Follow-up

The follow-up question regarding an algorithm that runs in $$O(m + n)$$ time seems unrelated to the linked list implementation. Such complexity often pertains to problems involving the merging or comparison of two lists or arrays, where `m` and `n` represent their respective sizes. This might have been included by mistake or requires additional context to address appropriately.

### Credit, Source, Etc

- Source: [LeetCode](url-path)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)
