class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def to_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(current_node.value)
            current_node = current_node.next
        return output
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        swap = self.head

        while swap and swap.next:
            
            
        

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
print(my_dll.to_list())
# assert my_dll.to_list() == [1,2,3,4]
my_dll.swap_pairs()
print(my_dll.to_list())
# assert my_dll.to_list() == [2,1,4,3]

pre = my_dll.head.next.next
while pre:
    print(str(pre.value))
    pre = pre.prev
nxt = my_dll.head
# while nxt:
#     print(nxt.value)
#     nxt = nxt.next

"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""