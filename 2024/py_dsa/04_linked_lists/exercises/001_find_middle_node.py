class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = self.head
        fast = slow.next
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow, slow.next
        return slow



# TESTING AREANAS: 
# For EVEN size linked-list, mid is both len(LL)/2 and len(LL)/2 - 1.
# Here, we are using the first N/2 - 1. 
# But be mindful that in cases of even numbers of elements, 
# the element at index: N/2 -1 and the element at index: N/2 are BOTH middle elements.
my_linked_list = LinkedList(1)
assert my_linked_list.find_middle_node().value == 1
my_linked_list.append(2)
assert [x.value for x in my_linked_list.find_middle_node()] == [1,2]
my_linked_list.append(3)
assert my_linked_list.find_middle_node().value == 2
my_linked_list.append(4)
assert [x.value for x in my_linked_list.find_middle_node()] == [2,3]
my_linked_list.append(5)
assert my_linked_list.find_middle_node().value == 3
my_linked_list.append(6)
assert [x.value for x in my_linked_list.find_middle_node()] == [3,4]
my_linked_list.append(7)
assert my_linked_list.find_middle_node().value == 4


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""