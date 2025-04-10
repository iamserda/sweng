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

    def pop(self):
        def swap(heap: list, parent_index: int, child_index: int):
            heap[parent_index], heap[child_index] = (
                heap[child_index],
                heap[parent_index],
            )

        if len(self.heap) == 1:
            print("EmptyHeapError: This binary heap is empty!")
            return
        elif len(self.heap) == 2:
            return self.heap.pop()

        current_index = 1
        last_index = len(self.heap) - 1
        self.heap[current_index], self.heap[last_index] = (
            self.heap[last_index],
            self.heap[current_index],
        )
        temp = self.heap.pop()
        heap_size = len(self.heap) - 1
        if heap_size > 1:
            while current_index <= heap_size:
                child1_index = current_index * 2
                child2_index = child1_index + 1
                if child2_index <= heap_size:
                    min_index = (
                        child1_index
                        if self.heap[child1_index] <= self.heap[child2_index]
                        else child2_index
                    )
                    swap(self.heap, current_index, min_index)
                    current_index = min_index
                    continue
                elif (
                    child1_index <= heap_size
                    and self.heap[child1_index] < self.heap[current_index]
                ):
                    swap(self.heap, current_index, child1_index)
                    current_index = child1_index
                    continue
                else:
                    break
        return temp


# TESTING ARENA
bheap = BinaryHeap()
bheap.insert(5)
print("insert(5):", bheap)  # insert(5): [None, 5]
bheap.insert(2)
print("insert(2):", bheap)  # insert(2): [None, 2, 5]
bheap.insert(1)
print("insert(1):", bheap)  # insert(1): [None, 1, 5, 2]
bheap.pop()
print("pop():", bheap)  # pop(): [None, 2, 5]
bheap.pop()
print("pop():", bheap)  # pop(): [None, 2]
bheap.pop()
print("pop():", bheap)  # pop(): [None]
bheap.pop()
print("pop():", bheap)  # EmptyHeapError: This binary heap is empty! >> pop(): [None]
