class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self, head):
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverse_list(head.next)
            head.next.next = head
        head.next = None
        return new_head

    def get_values(self):
        values = []
        temp = self.head
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values

# Test Arena:

newLL = LinkedList()
newLL.head = Node(1)
newLL.head.next = Node(2)
newLL.head.next.next = Node(3)
print(newLL.get_values())
newLL.head = newLL.reverse_list(newLL.head)
print(newLL.get_values())
