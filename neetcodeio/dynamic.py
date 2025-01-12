class DynamicArray:

    def __init__(self, capacity: int = 0):
        self.arr = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        if self.getCapacity() < 1:
            raise IndexError("Cannot use 'get' on an empty array")
        elif i > self.getCapacity():
            raise IndexError("Cannot use 'get' on an empty array")
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.getCapacity():
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        self.arr.append(n)
        self.capacity += 1

    def popback(self) -> int:
        if self.getCapacity == 0:
            raise Error("List is empty, can't apply this method on an empty list.")
        self.arr.pop()
        self.capacity -= 1
        

    def resize(self) -> None:
        new_arr = []
        for item in self.arr:
            new_arr.append(item)
        for i in range(len(self.arr), self.capacity * 2)

    # def getSize(self) -> int:
        

    # def getCapacity(self) -> int:
