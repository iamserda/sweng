from node import Node


class LinkedList:
    """Class representing the ADT: Linked-List"""

    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length = 1

    def append(self, value):
        """ Insert a new Node at the end of the Linked List"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self.head
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return self.head

    def prepend(self, value):
        """ Insert a value at the beginning of the LinkedList"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def insert(self, value, index):
        """ Creates a new node, and inserts it at a desired index."""
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        temp_ptr = self.head
        for i in range(0, self.length):
            if i + 1 == index:
                new_node.next = temp_ptr.next
                temp_ptr.next = new_node
                self.length += 1
                break
            temp_ptr = temp_ptr.next
        temp_ptr = None  # clear temp_ptr
        return self.head

    def pop(self):
        """Removes the last Node from the Linked-List and returns it. Returns None if there aren't any Nodes in LinkedList."""
        temp = self.head
        if not self.length:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = self.head
        while temp.next:
            if temp.next == self.tail:
                self.tail = temp
                temp = temp.next
                self.tail.next = None
                break
            temp = temp.next
        self.length -= 1
        return temp

    def pop_first(self):
        """method: pop: removes the last Node from the Linked-List and returns it to the caller. Returns None when there are no Nodes."""
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        if temp == self.tail:
            self.tail = self.head
        self.length -= 1
        return temp

    def get(self, index):
        """Returns the Node at a given index"""
        if index < 0 or index >= self.length:
            return None
        i = 0
        temp = self.head
        while temp:
            if i == index:
                return temp
            else:
                temp = temp.next
                i += 1
        return None

    def set(self, index, value):
        """Updates the value of a Node at a given valid index."""
        node = self.get(index)
        if node:
            node.value = value
            return node
        else:
            return None

    def insert2(self, index, value):
        """ Creates a new node, and inserts it at a desired index."""
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev_node = self.get(index - 1)
        if prev_node:
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1
            return self.head

    def remove(self, index):
        """Removes a Node from a specified index."""
        if index < 0 or index >= self.length or not self.head:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        temp_node = prev_node.next
        prev_node.next = temp_node.next
        temp_node.next = None
        self.length -= 1
        return temp_node

    def print_all_nodes(self):
        """Prints a list representation of all the nodes."""
        my_arr = []
        my_ptr = self.head
        while my_ptr:
            my_arr.append(my_ptr.value)
            my_ptr = my_ptr.next
        print("Linked-List:", my_arr, "Length:", self.length)

    def reverse_all(self):
        """ Reverse a linked-list."""
        if not self.length:
            return None
        if self.head == self.tail:
            return self
        # head tail pointers swap
        self.head, self.tail = self.tail, self.head
        left_ptr = None
        temp_ptr = self.tail
        right_ptr = temp_ptr
        while temp_ptr:
            right_ptr = right_ptr.next
            temp_ptr.next = left_ptr
            left_ptr = temp_ptr
            temp_ptr = right_ptr

    def reorder(self, start_index: int, end_index: int) -> None:
        """Given two indices, """
        if start_index >= self.length and end_index >= self.length:
            return None

        if start_index < 0 or end_index < 0 or end_index < start_index:
            return None

        if start_index == 0 and end_index == self.length - 1:
            return self.reverse_all()

        end_ptr = self.get(end_index)
        if start_index == 0:
            while self.head != end_ptr:
                start_ptr = self.head
                self.head = self.head.next
                start_ptr.next = end_ptr.next
                end_ptr.next = start_ptr
        else:
            prev_ptr = self.get(start_index - 1)
            while prev_ptr.next != end_ptr:
                temp_ptr = prev_ptr.next
                prev_ptr.next = temp_ptr.next
                temp_ptr.next = end_ptr.next
                end_ptr.next = temp_ptr


# Tests Arena
if __name__ == "__main__":
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
