class BinaryHeap:
    def __init__(self):
        self.heap = [None]

    def __str__(self):
        return self.heap.__str__()

    def insert(self, value):
        if value is None:
            return
        self.heap.append(value)
        if len(self.heap) > 2:
            current_index = len(self.heap) - 1
            while current_index > 0:
                parent_index = current_index // 2
                if (
                    parent_index > 0
                    and self.heap[current_index] < self.heap[parent_index]
                ):
                    self.heap[current_index], self.heap[parent_index] = (
                        self.heap[parent_index],
                        self.heap[current_index],
                    )
                    current_index = parent_index
                else:
                    break


bheap = BinaryHeap()
bheap.insert(5)
print(bheap)
bheap.insert(2)
print(bheap)
bheap.insert(1)
print(bheap)
