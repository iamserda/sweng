from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root


def level_order_traversal(root):
    results = []
    _q = deque()
    _q.append(root)
    while _q:
        node = _q.popleft()
        if isinstance(node, TreeNode):
            results.append(node.val)
            _q.append(node.left)
            _q.append(node.right)
    return results


root = TreeNode(8)
print("Pre:", level_order_traversal(root))
for num in [12, 4, 10, 14, 2, 6]:
    root = insert(root, num)
print("Post addition:", level_order_traversal(root))

print("Pre Removal:", level_order_traversal(root))
for num in [8, 12, 4, 10, 14, 2, 6]:
    root = remove(root, num)
print("Pre Removal:", level_order_traversal(root))
