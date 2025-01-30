class Node:
    """Node class with constructor"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def deleteDuplicatesUnsorted(head: Node) -> Node:
    """Given the head of a linked list, find all the values that appear more 
    than once in the list and delete the nodes that have any of those values. 
    Return the linked list after the deletions."""
    
    
    
# Testing Arenas: DO NOT CHANGE any code below!
def linkedlist_to_arr(head:Node)->list:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

#Test 0: PASSED!
head = Node(3)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(2)
head = deleteDuplicatesUnsorted(head=head)
arr = linkedlist_to_arr(head)
try:
    assert arr == [4,5], f"Failed! -> output: {arr}, expected: [4,5]."
except Exception as err:
    print(err)
    pass

#Test 1: PASSED!
head = Node(3)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
head = deleteDuplicatesUnsorted(head=head)
arr = linkedlist_to_arr(head)
try:
    assert arr == [3,4,5,1,2,0], f"Failed! -> output: {arr}, expected: [3,4,5,1,2,0]."
except Exception as err:
    print(err)
    pass