class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int = 0) -> int:
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for counter in range(self.length):
            if counter == index:
                return temp.val
            temp = temp.next
        return -1

    def get_values(self):
        values = []
        temp = self.head
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values

    def prepend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            self.length += 1

    def insert_at(self, val, index):
        new_node = Node(val)
        if index >= 0 and index < self.length:
            temp = self.head
            counter = 0
            while temp:
                if counter + 1 == index:
                    new_node.next = temp.next
                    temp.next.prv = new_node
                    new_node.prv = temp
                    temp.next = new_node
                    return True
                temp = temp.next
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return IndexError(f"Index: {index} is NOT VALID")
        # remove head node
        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            removed.next = None
            if self.tail == removed:
                self.tail = None
            self.length -= 1
            return removed
        temp = self.head
        counter = 0
        while temp and temp.next:
            if counter + 1 == index:
                removed = temp.next
                temp.next = removed.next
                if temp.next:
                    temp.next.prev = temp
                if removed == self.tail:
                    self.tail = removed.prev
                removed.prev = None
                removed.next = None
                self.length -= 1
                return removed
            temp = temp.next
            counter += 1


# TESTING ARENA:

dll = DoublyLinkedList()
dll.append(0)
print(dll.get_values())
dll.append(1)
print(dll.get_values())
dll.append(2)
print(dll.get_values())
dll.append(3)
print(dll.get_values())
dll.append(4)
print(dll.get_values())
dll.append(5)
print(dll.get_values())


def test_remove(index):
    removed_node = dll.remove(index)
    print(f"removed: {removed_node.val}")
    print(dll.get_values())


for i in range(-1, 7, 1):
    removed_node = dll.remove(i)
    if isinstance(removed_node, Node):
        dll.prepend(f"x{i}")
        print(f"removed: {removed_node.val}")
        print(dll.get_values())
    else:
        print(removed_node)

temp = dll.head
while temp:
    print(temp.val)
    temp = temp.next
