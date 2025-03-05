class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


# TESTING ARENAS:
my_binary_tree = BinaryTree()
my_binary_tree.root = TreeNode(8)
