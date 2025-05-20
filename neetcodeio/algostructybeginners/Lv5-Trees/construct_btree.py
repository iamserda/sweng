# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition of Binary Tree
class Solution:
    @classmethod
    def dfs(cls, root):
        if not root:
            return
        cls.dfs(root.left)
        print(root.val)
        cls.dfs(root.right)

    def buildTree(self, preorder: list[int], inorder: list[int]) -> list[TreeNode]:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        left = True
        for idx in range(len(inorder)):
            if inorder[idx] == root.val:
                left = False
                continue
            new_node = TreeNode(inorder[idx])
            if left:
                if not root.left:
                    root.left = new_node
                else:
                    temp = root.left
                    while temp:
                        if temp.left:
                            temp = temp.left
                        else:
                            temp.left = new_node
                            break
            else:
                if not root.right:
                    root.right = new_node
                else:
                    temp = root.right
                    while temp:
                        if temp.right:
                            temp = temp.right
                        else:
                            temp.right = new_node
                            break
        return root


# Testing Arena:

# Test1:
sol = Solution()
root = sol.buildTree([1, 2, 3, 4], [2, 1, 3, 4])
sol.dfs(root)

# Test2:
sol = Solution()
root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
sol.dfs(root)
