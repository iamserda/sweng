class Heap:
    def __init__(self, arr=[]):
        self.container = [None, *arr]

    @property
    def length(self):
        return len(self.container[1:])


min_heap = Heap([])
min_heap.prince = 1
print(min_heap.length)
