class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0
        self.size = 0

    def insert(self, value):
        