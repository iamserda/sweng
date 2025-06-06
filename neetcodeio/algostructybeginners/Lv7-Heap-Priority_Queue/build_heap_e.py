class MinHeap:
    def __init__(self):
        self.container = [None]

    def insert(self, value):
        self.container.append(value)
        child = len(self.container) - 1
        while child > 1:
            parent = child // 2
            if self.container[child] < self.container[parent]:
                # swap values of child and parent indices
                self.container[child], self.container[parent] = (
                    self.container[parent],
                    self.container[child],
                )
                child = parent
                continue
            break

    def remove(self):
        length = len(self.container)
        if length <= 1:
            return
        if length == 2:
            return self.container.pop()

        start = 1
        end = length - 1
        # swap
        self.container[start], self.container[end] = (
            self.container[end],
            self.container[start],
        )
        removed_val = self.container.pop()
        index = start
        end = len(self.container) - 1
        while index <= end:
            left = 2 * index
            right = left + 1
            # true if index is a leaf node
            if left > end:
                break
            # True of this node's left child is the LAST leaf node.
            # checks if we have reached the last parent node,
            if right > end:
                if self.container[left] < self.container[index]:
                    self.container[index], self.container[left] = (
                        self.container[left],
                        self.container[index],
                    )
                break
            smaller = left if self.container[left] <= self.container[right] else right
            if self.container[smaller] < self.container[index]:
                self.container[smaller], self.container[index] = (
                    self.container[index],
                    self.container[smaller],
                )
                index = smaller
                continue
            break

        return removed_val


if __name__ == "__main__":
    min_heap = MinHeap()
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
