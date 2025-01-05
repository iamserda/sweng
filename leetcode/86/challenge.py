# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def partition(self, head: list, x: int)->list:
        """Write solution here!"""


# Test Arenas:
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

result = partition(head, 3) # expected output: [1,2,2,4,3,5]
arr_output = []
temp = result
while temp:
    arr_output.append(temp.val)
    temp = temp.next

assert arr_output == [1,2,2,4,3,5]