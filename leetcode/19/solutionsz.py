# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head:list, n: int) ->list:
        fast = head
        slow = head
        length = 1

        if head is None:
            return head
        if n == 1:
            if not head.next:
                temp = head
                head = head.next
                return head
        
        for i in range(n):
            fast = fast.next
            if fast:
                length += 1

        while fast and fast.next:
            length += 1
            fast = fast.next
            slow = slow.next
        
        # how we remove the 1st item.
        if n == length:
            temp = head
            head = head.next
            return head

        temp = slow.next
        slow.next = temp.next
        temp.next = None
        return head