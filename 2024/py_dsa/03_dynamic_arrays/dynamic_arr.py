"""Prototype for a dynamic array similar to ArrayList in Java or C/CPP"""


class DynamicArray:
    """Prototype for a dynamic array similar to ArrayList in Java or C/CPP"""

    def __init__(self, capacity: int):
        self.capacity = capacity or 1
        self.arr = [None] * self.capacity
        self.size = 0

    def getter(self, i: int) -> int:
        """ Given an *valid* index, returns the value at that index."""
        if self.size > 0 and i < self.size:
            return self.arr[i]

    def setter(self, i: int, n: int) -> bool:
        """ Given an *valid* index, updates the value at that index."""
        if self.size > 0 and 0 <= i < self.size:
            self.arr[i] = n
            last = len(self.arr) - 1
            return self.arr[last]
        return False

    def push(self, n: int) -> bool:
        """Appends a new item at the end of the array."""
        if not len(self.arr) + 1 <= self.capacity:
            self.resize()
        self.arr.append(n)
        self.size = self.get_size() + 1
        last = len(self.arr) - 1
        return self.arr[last]

    def pop(self) -> int:
        """ a new item at the end of the array."""
        if self.size:
            item = self.arr.pop()
            self.size = self.get_size() - 1
            return item

    def resize(self) -> None:
        """ Doubles the size of the array"""
        arr_ptr = []
        for i in range(self.size):
            arr_ptr[i] = self.arr[i]
        self.arr = arr_ptr
        self.capacity = self.capacity * 2 if self.capacity else 1
        return True

    def get_size(self) -> int:
        """Returns the current size, integer, of this DynamicArray object"""
        return self.size

    def get_capacity(self) -> int:
        """Returns the current capacity or maximum size, integer, of this DynamicArray object."""
        return self.capacity
