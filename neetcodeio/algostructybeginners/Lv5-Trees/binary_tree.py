class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


# TESTING ARENAS:
#        8
#     /    \
#    10     1
#   /  \    /\
#  2   11  2  12

my_binary_tree = BinaryTree()
my_binary_tree.root = TreeNode(8)
my_binary_tree.root.left = TreeNode(10)
my_binary_tree.root.right = TreeNode(1)
my_binary_tree.root.left.left = TreeNode(2)
my_binary_tree.root.left.right = TreeNode(11)
my_binary_tree.root.right.left = TreeNode(2)
my_binary_tree.root.right.right = TreeNode(12)
