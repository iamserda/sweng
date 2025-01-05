# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1,list2):
    temp1 = list1
    temp2 = list2
    new_list = Node(0)

    tail = new_list

    while temp1 or temp2:

        if not temp1:
            tail.next = temp2
            tail = tail.next
            temp2 = temp2.next
        elif not temp2:
            tail.next = temp1
            tail = tail.next
            temp1 = temp1.next
        elif temp1.val <= temp2.val:
            tail.next = temp1
            tail = tail.next
            temp1 = temp1.next
        else:
            tail.next = temp2
            tail = tail.next
            temp2 = temp2.next
    
    return new_list.next


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
