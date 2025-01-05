from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self.first
    
    def dequeue(self):
        if not self.first:
            return
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.last = None
        return temp
    
    def queue_to_arr(self):
        arr = []
        temp = self.first
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return arr

# Testing Arenas
new_queue = Queue()
new_queue.enqueue(8)
new_queue.enqueue(9)
new_queue.enqueue(10)
new_queue.dequeue()
new_queue.enqueue(11)
new_queue.dequeue()
new_queue.enqueue(12)
new_queue_arr = new_queue.queue_to_arr()
print(new_queue_arr)