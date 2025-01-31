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
            counter = 0
            while temp:
                if counter == index:
                    return temp.val
                temp = temp.next
                counter += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove(self, index: int) -> bool:
        if self.head and index < self.length:
            counter = 0
            temp = self.head
            while temp:
                if counter == 0 and index == counter:
                    self.head = temp.next
                    self.length -= 1
                    temp.next = None
                    if self.length == 0:
                        self.tail = None
                    return True
                elif counter + 1 == index:
                    removed = temp.next
                    if removed:
                        temp.next = removed.next
                        removed.next = None
                        self.length -= 1
                        if removed == self.tail:
                            self.tail = temp
                        return True
                temp = temp.next
                counter += 1
        return False

    def getValues(self) -> List[int]:
        temp = self.head
        values = []
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values


singly = LinkedList()
singly.insertHead(1)
print(singly.getValues())
