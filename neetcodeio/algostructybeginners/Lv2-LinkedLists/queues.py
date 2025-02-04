"""
title: Design a Doube-Ended Queue
url: https://neetcode.io/problems/queue
owner: neetcode.io
desicription: double-ended queue using a doubly-linked-list
solver: @iamserda
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prv = None
        self.nxt = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prv = self.tail
            self.tail.nxt = new_node
            self.tail = self.tail.nxt

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.nxt = self.head
            self.head.prv = new_node
            self.head = new_node

    def pop(self) -> int:
        if self.tail:
            removed = self.tail
            if self.tail.prv:
                self.tail = self.tail.prv
                self.tail.nxt = None
                removed.prv = None
            else:
                self.head = self.tail = None
            return removed.val
        return -1

    def popleft(self) -> int:
        if not self.head:
            return -1
        if self.head == self.tail:
            removed = self.head
            self.head = self.tail = None
            return removed.val
        removed = self.head
        self.head = self.head.nxt
        self.head.prv = None
        removed.nxt = None
        return removed.val


# Testing Arena:
myQueue = Deque()
mydict = {
    "append": myQueue.append,
    "appendLeft": myQueue.appendleft,
    "isEmpty": myQueue.isEmpty,
    "pop": myQueue.pop,
    "popLeft": myQueue.popleft,
}

# transactions
transactions = [
    ("isEmpty", None),
    ("append", 10),
    ("isEmpty", None),
    ("appendLeft", 20),
    ("popLeft", None),
    ("pop", None),
    ("pop", None),
    ("append", 30),
    ("pop", None),
    ("isEmpty", None),
]

# Output:
expected = [True, None, False, None, 20, 10, -1, None, 30, True]
output = []

for transaction in transactions:
    if isinstance(transaction, tuple):
        method = mydict[transaction[0]]
        param = transaction[1]
        if param:
            output.append(method(param))
        else:
            output.append(method())
    else:
        raise TypeError(
            "Wrong datatype: expecting either of string or a tuple of size 2."
        )
if len(expected) == len(output):
    results = True
    for index in range(len(expected)):
        assert expected[index] == output[index]
