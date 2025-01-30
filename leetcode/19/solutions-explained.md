# Remove Nth Node From End of List

## Intuition
Faced with the challenge of removing the nth node from the end of a singly linked list, the direct approach of calculating the total length of the list, then iterating again to the correct position for removal, seems inefficient. Instead, a two-pointer strategy promises a more efficient solution by potentially traversing the list only once.

## Approach
The `Solution` class implements the `removeNthFromEnd` method with a two-pointer technique involving `fast` and `slow` pointers:
- Both `fast` and `slow` pointers start at the head of the list.
- The `fast` pointer advances `n` steps ahead to create a gap between `fast` and `slow`.
- Then, both pointers move forward in tandem until `fast` reaches the end of the list. At this point, `slow` is exactly `n` nodes away from the end.
- Special cases are handled:
  - If the list is empty (`head` is `None`), it simply returns `head`.
  - If `n` equals the length of the list, indicating the need to remove the first node, it updates `head` to `head.next` and returns the updated list.
- Finally, `slow.next` is set to `slow.next.next`, effectively skipping over the nth node from the end, which removes it from the list.

## Complexity
- **Time Complexity**: $$O(L)$$, where $$L$$ is the length of the linked list. The algorithm makes a maximum of two passes through the list: one to set the `fast` pointer `n` steps ahead and another to move both `fast` and `slow` to their final positions.
- **Space Complexity**: $$O(1)$$, as it uses a fixed amount of space regardless of the input list size.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        if head is None:
            return head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
```

### Credit, Source, Etc
- This solution provides a practical application of the two-pointer technique, demonstrating its utility in efficiently solving problems that would otherwise require knowing the total length of a linked list.
- Tailored for use cases where direct access to list elements is not possible, emphasizing the value of pointer manipulation in linked list operations.

Designed to be efficient and straightforward, this method underscores the importance of algorithm optimization in data structure manipulation, particularly when working with constraints typical of linked lists.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/two-sum/)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)