from random import randint


class Heap:
    def __init__(self):
        self.root = [None]

    def insert(self, value):
        self.root.append(value)
        if len(self.root) == 2:
            return
        node_idx = len(self.root) - 1
        parent_idx = node_idx // 2
        while parent_idx >= 1 and self.root[node_idx] < self.root[parent_idx]:
            self.root[node_idx], self.root[parent_idx] = (
                self.root[parent_idx],
                self.root[node_idx],
            )
            node_idx = parent_idx
            parent_idx = node_idx // 2
        return self.root


heap = Heap()
for i in [randint(1, 100) for i in range(7)]:
    print(heap.insert(i))
