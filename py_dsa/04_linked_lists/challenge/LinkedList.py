from Node import Node


class LinkedList:
    """Class representing the ADT: Linked-List"""

    def __init__(self, value):
        """Constructor"""

    def append(self, value):
        """ Insert a new Node at the end of the Linked List"""

    def prepend(self, value):
        """ Insert a value at the beginning of the LinkedList"""

    def insert(self, value, index):
        """ Creates a new node, and inserts it at a desired index."""

    def pop(self):
        """Removes the last Node from the Linked-List and returns it. Returns None if there aren't any Nodes in LinkedList."""

    def pop_first(self):
        """method: pop: removes the last Node from the Linked-List and returns it to the caller. Returns None when there are no Nodes."""

    def get(self, index):
        """Returns the Node at a given index"""

    def set(self, index, value):
        """Updates the value of a Node at a given valid index."""

    def insert2(self, index, value):
        """ Creates a new node, and inserts it at a desired index."""

    def remove(self, index):
        """Removes a Node from a specified index."""

    def print_all_nodes(self):
        """Prints a list representation of all the nodes."""

    def reverse_all(self):
        """ Reverse a linked-list."""

    def reorder(self, start_index: int, end_index: int) -> None:
        """Given two indices, """


# Tests Arena
myLL = LinkedList(12)  # [12]
myLL.append(13)  # [12,13]
myLL.prepend(10)  # [10,11,13]
myLL.insert(11, 1)  # [10,11,12,13]
myLL.insert(11, -1)  # NOCHANGE: [10,11,12,13]
myLL.insert(11, 4)  # NOCHANGE: [10,11,12,13]
myLL.remove(1)  # [10,12,13] returns 11
myLL.remove(11)  # NOCHANGE [10,11,12,13]
myLL.pop()  # [10,12] returns 13
myLL.pop_first()  # [12] returns 10
node = myLL.get(0)  # [12]
myLL.print_all_nodes()
print(myLL.get(-10))  # None
print(myLL.get(10))  # None
myLL.set(0, 23)  # [12] >> [23]
print(myLL.set(-10, 20))  # NOCHANGE
print(myLL.set(10, 23))  # NOCHANGE
myLL.append(24)  # [23,24]
myLL.insert(10, 1)  # [23,10,24]
myLL.print_all_nodes()
myLL.reverse_all()  # [24, 10, 23]
myLL.append(3)  # [24, 10, 23, 3]
myLL.insert(32, 1)  # [24, 32, 10, 23, 3]
myLL.reverse_all()  # [3, 23, 10, 32, 24]
myLL.append(myLL.pop_first().value)  # [23, 10, 32, 24, 3]
myLL.insert(6, 1)  # [23, 6, 10, 32, 24, 3]
myLL.print_all_nodes()
myLL.reorder(0, 5)  # [3, 24, 32, 10, 6, 23]
myLL.print_all_nodes()
myLL.reorder(1, 5)  # [3, 23, 6, 10, 32, 24]
myLL.print_all_nodes()
myLL.reorder(10, 50)  # NOCHANGE
myLL.print_all_nodes()
myLL.reorder(-1, -5)  # NOCHANGE
myLL.print_all_nodes()
myLL.reorder(4, 1)  # NOCHANGE
