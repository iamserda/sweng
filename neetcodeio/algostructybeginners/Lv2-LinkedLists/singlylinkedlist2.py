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
        pass

    def insertTail(self, val: int) -> None:
        pass

    def remove(self, index: int) -> bool:
        pass

    def getValues(self) -> list[int]:
        values = []
        if self.head:
            temp = self.head
            while temp:
                values.append(temp.val)
                temp = temp.next
        return values

singly = LinkedList()
singly.head = Node(1)
singly.tail = singly.head
singly.length = 1
print(singly.get(1))
print(singly.getValues())
