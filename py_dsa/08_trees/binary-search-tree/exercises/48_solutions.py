class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

assert my_tree.root == None
