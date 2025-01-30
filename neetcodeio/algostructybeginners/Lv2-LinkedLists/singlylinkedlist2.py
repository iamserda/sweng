"""Challenge: Design a Singly-Linked Lists with the following methods: get, insertHead, insertTail, remove and getValues."""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= 0 and index < self.length:
            temp = self.head
            for i in range(self.length):
                if i == index:
                    return temp.val
                temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        elif self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        elif self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove(self, index: int) -> Node:
        if self.length == 0 or index < 0 or index >= self.length:
            return (
                ValueError("Empty Error!")
                if self.length == 0
                else IndexError(f"Index {index} is NOT VALID!")
            )

        temp = self.head
        counter = 0
        while temp:
            if index == counter == 0:
                removed = self.head
                self.head = self.head.next
                removed.next = None
                self.length -= 1
                if self.length == 0:
                    self.tail = None
                return removed

            if counter + 1 == index:
                if temp.next:
                    removed = temp.next
                    temp.next = removed.next
                    removed.next = None
                    self.length -= 1
                    if removed == self.tail:
                        self.tail = temp
                    return removed
            temp = temp.next
            counter += 1

    def getValues(self) -> list[int]:
        values = []
        temp = self.head
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values


singly = LinkedList()
singly.insertHead(1)
singly.insertTail(2)
singly.insertTail(3)
assert singly.get(0) == 1
assert singly.get(1) == 2
assert singly.get(2) == 3
assert singly.get(3) == -1
