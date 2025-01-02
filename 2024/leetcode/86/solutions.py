# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Initialize heads and tails for two lists
    pre_head = pre_tail = post_head = post_tail = None
    
    current = head
    while current:
        next_node = current.next  # Save next node
        current.next = None  # Break the link to ensure clean partitioning
        
        if current.val < x:
            if not pre_head:  # Initialize pre list
                pre_head = pre_tail = current
            else:
                pre_tail.next = current
                pre_tail = current
        else:
            if not post_head:  # Initialize post list
                post_head = post_tail = current
            else:
                post_tail.next = current
                post_tail = current
                
        current = next_node  # Move to the next node
    
    # Connect the two lists
    if pre_tail:
        pre_tail.next = post_head
        return pre_head
    else:
        return post_head


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