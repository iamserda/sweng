import math, random


# Designing a mvp static array: get, prepend, push, pop, pop_first,
class StaticArray:
    def __init__(self, length=1):
        self.store = [None] * length
        self.size = 0
        self.capacity = length

    def get(self, index):
        if self.size == 0:
            print("This is an empty instanceof StaticArray.")
        if index > -1 and index < self.size:
            for i in range(self.size):
                if i == index:
                    return self.store[index]
        print(f"This index: {index} is out of range for this instance of StaticArray.")

    def push(self, value):
        if self.size and self.size + 1 >= self.capacity:
            self.double_array_size()
        self.store[self.size] = value
        self.size += 1

    def prepend(self, value):
        if self.size and self.size + 1 >= self.capacity:
            self.double_array_size()
        for index in range(self.size, 0, -1):
            self.store[index] = self.store[index - 1]
        self.store[0] = value
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            remove, self.store[self.size] = self.store[self.size], None
            return remove

    def pop_first(self):
        if self.size <= 0:
            print("This instance of StacticArray is Empty.")
            return None
        else:
            removed = self.store[0]
            if self.size > 1:
                for index in range(1, self.size):
                    self.store[index - 1] = self.store[index]
            self.size -= 1
            self.store[self.size] = None
            return removed

    def double_array_size(self):
        self.capacity *= 2
        new_store = [None] * self.capacity
        for index, item in enumerate(self.store):
            new_store[index] = item
        self.store = new_store
        return True

    def print_self(self):
        print(self.store)


# Testing Arena:


def test():
    my_array = StaticArray()
    # add
    my_array.print_self()
    print(my_array.size)
    print(my_array.capacity)
    for i in range(10):
        my_array.prepend(random.randint(1, 100))

    # remove
    my_array.print_self()
    print(my_array.size)
    print(my_array.capacity)
    for i in range(my_array.size):
        my_array.pop_first()
        my_array.print_self()
    my_array.print_self()
    print(my_array.size)
    print(my_array.capacity)


test()
