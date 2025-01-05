 # 3. Stacks

#### README for Stacks

Stacks are a type of abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element that was not yet removed. The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out). Additionally, many stack implementations have a top operation to look at the last element added without removing it. Stacks are fundamentally important, as they can be used to reverse the order of elements and are pivotal in numerous algorithms.

##### Key Operations
- **Push (Insertion)**: O(1)
- **Pop (Deletion)**: O(1)
- **Top (Peek)**: O(1)
- **Search**: O(n) - Searching for an element not knowing the last pushed item.

##### Use Cases
- Backtracking algorithms (e.g., navigating through browser history).
- Syntax parsing (e.g., compilers and calculators).
- Calling functions (Call Stack in programming languages).

##### Python Implementation
```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        for item in reversed(self.items):
            print(item)

# Example usage
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.print_stack()  # Output: C B A
print("Top:", stack.peek())  # Output: Top: C
stack.pop()
stack.print_stack()  # Output: B A
```

#### Further Steps
- Explore implementing stacks using linked lists to optimize for space usage.
- Investigate applications of stacks in more complex algorithms, such as Depth-First Search (DFS) in graph theory.