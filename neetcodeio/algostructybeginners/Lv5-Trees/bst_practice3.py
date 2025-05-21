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

    @staticmethod
    def rm(current, value):
        if isinstance(current, TreeNode):
            if value > current.value:
                current.right = BinarySearchTree.rm(current.right, value)
            elif value < current.value:
                current.left = BinarySearchTree.rm(current.left, value)
            elif value == current.value:
                if current.left is None:
                    return current.right
                if current.right is None:
                    return current.left
                else:
                    smallest = current.right
                    while smallest and smallest.left:
                        smallest = smallest.left
                    current.value = smallest.value
                    current.right = BinarySearchTree.rm(current.right, value)
            return current

    def remove(self, value):
        if self.root is not None:
            self.root = BinarySearchTree.rm(self.root, value)
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
