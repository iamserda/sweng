# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        pre = ListNode(-1)
        current = pre
        temp1 = list1
        temp2 = list2
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
