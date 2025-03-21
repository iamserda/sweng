class Node:
    def __init__(self, value: any):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_recursive(self, value):

        def inserter(root, value):
            if not root:
                return Node(value)
            else:
                if value > root.value:
                    root.right = inserter(root.right, value)
                elif value < root.value:
                    root.left = inserter(root.left, value)
            return root

        self.root = inserter(self.root, value)
        return self.root


my_bst = BinarySearchTree()
my_bst.insert_recursive(8)
my_bst.insert_recursive(12)
my_bst.insert_recursive(4)
print(my_bst.root, my_bst.root.left, my_bst.root.right)
