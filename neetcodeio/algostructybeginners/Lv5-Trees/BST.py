class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0
        self.size = 0

    def search(self, value):
        def found(root, value):
            if not root:
                return False
            elif value > root.value:
                return found(root.right, value)
            elif value < root.value:
                return found(root.left, value)
            else:
                return True

        return found(self.root, value)

    def insert(self, value):

        def insrt(root, value):
            if not root:
                return TreeNode(value)
            else:
                if value > root.value:
                    root.right = insrt(root.right, value)
                elif value < root.value:
                    root.left = insrt(root.left, value)
            return root

        self.root = insrt(self.root, value)
        return self.root

    def remove(self, value):
        if not self.root:
            return None

        def min_value_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        def rm(root, value):
            if value > root.value:
                root.right = rm(root.right, value)
            elif value < root.value:
                root.left = rm(root.left, value)
            else:
                # if they are equal, which means I found the node to be removed.
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node = min_value_node(root.right)
                    root.val = min_node.value
                    root.right = rm(root.right, min_node.value)
            return root

        self.root = rm(self.root, value)
        return self.root


my_bst = BinarySearchTree()
my_bst.insert(8)
my_bst.insert(12)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(2)
my_bst.insert(14)
my_bst.insert(10)
print(my_bst.search(10))

root = my_bst.root
my_bst.remove(4)
if root:
    print(root.value)
if root.left:
    print(root.left.value)
if root.right:
    print(root.right.value)
