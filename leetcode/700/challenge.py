class Node:
    def __init__(self, val: int):


class MyLinkedList:

    def __init__(self):
        """"""
        
    def get(self, index: int) -> int:
        """"""

    def addAtHead(self, val: int) -> None:
        """"""

    def addAtTail(self, val: int) -> None:
        """"""

    def addAtIndex(self, index: int, val: int) -> None:
        """"""

    def deleteAtIndex(self, index: int) -> None:
        """"""

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

#TESTING ARENA:

h = MyLinkedList()
h.addAtHead(7)
h.addAtHead(2)
h.addAtHead(1)
h.addAtIndex(3,0)
h.deleteAtIndex(2)
h.addAtHead(6)
h.print_all()
h.addAtTail(4)
h.print_all()
h.get(4)
h.addAtHead(4)
h.print_all()
h.addAtIndex(5,0)
h.print_all()
h.addAtHead(6)
h.print_all()

#output sequence
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