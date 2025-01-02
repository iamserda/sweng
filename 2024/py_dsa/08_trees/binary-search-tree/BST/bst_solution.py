from node_solution import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if value is None:
            return
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if new_node.value == temp.value:
                raise ValueError(
                    "DuplicateNodeError: A node with this value already exist!")

            if new_node.value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
            else:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left

    def search(self, lookup_value):
        """search method for BST"""
        temp = self.root
        while temp is not None:
            if temp.value == lookup_value:
                print("Found!")
                print(f"temp: {temp.value} at mem.loc: {temp}.")
                return True
            elif lookup_value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False  # Value was not found!


# TESTING ARENAS:
my_bst = BinarySearchTree()
arr = [20, 10, 30, 5, 15, 25, 35, 2, 8, 12, 18, 22, 26, 33,
       40, 1, 3, 11, 13, 17, 19, 21, 23, 24, 28, 31, 39, 38, 41]
for ar in arr:
    my_bst.insert(ar)

print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.left.left.value)
print(my_bst.root.left.right.value)
print(my_bst.root.right.value)
print(my_bst.root.right.left.value)
print(my_bst.root.right.right.value)

assert my_bst.search(40) is True
assert my_bst.search(41) is True
assert my_bst.search(42) is False
