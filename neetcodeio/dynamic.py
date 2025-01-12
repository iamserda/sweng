class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array: list = [None]*capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        if len(self.array) == 0:
            raise IndexError("Cannot use method 'get()' on an empty Dynamic Array instance.")
        if i >= self.capacity:
            raise IndexError("Requested index is out of range.")
        return self.array[i]
    
    def set(self, i: int, n: int) -> None:
        if i >= self.capacity:
            raise IndexError("Index is out of range for this task. Cannot set a new value at this index. Consider .pushback() method.")
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        if len(self.array) == 0:
            raise IndexError("Cannot use menthod 'popback' on an empty Dynamic Array instance.")
        return self.array.pop()
