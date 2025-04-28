class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if val > temp.val:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    temp = temp.right
                    continue
                if val < temp.val:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    temp = temp.left
                    continue
                break
        return self.root

    def insert_recursive(self, val):
        def _insert(root, val):
            if root is None:
                return TreeNode(val)
            if val > root.val:
                root.right = _insert(root.right, val)
            if val < root.val:
                root.left = _insert(root.left, val)
            return root

        self.root = _insert(self.root, val)
        return self.root

    def remove(self, val):
        if isinstance(self.root, TreeNode):
            self.root = self.rm(self.root, val)
        return self.root

    def rm(self, root, val):
        if root is None:
            return root
        elif val > root.val:
            root.right = self.rm(root.right, val)
        elif val < root.val:
            root.left = self.rm(root.left, val)
        elif val == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                temp = root.right
                while temp and temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.rm(root.right, temp.val)
        return root

    def level_order_traversal(self):
        pass


# Testing Arenas:
bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(4)
bst.insert(6)
assert bst.root.val == 4
assert bst.root.left.val == 2
assert bst.root.right.val == 6
bst.remove(4)
# print(bst.level_order_traversal())
assert bst.root.val == 6
assert bst.root.left.val == 2
assert bst.root.right is None
# print(bst_two.level_order_traversal())

bst.remove(6)
assert bst.root.val == 2
assert bst.root.left is None
assert bst.root.right is None
# print(bst_two.level_order_traversal())

# Testing Arenas:
bst_two = BinarySearchTree()
bst_two.insert_recursive(4)
bst_two.insert_recursive(2)
bst_two.insert_recursive(6)
assert bst_two.root.val == 4
assert bst_two.root.left.val == 2
assert bst_two.root.right.val == 6
bst_two.remove(4)
# print(bst_two.level_order_traversal())

assert bst_two.root.val == 6
assert bst_two.root.left.val == 2
assert bst_two.root.right is None
# print(bst_two.level_order_traversal())

bst_two.remove(6)
assert bst_two.root.val == 2
assert bst_two.root.left is None
assert bst_two.root.right is None
# print(bst_two.level_order_traversal())
