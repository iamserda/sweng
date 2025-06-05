class Heap:
    def __init__(self, max=False):
        self.container = [None]
        self.max = max

    def insert(self, value):
        self.container.append(value)
        self.bubble_up(len(self.container) - 1)

    def bubble_up(self, _index):
        if _index >= len(self.container) or _index < 1:
            # out of range
            return

        p_index = _index // 2
        while (
            p_index >= 1
            and _index >= 1
            and self.container[_index] < self.container[p_index]
        ):
            # swap value at _index with its parent at p_index
            self.container[_index], self.container[p_index] = (
                self.container[p_index],
                self.container[_index],
            )
            # set parent index as the new child index
            _index = p_index
            # calculate the parent's index
            p_index = _index // 2

    def remove(self):
        if len(self.container) == 1:
            return
        if len(self.container) == 2:
            return self.container.pop()
        # swap index 1 with last index
        start = 1
        end = len(self.container) - 1
        self.container[start], self.container[end] = (
            self.container[end],
            self.container[start],
        )
        removed_val = self.container.pop()
        self.percolate()
        return removed_val

    def percolate(self, index=1):
        left = index * 2
        last_index = len(self.container) - 1

        if left > last_index:
            return

        if left + 1 > last_index:
            if self.container[left] < self.container[index]:
                self.container[left], self.container[index] = (
                    self.container[index],
                    self.container[left],
                )
            return

        smaller_child_index = (
            left if self.container[left] < self.container[left + 1] else left + 1
        )
        if self.container[smaller_child_index] < self.container[index]:
            self.container[smaller_child_index], self.container[index] = (
                self.container[index],
                self.container[smaller_child_index],
            )
            index = smaller_child_index
            return self.percolate(index)


min_heap = Heap(max=False)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(3)
min_heap.insert(1)
print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print("pre:", min_heap.container[1:])
min_heap.remove()
print("post:", min_heap.container[1:])

print(min_heap.container)
