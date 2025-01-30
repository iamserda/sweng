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
        arr = list()
        current = self.head
        while current:
            arr.append(current)
            current = current.next
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
    
    def swap_first_last_nodes(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            return self
        
        new_tail = self.pop_first()
        new_head = self.pop()
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head
        self.length += 1
        
        self.tail.next = new_tail
        new_tail.prev = self.tail
        self.tail = new_tail
        self.length += 1
        return self