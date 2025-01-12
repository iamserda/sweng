class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array: list = [None]*capacity
        self.capacity = capacity
        
    def get(self, i: int) -> int:
        if self.capacity == 0:
            raise IndexError("Cannot uset get() on an empty Dynamic Array instance.")
        if i >= self.capacity:
            raise IndexError("Requested index is out of range.")
        return self.array[i]
    
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
    # def popback(self) -> int:
    # def resize(self) -> None:
    # def getSize(self) -> int:

    def getCapacity(self) -> int:
        return self.capacity

dyn_arr = DynamicArray(3)
assert dyn_arr.getCapacity() == 3