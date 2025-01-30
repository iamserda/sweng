class Node:
    """Node class with constructor"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicatesUnsorted(head: Node) -> Node:
    """Given the head of a linked list, find all the values that appear more 
    than once in the list and delete the nodes that have any of those values. 
    Return the linked list after the deletions."""
    if not head:
        return
    if not head.next:
        return head

    node = Node(0)
    node.next = head
    temp = head
    hash_counter = {}

    while temp:
        if temp.val not in hash_counter:
            hash_counter[temp.val] = 1
        else:
            hash_counter[temp.val] += 1
        temp = temp.next

    pre = node
    temp = head
    while temp:
        if hash_counter[temp.val] == 1:
            pre = temp
            temp = temp.next
        else:
            pre.next = temp.next
            temp.next = None
            temp = pre.next

    head = node.next
    node.next = None
    return head

def linkedlist_to_arr(head:Node)->list:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Testing Arenas:

#Test 0: PASSED!
head = Node(3)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(2)
head = deleteDuplicatesUnsorted(head=head)
arr = linkedlist_to_arr(head)
assert arr == [4,5]

#Test 1: PASSED!
head = Node(3)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
head = deleteDuplicatesUnsorted(head=head)
arr = linkedlist_to_arr(head)
assert arr == [3,4,5,1,2,0]

#Test 2: FAILED
head = Node(3)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
arr = linkedlist_to_arr(head)
assert arr != [3,4,5,1,2]
