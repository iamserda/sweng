### 4. Queues

#### README for Queues

Queues are a fundamental data structure that operate in a FIFO (first in, first out) manner, akin to a line of people waiting for a service where the first person to line up is the first to be served. This structure has two main operations: enqueue, which adds an element to the end of the queue, and dequeue, which removes the element from the front of the queue. Queues are widely used in computer science for managing tasks in schedulers, buffering, and breadth-first search algorithms.

##### Key Operations
- **Enqueue (Insertion)**: O(1)
- **Dequeue (Removal)**: O(1)
- **Peek (Front/Back)**: O(1)
- **Search**: O(n)

##### Use Cases
- Handling asynchronous data (e.g., in web servers for incoming requests).
- Implementing breadth-first search (BFS) in graphs.
- Queueing systems for printers or task scheduling.

##### Python Implementation
```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def print_queue(self):
        for item in self.items:
            print(item, end=" <- ")
        print("End")

# Example usage
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.print_queue()  # Output: A <- B <- C <- End
print("Front:", queue.peek())  # Output: Front: A
queue.dequeue()
queue.print_queue()  # Output: B <- C <- End
```

#### Further Steps
- Implement queues using linked lists or circular arrays to optimize for different use cases.
- Explore variations like priority queues, where elements are processed based on their priority rather than their insertion order.

Queues offer a straightforward yet versatile way to manage data in a FIFO manner, essential in scenarios where order and timing are crucial.