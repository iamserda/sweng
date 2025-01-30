# Linked Lists(Singly)

## README for Linked Lists

Linked Lists are a fundamental data structure consisting of a sequence of elements, each contained in a "node". The node holds a value and a pointer to the next node in the sequence. This structure allows for efficient insertion and deletion of elements as it doesn't require the elements to be stored in contiguous memory locations.

## Key Operations
- **Access**: O(n)
- **Insertion/Deletion at the beginning**: O(1)
- **Insertion/Deletion at the end**: O(n) for a singly linked list, O(1) for a doubly linked list with a tail pointer
- **Search**: O(n)

## Use Cases
- When you need constant-time insertions/deletions from the list (e.g., stack/queue implementations).
- When you don't know the memory size required for your data in advance.
- Implementing graphs.

## Python Implementation
```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beginning(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
            self.length = 1
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert_at_end(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
            self.length = 1
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = self.tail.next
        self.length += 1

    def delete_node(self, index):
        if index == 0:
            temp = self.head
            self.head = self.head.next
            
        temp = Node(0)
        temp.next = self.head


        while temp.next is not None:
            if temp.next.value == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
llist = LinkedList()
llist.insert_at_beginning(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.print_list()  # Output: 1 -> 2 -> 3 -> None
llist.delete_node(2)
llist.print_list()  # Output: 1 -> 3 -> None
```

## Further Steps
- Experiment with doubly linked lists, where each node has a pointer to both the next and previous nodes.
- Try implementing a circular linked list where the last element points back to the first element.