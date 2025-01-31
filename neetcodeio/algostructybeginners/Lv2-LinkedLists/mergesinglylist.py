<<<<<<< HEAD
"""
Problem: 
Given the head pointer to two sorted linked list, merge the two sorted linked-list,
to result in a sorted linked. return the head of the newly sorted linked-list.
"""

=======
# Definition for singly-linked list.
>>>>>>> 6c8d8ed (solved: leetcode #21, neetcode merge-two-sorted-list -@iamserda)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
<<<<<<< HEAD

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
=======
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

>>>>>>> 6c8d8ed (solved: leetcode #21, neetcode merge-two-sorted-list -@iamserda)
        pre = ListNode(-1)
        current = pre
        temp1 = list1
        temp2 = list2
<<<<<<< HEAD
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                current.next = temp1
                temp1 = temp1.next
                current = current.next
                current.next = None
            else:
                current.next = temp2
                temp2 = temp2.next
                current = current.next
                current.next = None
        if temp1 or temp2:
            current.next = temp1 if temp1 else temp2
        return pre.next if pre.next else None


# TESTING ARENA:
=======
        while temp1 or temp2:
            if temp1:
                if temp2:
                    if temp1.val <= temp2.val:
                        node = temp1
                        temp1 = temp1.next
                        node.next = None
                        current.next = node
                        current = current.next
                        continue
                    node = temp2
                    temp2 = temp2.next
                    node.next = None
                    current.next = node
                    current = current.next
                    continue
                node = temp1
                temp1 = temp1.next
                node.next = None
                current.next = node
                current = current.next
                continue
            if temp2:
                node = temp2
                temp2 = temp2.next
                node.next = None
                current.next = node
                current = current.next
                continue
        return pre.next if pre.next else None


>>>>>>> 6c8d8ed (solved: leetcode #21, neetcode merge-two-sorted-list -@iamserda)
s1 = ListNode(11)
s1.next = ListNode(32)
s1.next.next = ListNode(53)

s2 = ListNode(20)
s2.next = ListNode(41)
s2.next = ListNode(63)

# Testing:
sol = Solution()
singly = sol.mergeTwoLists(s1, s2)
answer = []
while singly:
    answer.append(singly.val)
    singly = singly.next
print(answer)
