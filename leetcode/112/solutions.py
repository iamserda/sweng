# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: list[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        new_target_sum = targetSum - root.val
        if root.left is None and root.right is None:
            return new_target_sum == 0
        return self.hasPathSum(root.left, new_target_sum) or self.hasPathSum(
            root.right, new_target_sum
        )


sol = Solution()

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)
target = 22
assert sol.hasPathSum(tree, target) == True

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
target = 5
assert sol.hasPathSum(tree, target) == False


tree = TreeNode(1)
tree.left = TreeNode(2)
target = 0
assert sol.hasPathSum(tree, target) == False
