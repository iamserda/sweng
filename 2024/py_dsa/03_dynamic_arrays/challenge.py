"""Prototype for a dynamic array similar to ArrayList in Java or C/CPP"""


class DynamicArray:
    """Prototype for a dynamic array similar to ArrayList in Java or C/CPP"""

    def __init__(self, capacity: int):
        """Constructor Function"""

    def getter(self, i: int) -> int:
        """ Given an *valid* index, returns the value at that index."""

    def setter(self, i: int, n: int):
        """ Given an *valid* index, updates the value at that index."""

    def push(self, n: int):
        """Appends a new item at the end of the array."""

    def pop(self) -> int:
        """ a new item at the end of the array."""

    def resize(self) -> None:
        """ Doubles the size of the array"""

    def get_size(self) -> int:
        """Returns the current size, integer, of this DynamicArray object"""


    def get_capacity(self) -> int:
        """Returns the current capacity or maximum size, integer, of this DynamicArray object."""



# TESTING ARENA:
myDynArr = DynamicArray(1)
print("DynamicArray(1):",myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")

myDynArr.push(1)
print("push(1):", myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")
assert myDynArr.get_capacity() == 1
assert myDynArr.get_size() == 1

myDynArr.push(2)
print("push(2):", myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")
assert myDynArr.get_capacity() == 2
assert myDynArr.get_size() == 2

myDynArr.push(3)
print("push(3):",myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")
assert myDynArr.get_capacity() == 4
assert myDynArr.get_size() == 3

print("pop():",myDynArr.pop(), myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")
assert myDynArr.get_capacity() == 4
assert myDynArr.get_size() == 2

# IndexError: Out of Bound
print("setter(-1,90):",myDynArr.setter(-1, 90), myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")

# IndexError: Out of Bound
print(myDynArr.setter(3, 90))
print("setter(3,90):",myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")

print(myDynArr.setter(2, 90))
print("setter(2,90):",myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")


print("resize():", myDynArr.resize(), myDynArr.arr, f"len: {myDynArr.size}, cap: {myDynArr.capacity}")
assert myDynArr.get_capacity() == 8
assert myDynArr.get_size() == 2