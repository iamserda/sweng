class Node:
    def __init__(self, val: int):
        pass


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int):
        pass

    def addAtHead(self, val: int):
        pass

    def addAtTail(self, val: int):
        pass

    def addAtIndex(self, index: int, val: int):
        pass

    def deleteAtIndex(self, index: int):
        pass

    def print_all(self):
        arr = []
        """For testing purposes"""
        temp = self.head
        count = 0
        while temp:
            arr.append(temp.val)
            temp = temp.next
            count += 1
        print(arr, len(arr))
        return arr


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
