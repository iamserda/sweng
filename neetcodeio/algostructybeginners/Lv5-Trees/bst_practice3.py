from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        def dfs(root, value):
            if not root:
                return False
            if root.value == value:
                return True
            return dfs(root.right, value) or dfs(root.left, value)

        return dfs(self.root, value)

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if new_node.value > temp.value:
                    if not temp.right:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right
                        continue
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left
                        continue
                break
        return self.root

    def remove(self, value):
        def rm(root, value):
            if value > root.value:
                root.right = rm(root.right, value)
            elif value < root.value:
                root.left = rm(root.left, value)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                temp = root.right
                while temp and temp.left:
                    temp = temp.left
                root.value = temp.value
                root.right = rm(root.right, temp.value)
            return root

        if isinstance(self.root, TreeNode):
            self.root = rm(self.root, value)
            return self.root

    def level_order_traversal(self):
        levels_arr = []
        if self.root is not None:
            qu = deque()
            qu.appendleft([self.root])
            while qu:
                row = qu.pop()
                level_children_nodes = []
                level_node_values = []
                for node in row:
                    level_node_values.append(node.value)
                    if node.left is not None:
                        level_children_nodes.append(node.left)
                    if node.right is not None:
                        level_children_nodes.append(node.right)
                if level_node_values:
                    levels_arr.append(level_node_values)
                if level_children_nodes:
                    qu.appendleft(level_children_nodes)
        return levels_arr

    def inoder_traversal(self, arr=[]):
        if not self.root:
            return arr

        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.value)
            inorder(root.right, arr)

        inorder(self.root, arr)
        return arr


my_bst = BinarySearchTree()
my_bst.insert(8)
my_bst.insert(12)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(2)
my_bst.insert(14)
my_bst.insert(10)

for i in range(2, 16, 2):
    print(f"Found {i}?: {my_bst.search(i)}")

print(my_bst.level_order_traversal())
my_bst.remove(4)
print("Traversed by Level:", my_bst.level_order_traversal())
print(f"Traversed in Order: {my_bst.inoder_traversal()}")
