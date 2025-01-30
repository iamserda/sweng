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

    def find_kth_from_end(self, k):
        """Returns the node a Kth position from the tail-end of the Linked-List."""
        fast = self.head
        slow = self.head

        if self.head is None:
            return None

        for i in range(1, k):
            fast = fast.next
            if fast is None:
                return None

        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
assert my_linked_list.find_kth_from_end(k).value == 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
