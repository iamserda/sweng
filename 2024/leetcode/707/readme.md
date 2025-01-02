# 707. Design Linked List

## Difficulty

Medium

## Topics

- Linked List
- Design

## Companies

This type of question can be commonly seen in interviews for companies that are testing for a strong understanding of data structures, such as Google, Amazon, Facebook, and Microsoft.

## Description

Design your implementation of the linked list. You can choose to use either a singly or doubly linked list. A singly linked list node should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node. If you opt for a doubly linked list, you will need an additional attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Gets the value of the `index`-th node in the linked list. If the index is invalid, return `-1`.
- `void addAtHead(int val)` Adds a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- `void addAtTail(int val)` Appends a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Adds a node of value `val` before the `index`-th node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node will not be inserted.
- `void deleteAtIndex(int index)` Deletes the `index`-th node in the linked list, if the index is valid.

### Example

Input:
```plaintext
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
```

Output:
```plaintext
[null, null, null, null, 2, null, 3]
```

Explanation:
- `MyLinkedList myLinkedList = new MyLinkedList();`
- `myLinkedList.addAtHead(1);`
- `myLinkedList.addAtTail(3);`
- `myLinkedList.addAtIndex(1, 2);`    // linked list becomes 1->2->3
- `myLinkedList.get(1);`              // returns 2
- `myLinkedList.deleteAtIndex(1);`    // now the linked list is 1->3
- `myLinkedList.get(1);`              // returns 3

### Constraints

- `0 <= index, val <= 1000`
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex`.

## Approach

Design a linked list class using either singly or doubly linked nodes. For a singly linked list, each node should have `val` and `next` properties, while for a doubly linked list, each node should also have a `prev` property.

### Singly Linked List Implementation

- Implement the constructor to initialize the head of the linked list.
- For `get`, iterate through the list to find the `index`-th node and return its value.
- For `addAtHead`, create a new node and point its `next` to the current head before updating the head to this new node.
- For `addAtTail`, iterate to the end of the list and link the last node's `next` to the new node.
- For `addAtIndex`, find the node before the `index` and adjust the pointers to insert the new node.
- For `deleteAtIndex`, find the node before the `index` and adjust the pointers to exclude the node at the `index`.

### Doubly Linked List Implementation

- Similar to the singly linked list, but also maintain the `prev` pointer for each node for easier insertion and deletion, especially at the tail of the list.

This design challenge tests your ability to implement fundamental operations of linked lists and manage edge cases, such as inserting or deleting at the head or tail of the list.
