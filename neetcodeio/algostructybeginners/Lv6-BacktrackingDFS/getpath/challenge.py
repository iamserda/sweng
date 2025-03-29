class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def path_from_root(root: TreeNode, k: int, path: list) -> list:
    """Find a path [a,..,z] where k is not the path in a give Binary Tree, from root to leaf."""
    pass


def path_from_leaf(root: TreeNode, k: int, path: list) -> list:
    """Find a path [a,..,z] where k is not the path in a give Binary Tree. Order from Leaf Node to Root."""
    pass

# TESTING ARENA

root = TreeNode(5)
root.left = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(20)
root.left.left.right = TreeNode(32)
root.left.right.left = TreeNode(2)
root.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)
root.right.left.right = TreeNode(30)
root.right.right.right = TreeNode(3)


def test1(root, k, path_):
    print("Test #1:")
    if path_from_root(root, k, path_):
        print("FOUND!:", path_)
    else:
        print("Path NOT FOUND!")


def test2(root, k, path_):
    print("Test #2:")
    if path_from_leaf(root, k, path_):
        print("Path FOUND:", path_)
    else:
        print("Path NOT FOUND!")


test1(root, 3, [])  # [30, 9, 7, 5]
test2(root, 3, [])  # [5, 7, 9, 30]
