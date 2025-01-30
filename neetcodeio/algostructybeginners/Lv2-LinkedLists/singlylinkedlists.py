class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        temp = self.head
        for i in range(0, self.length):
            if i == index:
                return temp.val
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if not self.head or index >= self.length:
            return False
        counter = 0
        temp = self.head
        if index == counter:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True
        while temp.next:
            if counter + 1 == index:
                node = temp.next
                temp.next = node.next
                node.next = None
                self.length -= 1
                return True
        return False

    def getValues(self) -> list[int]:
        temp = self.head
        values = []
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values


new_list = LinkedList()
print(new_list.get(0))
new_list.insertHead(10)
new_list.insertTail(11)
new_list.insertHead(9)
print(new_list.remove(1))
print(new_list.getValues())
