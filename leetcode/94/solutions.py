class TreeNode:
     def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None

class Solution:
    def inorderTraversal(self, root):
        ans_arr = []
        def inorder(rootie):
            if not rootie:
                return
            else:
                inorder(rootie.left)
                ans_arr.append(rootie.val)
                inorder(rootie.right)
        inorder(root)
        return ans_arr

tree = TreeNode(8)
tree.left = TreeNode(4)
tree.right = TreeNode(12)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(6)
tree.right.left = TreeNode(10)
tree.right.right = TreeNode(14)

sol = Solution()
print(sol.inorderTraversal(tree))