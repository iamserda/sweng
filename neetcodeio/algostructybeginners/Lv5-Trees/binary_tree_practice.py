from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def iter_search(self, value):
        if not self.root:
            return
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if value > temp.value and temp.right:
                temp = temp.right
            if value < temp.value and temp.left:
                temp = temp.left
        return False

    def bfs_to_list(self):
        temp = self.root
        arr = list()
        if temp:
            q = deque()
            q.append(temp)
            while q:
                elem = q.popleft()
                arr.append(elem.value)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
        return arr

    def traverse_in_order(self):
        arr = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.value)
            inorder(root.right)

        inorder(self.root)
        return arr


tree = Tree()
tree.root = TreeNode(5)
tree.root.left = TreeNode(3)
tree.root.left.left = TreeNode(2)
tree.root.left.right = TreeNode(4)
tree.root.right = TreeNode(8)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(9)

print("BFS-Traversal:", tree.bfs_to_list())
print("DFS-Traversal:", tree.traverse_in_order())
