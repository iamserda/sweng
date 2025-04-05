from random import randint


class Heap:
    def __init__(self):
        self.root = [None]

    def insert(self, value):
        self.root.append(value)
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

    def pop(self):
        if len(self.root) < 2:
            return None

        elif len(self.root) == 2:
            return self.root.pop()  # removing root.

        temp = self.root[1]
        self.root[1] = self.root[len(self.root) - 1]
        self.root.pop()
        current = 1
        while current < len(self.root):
            if (
                2 * current < len(self.root)
                and self.root[current] > self.root[2 * current]
            ):
                self.root[current], self.root[2 * current] = (
                    self.root[2 * current],
                    self.root[current],
                )
                current *= 2
            elif (
                2 * current + 1 < len(self.root)
                and self.root[current] > self.root[2 * current + 1]
            ):
                self.root[current], self.root[2 * current + 1] = (
                    self.root[2 * current + 1],
                    self.root[current],
                )
                current *= 2 + 1
            else:
                break
        return temp


def display(arr):
    i = 1
    for i in range(1, len(arr)):
        if 2 * i < len(arr) and 2 * i + 1 < len(arr):
            print([arr[i], [arr[2 * i], arr[2 * i + 1]]])
        else:
            print(arr[i], "index1:", 2 * i, " index2:", 2 * i + 1)


heap = Heap()
arr = [26, 30, 65, 68, 19, 26, 21, 16, 19, 14]
print("pre-insertion:", heap.root)
for i in reversed(arr):
    print(f"ins({i}):", heap.insert(i)[1:])

for _ in [26, 30, 65, 68, 19, 26, 21, 16, 19, 14]:
    print(f"pop({heap.pop()}):", heap.root[1:])
