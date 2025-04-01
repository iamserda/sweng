arr = []


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    @classmethod
    def dfs(cl, node):
        global arr
        if not node:
            return
        TreeNode.dfs(node.left)
        print(node.value)
        TreeNode.dfs(node.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)

dfs = TreeNode.dfs
dfs(root)  # expect 5 prints
