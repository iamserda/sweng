class DynamicArray:

    def __init__(self, capacity: int):
        self.store = [None] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.length:
            return -1
        for index in range(self.length):
            if index == i:
                return self.store[index]
        return -1

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.length:
            return

        for index in range(self.length):
            if index == i:
                self.store[index] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.store[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            val = self.store[self.length - 1]
            self.store[self.length - 1] = None
            self.length -= 1
            return val
        return -1

    def resize(self) -> None:
        self.capacity *= 2
        new_store = [None] * self.capacity
        for i in range(self.length):
            new_store[i] = self.store[i]
        self.store = new_store

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity


# TESTING ARENA:
# tasks: ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
# expected: [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
# output: [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, -1, 1, 2]

my_arr = DynamicArray(1)
print(my_arr.store)
print(my_arr.getSize())  # 0
print(my_arr.getCapacity())  # 1
my_arr.pushback(1)  # None
print(my_arr.store)
print(my_arr.getSize())  # 1
print(my_arr.getCapacity())  # 1
my_arr.pushback(2)  # None
print(my_arr.store)
print(my_arr.getSize())  # 2
print(my_arr.getCapacity())  # 2
my_arr.get(1)  # 2
my_arr.set(1, 3)
print(my_arr.store)  # [1, 3]
print(my_arr.getSize())  # 2
print(my_arr.getCapacity())  # 2
my_arr.get(1)  # 3
print(my_arr.popback())
print(my_arr.store)  # [1, None]
print(my_arr.getSize())  # 1
print(my_arr.getCapacity())  # 2
