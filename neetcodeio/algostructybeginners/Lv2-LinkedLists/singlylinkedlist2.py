"""Challenge: Design a Singly-Linked Lists with the following methods: get, insertHead, insertTail, remove and getValues.
"""


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

    def remove(self, index: int) -> bool:
        if self.length == 0 or index < 0 or index >= self.length:
            return False

        temp = self.head
        counter = 0
        while temp:
            if index == 0 and counter == index:
                self.head = self.head.next
                self.length -= 1
                if self.length == 0:
                    self.tail = None
                return True

            if counter + 1 == index:
                if temp.next:
                    rm_node = temp.next
                    temp.next = rm_node.next
                    rm_node.next = None
                    self.length -= 1
                    if rm_node == self.tail:
                        self.tail = temp
                    return True
            temp = temp.next
            counter += 1
        return False

    def getValues(self) -> list[int]:
        values = []
        if self.head:
            temp = self.head
            while temp:
                values.append(temp.val)
                temp = temp.next
        return values

singly = LinkedList()
singly.insertHead(1)
singly.remove(0)
print(singly.getValues())
