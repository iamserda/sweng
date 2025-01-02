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
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.value == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.value == key:
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

## Code Walk-through

Sure, let's walk through the code piece by piece. This Python script defines a simple implementation of a singly linked list using two classes: `ListNode` and `LinkedList`.

### `ListNode` Class

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
```

- The `ListNode` class is designed to represent a node in a linked list.
- Each node has two attributes:
  - `value`: Stores the data of the node. It defaults to `0` if no value is provided.
  - `next`: A pointer to the next node in the list. It defaults to `None`, indicating the end of the list or that the node is not linked.

### `LinkedList` Class

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

- The `LinkedList` class represents the linked list itself.
- It has a single attribute, `head`, which points to the first node in the list. Initially, this is `None`, indicating the list is empty.

#### `insert_at_beginning` Method

```python
def insert_at_beginning(self, value):
    new_node = ListNode(value)
    new_node.next = self.head
    self.head = new_node
```

- This method inserts a new node at the beginning of the list.
- A new `ListNode` is created with the given `value`.
- The new node's `next` pointer is set to the current `head` of the list, effectively placing it at the beginning.
- The `head` of the list is then updated to point to this new node.

#### `insert_at_end` Method

```python
def insert_at_end(self, value):
    new_node = ListNode(value)
    if not self.head:
        self.head = new_node
        return
    last = self.head
    while last.next:
        last = last.next
    last.next = new_node
```

- This method inserts a new node at the end of the list.
- If the list is empty (`self.head` is `None`), the new node becomes the head of the list.
- Otherwise, it iterates through the list to find the last node (where `last.next` is `None`) and sets `last.next` to the new node.

#### `delete_node` Method

```python
def delete_node(self, key):
    temp = self.head
    if temp is not None:
        if temp.value == key:
            self.head = temp.next
            temp = None
            return
    while temp is not None:
        if temp.value == key:
            break
        prev = temp
        temp = temp.next
    if temp == None:
        return
    prev.next = temp.next
    temp = None
```

- This method removes a node from the list by its `value`.
- First, it checks if the node to delete is the head of the list. If so, it updates the head to the next node.
- If the node is not the head, it searches through the list to find the node with the matching `value`.
- Once found, it bypasses the node to be deleted by setting `prev.next` to `temp.next`, effectively removing the node from the list.

#### `print_list` Method

```python
def print_list(self):
    temp = self.head
    while temp:
        print(temp.value, end=" -> ")
        temp = temp.next
    print("None")
```

- This method prints the values of the nodes in the list from the head to the end, followed by `None` to indicate the end of the list.

### Example Usage

The example at the end of the script demonstrates creating a `LinkedList` object, inserting nodes at the beginning and end of the list, printing the list, deleting a node, and printing the list again to show the updated structure.

This walkthrough should give you a clear understanding of how the linked list implementation works in this code.