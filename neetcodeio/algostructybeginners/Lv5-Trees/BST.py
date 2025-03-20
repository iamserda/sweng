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
            # if they are equal, which means I found the node to be removed.
            else:
                # if the node has no left subtree, we return the right
                # if the node has no right subtree, we return the left
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                # Otherwise:
                # find the smallest node in the right subtree
                min_node = min_value_node(root.right)
                # replace root_val with min_node_val
                root.val = min_node.value
                # now remove the min node recursively
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

for i in range(2, 16, 2):
    print(f"Found {i}?: {my_bst.search(i)}")
