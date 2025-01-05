# [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/post-solution/?submissionId=1170449976)

## Intuition

When presented with the challenge of finding the middle node of a linked list, the immediate thought is to traverse the list to count the elements, and then use that count to find the middle element with a second traversal. However, this method requires two passes through the list. A more efficient approach, which comes to mind, involves traversing the list in a single pass. This is where the two-pointer technique, specifically the fast and slow pointer method, becomes highly effective.

## Approach

The solution utilizes two pointers, `fast` and `slow`, both starting at the head of the list. The `fast` pointer moves through the list at twice the speed of the `slow` pointer. This means that for every increment of the `slow` pointer, the `fast` pointer moves two nodes ahead. The loop continues until the `fast` pointer reaches the end of the list (it becomes `None` or its `next` is `None`), at which point the `slow` pointer will be at the midpoint of the list. This approach efficiently finds the middle node in a single pass through the list, regardless of the total number of nodes.

## Complexity

- Time complexity: $$O(n)$$

  The algorithm traverses the list only once. Despite the `fast` pointer moving at twice the speed, the overall traversal counts as a single pass through the list, making the time complexity linear in terms of the number of nodes in the list.

- Space complexity: $$O(1)$$

  The space complexity is constant because the algorithm uses a fixed amount of space (the two pointers `fast` and `slow`) regardless of the size of the input list.

## Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/description)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)