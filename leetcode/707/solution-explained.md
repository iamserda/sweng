# [Implement MyLinkedList](https://example.com/)

## Intuition
When tasked with implementing a linked list from the ground up, the immediate thought is to capture the essence of a linked list's structure and operations. The focus is on creating a flexible, efficient data structure that allows dynamic insertion and deletion of elements. The primary challenge lies in correctly managing pointers to ensure the integrity of the list across various operations.

## Approach
The implementation strategy revolves around defining a `Node` class to represent individual elements in the list and a `MyLinkedList` class for managing the list. Key operations include:

- **Initialization**: Set up an initially empty list, characterized by a `head` and `tail` pointer, and a `length` counter for tracking the list's size.
- **Add at Head**: Insert a new element at the beginning of the list, adjusting the `head` pointer and handling edge cases for an initially empty list.
- **Add at Tail**: Append a new element at the end, utilizing the `tail` pointer for efficient access.
- **Add at Index**: Insert a new element at a specified position, which involves traversing the list to the correct location before insertion.
- **Delete at Index**: Remove an element from a specified position, with special attention to maintaining list integrity when removing the head or tail.
- **Get**: Retrieve the value of an element at a specified index by traversing the list from the head.

## Complexity

- Time complexity:
  - For operations requiring traversal (`get`, `addAtIndex`, and `deleteAtIndex`), the worst-case time complexity is $$O(n)$$, where `n` is the length of the list.
  - For operations that modify the head or tail directly (`addAtHead`, `addAtTail`), the time complexity is $$O(1)$$.
- Space complexity: $$O(n)$$, where `n` is the number of elements in the list. This accounts for the space needed to store each node.

## Code
The provided code snippet defines the `MyLinkedList` class and its associated methods, showcasing how to implement fundamental linked list operations in Python.
```python
class Node:
    def __init__(self, val: int):
        self. val = val
        self. next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        temp = self.head
        while temp:
            if i == index:
                return temp.val
            else:
                temp = temp.next
                i += 1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1



    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            return self.addAtHead(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return -1
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)
        new_node = Node(val)
        i = 0
        temp = self.head
        while temp:
            if i == index - 1:
                break
            else:
                temp = temp.next
                i += 1
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return
        i = 0
        prev = self.head
        while prev:
            if i == index - 1:
                break
            else:
                prev = prev.next
                i += 1
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        if temp == self.tail:
            self.tail = prev
    def print_all(self):
        temp = self.head
        i = 0
        while temp:
            print(temp.val)
            temp = temp.next
            i += 1
        print(f"Length: {self.length}")
```

### Follow-up
The follow-up question regarding an algorithm that runs in $$O(m + n)$$ time seems unrelated to the linked list implementation. Such complexity often pertains to problems involving the merging or comparison of two lists or arrays, where `m` and `n` represent their respective sizes. This might have been included by mistake or requires additional context to address appropriately.

### Credit, Source, Etc

- Source: [LeetCode](url-path)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)