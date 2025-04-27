# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if root is None:
            return
        elif val == root.val:
            return True
        elif val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)


bst = TreeNode(
    5,
    left=TreeNode(3, left=TreeNode(1), right=TreeNode(4)),
    right=TreeNode(7, left=TreeNode(6), right=TreeNode(8)),
)

sol = Solution()
assert sol.searchBST(bst, 2) == None or False
assert sol.searchBST(bst, 0) == None or False
assert sol.searchBST(bst, 9) == None or False
assert sol.searchBST(bst, 1) == True
assert sol.searchBST(bst, 3) == True
assert sol.searchBST(bst, 4) == True
assert sol.searchBST(bst, 5) == True
assert sol.searchBST(bst, 6) == True
assert sol.searchBST(bst, 7) == True
assert sol.searchBST(bst, 8) == True
