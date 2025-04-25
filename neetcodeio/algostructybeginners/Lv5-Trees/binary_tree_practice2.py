from collections import deque
from random import randint


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
        else:
            q = deque()
            q.append(self.root)
            while q:
                node = q.popleft()
                if not node.left:
                    node.left = new_node
                    return
                if not node.right:
                    node.right = new_node
                    return
                q.append(node.left)
                q.append(node.right)

    def display_inorder(self):
        if not self.root:
            return []
        arr = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(self.root)
        print(arr)
        return arr

    def display_level_order(self):
        arr = []
        if self.root:
            q = deque()
            q.append(self.root)
            while q:
                node = q.popleft()
                if node is None:
                    break
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)
        print(arr)
        return arr


btree = BinaryTree()
btree.display_level_order()
for i in range(1, 10):
    btree.insert(i)
btree.display_level_order()
