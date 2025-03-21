# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        left = 0
        right = len(stack) - 1
        while left <= right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
        return True
