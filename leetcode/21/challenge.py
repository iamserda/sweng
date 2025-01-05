# Definition for singly-linked list.
class Node:
    """Do not modify..."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1,list2):
    """Start Here"""


# Testing Arenas:
def to_list(singly):
    arr = []
    while singly:
        arr.append(singly.val)
        singly = singly.next
    return arr

s1 = Node(1)
s1.next = Node(2)
s1.next.next = Node(4)
assert to_list(s1) == [1,2,4]

s2 = Node(1)
s2.next = Node(3)
s2.next.next = Node(4)
assert to_list(s2) == [1,3,4]


merged_linked = mergeTwoLists(s1, s2)
assert to_list(merged_linked) == [1,1,2,3,4,4]
