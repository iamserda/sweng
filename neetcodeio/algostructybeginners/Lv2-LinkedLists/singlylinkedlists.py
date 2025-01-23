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
        if self.head and index + 1 <= self.length:
            i = 0
            ptr = self.head
            while ptr:
                if index == i:
                    return ptr.val
                ptr = ptr.next
                i += 1
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
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.length += 1

    def remove(self, index: int) -> bool:
        if not self.head or index >= self.length:
            return False
        elif index == 0:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True
        # for i in range(self.length):
        #     if i + 1 == index:
        #         self.
        return False

    def getValues(self) -> List[int]:
        if not self.head:
            return []
        ptr = self.head
        answer_list = []
        while ptr:
            answer_list.append(ptr.val)
            ptr = ptr.next
        return answer_list
