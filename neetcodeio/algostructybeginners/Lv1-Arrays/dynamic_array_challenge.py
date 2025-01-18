class DynamicArray:
    """
        Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

    Your DynamicArray class should support the following operations:

    DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    int get(int i) will return the element at index i. Assume that index i is valid.
    void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    void pushback(int n) will push the element n to the end of the array.
    int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    void resize() will double the capacity of the array.
    int getSize() will return the number of elements in the array.
    int getCapacity() will return the capacity of the array.
    If we call void pushback(int n) but the array is full, we should resize the array first.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            capacity = 1
        self.array = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if self.size == 0:
            return
        if 0 <= i < self.size:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            return
        if self.size == 0:
            return
        return self.array[i]

    def pushback(self, n: int) -> None:
        if self.size + 1 <= self.capacity:
            self.array.append(n)
            self.size += 1

    # def popback(self) -> int:
    #     if self.size > 0:
    #         self.size -= 1
    #         return self.array.pop()

    # def resize(self) -> None:
    #     new_arr = []
    #     new_size = len(self.array) * 2
    #     new_capacity = new_size * 2
    #     for item in self.array:
    #         new_arr.push
    #     self.array = new_arr
    #     self.size = new_size
    #     self.capacity = new_capacity

    # def getSize(self) -> int:
    #     return self.size

    # def getCapacity(self) -> int:
    #     return self.capacity
