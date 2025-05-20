class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(node, target):
    """Given a BinaryTreeNode, and a target value,
    this function returns a boolean True if there is a Node within the Tree
    with a value that matches the target. Otherwise, it returns False."""
    if not isinstance(node, BinTreeNode):
        raise TypeError("Node MUST BE a BinTreeNode type. Invalid param.")
    if target is None:
        raise TypeError("Invalid param: Expected target to be a valid non-NoneType.")

    if target > node.value:
        if node.right is None:
            return False
        return search(node.right, target)

    if target < node.value:
        if node.left is None:
            return False
        return search(node.left, target)

    if target == node.value:
        return True
    return False


root = BinTreeNode(2)
root.right = BinTreeNode(3)
root.left = BinTreeNode(1)
root.right.right = BinTreeNode(4)

try:
    assert search(node=root, target=5) == False
    assert search(node=root, target=4) == True
    assert search(None, 5) is Exception
    assert search(root, None) is Exception
except Exception as err:
    print(f"Error: {err}")
    pass
