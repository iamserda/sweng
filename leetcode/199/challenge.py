# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view(self, root: list[TreeNode]) -> list[int]:
        pass


# Testing Arena
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()
assert sol.right_side_view(root) == [1, 3, 4]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
sol = Solution()
assert sol.right_side_view(root) == [1, 3, 4, 5]


root = TreeNode(4)
root.right = TreeNode(6)
sol = Solution()
assert sol.right_side_view(root) == [4, 6]

root = None

sol = Solution()
assert sol.right_side_view(root) == []
