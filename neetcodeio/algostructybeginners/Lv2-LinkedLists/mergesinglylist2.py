class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


# TESTING ARENA:
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
