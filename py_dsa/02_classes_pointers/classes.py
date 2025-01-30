class Node:
    def __init__(self, value):
        self.value = None
        if value is not None:
            self.value = value

    def set_value(self, value):
        if value is not None:
            self.value = value

    def get_value(self):
        return self.value


class Person:
    def __init__(self, first="", last=""):
        self.first = first
        self.last = last

    def set_first(self, first):
        if first is not None:
            self.first = first

    def get_first(self):
        return self.first

    def set_last(self, last):
        if last is not None:
            self.last = last

    def get_last(self):
        return self.last


node1 = Node(8)
node2 = Node(10)

print(node1.get_value())
node1.set_value(10)
print(node1.get_value())

print(node2.get_value())
node2.set_value(24)
print(node2.get_value())

eddig = Person("Eddy", "Gordo")
liuk = Person("Liu", "Kang")
print(eddig.get_first(), eddig.get_last())
print(liuk.get_first(), liuk.get_last())
