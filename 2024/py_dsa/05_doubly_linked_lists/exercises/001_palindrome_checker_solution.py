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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
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
        
    def is_palindrome(self):
        if not self.head:
            return True
        L = self.head
        R = self.tail
        index = 0
        mid = self.length // 2
        while index <= mid:
            if L.value == R.value:
                L = L.next
                R = R.prev
                index += 1
                continue
            return False
        return True




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(2)
my_dll_1.append(1)
assert my_dll_1.is_palindrome() == True

my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)
assert my_dll_1.is_palindrome() == True

my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
assert my_dll_1.is_palindrome() == False


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""