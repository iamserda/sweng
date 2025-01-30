# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

## Intuition

Upon seeing the problem of reversing a singly-linked list, the immediate thought is how to reorient the arrows (pointers) so that they point backward, making the last node the new head. The main challenge is doing this without losing track of the nodes as we change their pointers, ensuring that each node points to its predecessor instead of its successor.

## Approach

The solution employs a straightforward yet effective method using three pointers: `left_ptr`, `temp_ptr`, and `right_ptr`. Initially, `left_ptr` acts as a placeholder for the new reversed list, starting as `None` since the new head's previous node does not exist. `temp_ptr` starts at the head of the original list, and `right_ptr` is used to keep track of the list's remainder as we iterate. The process involves pointing the current node (`temp_ptr`) to `left_ptr`, effectively reversing the link, and then advancing `left_ptr` and `temp_ptr` forward (in the original list's perspective) until all nodes have been reversed. Finally, `head` is updated to `left_ptr`, which points to the new head of the reversed list.

## Complexity

- Time complexity: $$O(n)$$

  Each node in the list is visited exactly once to reverse its pointer, leading to a linear time complexity proportional to the length of the list.

- Space complexity: $$O(1)$$

  The space used does not depend on the size of the input list. Only a fixed number of pointers (`left_ptr`, `temp_ptr`, `right_ptr`) are used regardless of the list's length, ensuring a constant space complexity.

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        left_ptr = None
        temp_ptr = head
        right_ptr = temp_ptr
        while temp_ptr:
            right_ptr = right_ptr.next
            temp_ptr.next = left_ptr
            left_ptr = temp_ptr
            temp_ptr = right_ptr
        head = left_ptr
        return head
```

### Credit, Source, Etc

- Source: [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
