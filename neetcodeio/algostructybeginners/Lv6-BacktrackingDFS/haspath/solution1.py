class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def has_path_without_K(root: TreeNode, k: int) -> bool:
    """Returns True of a path was found without K"""
    if root is None or root.value == k:
        return False
    if root.left is None and root.right is None:
        return True
    if has_path_without_K(root.left, k) or has_path_without_K(root.right, k):
        return True
    return False


# TESTING ARENAS:

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

print("FOUND!" if has_path_without_K(root, 3) else "NOT FOUND!")  # FOUND

root = TreeNode(5)
root.left = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(20)
root.left.left.right = TreeNode(32)
root.left.right.left = TreeNode(2)
root.right = TreeNode(7)
root.right.left = TreeNode(3)
root.right.right = TreeNode(8)
root.right.left.right = TreeNode(30)
root.right.right.right = TreeNode(3)
path_: list = []

print("FOUND!" if has_path_without_K(root, 3) else "NOT FOUND!")  # NOT FOUND
