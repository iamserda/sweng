# practice building a min_heap/priority_queue minima


class MinHeap:
    def __init__(self):
        self.heap = [None]

    def get(self):
        return self.heap[1:]

    def push(self, val):
        self.heap.append(val)
        if len(self.heap) >= 2:
            index = len(self.heap) - 1
            while index > 1:
                parent_index = index // 2
                if parent_index >= 1 and self.heap[index] < self.heap[parent_index]:
                    self.heap[index], self.heap[parent_index] = (
                        self.heap[parent_index],
                        self.heap[index],
                    )
                    index = parent_index
                    continue
                break
        return self.heap[1:]


mh = MinHeap()
print(mh.push(10))
print(mh.push(15))
print(mh.push(9))
assert mh.get() == [9, 15, 10]
