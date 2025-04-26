# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        pass


class Solution:
    def searchBST(self, root, val):
        pass


bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.left.right = TreeNode(4)
bst.right = TreeNode(7)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(8)

sol = Solution()
assert sol.searchBST(bst, 2) == None or False
assert sol.searchBST(bst, -1) == None or False
assert sol.searchBST(bst, 10) == None or False
assert sol.searchBST(bst, 1) == None or False
assert sol.searchBST(bst, 6) == True
assert sol.searchBST(bst, 1) == True
assert sol.searchBST(bst, 4) == True
assert sol.searchBST(bst, 8) == True
