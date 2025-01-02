class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        temp = self.head
        while temp:
            if i == index:
                return temp.val
            else:
                temp = temp.next
                i += 1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            return self.addAtHead(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return -1
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)
        new_node = Node(val)
        i = 0
        temp = self.head
        while temp:
            if i == index - 1:
                break
            else:
                temp = temp.next
                i += 1
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return
        i = 0
        prev = self.head
        while prev:
            if i == index - 1:
                break
            else:
                prev = prev.next
                i += 1
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        if temp == self.tail:
            self.tail = prev

    def print_all(self):
        arr = []
        """For testing purposes"""
        temp = self.head
        i = 0
        while temp:
            arr.append(temp.val)
            temp = temp.next
            i += 1
        print(arr)
        print(len(arr))


# TESTING ARENA:

h = MyLinkedList()
h.addAtHead(7)
h.addAtHead(2)
h.addAtHead(1)
h.addAtIndex(3, 0)
h.deleteAtIndex(2)
h.addAtHead(6)
h.print_all()
h.addAtTail(4)
h.print_all()
h.get(4)
h.addAtHead(4)
h.print_all()
h.addAtIndex(5, 0)
h.print_all()
h.addAtHead(6)
h.print_all()

# output sequence
# [[],
# [7],
# [2,7],
# [1,2,7],
# [1,2,7,0],
# [1,2,0],
# [6,1,2,0],
# [6,1,2,0,4],
# "4",
# [4,6,1,2,0,4],
# [4,6,1,2,0,0,4],
# [6,4,6,1,2,0,0,4]]
