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

    def insert_iterative(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    temp = temp.right
                elif value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    temp = temp.left
                break


my_bst = BinarySearchTree()
my_bst.insert_iterative(8)
my_bst.insert_iterative(12)
my_bst.insert_iterative(4)
my_bst.insert_recursive(2)
my_bst.insert_recursive(10)
my_bst.insert_recursive(14)
my_bst.insert_recursive(6)
print(my_bst.root)
print(my_bst.root.left, my_bst.root.right)
print(my_bst.root.left.left, my_bst.root.left.right)
print(my_bst.root.right.left, my_bst.root.right.right)
