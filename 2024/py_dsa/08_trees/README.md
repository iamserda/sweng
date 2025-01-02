# 6. Trees

## README for Trees

Trees are a hierarchical data structure consisting of nodes, where each node contains a value and a list of references to other nodes (the "children"). The first node of the tree is called the root, and nodes with no children are called leaves. Trees are used to represent hierarchical relationships and are fundamental in algorithms involving hierarchical data, database systems, and more.

### Key Operations

- **Insertion**: Varies based on the type of tree.
- **Deletion**: Varies based on the type of tree.
- **Traversal**: In-order, Pre-order, Post-order, Level-order (BFS).

### Use Cases

- Representing hierarchical data (e.g., file systems).
- Implementing search trees (e.g., Binary Search Trees, AVL Trees) for efficient search, insertion, and deletion operations.
- Storing data in a hierarchical structure to facilitate operations like prefix matching used in trie data structures.

### Python Implementation (Binary Tree)

Here's a simple implementation of a binary tree, where each node has at most two children:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

# Example usage
bt = BinaryTree()
bt.insert(3)
bt.insert(1)
bt.insert(4)
print("In-order traversal:", bt.inorder_traversal(bt.root))  # Output: [1, 3, 4]
```

## Further Steps
- Explore different types of binary trees such as AVL trees, Red-Black trees, which are self-balancing binary search trees.
- Implement tree traversal methods and understand their applications.

Trees are a versatile and powerful data structure capable of representing complex hierarchical data. When you're ready to learn about Binary Search Trees (BST), just let me know!