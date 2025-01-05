class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def to_list(self):
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return arr

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    def reverse(self):
        """Start here:"""

doubly = DoublyLinkedList(1)
doubly.append(2)
doubly.append(3)
doubly.append(4)
doubly.append(5)
assert doubly.to_list() == [1,2,3,4,5]
doubly.reverse()
assert doubly.to_list() == [5,4,3,2,1]