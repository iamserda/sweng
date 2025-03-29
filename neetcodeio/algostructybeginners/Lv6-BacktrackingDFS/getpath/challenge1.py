class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pathfinder(root: TreeNode, k: int, path: list) -> list:
    """Find a path [a,..,z] where k is not the path in a give Binary Tree"""
    pass


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
path_: list = []
if pathfinder(root, 6, path_):
    print("Path Found:", f"end <-{path_}<-start")
else:
    print("Path NOT FOUND!")
